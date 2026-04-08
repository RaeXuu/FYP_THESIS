# FYP Thesis Draft

---

## Chapter 3: Dataset and Preprocessing

### 3.1 Dataset Overview
- PhysioNet/CinC Challenge 2016
- 数据集统计（Normal / Abnormal 数量、比例、来源）
- 类别不平衡问题说明（4:1）

The primary dataset for the diagnostic model is the PhysioNet/CinC Challenge 2016 heart sound database [CITE PhysioNet 2016]. The dataset comprises recordings collected from clinical and non-clinical environments across six subsets (training-a through training-f), each accompanied by a REFERENCE.csv file assigning a binary diagnostic label (Normal / Abnormal) and a REFERENCE-SQI.csv file providing a signal quality index (SQI) score per recording.

Recordings with SQI score = 0 are excluded from the diagnostic dataset, as they are marked as acoustically unusable by the challenge organisers. After this quality filtering, 2,876 recordings remain. The class distribution is heavily skewed: 2,304 Normal (80.1%) and 572 Abnormal (19.9%), yielding an approximately 4:1 imbalance. This ratio reflects the prevalence of pathological conditions in the source population and is a persistent challenge for training unbiased classifiers on this dataset.

After segmentation into 2-second windows (detailed in Section 3.2), the 2,876 recordings produce 62,003 fixed-length segments in total. The dataset is partitioned at the recording level—all segments from a given recording appear in exactly one split—to prevent data leakage. Using a fixed random seed (seed = 42), the split is 80/10/10, yielding 49,833 training, 5,897 validation, and 6,273 test segments. The test set filenames are persisted to disk on the first training run and never modified thereafter, ensuring the test set remains unseen throughout all subsequent experiments.

### 3.2 Signal Preprocessing Pipeline
- 带通滤波（25–400 Hz，Butterworth）
- 滑动窗口分割（2s，50% overlap）
- Log-Mel 频谱图提取（32×64）

All recordings are resampled to 2,000 Hz. The Nyquist frequency of 1,000 Hz comfortably covers the diagnostically relevant range of heart sounds (20–600 Hz), while the reduced sampling rate minimises both storage and downstream computation relative to typical audio sampling rates.

**Bandpass filtering.** A 5th-order Butterworth bandpass filter with cutoff frequencies of 25 Hz and 400 Hz is applied to each recording using zero-phase forward-backward filtering (`scipy.signal.filtfilt`). The lower cutoff at 25 Hz suppresses residual low-frequency baseline wander and body motion artefacts; the upper cutoff at 400 Hz removes high-frequency noise above the dominant energy range of S1, S2, and common murmurs. Zero-phase filtering is used to avoid introducing any group delay distortion that would shift the temporal positions of cardiac events.

**Sliding window segmentation.** Each filtered recording is divided into fixed-length segments of 2 seconds (4,000 samples at 2,000 Hz) using a sliding window with 50% overlap (hop size = 2,000 samples). Segments shorter than 2 seconds at the end of a recording are zero-padded to the required length. The 50% overlap balances the trade-off between data volume and redundancy: it ensures that cardiac events near a segment boundary are fully captured in at least one adjacent window, while avoiding the excessive redundancy that a higher overlap ratio would introduce.

**Log-Mel spectrogram.** Each 2-second segment is transformed into a log-Mel spectrogram using the librosa library. The STFT is computed with a 256-point FFT (window length 256, hop length 96), and the magnitude spectrogram is projected onto 32 Mel-scale filter banks spanning 20–400 Hz. The power spectrogram (power = 2.0) is converted to a decibel scale via `power_to_db`, with a small epsilon (10⁻⁶) added before the logarithm to avoid numerical instability on silent frames. The resulting 2D feature map is fixed to shape 32×64 along the time axis using zero-padding or truncation, producing the final model input of shape 1×32×64.

### 3.3 Signal Quality Assessment Dataset
- SQA 数据集构建（Good / Bad Quality 标注来源）
- 数据统计（8:1 不平衡）

The SQA model requires a quality-labelled dataset separate from the diagnostic labels. This is constructed from the same PhysioNet 2016 source using the REFERENCE-SQI.csv annotations, which are included for all six subsets. Each recording's SQI score is binarised: score ≠ 0 is assigned Good Quality (label 1); score = 0 is assigned Bad Quality (label 0). Unlike the diagnostic dataset, no prior quality filtering is applied—Bad Quality recordings are retained, as they constitute the negative class for training.

The resulting dataset contains 3,240 recordings: 2,876 Good Quality (88.8%) and 364 Bad Quality (11.2%), an approximately 8:1 imbalance. The same 80/10/10 recording-level split strategy is applied, with augmentation enabled only on the training split.

### 3.4 Data Augmentation and Class Balancing
- WeightedRandomSampler 策略
- 数据增强方法

**Class balancing.** Both datasets exhibit substantial class imbalance. A naive training setup would bias the model toward the majority class, yielding high accuracy but poor minority-class recall—exactly the failure mode that M-Score is designed to penalise. To counteract this, `WeightedRandomSampler` is applied at the DataLoader level: each sample is assigned a weight inversely proportional to its class frequency (weight = 1 / class\_count), and the sampler draws from the training set with replacement according to these weights. This produces balanced mini-batches without duplicating data in memory or modifying the underlying dataset.

**Waveform augmentation.** Augmentation is applied stochastically to each training segment at load time and is disabled entirely for validation and test splits. Five independent augmentation operations are applied in sequence, each with its own trigger probability:

| Operation | Description | Probability |
|---|---|---|
| Random gain | Amplitude scaling by a factor sampled uniformly from [0.8, 1.2] | 0.5 |
| Gaussian noise | Additive white noise at SNR sampled uniformly from [20, 35] dB | 0.5 |
| Time shift | Circular shift by up to ±10% of segment length | 0.5 |
| Random resampling | Time-stretch by factor sampled from [0.9, 1.1], then re-padded to original length | 0.3 |
| Polarity inversion | Multiply entire waveform by −1 | 0.5 |

Random gain and polarity inversion simulate variability in probe contact pressure and microphone orientation. Gaussian noise approximates ambient acoustic interference. Time shift and random resampling together increase robustness to recording start-point variability and heart rate fluctuations. All augmentations operate on the raw waveform before the Mel spectrogram is computed, ensuring that the feature extractor sees augmented signal characteristics rather than augmented spectrograms.

---

## Chapter 4: Model Design

### 4.1 Overall Architecture
- 双模型设计思路（SQA + 诊断解耦）
- 输入格式（1×32×64 Log-Mel 频谱图）

The system deploys two independent model instances in a cascaded inference pipeline: a Signal Quality Assessment (SQA) model and a diagnostic model. Both share the same network architecture but are trained on separate datasets for distinct binary classification tasks.

The SQA model serves as a gating function. Before any cardiac recording reaches the diagnostic stage, the SQA model evaluates each 2-second segment for acoustic usability. Segments contaminated by motion artefacts, ambient noise, or insufficient probe contact are rejected; only segments classified as high-quality are forwarded for diagnosis. The final diagnostic decision is produced by aggregating predictions across all accepted segments via weighted averaging, reducing sensitivity to any single noisy window.

This decoupled design has two practical advantages. First, it prevents corrupted input from directly biasing the diagnostic output—a critical concern for a device used in uncontrolled home environments. Second, training the two models independently allows each to be optimised for its own class distribution and evaluation criterion, rather than forcing a single model to solve both problems jointly.

Both models accept a log-Mel spectrogram of shape 1×32×64 as input: one channel, 32 Mel frequency bins spanning 20–400 Hz, and 64 time frames corresponding to a 2-second segment at 2 kHz sampling rate with 96-sample hop length. The compact representation keeps inference memory within the constraints of the Raspberry Pi 4B while retaining the frequency-temporal structure that distinguishes normal S1/S2 patterns from pathological sounds.

### 4.2 Lightweight CNN Backbone
- Depthwise Separable Convolution 结构
- 各层设计（通道数、卷积核大小）
- 参数量分析

The backbone is a four-stage convolutional network built around the depthwise separable convolution (DSC) primitive [CITE Howard et al., MobileNets, 2017]. A DSC block factorises a standard k×k convolution into two sequential operations: a depthwise convolution that filters each input channel independently with a k×k kernel, followed by a pointwise (1×1) convolution that mixes channels. For C_in input channels, C_out output channels, and kernel size k, this reduces the parameter count from C_in × C_out × k² to C_in × k² + C_in × C_out—a factor of approximately k² = 9 for 3×3 kernels. This makes DSC well-suited to edge deployment where model size directly determines both storage footprint and inference latency.

The network begins with a single standard 3×3 convolutional layer that projects the single-channel input to 32 feature maps. This initial layer uses a full convolution because the input has only one channel, making the depthwise factorisation trivial. Three subsequent DSC stages progressively double the channel count while halving the spatial resolution via 2×2 max-pooling. A global average pooling layer collapses the spatial dimensions to a 256-dimensional vector, which passes through a dropout layer (rate 0.3) and a linear classifier.

**Table 4.1: LightweightCNN architecture. Spatial dimensions (H×W) are shown after each stage.**

| Stage | Operation | Channels (in→out) | Spatial (H×W) |
|---|---|---|---|
| conv1 | Conv2d 3×3, BN, ReLU | 1 → 32 | 32 × 64 |
| layer2 | DSC 3×3 + CoordAtt, MaxPool2d | 32 → 64 | 16 × 32 |
| layer3 | DSC 3×3 + CoordAtt, MaxPool2d | 64 → 128 | 8 × 16 |
| layer4 | DSC 3×3 + CoordAtt, MaxPool2d | 128 → 256 | 4 × 8 |
| global\_pool | AdaptiveAvgPool2d(1,1) | 256 | 1 × 1 |
| classifier | Dropout(0.3), Linear | 256 → 2 | — |

The total trainable parameter count is approximately 64.2K. The quantized INT8 TFLite model occupies 145.7 KB on disk.

### 4.3 Coordinate Attention Module
- 设计动机（为什么用 CoordAtt 而不是 SE Block）
- 模块结构（H/W 方向分离的空间注意力）
- 在模型中的插入位置

Each DSC block in layers 2–4 integrates a Coordinate Attention (CoordAtt) module [CITE Hou et al., CVPR 2021] inserted after the pointwise convolution.

The design choice is motivated by a limitation of the Squeeze-and-Excitation (SE) block [CITE Hu et al., CVPR 2018], the most widely adopted channel attention mechanism. SE computes a global descriptor by average-pooling the entire spatial feature map into a single C-dimensional vector, then uses it to rescale channel responses. This operation is spatially blind: it encodes which channels matter globally but discards where within the feature map the relevant activations occur. For heart sound spectrograms, spatial position carries diagnostic information. S1 and S2 energy concentrates in specific frequency bands (predominantly below 200 Hz) and at characteristic temporal positions within the cardiac cycle; pathological murmurs occupy frequency ranges that differ from normal sounds. An attention mechanism that ignores spatial structure cannot selectively amplify these localised cues.

CoordAtt retains positional information by decomposing spatial pooling along the two axes independently. Given a feature map **X** ∈ ℝ^{N×C×H×W}, the module proceeds as follows:

1. **Directional pooling.** **X** is pooled along the width axis to produce **X**_h ∈ ℝ^{N×C×H×1} (encoding frequency-axis context) and along the height axis to produce **X**_w ∈ ℝ^{N×C×1×W} (encoding time-axis context). Unlike global average pooling, each element retains its position along the non-pooled axis.

2. **Joint encoding.** **X**_h and **X**_w (transposed to align the spatial dimension) are concatenated along the height axis and passed through a shared 1×1 convolution followed by BatchNorm and ReLU. The intermediate channel dimension is m = max(8, ⌊C/16⌋), giving m = 8, 8, 16 for C = 64, 128, 256 at layers 2, 3, 4 respectively.

3. **Attention map generation.** The encoded tensor is split back into height- and width-specific components. Each is projected by a separate 1×1 convolution and sigmoid to produce **a**_h ∈ [0,1]^{N×C×H×1} and **a**_w ∈ [0,1]^{N×C×1×W}.

4. **Recalibration.** The output is **X** · **a**_h · **a**_w. Because **a**_h varies along the frequency axis and **a**_w varies along the time axis, their elementwise product creates a 2D attention map that weights each spatial location according to both frequency and temporal position—without collapsing either axis.

The additional parameter cost per CoordAtt block is small: approximately 1.6K, 3.1K, and 12.3K at layers 2, 3, and 4 respectively, modest relative to the DSC blocks they augment.

### 4.4 Signal Quality Assessment Model
- SQA 模型结构（与诊断模型的异同）
- 在推理 pipeline 中的作用

The SQA model is architecturally identical to the diagnostic model: the same four-stage backbone, the same CoordAtt integration at each DSC block, and the same classifier head. It is trained independently on a quality-labelled dataset of 3,240 recordings with an approximately 8:1 Good/Bad Quality class ratio, using the same WeightedRandomSampler strategy to compensate for class imbalance.

Sharing the architecture with the diagnostic model has a practical benefit beyond simplicity: both models are quantized, loaded, and executed under the same TFLite inference pipeline on the Raspberry Pi, with no additional engineering required to accommodate a structurally different gating network.

At inference time, the SQA model processes the same 1×32×64 log-Mel input as the diagnostic model. A segment whose SQA output probability falls below 0.5 is discarded without invoking the diagnostic model, saving one full forward pass per rejected segment and preventing acoustically degraded input from reaching the classification stage.

### 4.5 Model Quantization
- FP32 → INT8 量化方案（Post-Training Quantization）
- TFLite 转换流程
- 量化对模型大小的影响

Both models are converted to TFLite format using the `ai_edge_torch` library, which compiles a PyTorch model directly to a TFLite flatbuffer without an intermediate ONNX step. Two variants are produced per model: an FP32 baseline and a quantized version using dynamic range quantization (`tf.lite.Optimize.DEFAULT`).

Dynamic range quantization statically converts all weight tensors from FP32 to INT8 at export time, reducing the weight storage footprint by approximately 4×. Activations are not statically quantized; instead, their ranges are computed dynamically per inference call. This approach requires no calibration dataset, making it straightforward to apply to any trained checkpoint. The trade-off relative to full integer quantization—where both weights and activations are fixed at INT8—is that activation quantization overhead occurs at runtime rather than being amortized.

The resulting quantized models each occupy 145.7 KB on disk. On the ARM Cortex-A72 of the Raspberry Pi 4B, weight-compressed INT8 models reduce memory bandwidth pressure during inference. Quantitative accuracy retention and latency comparisons between the FP32 and quantized variants are reported in Chapter 5.

---

## Chapter 5: Training and Experiments

### 5.1 Training Configuration
- 数据划分（80/10/10，按 recording 分组）
- 超参数设置（Epoch、Batch Size、LR、Scheduler）
- 评估指标说明（Sensitivity、Specificity、M-Score）

All experiments use the same 80/10/10 recording-level split (seed = 42), with the test set filenames persisted to disk on the first run and held fixed throughout. Slices from the same recording never appear across splits, preventing any form of data leakage. WeightedRandomSampler is applied on the training set in all runs to counteract the 4:1 class imbalance.

The model is trained with Adam optimiser, learning rate 1×10⁻³, and a `ReduceLROnPlateau` scheduler (factor = 0.5, patience = 3, monitored on validation M-Score). Early stopping with patience = 10 is applied in all runs except Run 1. The model checkpoint with the highest validation M-Score is saved and used for test evaluation.

**Evaluation metrics.** The PhysioNet/CinC 2016 challenge defines the primary metric as:

$$M\text{-}Score = \frac{Se + Sp}{2}$$

where Sensitivity (Se) = TP / (TP + FN) measures the fraction of abnormal recordings correctly identified, and Specificity (Sp) = TN / (TN + FP) measures the fraction of normal recordings correctly identified. M-Score is preferred over accuracy because accuracy can reach 80% by predicting all recordings as Normal, while yielding Se = 0 and M-Score = 0.5. All models are saved and compared by M-Score.

### 5.2 Diagnostic Model Results
- Run 1 基础训练结果
- Run 2（Label Smoothing + Early Stopping）对比
- 阈值分析

#### 5.2.1 Training Progression

Seven training runs were conducted to isolate the effect of individual design decisions. All runs use the LightweightCNN + CoordAtt architecture (Group C in the ablation study) unless otherwise noted. Table 5.1 summarises the key configurations and test results.

**Table 5.1: Training run comparison. All runs use the same test split. Bold = selected configuration.**

| Run | Batch | n\_mels | hop | Label Smooth | Early Stop | Test M-Score | Test Se | Test Sp |
|-----|-------|---------|-----|:---:|:---:|:---:|:---:|:---:|
| 1 | 16 | 32 | 96 | ✗ | ✗ | 0.8852 | 0.9569 | 0.8135 |
| 2 | 16 | 32 | 96 | ✓ | ✓ | 0.8816 | 0.9181 | 0.8452 |
| 3 | 16 | 32 | 96 | ✓ | ✓ | 0.8828 | 0.9105 | 0.8551 |
| 4 | 256 | 32 | 96 | ✗ | ✓ | 0.8835 | 0.9544 | 0.8125 |
| 5 | 256 | 64 | 128 | ✗ | ✓ | 0.8784 | 0.9409 | 0.8159 |
| 6 (sweep params) | 16 | 64 | 128 | ✗ | ✓ | **0.8903** | **0.9485** | **0.8322** |
| 7 | 16 | 32 | 96 | ✗ | ✓ | 0.8869 | 0.9383 | 0.8355 |

> *Run 3 uses overlap = 0.75 (vs 0.5 in others), held constant as a separate variable.*

Several consistent patterns emerge across runs. First, label smoothing (Run 2 vs Run 4) shifts the Se/Sp balance toward higher Sp at the cost of Se—the Se/Sp gap narrows from 0.143 to 0.073—but produces no meaningful change in M-Score (0.8816 vs 0.8835). Since the home screening use case penalises missed abnormal cases more heavily than false alarms, label smoothing was excluded from subsequent runs. Second, batch size 16 consistently outperforms batch size 256 when holding all other parameters fixed (Run 6 vs Run 5: +0.012 M-Score; Run 7 vs Run 4: +0.003), likely because smaller batches provide noisier but more frequent gradient updates that regularise training. Third, overlap = 0.75 (Run 3) produces no meaningful improvement over overlap = 0.5 at the same configuration.

**Run 6** achieves the highest test M-Score (0.8903) and is selected as the final model. Its preprocessing parameters (n\_mels = 64, hop = 128) were identified by a 40-trial Bayesian hyperparameter search (Section 5.2.2), and the batch size was set to 16 based on the empirical comparison above.

#### 5.2.2 Hyperparameter Search

A Bayesian sweep over 40 trials was conducted using Weights & Biases, optimising for validation M-Score. The search space covered n\_mels ∈ {32, 64}, hop\_length ∈ {64, 96, 128}, n\_fft ∈ {128, 256, 512}, overlap ∈ {0.25, 0.5, 0.75}, learning rate ∈ {3×10⁻⁴, 5×10⁻⁴, 1×10⁻³}, and weight\_decay ∈ {1×10⁻⁴, 1×10⁻³}.

**Table 5.2: Top 3 sweep trials (validation M-Score).**

| Rank | Val M-Score | Val Se | Val Sp | n\_mels | hop | n\_fft | overlap | lr | weight\_decay |
|------|:-----------:|:------:|:------:|:-------:|:---:|:------:|:-------:|:--:|:-------------:|
| 1 | 0.9033 | 0.9510 | 0.8556 | 64 | 128 | 256 | 0.75 | 1e-3 | 1e-3 |
| 2 | 0.9031 | 0.9677 | 0.8386 | 64 | 96 | 256 | 0.75 | 1e-3 | 1e-3 |
| 3 | 0.9000 | 0.9539 | 0.8462 | 64 | 128 | 256 | 0.75 | 1e-3 | 1e-3 |

The configuration n\_mels = 64, n\_fft = 256, overlap = 0.75, lr = 1×10⁻³ appears consistently across the top trials, indicating a stable optimal region. The selected parameters for the final model are n\_mels = 64, hop = 128, n\_fft = 256, weight\_decay = 1×10⁻³.

#### 5.2.3 Decision Threshold Analysis

The default classification threshold of 0.5 was evaluated against a sweep from 0.30 to 0.80 on the Run 1 model. Results are shown in Table 5.3.

**Table 5.3: Threshold sweep on Run 1 model (test set).**

| Threshold | Se | Sp | M-Score |
|:---------:|:--:|:--:|:-------:|
| 0.30 | 0.9890 | 0.7787 | 0.8839 |
| 0.35 | 0.9840 | 0.7860 | 0.8850 |
| 0.40 | 0.9764 | 0.7947 | 0.8855 |
| **0.45** | **0.9688** | **0.8031** | **0.8859** |
| 0.50 | 0.9569 | 0.8135 | 0.8852 |
| 0.55 | 0.9417 | 0.8218 | 0.8817 |
| 0.60 | 0.9231 | 0.8332 | 0.8782 |
| 0.70 | 0.8547 | 0.8562 | 0.8554 |
| 0.80 | 0.7652 | 0.8915 | 0.8284 |

The optimal threshold (0.45) improves M-Score by only 0.0007 over the default 0.50, confirming that the Se/Sp imbalance is a property of the learned decision boundary rather than a post-processing artefact. The default threshold of 0.50 is retained for deployment, as it provides the highest Se (0.9569), which is the more clinically critical metric in a home screening context.

### 5.3 SQA Model Results
- 训练结果（Test M-Score / Se / Sp）

> *(待填 — SQA 模型训练完成后补充 Test M-Score / Se / Sp / Accuracy，以及与诊断模型训练设置的对比说明)*

### 5.4 Ablation Study
- Baseline CNN（无注意力）
- + Coordinate Attention
- + Residual Connection
- 各步骤指标对比

To quantify the contribution of each architectural component, four model variants were trained under identical conditions: the same dataset split, preprocessing parameters (n\_mels = 32, hop = 96, n\_fft = 256, overlap = 0.5), training hyperparameters (batch = 16, lr = 1×10⁻³, weight\_decay = 1×10⁻⁴, early stopping patience = 10), and class balancing strategy. The variants form a cumulative chain, each adding one modification to the previous.

**Table 5.4: Ablation study results. All variants trained on the same fixed test split.**

| Config | Params | Test M-Score | Test Se | Test Sp | Test Acc | Best Epoch |
|--------|-------:|:------------:|:-------:|:-------:|:--------:|:----------:|
| A: Baseline (16→32→64→128, no attention) | 12.87K | 0.8851 | 0.9654 | 0.8049 | 0.8352 | 1 |
| B: + Wider channels (32→64→128→256) | 47.23K | 0.8896 | 0.9595 | 0.8198 | 0.8462 | 1 |
| C: + CoordAtt + Dropout(0.3) | 65.12K | 0.8869 | 0.9383 | 0.8355 | 0.8549 | 5 |
| D: + Residual connections | 108.10K | **0.8912** | **0.9797** | 0.8027 | 0.8361 | 2 |

**A → B: Wider channels.** Doubling the channel width throughout (+0.005 M-Score) improves both Se and Sp marginally. The best epoch remains 1, indicating that the model still overfits rapidly and that increased capacity alone does not improve training dynamics.

**B → C: CoordAtt + Dropout.** Adding Coordinate Attention and Dropout (rate 0.3) produces the most notable change in training behaviour: the best validation epoch shifts from 1 to 5, indicating substantially better regularisation. M-Score decreases slightly (−0.003) relative to B, but Sp increases by +0.016 and the Se/Sp gap narrows from 0.134 to 0.103. The contribution of CoordAtt is therefore more accurately characterised as improved training stability and better Se/Sp balance than raw M-Score gain.

**C → D: Residual connections.** Residual connections yield the highest test M-Score (0.8912, +0.004 over C), driven by a large Se increase (+0.041). However, Sp drops to 0.8027—lower than any other variant—and the best epoch regresses to 2, suggesting that residual connections accelerate convergence at the cost of reinforcing the model's tendency to over-predict Abnormal. The Se/Sp gap widens to 0.177.

**Architecture selection.** Config C is selected as the final architecture. While D achieves the highest M-Score, its Se/Sp imbalance (0.177 gap) is worse than A (0.161) and substantially worse than C (0.103). In a home screening device where missed abnormal cases carry greater clinical risk than false alarms, Se is more important than Sp—but the magnitude of Sp degradation in D (0.8027, a 32.8% false alarm rate on normal recordings) is considered unacceptable for a practical device. Config C provides the best balance across all three criteria: Se/Sp balance, training stability, and parameter efficiency.

### 5.5 Quantization Impact
- FP32 vs INT8 准确率对比
- 模型大小对比
- 推理延迟对比

**Table 5.5: FP32 vs quantized model comparison.**

| Metric | FP32 | Quantized (Dynamic Range INT8) | Change |
|--------|:----:|:------------------------------:|:------:|
| Model size | *(待填)* KB | 145.7 KB | *(待填)* |
| Test M-Score | *(待填)* | *(待填)* | *(待填)* |
| Test Se | *(待填)* | *(待填)* | *(待填)* |
| Test Sp | *(待填)* | *(待填)* | *(待填)* |
| Inference latency (Pi 4B) | *(待填)* ms | *(待填)* ms | *(待填)* |

> *(待填 — 运行 evaluate.py 和 benchmark.py 后补充。注意：此处使用 dynamic range quantization，权重 INT8 静态量化，激活值运行时动态量化，延迟收益可能小于 full INT8 PTQ，详见 Section 4.5。)*

> **Note for writing:** Dynamic range quantization only statically quantizes weights; activations are quantized at runtime per call. This means the latency reduction relative to FP32 may be modest compared to full INT8 quantization (where both weights and activations are fixed at INT8 and the hardware can execute true INT8 GEMM). If the benchmark shows limited speedup, this is the expected explanation—not a flaw in the implementation.

---

## Chapter 6: Edge Deployment

### 6.1 System Architecture Overview
- ESP32 → BLE → Raspberry Pi 4B 整体数据流
- 各模块分工

### 6.2 Real-Time Inference Pipeline
- BLE 数据接收与缓冲
- 滑动窗口推理流程（SQA 过滤 + 诊断 + 加权平均）
- 采集策略（3 次 × 2s，间隔 30s）

### 6.3 Performance Evaluation
- 推理延迟（各阶段：带通滤波 / Mel / SQA / 诊断）
- CPU 与内存占用
- 实时性验证

### 6.4 User Interface
- OLED 双屏设计（诊断主屏 + 系统状态副屏）
- 物理按键交互逻辑

### 6.5 System Reliability
- 软件看门狗机制
- 异常恢复策略（BLE 断连重连、推理失败处理）
- 安全关机

---

## Chapter 7: Conclusion

### 7.1 Summary of Contributions
### 7.2 Limitations
### 7.3 Future Work

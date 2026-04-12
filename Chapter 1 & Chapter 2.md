## 电子听诊器硬件采集与传输技术现状

高质量的心音信号（Phonocardiogram,
PCG）采集是实现智能诊断的物理基础，其硬件架构主要涵盖传感器选型、模拟前端处理与无线数据传输三个核心环节。

在传感器技术层面，Leng等\[20\]在对电子听诊器架构的系统性分析中指出，压电传感器（Piezoelectric
Sensor）与微机电系统（MEMS）麦克风是当前的主流选择。尽管MEMS具有体积小、一致性好的优势，但压电传感器因其对低频信号（心音主要能量集中在20-200Hz频段）具有更优异的响应特性，在捕捉第三、第四心音及微弱的病理性杂音方面表现更为出色。NXP发布的《医疗听诊器设计参考手册》\[21\]进一步为采集电路的设计提供了工业级规范，明确指出由于心音信号极其微弱（毫伏级），模拟前端（AFE）必须包含多级放大电路与高精度的有源滤波器，以有效抑制接触摩擦噪声和50Hz/60Hz工频干扰，确保进入模数转换器（ADC）的信号具有高信噪比。

随着可穿戴技术与物联网（IoT）的融合，硬件形态正经历从"手持式"向"穿戴式"的演变。Iqbal等\[18\]回顾了医疗可穿戴设备的最新进展，指出蓝牙（Bluetooth）和Wi-Fi已取代传统线缆，成为连续健康监测的标准通信协议。Lee等\[13\]在《Science
Advances》上发表的研究展示了一种全柔性可穿戴听诊器，通过柔性电子技术解决了刚性传感器与皮肤接触不紧密导致的运动伪影问题，实现了实时的连续听诊。这种"无感化"设计虽然代表了未来方向，但在现阶段，利用ESP32等高性能、低成本的微控制器（MCU）集成高保真ADC与双模蓝牙/Wi-Fi功能，仍是兼顾信号质量与系统成本的最佳工程实践。

## 心音信号预处理与去噪技术

采集到的PCG信号具有非平稳、非线性的特点，且极易受到环境噪声、呼吸音及听诊头摩擦音的污染。因此，信号预处理是后续特征提取与分类的前提。

小波变换（Wavelet
Transform）因其具备多分辨率分析能力，能同时在时域和频域表征信号特征，长期以来是心音去噪的主流方法。Heil和Walnut\[10\]确立了小波变换的数学理论基础。在此基础上，Ali等\[8\]通过系统比较不同离散小波基（DWT）的处理效果，证明了Daubechies系列小波配合软阈值策略能显著提升信噪比，且保留了关键的心音成分。国内学者成谢锋等\[9\]针对心音信号的冲击特性，提出了一种构造专用小波的方法，实验表明自构小波在去噪和信号重构的均方误差（MSE）指标上优于通用的db5或sym5小波。

近年来，针对复杂声学环境下的去噪难题，更先进的信号分解算法与深度学习模型开始应用。Yang等\[22\]在2025年的最新研究中，提出了一种基于中值集合经验模态分解（MEEMD）与Hurst指数相结合的阈值去噪方法，该方法有效克服了传统EMD算法中的模态混叠（Mode
Mixing）问题，能更精准地分离噪声主导的模态分量。与此同时，Ali等\[5\]提出的LU-Net框架展示了基于深度学习的去噪新思路，利用改进的U-Net架构进行端到端的信号增强，在处理非平稳突发噪声方面展现出优于传统滤波器的实时性与鲁棒性。

## 心音分类算法的演进：从机器学习到Transformer

心音自动分类算法作为智能听诊器的"大脑"，经历了从人工特征工程到深度表征学习，再到大模型范式的三次跨越。

### 传统机器学习方法 

在深度学习普及之前，心音分类主要依赖专家知识驱动的特征工程。Li等\[19\]和Ben
Hamza等\[3\]的综述文章详细梳理了这一阶段的技术路线，主流特征包括梅尔频率倒谱系数（MFCC）、短时傅里叶变换（STFT）频谱图以及时域统计特征（如能量熵、过零率）。Yaseen等\[7\]的研究展示了典型的工作流：通过提取多种时频域特征构建高维特征向量，并对比支持向量机（SVM）、K近邻（KNN）和随机森林（Random
Forest）的分类效果。研究发现，SVM在小样本数据集上表现稳健，但传统方法高度依赖特征提取的质量，泛化能力较弱，难以应对临床环境中变异性较大的病理信号。

### 深度神经网络（CNN与RNN） 

随着PhysioNet等大型公开数据集的发布，深度学习（DL）逐渐占据主导地位。Ren等\[2\]和Partovi等\[17\]的综述指出，卷积神经网络（CNN）凭借其强大的空间特征提取能力，成为处理心音图谱的首选。Guo等\[12\]利用包含约6000个样本的大规模数据集，训练了一个深层CNN模型用于肺动脉高压筛查，证明了深度模型在挖掘深层病理特征上的优势。考虑到心音信号的时间序列特性，Chen等\[24\]指出，结合CNN提取频域特征与循环神经网络（RNN，如LSTM/GRU）提取时序依赖关系的混合架构（CRNN）是这一时期的研究热点。Ameen等\[25\]的对比研究也表明，相较于心电（ECG）信号，PCG信号的分类更依赖于时频转换后的深度特征学习。

### Transformer架构与多模态融合 

为了突破CNN在全局上下文建模上的局限，2023年至2025年间，学术界开始将Transformer架构引入心音分析。Yang等\[6\]直接利用Transformer对心音信号进行编码分类，有效提升了瓣膜病的诊断精度。为了兼顾局部细节与全局关联，Cheng等\[26\]提出了CTENN模型，串联了1D卷积与Transformer
Encoder，实现了特征提取的互补。Wang等\[14\]提出的PCTMF-Net则采用了并行结构，利用二阶谱分析提取特征后，同时输入CNN和Transformer进行融合。

更进一步，Liu等\[15\]创新性地结合了双谱（Bispectrum）特征与Vision
Transformer（ViT），利用双谱的高阶统计特性抑制高斯噪声，提升了模型在噪杂环境下的鲁棒性。Han等\[1\]在2025年提出的ENACT-Heart模型更是代表了当前的性能前沿，该模型构建了一个混合专家系统（Mixture
of
Experts），分别利用CNN处理视听图、ViT处理频谱图，通过多模态特征的深度融合，在多个基准数据集上刷新了分类准确率记录。

## 边缘计算与轻量化部署研究

尽管基于Transformer的先进模型在准确率上取得了突破，但其巨大的参数量和计算开销阻碍了其在便携式医疗设备上的直接部署。Wang等\[14\]和Guo等\[12\]提出的模型通常需要高性能GPU服务器支持。然而，Ghouse等\[11\]强调，在医疗资源匮乏或网络覆盖不佳的偏远地区，依赖云端的诊断系统往往无法工作，开发基于低成本嵌入式设备的"离线诊断系统"具有极高的应用价值。

针对这一矛盾，"边缘人工智能（Edge
AI）"成为了连接高精度算法与低成本硬件的桥梁。Zhang等\[4\]在2023年的工作为本课题提供了直接的参考范例，他们设计了一种基于树莓派
Zero
2W的低成本数字听诊器（硬件成本仅约25美元），并提出了一种轻量级的CNN与随机森林混合模型，成功在算力受限的树莓派上实现了心肺疾病的实时检测，证明了边缘计算架构的可行性。此外，Jumphoo等\[16\]探讨了利用数据高效的图像Transformer（DeiT）进行迁移学习，通过模型剪枝与量化技术，证明了先进模型经过优化后也可以适配小样本、低算力的边缘应用场景。这些研究表明，通过"ESP32采集 +
树莓派边缘推理"的分层架构，可以在保证诊断精度的同时，显著降低系统成本与功耗，促进智能听诊技术的普及。

# 参考文献

\[1\] Han J, et al. ENACT-Heart - ENsemble-based Assessment Using CNN
and Transformer on Heart Sounds\[J\]. arXiv preprint arXiv:2502.16914,
2025.

\[2\] Ren Z, et al. A Comprehensive Survey on Heart Sound Analysis in
the Deep Learning Era\[J\]. IEEE Computational Intelligence Magazine,
2024.

\[3\] Ben Hamza M F A, Sjarif N N A. A Comprehensive Overview of Heart
Sound Analysis Using Machine Learning Methods\[J\]. IEEE Access, 2024.

\[4\] Zhang M, et al. A Low-Cost AI-Empowered Stethoscope and a
Lightweight Model for Detecting Cardiac and Respiratory Diseases\[J\].
Sensors, 2023, 23(5): 2591.

\[5\] Ali S N, et al. An End-to-End Deep Learning Framework for
Real-Time Denoising of Heart Sounds\[J\]. IEEE Access, 2023, 11:
87901-87915.

\[6\] Yang D, et al. Assisting Heart Valve Diseases Diagnosis via
Transformer-Based Classification of Heart Sound Signals\[J\].
Electronics, 2023, 12(10): 2221.

\[7\] Yaseen, Son G Y, Kwon S. Classification of Heart Sound Signal
Using Multiple Features\[J\]. Applied Sciences, 2018, 8(12): 2344.

\[8\] Ali M N, et al. Denoising of Heart Sound Signals Using Discrete
Wavelet Transform\[J\]. Circuits, Systems, and Signal Processing, 2017,
36: 4482-4497.

\[9\] 成谢锋, 杨贺. 5种小波在心音信号处理中的分析与比较\[J\].
南京邮电大学学报(自然科学版), 2015, 35(1): 38-46.

\[10\] Heil C E, Walnut D F. Continuous and Discrete Wavelet
Transforms\[J\]. SIAM Review, 1989, 31(4): 628-666.

\[11\] Ghouse H, et al. AI-Enhanced Stethoscope in Remote Diagnostics
for Cardiopulmonary Diseases\[C\]. AIP Conference Proceedings, 2025.

\[12\] Guo L, et al. Development and Evaluation of a Deep
Learning--Based Pulmonary Hypertension Screening Algorithm Using a
Digital Stethoscope\[J\]. Journal of the American Heart Association,
2025.

\[13\] Lee S H, et al. Fully portable continuous real-time auscultation
with a soft wearable stethoscope\[J\]. Science Advances, 2023.

\[14\] Wang R, et al. PCTMF-Net: heart sound classification with
parallel CNNs-transformer and second-order spectral analysis\[J\]. The
Visual Computer, 2023, 39: 3811-3822.

\[15\] Liu Z, et al. Heart sound classification based on bispectrum
features and Vision Transformer model\[J\]. Alexandria Engineering
Journal, 2023, 85: 49-59.

\[16\] Jumphoo T, et al. Exploiting Data-Efficient Image
Transformer-Based Transfer Learning for Valvular Heart Diseases
Detection\[J\]. IEEE Access, 2024, 12: 15855-15866.

\[17\] Partovi E, et al. A review on deep learning methods for heart
sound signal analysis\[J\]. Frontiers in Artificial Intelligence, 2024,
7: 1434022.

\[18\] Iqbal S M A, et al. Advances in healthcare wearable devices\[J\].
npj Flexible Electronics, 2021, 5: 9.

\[19\] Li S, et al. A Review of Computer-Aided Heart Sound Detection
Techniques\[J\]. BioMed Research International, 2020.

\[20\] Leng S, et al. The electronic stethoscope\[J\]. BioMedical
Engineering OnLine, 2015, 14: 66.

\[21\] NXP Semiconductors. Medical Stethoscope Design Reference Manual
(DRM132)\[M\]. 2012.

\[22\] Yang X, et al. The heart sound classification of congenital heart
disease by using median EEMD-Hurst\[J\]. Medical & Biological
Engineering & Computing, 2025.

\[23\] Seah J J, et al. Review on the Advancements of Stethoscope Types
in Chest Auscultation\[J\]. Diagnostics, 2023, 13: 1545.

\[24\] Chen J, et al. Artificial intelligence for heart sound
classification: A review\[J\]. Expert Systems, 2024.

\[25\] Ameen A, et al. Advances in ECG and PCG-based cardiovascular
disease classification: a review\[J\]. Journal of Big Data, 2024, 11:
159.

\[26\] Cheng J, Sun K. Heart Sound Classification Network Based on
Convolution and Transformer\[J\]. Sensors, 2023, 23: 8168.

\[27\] Swarup S, Makaryus A N. Digital stethoscope: technology
update\[J\]. Medical Devices: Evidence and Research, 2018, 11: 29.

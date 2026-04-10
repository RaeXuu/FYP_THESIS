2.3.3 Relevant Algorithm Theories                                                                                                                         
                                                                                                                                                            
  Depthwise Separable Convolution                                                                                                                           
                                                                                                                                                            
  Standard convolution applies a single filter that operates across all input channels simultaneously, resulting in high parameter counts and computational 
  cost. Depthwise Separable Convolution (DSConv), introduced by Howard et al. in MobileNet, factorises this operation into two stages: a depthwise          
  convolution that applies a single filter per input channel independently, followed by a pointwise convolution (1×1 convolution) that linearly combines the
   depthwise outputs across channels.                                                                                                                       
                                                                                                                                                            
  For a standard convolution with input channels $C_{in}$, output channels $C_{out}$, and kernel size $K \times K$, the computational cost is $K^2 \cdot    
  C_{in} \cdot C_{out}$. DSConv reduces this to $K^2 \cdot C_{in} + C_{in} \cdot C_{out}$, achieving a reduction factor of approximately $1/C_{out} +       
  1/K^2$. For $K=3$ and typical channel sizes, this corresponds to roughly an 8–9× reduction in both parameters and multiply-accumulate operations, making  
  DSConv well-suited for resource-constrained embedded deployment.                                                                                          
                                                                                                                                                            
  ---                                                                                                                                                       
  Coordinate Attention                                                                                                                                   
                      
  Channel attention mechanisms such as Squeeze-and-Excitation (SE) networks recalibrate feature responses by modelling inter-channel dependencies through
  global average pooling, but this collapses all spatial information and loses positional context. Coordinate Attention (CoordAtt), proposed by Hou et al.,
  addresses this limitation by decomposing spatial information into two one-dimensional feature encodings along the horizontal and vertical axes            
  respectively.                                                                                                                                             
                                                                                                                                                            
  Specifically, given a feature map of size $C \times H \times W$, CoordAtt performs two separate pooling operations: one along the height dimension,       
  producing a $C \times H \times 1$ tensor, and one along the width dimension, producing a $C \times 1 \times W$ tensor. These are concatenated, passed     
  through a shared convolutional transformation, and then split back to generate two attention maps — one encoding horizontal context and one encoding      
  vertical context. The final output is the element-wise product of the input feature map with both attention maps.                                         
                                                                                                                                                            
  In the context of Log-Mel spectrograms, this design is particularly meaningful: the horizontal axis encodes temporal structure (cardiac cycle phases such 
  as S1/S2), while the vertical axis encodes frequency structure (harmonic components of heart sounds). CoordAtt therefore enables the model to attend to   
  both when and at what frequency relevant features occur, rather than treating the spectrogram as a generic 2D image.                                      
                                                                                                                                                            
  ---                                                                                                                                                       
  Signal Quality Assessment and Weighted Inference                                                                                                          
                                                                                                                                                         
  In real-world recording environments, heart sound signals are frequently contaminated by motion artefacts, breathing noise, and poor sensor contact,      
  producing segments of degraded quality that can mislead a diagnostic model. A Signal Quality Assessment (SQA) module is therefore incorporated as a pre-filter in the inference pipeline.                                                                                                                     
                                                                                                                                                            
  The SQA model shares the same LightweightCNN architecture as the diagnostic model and is trained on labelled quality annotations derived from the         
  PhysioNet 2016 dataset. It outputs a continuous probability $P(\text{Good})$ for each 2-second segment, representing the model's confidence that the      
  segment contains a clean, interpretable signal.                                                                                                           
                                                                                                                                                            
  Rather than applying a hard binary threshold to gate segments in or out, the system adopts a weighted average inference strategy. For a 20-second         
  recording chunk segmented into $N$ overlapping windows, the final diagnostic result is computed as:                                                       
                                                                                                                                                            
  $$\hat{y} = \frac{\sum_{i=1}^{N} P_i(\text{Good}) \cdot P_i(\text{Abnormal})}{\sum_{i=1}^{N} P_i(\text{Good})}$$                                          
                                                                                                                                                            
  where $P_i(\text{Abnormal})$ is the diagnostic model's output for segment $i$. This formulation naturally downweights noisy segments without discarding   
  them entirely, and avoids the need to tune a separate quality threshold at deployment time.                                                               
                                                                                                                                                            
  ---                                                                                                                                                       
  Post-Training Quantization                                                                                                                       
                                                                                                                                                            
  Deep learning models are typically trained using 32-bit floating-point (FP32) arithmetic, which places significant demands on memory bandwidth and     
  arithmetic throughput. Post-Training Quantization (PTQ) reduces model size and inference latency by mapping FP32 weights and activations to
  lower-precision integer representations after training, without requiring retraining.                                                                                                                                                                           
  In this work, dynamic range quantization is applied, converting model weights to 8-bit integers (INT8) while activations are quantised dynamically at     
  inference time. For a floating-point value $x$ with range $[\alpha, \beta]$, the quantised representation is:                                             
                                                                                                                                                         
  $$x_q = \text{round}\left(\frac{x - \alpha}{\beta - \alpha} \cdot (2^b - 1)\right)$$                                                                      
                                                                                                                                                            
  where $b$ is the bit-width. This reduces model size by approximately 75% and accelerates inference on hardware with efficient integer 
  arithmetic units, such as the ARM Cortex-A72 on the Raspberry Pi 4B. The accuracy impact of quantisation is evaluated empirically in Chapter 4 by         
  comparing FP32 and INT8 performance on the held-out test set.      



- **深度可分离卷积 (DSConv)**: 需引用 MobileNet 论文。
    
    - _格式示例_：图 2.x 深度可分离卷积结构示意图 [1]。
        
    - _对应文献_：CHS-Net: A Deep learning approach for hierarchical segmentation of COVID-19 infected CT images - Scientific Figure on ResearchGate. Available from: https://www.researchgate.net/figure/Standard-convolution-operation-vs-depthwise-separable-convolution-operation_fig4_347125085 [accessed 10 Apr 2026]
        
- **坐标注意力机制 (CoordAtt)**: 需引用 Hou 等人的论文。
    
    - _格式示例_：图 2.x 坐标注意力模块结构图 [2]。
        
    - _对应文献_：Cao, Yining & Li, Chao & Peng, Yakun & Ru, Huiying. (2023). MCS-YOLO: A Multiscale Object Detection Method for Autonomous Driving Road Environment Recognition. IEEE Access. PP. 1-1. 10.1109/ACCESS.2023.3252021. 
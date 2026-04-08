# FYP Thesis Draft

---

## Chapter 3: Dataset and Preprocessing

### 3.1 Dataset Overview
- PhysioNet/CinC Challenge 2016
- 数据集统计（Normal / Abnormal 数量、比例、来源）
- 类别不平衡问题说明（4:1）

### 3.2 Signal Preprocessing Pipeline
- 带通滤波（25–400 Hz，Butterworth）
- 滑动窗口分割（2s，50% overlap）
- Log-Mel 频谱图提取（32×64）

### 3.3 Signal Quality Assessment Dataset
- SQA 数据集构建（Good / Bad Quality 标注来源）
- 数据统计（8:1 不平衡）

### 3.4 Data Augmentation and Class Balancing
- WeightedRandomSampler 策略
- 数据增强方法

---

## Chapter 4: Model Design

### 4.1 Overall Architecture
- 双模型设计思路（SQA + 诊断解耦）
- 输入格式（1×32×64 Log-Mel 频谱图）

### 4.2 Lightweight CNN Backbone
- Depthwise Separable Convolution 结构
- 各层设计（通道数、卷积核大小）
- 参数量分析

### 4.3 Coordinate Attention Module
- 设计动机（为什么用 CoordAtt 而不是 SE Block）
- 模块结构（H/W 方向分离的空间注意力）
- 在模型中的插入位置

### 4.4 Signal Quality Assessment Model
- SQA 模型结构（与诊断模型的异同）
- 在推理 pipeline 中的作用

### 4.5 Model Quantization
- FP32 → INT8 量化方案（Post-Training Quantization）
- TFLite 转换流程
- 量化对模型大小的影响

---

## Chapter 5: Training and Experiments

### 5.1 Training Configuration
- 数据划分（80/10/10，按 recording 分组）
- 超参数设置（Epoch、Batch Size、LR、Scheduler）
- 评估指标说明（Sensitivity、Specificity、M-Score）

### 5.2 Diagnostic Model Results
- Run 1 基础训练结果
- Run 2（Label Smoothing + Early Stopping）对比
- 阈值分析

### 5.3 SQA Model Results
- 训练结果（Test M-Score / Se / Sp）

### 5.4 Ablation Study
- Baseline CNN（无注意力）
- + Coordinate Attention
- + Residual Connection
- 各步骤指标对比

### 5.5 Quantization Impact
- FP32 vs INT8 准确率对比
- 模型大小对比
- 推理延迟对比

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

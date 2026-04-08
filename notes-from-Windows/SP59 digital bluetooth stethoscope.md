**[Digital Bluetooth Stethoscope数字蓝牙听诊器]{.mark}**

**ID:** SP59\
**Program:** 3+1+1 students at NUSRI Suzhou\
**Academic Year:** AY 2025/2026 (September 2025 -- May 2026)

**Summary**

*(200 -- 400 words)*

The stethoscope is a critical instrument for doctors in diagnosis. In
this project, we aim to implement a **digital Bluetooth stethoscope**
that can mimic a mechanical stethoscope using a **microphone**. The
sensed signals will be transmitted and displayed **digitally**. The
collected data can be further analyzed using **AI** to aid in diagnosis.

**Project scope includes:项目范围包括**

1.  Literature review of stethoscopes文献综述

2.  Design and implementation of the digital Bluetooth
    stethoscope设计与实现

3.  Training a diagnosis model using available stethoscope
    datasets训练模型

4.  Designing a user interface (UI) to collect data from the stethoscope
    and apply AI analysis

**Expected learning outcomes for students:**预期学习成果

1.  Understanding the principles of stethoscopes工作原理

2.  Developing a working prototype

3.  Training an AI model based on stethoscope datasets

4.  Implementing a GUI for the prototype with an AI-aided diagnosis tool

**Achievable outcomes by FYP students:**可实现的成果

1.  A completed prototype with software GUI

2.  A trained AI model with good diagnosis accuracy

**Requirements:**要求

- Prior experience in software and hardware implementation is a must.

- If two students work on the project, each should focus on different
  designs while achieving the outcomes above.

**Prerequisites:**先决条件

- PCB design skills

- Embedded system development skills

**Student Workload Distribution**

  --------------------------------------------------------------
  **Student**   **Responsibility**
  ------------- ------------------------------------------------
  Student 1     Digital Bluetooth stethoscope prototype

  Student 2     Train the AI model, develop GUI, incorporate
                diagnosis tool
  --------------------------------------------------------------

**Supervisor:** Heng Chun Huat (<elehch@nus.edu.sg>)\
**Laboratory Work:** PCB, soldering, and hardware development\
**Number of Students:** 2

**Continuous Assessment (CA) Requirements**

  --------------------------------------------------------------
  **CA**   **Requirement**
  -------- -----------------------------------------------------
  CA1      Design the digital Bluetooth stethoscope prototype,
           train the AI model

  CA2      Prototype demonstration, GUI development
  --------------------------------------------------------------

**Keywords:** [keyword1; keyword2; keyword3; keyword4]{.mark}

[Contents最后记得更新整个目录]{.mark}

[1 Introduction [4](#introduction)](#introduction)

[1.1 Background [4](#background)](#background)

[2 Literature Review [7](#literature-review)](#literature-review)

[2.1 实验过程 [10](#实验过程)](#实验过程)

[2.1.1 模型更改前 [10](#模型更改前)](#模型更改前)

[2.1.2 更改模型后 [22](#更改模型后)](#更改模型后)

[2.1.3 打开数据集增强、优化器加入权重衰减、加入学习率调度器
[28](#打开数据集增强优化器加入权重衰减加入学习率调度器)](#打开数据集增强优化器加入权重衰减加入学习率调度器)

[2.1.4 加入测试集 [35](#加入测试集)](#加入测试集)

[2.1.5 Hop_length由32改成了64
[49](#hop_length由32改成了64)](#hop_length由32改成了64)

[2.1.6 量化 FP32 转化成 INT 8
[50](#量化-fp32-转化成-int-8)](#量化-fp32-转化成-int-8)

[References [51](#references)](#references)

[Appendices [52](#appendices)](#appendices)

# Introduction

## Background

听诊提供了一种非侵入性、低成本和便携的工作方式。

1.  **Principles of the Stethoscope**

**1. 1 Basic Acoustic Principles**

A stethoscope is an **acoustic transmission device** that uses
**air/solid media conduction and the principle of resonance.**
空气/固体介质传声和共振原理

The stethoscope does not "amplify" the sound energy itself, but enhances
the recognition of useful sounds by blocking ambient noise, matching
acoustic impedance, and selectively transmitting certain frequencies.
阻隔环境噪音、匹配声阻抗，并选择性地传输特定频率。

**1.2 Structure and Functional Principles**

![](./media/image1.png){width="3.7146719160104986in"
height="2.665277777777778in"}

Reference:

1.  Littmann D. *The stethoscope and its use.* Am J Cardiol.
    1963;11:104--117.

2.  F. Rappaport, H. Sprague. *The stethoscope and its variations.*
    Circulation.

<!-- -->

2.  **Medical Knowledge**

![The main parts of a stethoscope are the chest piece, flexible tubing
and metal ear tubes](./media/image2.jpeg){width="2.509017935258093in"
height="5.519444444444445in"}

**Cardiac Auscultation 心脏听诊**From *Harrison's Principles of Internal
Medicine*

1.  

<!-- -->

a)  Heart Sounds心音

    i.  The first heart sound S1：Closure of mitral and tricuspid
        valves. Intensity influenced by valve mobility, contractility,
        and PR interval.

    ii. The second heart sound S2：Closure of aortic (A2) and pulmonic
        (P2) valves. Normally splits with inspiration.

b)  Systolic Murmurs收缩期杂音

    i.  **Ejection (mid-systolic, crescendo--decrescendo)** 射血性杂音

    ii. **Holosystolic (pansystolic)** 全收缩期杂音

    iii. **Late systolic**收缩晚期杂音

c)  Diastolic Murmurs 舒张期杂音

    i.  Aortic regurgitation (AR)

    ii. Mitral stenosis (MS)

    iii. Pulmonic regurgitation (PR)

d)  Additional Heart Sounds

e)  Continuous Murmurs

f)  Dynamic Auscultation动态听诊

![图表 AI
生成的内容可能不正确。](./media/image3.png){width="3.9242377515310585in"
height="5.106237970253718in"}

图 246-4 心音

A.
正常。S₁：第一心音；S₂：第二心音；A₂：第二心音的主动脉成分；P₂：第二心音的肺动脉成分。

B. 房间隔缺损伴 S₂固定分裂。

C.
右束支传导阻滞（RBBB）、特发性肺动脉（PA）扩张时，S₂出现生理性但增宽的分裂，且吸气时分裂加重。

D. 左束支传导阻滞（LBBB）、主动脉瓣狭窄时，S₂出现逆分裂或反常分裂。

E. 肺动脉高压时，S₂出现接近固定的分裂。

![](./media/image4.png){width="6.268055555555556in"
height="1.6888888888888889in"}

2.  **Electrocardiography (ECG) 心电图**

![](./media/image5.png){width="6.778488626421697in"
height="2.800838801399825in"}

low energy

low cost

environment

# Literature Review

1.  已发表的论文

Huang, DM., Huang, J., Qiao, K. *et al.* Deep learning-based lung sound
analysis for intelligent stethoscope. *Military Med Res* **10**, 44
(2023). <https://doi.org/10.1186/s40779-023-00479-3>

Leng, S., Tan, R. S., Chai, K. T., Wang, C., Ghista, D., & Zhong, L.
(2015). The electronic stethoscope. *Biomedical engineering
online*, *14*, 66. https://doi.org/10.1186/s12938-015-0056-y

![](./media/image6.png){width="6.268055555555556in"
height="5.185416666666667in"}

2.  成熟的产品

- 3M Littmann

![3M™ Littmann® Stethoscopes and eMurmur® Partner to Launch New
Educational Apps](./media/image7.png){width="3.2311253280839893in"
height="1.2080916447944008in"}

- Eko

![Eko Health Raises \$41 Million to Scale AI-Driven Heart and Lung
Disease Detection](./media/image8.png){width="2.5317924321959757in"
height="1.3250349956255467in"}

![](./media/image9.png){width="6.668870297462817in"
height="3.470651793525809in"}

![](./media/image10.png){width="6.768055555555556in"
height="3.3986111111111112in"}

![文本 AI
生成的内容可能不正确。](./media/image11.png){width="6.8823053368328955in"
height="2.2890474628171478in"}

## 实验过程

### 模型更改前

![](./media/image12.png){width="6.268055555555556in"
height="4.6409722222222225in"}

你看下我跑出来的结果。我感觉模型在前几轮就优化到最佳了。感觉是模型限制了表现。所以改模型应该是对的思路。观察下来感觉Loss也是小的，不错不错
(FypProj) rae@Rae:/mnt/d/FypProj\$
/home/rae/micromamba/envs/FypProj/bin/python
/mnt/d/FypProj/src/train/train_lightweight.py

Using device: cuda

============================================================

\[CONFIG\] Using config.yaml at:

/mnt/d/FypProj/config.yaml

{\'data\': {\'bandpass\': {\'high\': 400, \'low\': 25},

          \'overlap\': 0.5,

          \'sample_rate\': 2000,

          \'segment_length\': 2.0},

 \'mel\': {\'fmax\': 400,

         \'fmin\': 20,

         \'hop_length\': 96,

         \'n_fft\': 256,

         \'n_mels\': 32,

         \'power\': 2.0,

         \'win_length\': 256}}

============================================================

\[Dataset\] 开始预处理音频并切片\...

\[Dataset\] 总音频数: 2876 \| 总切片数: 62003

\[Dataset\] 开始预处理音频并切片\...

\[Dataset\] 总音频数: 2876 \| 总切片数: 62003

\[Group Split by fname\]

  train samples = 49833

  val   samples = 12170

  unique train recordings = 2300

  unique val   recordings = 576

Epoch \[1/25\]

Train Loss: 0.2762 \| Train Acc: 0.8694                                 
           

Val   Loss: 0.2677 \| Val   Acc: 0.8698

\[Validation\] Confusion Matrix:

\[\[8966  538\]

 \[1047 1619\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.8954    0.9434    0.9188      9504

    Abnormal     0.7506    0.6073    0.6714      2666

    accuracy                         0.8698     12170

   macro avg     0.8230    0.7753    0.7951     12170

weighted avg     0.8637    0.8698    0.8646     12170

✅ New best model saved! Acc=0.8698

Epoch \[2/25\]

Train Loss: 0.2261 \| Train Acc: 0.8967                                 
           

Val   Loss: 0.2652 \| Val   Acc: 0.8701

\[Validation\] Confusion Matrix:

\[\[8319 1185\]

 \[ 396 2270\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9546    0.8753    0.9132      9504

    Abnormal     0.6570    0.8515    0.7417      2666

    accuracy                         0.8701     12170

   macro avg     0.8058    0.8634    0.8275     12170

weighted avg     0.8894    0.8701    0.8757     12170

✅ New best model saved! Acc=0.8701

Epoch \[3/25\]

Train Loss: 0.2056 \| Train Acc: 0.9057                                 
           

Val   Loss: 0.2597 \| Val   Acc: 0.8823

\[Validation\] Confusion Matrix:

\[\[8622  882\]

 \[ 550 2116\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9400    0.9072    0.9233      9504

    Abnormal     0.7058    0.7937    0.7472      2666

    accuracy                         0.8823     12170

   macro avg     0.8229    0.8504    0.8352     12170

weighted avg     0.8887    0.8823    0.8847     12170

✅ New best model saved! Acc=0.8823

Epoch \[4/25\]

Train Loss: 0.1944 \| Train Acc: 0.9125                                 
           

Val   Loss: 0.2594 \| Val   Acc: 0.8832

\[Validation\] Confusion Matrix:

\[\[8871  633\]

 \[ 789 1877\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9183    0.9334    0.9258      9504

    Abnormal     0.7478    0.7041    0.7253      2666

    accuracy                         0.8832     12170

   macro avg     0.8331    0.8187    0.8255     12170

weighted avg     0.8810    0.8832    0.8819     12170

✅ New best model saved! Acc=0.8832

Epoch \[5/25\]

Train Loss: 0.1816 \| Train Acc: 0.9184                                 
           

Val   Loss: 0.2583 \| Val   Acc: 0.8780

\[Validation\] Confusion Matrix:

\[\[8728  776\]

 \[ 709 1957\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9249    0.9184    0.9216      9504

    Abnormal     0.7161    0.7341    0.7249      2666

    accuracy                         0.8780     12170

   macro avg     0.8205    0.8262    0.8233     12170

weighted avg     0.8791    0.8780    0.8785     12170

Epoch \[6/25\]

Train Loss: 0.1738 \| Train Acc: 0.9228                                 
           

Val   Loss: 0.2763 \| Val   Acc: 0.8765

\[Validation\] Confusion Matrix:

\[\[8464 1040\]

 \[ 463 2203\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9481    0.8906    0.9185      9504

    Abnormal     0.6793    0.8263    0.7456      2666

    accuracy                         0.8765     12170

   macro avg     0.8137    0.8585    0.8320     12170

weighted avg     0.8892    0.8765    0.8806     12170

Epoch \[7/25\]

Train Loss: 0.1652 \| Train Acc: 0.9273                                 
           

Val   Loss: 0.2559 \| Val   Acc: 0.8800

\[Validation\] Confusion Matrix:

\[\[8704  800\]

 \[ 660 2006\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9295    0.9158    0.9226      9504

    Abnormal     0.7149    0.7524    0.7332      2666

    accuracy                         0.8800     12170

   macro avg     0.8222    0.8341    0.8279     12170

weighted avg     0.8825    0.8800    0.8811     12170

Epoch \[8/25\]

Train Loss: 0.1588 \| Train Acc: 0.9318                                 
           

Val   Loss: 0.2627 \| Val   Acc: 0.8786

\[Validation\] Confusion Matrix:

\[\[8600  904\]

 \[ 573 2093\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9375    0.9049    0.9209      9504

    Abnormal     0.6984    0.7851    0.7392      2666

    accuracy                         0.8786     12170

   macro avg     0.8179    0.8450    0.8301     12170

weighted avg     0.8851    0.8786    0.8811     12170

Epoch \[9/25\]

Train Loss: 0.1572 \| Train Acc: 0.9308                                 
           

Val   Loss: 0.2684 \| Val   Acc: 0.8822

\[Validation\] Confusion Matrix:

\[\[8639  865\]

 \[ 569 2097\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9382    0.9090    0.9234      9504

    Abnormal     0.7080    0.7866    0.7452      2666

    accuracy                         0.8822     12170

   macro avg     0.8231    0.8478    0.8343     12170

weighted avg     0.8878    0.8822    0.8843     12170

Epoch \[10/25\]

Train Loss: 0.1504 \| Train Acc: 0.9342                                 
           

Val   Loss: 0.2691 \| Val   Acc: 0.8781

\[Validation\] Confusion Matrix:

\[\[8926  578\]

 \[ 906 1760\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9079    0.9392    0.9233      9504

    Abnormal     0.7528    0.6602    0.7034      2666

    accuracy                         0.8781     12170

   macro avg     0.8303    0.7997    0.8133     12170

weighted avg     0.8739    0.8781    0.8751     12170

Epoch \[11/25\]

Train Loss: 0.1466 \| Train Acc: 0.9370                                 
           

Val   Loss: 0.2680 \| Val   Acc: 0.8819

\[Validation\] Confusion Matrix:

\[\[8842  662\]

 \[ 775 1891\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9194    0.9303    0.9248      9504

    Abnormal     0.7407    0.7093    0.7247      2666

    accuracy                         0.8819     12170

   macro avg     0.8301    0.8198    0.8248     12170

weighted avg     0.8803    0.8819    0.8810     12170

Epoch \[12/25\]

Train Loss: 0.1436 \| Train Acc: 0.9384                                 
           

Val   Loss: 0.3047 \| Val   Acc: 0.8728

\[Validation\] Confusion Matrix:

\[\[8341 1163\]

 \[ 385 2281\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9559    0.8776    0.9151      9504

    Abnormal     0.6623    0.8556    0.7466      2666

    accuracy                         0.8728     12170

   macro avg     0.8091    0.8666    0.8309     12170

weighted avg     0.8916    0.8728    0.8782     12170

Epoch \[13/25\]

Train Loss: 0.1414 \| Train Acc: 0.9390                                 
           

Val   Loss: 0.2796 \| Val   Acc: 0.8780

\[Validation\] Confusion Matrix:

\[\[9032  472\]

 \[1013 1653\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.8992    0.9503    0.9240      9504

    Abnormal     0.7779    0.6200    0.6900      2666

    accuracy                         0.8780     12170

   macro avg     0.8385    0.7852    0.8070     12170

weighted avg     0.8726    0.8780    0.8728     12170

Epoch \[14/25\]

Train Loss: 0.1376 \| Train Acc: 0.9404                                 
           

Val   Loss: 0.2850 \| Val   Acc: 0.8869

\[Validation\] Confusion Matrix:

\[\[9022  482\]

 \[ 894 1772\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9098    0.9493    0.9291      9504

    Abnormal     0.7862    0.6647    0.7203      2666

    accuracy                         0.8869     12170

   macro avg     0.8480    0.8070    0.8247     12170

weighted avg     0.8827    0.8869    0.8834     12170

✅ New best model saved! Acc=0.8869

Epoch \[15/25\]

Train Loss: 0.1334 \| Train Acc: 0.9424                                 
           

Val   Loss: 0.2809 \| Val   Acc: 0.8877

\[Validation\] Confusion Matrix:

\[\[8993  511\]

 \[ 856 1810\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9131    0.9462    0.9294      9504

    Abnormal     0.7798    0.6789    0.7259      2666

    accuracy                         0.8877     12170

   macro avg     0.8465    0.8126    0.8276     12170

weighted avg     0.8839    0.8877    0.8848     12170

✅ New best model saved! Acc=0.8877

Epoch \[16/25\]

Train Loss: 0.1302 \| Train Acc: 0.9437                                 
           

Val   Loss: 0.2737 \| Val   Acc: 0.8897

\[Validation\] Confusion Matrix:

\[\[8848  656\]

 \[ 686 1980\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9280    0.9310    0.9295      9504

    Abnormal     0.7511    0.7427    0.7469      2666

    accuracy                         0.8897     12170

   macro avg     0.8396    0.8368    0.8382     12170

weighted avg     0.8893    0.8897    0.8895     12170

✅ New best model saved! Acc=0.8897

Epoch \[17/25\]

Train Loss: 0.1292 \| Train Acc: 0.9442                                 
           

Val   Loss: 0.2862 \| Val   Acc: 0.8832

\[Validation\] Confusion Matrix:

\[\[8954  550\]

 \[ 872 1794\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9113    0.9421    0.9264      9504

    Abnormal     0.7654    0.6729    0.7162      2666

    accuracy                         0.8832     12170

   macro avg     0.8383    0.8075    0.8213     12170

weighted avg     0.8793    0.8832    0.8804     12170

Epoch \[18/25\]

Train Loss: 0.1264 \| Train Acc: 0.9456                                 
           

Val   Loss: 0.2768 \| Val   Acc: 0.8882

\[Validation\] Confusion Matrix:

\[\[8842  662\]

 \[ 699 1967\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9267    0.9303    0.9285      9504

    Abnormal     0.7482    0.7378    0.7430      2666

    accuracy                         0.8882     12170

   macro avg     0.8375    0.8341    0.8358     12170

weighted avg     0.8876    0.8882    0.8879     12170

Epoch \[19/25\]

Train Loss: 0.1246 \| Train Acc: 0.9464                                 
           

Val   Loss: 0.2693 \| Val   Acc: 0.8848

\[Validation\] Confusion Matrix:

\[\[8875  629\]

 \[ 773 1893\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9199    0.9338    0.9268      9504

    Abnormal     0.7506    0.7101    0.7298      2666

    accuracy                         0.8848     12170

   macro avg     0.8352    0.8219    0.8283     12170

weighted avg     0.8828    0.8848    0.8836     12170

Epoch \[20/25\]

Train Loss: 0.1227 \| Train Acc: 0.9482                                 
           

Val   Loss: 0.2885 \| Val   Acc: 0.8797

\[Validation\] Confusion Matrix:

\[\[8644  860\]

 \[ 604 2062\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9347    0.9095    0.9219      9504

    Abnormal     0.7057    0.7734    0.7380      2666

    accuracy                         0.8797     12170

   macro avg     0.8202    0.8415    0.8300     12170

weighted avg     0.8845    0.8797    0.8816     12170

Epoch \[21/25\]

Train Loss: 0.1190 \| Train Acc: 0.9506                                 
           

Val   Loss: 0.2861 \| Val   Acc: 0.8827

\[Validation\] Confusion Matrix:

\[\[8671  833\]

 \[ 595 2071\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9358    0.9124    0.9239      9504

    Abnormal     0.7132    0.7768    0.7436      2666

    accuracy                         0.8827     12170

   macro avg     0.8245    0.8446    0.8338     12170

weighted avg     0.8870    0.8827    0.8844     12170

Epoch \[22/25\]

Train Loss: 0.1170 \| Train Acc: 0.9510                                 
           

Val   Loss: 0.2843 \| Val   Acc: 0.8848

\[Validation\] Confusion Matrix:

\[\[8911  593\]

 \[ 809 1857\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9168    0.9376    0.9271      9504

    Abnormal     0.7580    0.6965    0.7260      2666

    accuracy                         0.8848     12170

   macro avg     0.8374    0.8171    0.8265     12170

weighted avg     0.8820    0.8848    0.8830     12170

Epoch \[23/25\]

Train Loss: 0.1165 \| Train Acc: 0.9499                                 
           

Val   Loss: 0.3090 \| Val   Acc: 0.8787

\[Validation\] Confusion Matrix:

\[\[8582  922\]

 \[ 554 2112\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9394    0.9030    0.9208      9504

    Abnormal     0.6961    0.7922    0.7411      2666

    accuracy                         0.8787     12170

   macro avg     0.8177    0.8476    0.8309     12170

weighted avg     0.8861    0.8787    0.8814     12170

Epoch \[24/25\]

Train Loss: 0.1138 \| Train Acc: 0.9524                                 
           

Val   Loss: 0.2853 \| Val   Acc: 0.8855

\[Validation\] Confusion Matrix:

\[\[8835  669\]

 \[ 725 1941\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9242    0.9296    0.9269      9504

    Abnormal     0.7437    0.7281    0.7358      2666

    accuracy                         0.8855     12170

   macro avg     0.8339    0.8288    0.8313     12170

weighted avg     0.8846    0.8855    0.8850     12170

Epoch \[25/25\]

Train Loss: 0.1119 \| Train Acc: 0.9523                                 
           

Val   Loss: 0.2884 \| Val   Acc: 0.8867

\[Validation\] Confusion Matrix:

\[\[8839  665\]

 \[ 714 1952\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9253    0.9300    0.9276      9504

    Abnormal     0.7459    0.7322    0.7390      2666

    accuracy                         0.8867     12170

   macro avg     0.8356    0.8311    0.8333     12170

weighted avg     0.8860    0.8867    0.8863     12170

Training finished. Best Val Acc=0.8897

Model saved to: /mnt/d/FypProj/checkpoints/best_model.pth

### 更改模型后

![图形用户界面, 文本 AI
生成的内容可能不正确。](./media/image13.png){width="6.268055555555556in"
height="1.086111111111111in"}

换成你说的模型了，但是好像过拟合了

(FypProj) rae@Rae:/mnt/d/FypProj\$
/home/rae/micromamba/envs/FypProj/bin/python
/mnt/d/FypProj/src/train/train_lightweight.py

Using device: cuda

============================================================

\[CONFIG\] Using config.yaml at:

/mnt/d/FypProj/config.yaml

{\'data\': {\'bandpass\': {\'high\': 400, \'low\': 25},

          \'overlap\': 0.5,

          \'sample_rate\': 2000,

          \'segment_length\': 2.0},

 \'mel\': {\'fmax\': 400,

         \'fmin\': 20,

         \'hop_length\': 96,

         \'n_fft\': 256,

         \'n_mels\': 32,

         \'power\': 2.0,

         \'win_length\': 256}}

============================================================

\[Dataset\] 开始预处理音频并切片\...

\[Dataset\] 总音频数: 2876 \| 总切片数: 62003

\[Dataset\] 开始预处理音频并切片\...

\[Dataset\] 总音频数: 2876 \| 总切片数: 62003

\[Group Split by fname\]

  train samples = 49833

  val   samples = 12170

  unique train recordings = 2300

  unique val   recordings = 576

Epoch \[1/25\]

Train Loss: 0.2340 \| Train Acc: 0.8874                                 

Val   Loss: 0.2360 \| Val   Acc: 0.8894

\[Validation\] Confusion Matrix:

\[\[8880  624\]

 \[ 722 1944\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9248    0.9343    0.9296      9504

    Abnormal     0.7570    0.7292    0.7428      2666

    accuracy                         0.8894     12170

   macro avg     0.8409    0.8318    0.8362     12170

weighted avg     0.8880    0.8894    0.8886     12170

✅ New best model saved! Acc=0.8894

Epoch \[2/25\]

Train Loss: 0.1859 \| Train Acc: 0.9139                                 

Val   Loss: 0.2860 \| Val   Acc: 0.8819

\[Validation\] Confusion Matrix:

\[\[9000  504\]

 \[ 933 1733\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9061    0.9470    0.9261      9504

    Abnormal     0.7747    0.6500    0.7069      2666

    accuracy                         0.8819     12170

   macro avg     0.8404    0.7985    0.8165     12170

weighted avg     0.8773    0.8819    0.8781     12170

Epoch \[3/25\]

Train Loss: 0.1653 \| Train Acc: 0.9234                                 

Val   Loss: 0.2641 \| Val   Acc: 0.8781

\[Validation\] Confusion Matrix:

\[\[9108  396\]

 \[1088 1578\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.8933    0.9583    0.9247      9504

    Abnormal     0.7994    0.5919    0.6802      2666

    accuracy                         0.8781     12170

   macro avg     0.8463    0.7751    0.8024     12170

weighted avg     0.8727    0.8781    0.8711     12170

Epoch \[4/25\]

Train Loss: 0.1463 \| Train Acc: 0.9346                                 

Val   Loss: 0.2624 \| Val   Acc: 0.8917

\[Validation\] Confusion Matrix:

\[\[9039  465\]

 \[ 853 1813\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9138    0.9511    0.9320      9504

    Abnormal     0.7959    0.6800    0.7334      2666

    accuracy                         0.8917     12170

   macro avg     0.8548    0.8156    0.8327     12170

weighted avg     0.8879    0.8917    0.8885     12170

✅ New best model saved! Acc=0.8917

Epoch \[5/25\]

Train Loss: 0.1326 \| Train Acc: 0.9414                                 

Val   Loss: 0.2994 \| Val   Acc: 0.8892

\[Validation\] Confusion Matrix:

\[\[8995  509\]

 \[ 839 1827\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9147    0.9464    0.9303      9504

    Abnormal     0.7821    0.6853    0.7305      2666

    accuracy                         0.8892     12170

   macro avg     0.8484    0.8159    0.8304     12170

weighted avg     0.8856    0.8892    0.8865     12170

Epoch \[6/25\]

Train Loss: 0.1210 \| Train Acc: 0.9478                                 

Val   Loss: 0.2624 \| Val   Acc: 0.8924

\[Validation\] Confusion Matrix:

\[\[8864  640\]

 \[ 670 1996\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9297    0.9327    0.9312      9504

    Abnormal     0.7572    0.7487    0.7529      2666

    accuracy                         0.8924     12170

   macro avg     0.8435    0.8407    0.8421     12170

weighted avg     0.8919    0.8924    0.8921     12170

✅ New best model saved! Acc=0.8924

Epoch \[7/25\]

Train Loss: 0.1122 \| Train Acc: 0.9514                                 

Val   Loss: 0.2964 \| Val   Acc: 0.8866

\[Validation\] Confusion Matrix:

\[\[9024  480\]

 \[ 900 1766\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9093    0.9495    0.9290      9504

    Abnormal     0.7863    0.6624    0.7191      2666

    accuracy                         0.8866     12170

   macro avg     0.8478    0.8060    0.8240     12170

weighted avg     0.8824    0.8866    0.8830     12170

Epoch \[8/25\]

Train Loss: 0.1044 \| Train Acc: 0.9546                                 

Val   Loss: 0.3136 \| Val   Acc: 0.8901

\[Validation\] Confusion Matrix:

\[\[8913  591\]

 \[ 746 1920\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9228    0.9378    0.9302      9504

    Abnormal     0.7646    0.7202    0.7417      2666

    accuracy                         0.8901     12170

   macro avg     0.8437    0.8290    0.8360     12170

weighted avg     0.8881    0.8901    0.8889     12170

Epoch \[9/25\]

Train Loss: 0.0953 \| Train Acc: 0.9597                                 

Val   Loss: 0.3092 \| Val   Acc: 0.8906

\[Validation\] Confusion Matrix:

\[\[8886  618\]

 \[ 714 1952\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9256    0.9350    0.9303      9504

    Abnormal     0.7595    0.7322    0.7456      2666

    accuracy                         0.8906     12170

   macro avg     0.8426    0.8336    0.8379     12170

weighted avg     0.8892    0.8906    0.8898     12170

Epoch \[10/25\]

Train Loss: 0.0892 \| Train Acc: 0.9623                                 

Val   Loss: 0.3353 \| Val   Acc: 0.8880

\[Validation\] Confusion Matrix:

\[\[9015  489\]

 \[ 874 1792\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9116    0.9485    0.9297      9504

    Abnormal     0.7856    0.6722    0.7245      2666

    accuracy                         0.8880     12170

   macro avg     0.8486    0.8104    0.8271     12170

weighted avg     0.8840    0.8880    0.8848     12170

### 打开数据集增强、优化器加入权重衰减、加入学习率调度器

![表格 AI
生成的内容可能不正确。](./media/image14.png){width="5.521604330708661in"
height="5.167387357830271in"}

\# 修改前

optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)

\# 修改后 (建议值 1e-4)

optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE,
weight_decay=1e-4)

\# 在优化器定义后加入

scheduler = torch.optim.lr_scheduler.ReduceLROnPlateau(optimizer,
mode=\'max\', factor=0.5, patience=3, verbose=True)

\# 在每个 Epoch 的 evaluate 之后更新

\# val_acc, val_loss, \... = evaluate(\...)

scheduler.step(val_acc)

(FypProj) rae@Rae:/mnt/d/FypProj\$
/home/rae/micromamba/envs/FypProj/bin/python
/mnt/d/FypProj/src/train/train_lightweight.py

Using device: cuda

============================================================

\[CONFIG\] Using config.yaml at:

/mnt/d/FypProj/config.yaml

{\'data\': {\'bandpass\': {\'high\': 400, \'low\': 25},

          \'overlap\': 0.5,

          \'sample_rate\': 2000,

          \'segment_length\': 2.0},

 \'mel\': {\'fmax\': 400,

         \'fmin\': 20,

         \'hop_length\': 96,

         \'n_fft\': 256,

         \'n_mels\': 32,

         \'power\': 2.0,

         \'win_length\': 256}}

============================================================

\[Dataset\] 开始预处理音频并切片\...

\[Dataset\] 总音频数: 2876 \| 总切片数: 62003

\[Dataset\] 开始预处理音频并切片\...

\[Dataset\] 总音频数: 2876 \| 总切片数: 62003

\[Group Split by fname\]

  train samples = 49833

  val   samples = 12170

  unique train recordings = 2300

  unique val   recordings = 576

Epoch \[1/25\]

Train Loss: 0.2509 \| Train Acc: 0.8782                                 
           

Val   Loss: 0.2428 \| Val   Acc: 0.8724

\[Validation\] Confusion Matrix:

\[\[8411 1093\]

 \[ 460 2206\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9481    0.8850    0.9155      9504

    Abnormal     0.6687    0.8275    0.7396      2666

    accuracy                         0.8724     12170

   macro avg     0.8084    0.8562    0.8276     12170

weighted avg     0.8869    0.8724    0.8770     12170

✅ New best model saved! Acc=0.8724

Epoch \[2/25\]

Train Loss: 0.2071 \| Train Acc: 0.9027                                 
           

Val   Loss: 0.2391 \| Val   Acc: 0.8786

\[Validation\] Confusion Matrix:

\[\[8567  937\]

 \[ 541 2125\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9406    0.9014    0.9206      9504

    Abnormal     0.6940    0.7971    0.7420      2666

    accuracy                         0.8786     12170

   macro avg     0.8173    0.8492    0.8313     12170

weighted avg     0.8866    0.8786    0.8815     12170

✅ New best model saved! Acc=0.8786

Epoch \[3/25\]

Train Loss: 0.1929 \| Train Acc: 0.9099                                 
           

Val   Loss: 0.2441 \| Val   Acc: 0.8815

\[Validation\] Confusion Matrix:

\[\[8754  750\]

 \[ 692 1974\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9267    0.9211    0.9239      9504

    Abnormal     0.7247    0.7404    0.7325      2666

    accuracy                         0.8815     12170

   macro avg     0.8257    0.8308    0.8282     12170

weighted avg     0.8825    0.8815    0.8820     12170

✅ New best model saved! Acc=0.8815

Epoch \[4/25\]

Train Loss: 0.1810 \| Train Acc: 0.9166                                 
           

Val   Loss: 0.2474 \| Val   Acc: 0.8822

\[Validation\] Confusion Matrix:

\[\[8914  590\]

 \[ 844 1822\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9135    0.9379    0.9256      9504

    Abnormal     0.7554    0.6834    0.7176      2666

    accuracy                         0.8822     12170

   macro avg     0.8344    0.8107    0.8216     12170

weighted avg     0.8789    0.8822    0.8800     12170

✅ New best model saved! Acc=0.8822

Epoch \[5/25\]

Train Loss: 0.1734 \| Train Acc: 0.9208                                 
           

Val   Loss: 0.2411 \| Val   Acc: 0.8828

\[Validation\] Confusion Matrix:

\[\[8821  683\]

 \[ 743 1923\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9223    0.9281    0.9252      9504

    Abnormal     0.7379    0.7213    0.7295      2666

    accuracy                         0.8828     12170

   macro avg     0.8301    0.8247    0.8274     12170

weighted avg     0.8819    0.8828    0.8823     12170

✅ New best model saved! Acc=0.8828

Epoch \[6/25\]

Train Loss: 0.1657 \| Train Acc: 0.9246                                 
           

Val   Loss: 0.2469 \| Val   Acc: 0.8860

\[Validation\] Confusion Matrix:

\[\[8653  851\]

 \[ 536 2130\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9417    0.9105    0.9258      9504

    Abnormal     0.7145    0.7989    0.7544      2666

    accuracy                         0.8860     12170

   macro avg     0.8281    0.8547    0.8401     12170

weighted avg     0.8919    0.8860    0.8882     12170

✅ New best model saved! Acc=0.8860

Epoch \[7/25\]

Train Loss: 0.1605 \| Train Acc: 0.9290                                 
           

Val   Loss: 0.2561 \| Val   Acc: 0.8867

\[Validation\] Confusion Matrix:

\[\[8780  724\]

 \[ 655 2011\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9306    0.9238    0.9272      9504

    Abnormal     0.7353    0.7543    0.7447      2666

    accuracy                         0.8867     12170

   macro avg     0.8329    0.8391    0.8359     12170

weighted avg     0.8878    0.8867    0.8872     12170

✅ New best model saved! Acc=0.8867

Epoch \[8/25\]

Train Loss: 0.1551 \| Train Acc: 0.9306                                 
           

Val   Loss: 0.2964 \| Val   Acc: 0.8800

\[Validation\] Confusion Matrix:

\[\[8689  815\]

 \[ 645 2021\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9309    0.9142    0.9225      9504

    Abnormal     0.7126    0.7581    0.7346      2666

    accuracy                         0.8800     12170

   macro avg     0.8218    0.8362    0.8286     12170

weighted avg     0.8831    0.8800    0.8813     12170

Epoch \[9/25\]

Train Loss: 0.1508 \| Train Acc: 0.9342                                 
           

Val   Loss: 0.2624 \| Val   Acc: 0.8825

\[Validation\] Confusion Matrix:

\[\[8785  719\]

 \[ 711 1955\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9251    0.9243    0.9247      9504

    Abnormal     0.7311    0.7333    0.7322      2666

    accuracy                         0.8825     12170

   macro avg     0.8281    0.8288    0.8285     12170

weighted avg     0.8826    0.8825    0.8826     12170

Epoch \[10/25\]

Train Loss: 0.1448 \| Train Acc: 0.9354                                 
           

Val   Loss: 0.2794 \| Val   Acc: 0.8784

\[Validation\] Confusion Matrix:

\[\[8629  875\]

 \[ 605 2061\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9345    0.9079    0.9210      9504

    Abnormal     0.7020    0.7731    0.7358      2666

    accuracy                         0.8784     12170

   macro avg     0.8182    0.8405    0.8284     12170

weighted avg     0.8835    0.8784    0.8804     12170

Epoch \[11/25\]

Train Loss: 0.1427 \| Train Acc: 0.9370                                 
           

Val   Loss: 0.2537 \| Val   Acc: 0.8845

\[Validation\] Confusion Matrix:

\[\[8594  910\]

 \[ 496 2170\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9454    0.9043    0.9244      9504

    Abnormal     0.7045    0.8140    0.7553      2666

    accuracy                         0.8845     12170

   macro avg     0.8250    0.8591    0.8398     12170

weighted avg     0.8927    0.8845    0.8873     12170

Epoch \[12/25\]

Train Loss: 0.1269 \| Train Acc: 0.9446                                 
           

Val   Loss: 0.2846 \| Val   Acc: 0.8812

\[Validation\] Confusion Matrix:

\[\[8883  621\]

 \[ 825 1841\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9150    0.9347    0.9247      9504

    Abnormal     0.7478    0.6905    0.7180      2666

    accuracy                         0.8812     12170

   macro avg     0.8314    0.8126    0.8214     12170

weighted avg     0.8784    0.8812    0.8795     12170

Epoch \[13/25\]

Train Loss: 0.1202 \| Train Acc: 0.9482                                 
           

Val   Loss: 0.3172 \| Val   Acc: 0.8774

\[Validation\] Confusion Matrix:

\[\[8597  907\]

 \[ 585 2081\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9363    0.9046    0.9202      9504

    Abnormal     0.6965    0.7806    0.7361      2666

    accuracy                         0.8774     12170

   macro avg     0.8164    0.8426    0.8281     12170

weighted avg     0.8837    0.8774    0.8798     12170

Epoch \[14/25\]

Train Loss: 0.1158 \| Train Acc: 0.9508                                 
           

Val   Loss: 0.2949 \| Val   Acc: 0.8791

\[Validation\] Confusion Matrix:

\[\[8741  763\]

 \[ 708 1958\]\]

\[Validation\] Classification Report:

              precision    recall  f1-score   support

      Normal     0.9251    0.9197    0.9224      9504

    Abnormal     0.7196    0.7344    0.7269      2666

    accuracy                         0.8791     12170

   macro avg     0.8223    0.8271    0.8247     12170

weighted avg     0.8801    0.8791    0.8796     12170

### 加入测试集

(FypProj) rae@Rae:/mnt/d/FypProj\$
/home/rae/micromamba/envs/FypProj/bin/python
/mnt/d/FypProj/src/train/train_lightweight_with_test.py

Using device: cuda

============================================================

\[CONFIG\] Using config.yaml at:

/mnt/d/FypProj/config.yaml

{\'data\': {\'bandpass\': {\'high\': 400, \'low\': 25},

\'overlap\': 0.5,

\'sample_rate\': 2000,

\'segment_length\': 2.0},

\'mel\': {\'fmax\': 400,

\'fmin\': 20,

\'hop_length\': 96,

\'n_fft\': 256,

\'n_mels\': 32,

\'power\': 2.0,

\'win_length\': 256}}

============================================================

\[Dataset\] 开始预处理音频并切片\...

\[Dataset\] 总音频数: 2876 \| 总切片数: 62003

\[Dataset\] 开始预处理音频并切片\...

\[Dataset\] 总音频数: 2876 \| 总切片数: 62003

\[Group Split by fname (80/10/10)\]

train samples = 49833 \| val samples = 5897 \| test samples = 6273

Epoch \[1/25\]

Train Loss: 0.2531 \| Train Acc: 0.8763

Val Loss: 0.2360 \| Val Acc: 0.8857

\[Validation\] Confusion Matrix:

\[\[4053 362\]

\[ 312 1170\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9285 0.9180 0.9232 4415

Abnormal 0.7637 0.7895 0.7764 1482

accuracy 0.8857 5897

macro avg 0.8461 0.8537 0.8498 5897

weighted avg 0.8871 0.8857 0.8863 5897

✅ New best model saved! Acc=0.8857

Epoch \[2/25\]

Train Loss: 0.2085 \| Train Acc: 0.9011

Val Loss: 0.2194 \| Val Acc: 0.8976

\[Validation\] Confusion Matrix:

\[\[4189 226\]

\[ 378 1104\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9172 0.9488 0.9328 4415

Abnormal 0.8301 0.7449 0.7852 1482

accuracy 0.8976 5897

macro avg 0.8737 0.8469 0.8590 5897

weighted avg 0.8953 0.8976 0.8957 5897

✅ New best model saved! Acc=0.8976

Epoch \[3/25\]

Train Loss: 0.1925 \| Train Acc: 0.9098

Val Loss: 0.2197 \| Val Acc: 0.8937

\[Validation\] Confusion Matrix:

\[\[4168 247\]

\[ 380 1102\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9164 0.9441 0.9300 4415

Abnormal 0.8169 0.7436 0.7785 1482

accuracy 0.8937 5897

macro avg 0.8667 0.8438 0.8543 5897

weighted avg 0.8914 0.8937 0.8920 5897

Epoch \[4/25\]

Train Loss: 0.1822 \| Train Acc: 0.9154

Val Loss: 0.2371 \| Val Acc: 0.8957

\[Validation\] Confusion Matrix:

\[\[4155 260\]

\[ 355 1127\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9213 0.9411 0.9311 4415

Abnormal 0.8125 0.7605 0.7856 1482

accuracy 0.8957 5897

macro avg 0.8669 0.8508 0.8584 5897

weighted avg 0.8940 0.8957 0.8945 5897

Epoch \[5/25\]

Train Loss: 0.1738 \| Train Acc: 0.9206

Val Loss: 0.2240 \| Val Acc: 0.8942

\[Validation\] Confusion Matrix:

\[\[4222 193\]

\[ 431 1051\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9074 0.9563 0.9312 4415

Abnormal 0.8449 0.7092 0.7711 1482

accuracy 0.8942 5897

macro avg 0.8761 0.8327 0.8511 5897

weighted avg 0.8917 0.8942 0.8910 5897

Epoch \[6/25\]

Train Loss: 0.1648 \| Train Acc: 0.9235

Val Loss: 0.2389 \| Val Acc: 0.8877

\[Validation\] Confusion Matrix:

\[\[4268 147\]

\[ 515 967\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.8923 0.9667 0.9280 4415

Abnormal 0.8680 0.6525 0.7450 1482

accuracy 0.8877 5897

macro avg 0.8802 0.8096 0.8365 5897

weighted avg 0.8862 0.8877 0.8820 5897

Epoch \[7/25\]

Train Loss: 0.1431 \| Train Acc: 0.9361

Val Loss: 0.2595 \| Val Acc: 0.8998

\[Validation\] Confusion Matrix:

\[\[4215 200\]

\[ 391 1091\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9151 0.9547 0.9345 4415

Abnormal 0.8451 0.7362 0.7869 1482

accuracy 0.8998 5897

macro avg 0.8801 0.8454 0.8607 5897

weighted avg 0.8975 0.8998 0.8974 5897

✅ New best model saved! Acc=0.8998

Epoch \[8/25\]

Train Loss: 0.1388 \| Train Acc: 0.9377

Val Loss: 0.2471 \| Val Acc: 0.8957

\[Validation\] Confusion Matrix:

\[\[4229 186\]

\[ 429 1053\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9079 0.9579 0.9322 4415

Abnormal 0.8499 0.7105 0.7740 1482

accuracy 0.8957 5897

macro avg 0.8789 0.8342 0.8531 5897

weighted avg 0.8933 0.8957 0.8924 5897

Epoch \[9/25\]

Train Loss: 0.1314 \| Train Acc: 0.9415

Val Loss: 0.2562 \| Val Acc: 0.9013

\[Validation\] Confusion Matrix:

\[\[4239 176\]

\[ 406 1076\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9126 0.9601 0.9358 4415

Abnormal 0.8594 0.7260 0.7871 1482

accuracy 0.9013 5897

macro avg 0.8860 0.8431 0.8614 5897

weighted avg 0.8992 0.9013 0.8984 5897

✅ New best model saved! Acc=0.9013

Epoch \[10/25\]

Train Loss: 0.1286 \| Train Acc: 0.9439

Val Loss: 0.2357 \| Val Acc: 0.9020

\[Validation\] Confusion Matrix:

\[\[4230 185\]

\[ 393 1089\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9150 0.9581 0.9360 4415

Abnormal 0.8548 0.7348 0.7903 1482

accuracy 0.9020 5897

macro avg 0.8849 0.8465 0.8632 5897

weighted avg 0.8999 0.9020 0.8994 5897

✅ New best model saved! Acc=0.9020

Epoch \[11/25\]

Train Loss: 0.1222 \| Train Acc: 0.9478

Val Loss: 0.2349 \| Val Acc: 0.9045

\[Validation\] Confusion Matrix:

\[\[4194 221\]

\[ 342 1140\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9246 0.9499 0.9371 4415

Abnormal 0.8376 0.7692 0.8020 1482

accuracy 0.9045 5897

macro avg 0.8811 0.8596 0.8695 5897

weighted avg 0.9027 0.9045 0.9031 5897

✅ New best model saved! Acc=0.9045

Epoch \[12/25\]

Train Loss: 0.1232 \| Train Acc: 0.9479

Val Loss: 0.2417 \| Val Acc: 0.9064

\[Validation\] Confusion Matrix:

\[\[4224 191\]

\[ 361 1121\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9213 0.9567 0.9387 4415

Abnormal 0.8544 0.7564 0.8024 1482

accuracy 0.9064 5897

macro avg 0.8878 0.8566 0.8706 5897

weighted avg 0.9045 0.9064 0.9044 5897

✅ New best model saved! Acc=0.9064

Epoch \[13/25\]

Train Loss: 0.1184 \| Train Acc: 0.9477

Val Loss: 0.2310 \| Val Acc: 0.9069

\[Validation\] Confusion Matrix:

\[\[4122 293\]

\[ 256 1226\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9415 0.9336 0.9376 4415

Abnormal 0.8071 0.8273 0.8171 1482

accuracy 0.9069 5897

macro avg 0.8743 0.8804 0.8773 5897

weighted avg 0.9077 0.9069 0.9073 5897

✅ New best model saved! Acc=0.9069

Epoch \[14/25\]

Train Loss: 0.1166 \| Train Acc: 0.9507

Val Loss: 0.2449 \| Val Acc: 0.8969

\[Validation\] Confusion Matrix:

\[\[4181 234\]

\[ 374 1108\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9179 0.9470 0.9322 4415

Abnormal 0.8256 0.7476 0.7847 1482

accuracy 0.8969 5897

macro avg 0.8718 0.8473 0.8585 5897

weighted avg 0.8947 0.8969 0.8951 5897

Epoch \[15/25\]

Train Loss: 0.1154 \| Train Acc: 0.9510

Val Loss: 0.2566 \| Val Acc: 0.8972

\[Validation\] Confusion Matrix:

\[\[4153 262\]

\[ 344 1138\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9235 0.9407 0.9320 4415

Abnormal 0.8129 0.7679 0.7897 1482

accuracy 0.8972 5897

macro avg 0.8682 0.8543 0.8609 5897

weighted avg 0.8957 0.8972 0.8962 5897

Epoch \[16/25\]

Train Loss: 0.1135 \| Train Acc: 0.9523

Val Loss: 0.2286 \| Val Acc: 0.8983

\[Validation\] Confusion Matrix:

\[\[4190 225\]

\[ 375 1107\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9179 0.9490 0.9332 4415

Abnormal 0.8311 0.7470 0.7868 1482

accuracy 0.8983 5897

macro avg 0.8745 0.8480 0.8600 5897

weighted avg 0.8960 0.8983 0.8964 5897

Epoch \[17/25\]

Train Loss: 0.1111 \| Train Acc: 0.9521

Val Loss: 0.2368 \| Val Acc: 0.9106

\[Validation\] Confusion Matrix:

\[\[4095 320\]

\[ 207 1275\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9519 0.9275 0.9395 4415

Abnormal 0.7994 0.8603 0.8287 1482

accuracy 0.9106 5897

macro avg 0.8756 0.8939 0.8841 5897

weighted avg 0.9136 0.9106 0.9117 5897

✅ New best model saved! Acc=0.9106

Epoch\[18/25\] Train Loss: 0.1099 \| Train Acc: 0.9535

Val Loss: 0.2483 \| Val Acc: 0.8976

\[Validation\] Confusion Matrix:

\[\[4104 311\]

\[ 293 1189\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9334 0.9296 0.9315 4415

Abnormal 0.7927 0.8023 0.7975 1482

accuracy 0.8976 5897

macro avg 0.8630 0.8659 0.8645 5897

weighted avg 0.8980 0.8976 0.8978 5897

Epoch \[19/25\]

Train Loss: 0.1059 \| Train Acc: 0.9560

Val Loss: 0.2407 \| Val Acc: 0.9001

\[Validation\] Confusion Matrix:

\[\[4193 222\]

\[ 367 1115\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9195 0.9497 0.9344 4415

Abnormal 0.8340 0.7524 0.7911 1482

accuracy 0.9001 5897

macro avg 0.8767 0.8510 0.8627 5897

weighted avg 0.8980 0.9001 0.8984 5897

Epoch \[20/25\]

Train Loss: 0.1038 \| Train Acc: 0.9570

Val Loss: 0.2602 \| Val Acc: 0.9018

\[Validation\] Confusion Matrix:

\[\[4178 237\]

\[ 342 1140\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9243 0.9463 0.9352 4415

Abnormal 0.8279 0.7692 0.7975 1482

accuracy 0.9018 5897

macro avg 0.8761 0.8578 0.8663 5897

weighted avg 0.9001 0.9018 0.9006 5897

Epoch \[21/25\]

Train Loss: 0.1018 \| Train Acc: 0.9575

Val Loss: 0.3150 \| Val Acc: 0.8781

\[Validation\] Confusion Matrix:

\[\[4259 156\]

\[ 563 919\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.8832 0.9647 0.9222 4415

Abnormal 0.8549 0.6201 0.7188 1482

accuracy 0.8781 5897

macro avg 0.8691 0.7924 0.8205 5897

weighted avg 0.8761 0.8781 0.8711 5897

Epoch \[22/25\]

Train Loss: 0.0880 \| Train Acc: 0.9638

Val Loss: 0.2994 \| Val Acc: 0.8889

\[Validation\] Confusion Matrix:

\[\[4170 245\]

\[ 410 1072\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9105 0.9445 0.9272 4415

Abnormal 0.8140 0.7233 0.7660 1482

accuracy 0.8889 5897

macro avg 0.8622 0.8339 0.8466 5897

weighted avg 0.8862 0.8889 0.8867 5897

Epoch \[23/25\]

Train Loss: 0.0859 \| Train Acc: 0.9647

Val Loss: 0.2857 \| Val Acc: 0.8994

\[Validation\] Confusion Matrix:

\[\[4191 224\]

\[ 369 1113\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9191 0.9493 0.9339 4415

Abnormal 0.8325 0.7510 0.7896 1482

accuracy 0.8994 5897

macro avg 0.8758 0.8501 0.8618 5897

weighted avg 0.8973 0.8994 0.8977 5897

Epoch \[24/25\]

Train Loss: 0.0833 \| Train Acc: 0.9658

Val Loss: 0.2574 \| Val Acc: 0.9033

\[Validation\] Confusion Matrix:

\[\[4182 233\]

\[ 337 1145\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9254 0.9472 0.9362 4415

Abnormal 0.8309 0.7726 0.8007 1482

accuracy 0.9033 5897

macro avg 0.8782 0.8599 0.8684 5897

weighted avg 0.9017 0.9033 0.9021 5897

Epoch \[25/25\]

Train Loss: 0.0826 \| Train Acc: 0.9674

Val Loss: 0.3163 \| Val Acc: 0.8928

\[Validation\] Confusion Matrix:

\[\[4247 168\]

\[ 464 1018\]\]

\[Validation\] Classification Report:

precision recall f1-score support

Normal 0.9015 0.9619 0.9307 4415

Abnormal 0.8583 0.6869 0.7631 1482

accuracy 0.8928 5897

macro avg 0.8799 0.8244 0.8469 5897

weighted avg 0.8907 0.8928 0.8886 5897

!!!!!!!!!!!!!!!!!!!! FINAL TEST ON TEST SET !!!!!!!!!!!!!!!!!!!!

Test Loss: 0.3864 \| Test Acc: 0.8623 \| M-Score: 0.8497

\[Test Set\] Classification Report:

precision recall f1-score support

Normal 0.9564 0.8699 0.9111 5089

Abnormal 0.5973 0.8294 0.6945 1184

accuracy 0.8623 6273

macro avg 0.7768 0.8497 0.8028 6273

weighted avg 0.8886 0.8623 0.8702 6273

![文本 AI
生成的内容可能不正确。](./media/image15.png){width="6.268055555555556in"
height="5.076388888888889in"}

![图形用户界面, 表格 AI
生成的内容可能不正确。](./media/image16.png){width="6.268055555555556in"
height="2.877083333333333in"}

目前的模型

![](./media/image17.png){width="6.268055555555556in"
height="1.167361111111111in"}

### Hop_length由32改成了64

![文本 AI
生成的内容可能不正确。](./media/image18.png){width="5.127972440944882in"
height="4.071812117235345in"}

![图形用户界面, 文本 AI
生成的内容可能不正确。](./media/image19.png){width="6.268055555555556in"
height="2.8493055555555555in"}

### 量化 FP32 转化成 INT 8

500个样本

![图片包含 图形用户界面 AI
生成的内容可能不正确。](./media/image20.png){width="6.268055555555556in"
height="1.4395833333333334in"}

全部样本

![](./media/image21.png){width="6.268055555555556in"
height="1.4236111111111112in"}

### Not Certain 模型0的加入

![](./media/image22.png){width="6.268055555555556in"
height="2.1368055555555556in"}

引入 **WeightedRandomSampler** 来解决那 364 vs 2876 的样本不平衡问题。

 **EPOCHS**: 统一改回 **25**。

 **验证集数据增强**: 之前的质量脚本有一个隐藏
Bug------验证集也开启了数据增强。现在已修复，确保验证集是"干净"的（augment=False）。

 **学习率调度器**: 补上了
ReduceLROnPlateau，让质量模型在瓶颈期也能自动降速。

 **指标完整性**: 补上了 **Confusion Matrix（混淆矩阵）** 和 **Current
Learning Rate** 的打印。

 **结束总结**: 补上了训练结束后的最终路径和最高准确率提示。

![](./media/image23.png){width="4.53980971128609in"
height="3.9382567804024498in"}

### 调整后重新训练

**改动 A：引入标签平滑 (Label Smoothing)**

与其让模型死磕"这绝对是 0"或"这绝对是
1"，不如给它一点模糊空间。这能有效防止模型产生过高的置信度，从而抑制过拟合。

Python

\# 修改前

criterion = nn.CrossEntropyLoss()

\# 修改后：给模型留 10% 的宽容度

criterion = nn.CrossEntropyLoss(label_smoothing=0.1)

**改动 B：修改监控指标（从 Acc 改为 Loss）**

现在的脚本是在"准确率最高"时保存。但正如你所见，准确率高的时候 Loss
可能已经在反弹了。

- **策略**：改为在 **Val Loss 最低**时保存模型。这样选出的模型虽然 Acc
  可能低一点点，但泛化能力（面对新噪声的能力）会强得多。

**改动 C：增加 Dropout（如果模型里没有）**

如果你的 LightweightCNN 里 Dropout 比较低，建议在全连接层前将其提高到
**0.5**。

效果很差

只保留了改动B，提前终止了训练

![文本 AI
生成的内容可能不正确。](./media/image24.png){width="5.200539151356081in"
height="4.350107174103237in"}

### Evaluate_tflite.py改动

这是一个非常专业的工程和学术权衡问题。

你现在的处境是：在训练 quality_model
时，为了尽可能利用有限的噪声样本（只有 364 个），你通过 **80/20
的比例**把数据分成了"训练集"和"验证集"。

**如果你直接运行之前的 evaluate_tflite.py 遍历整个
CSV，结果会非常虚高**，因为 80%
的数据模型已经"背过"了，这在论文里是不及格的。

针对"数据用完了"的情况，我有三个建议方案，按**推荐程度**排序：

**方案 A：使用"真·验证集"进行隔离评估（最推荐，最严谨）**

虽然你在训练中用了那 20% 的验证集来挑选
best_model，但模型在训练（权重更新）过程中并没"见过"这些数据。
**做法**：修改
evaluate_tflite.py，让它使用和训练脚本**完全相同**的随机种子（Seed
42）和分割逻辑，**只对那 20% 的样本进行推理**。

- **优点**：数据真实，符合毕设要求的"不使用训练数据进行测试"的原则。

- **论文写法**：你可以理直气壮地写："由于样本量限制，本研究采用留出法（Hold-out），在隔离的
  20% 测试集上验证了模型的鲁棒性。

Evaluate_tflite

![](./media/image25.png){width="6.268055555555556in"
height="1.4541666666666666in"}

Benchmark

![](./media/image26.png){width="6.268055555555556in"
height="1.8597222222222223in"}

Run_Inference

![](./media/image27.png){width="6.268055555555556in"
height="1.1590277777777778in"}

![文本 AI
生成的内容可能不正确。](./media/image28.png){width="6.276462160979878in"
height="1.3973665791776029in"}

### Main_pi.py

![](./media/image29.png){width="6.268055555555556in"
height="2.720138888888889in"}

### 转移到树莓派上

![](./media/image30.png){width="6.268055555555556in"
height="5.652083333333334in"}

### Wyl的心音经过了esp32的传输，在树莓派里进行推理

有denoise处理的置信度相比原始音频有了明显提升

![图形用户界面, 应用程序, 表格 AI
生成的内容可能不正确。](./media/image31.png){width="6.268055555555556in"
height="2.4479166666666665in"}

(.venv) rasp4b@Rasp4B:\~/FypPi \$/home/rasp4b/FypPi/.venv/bin/python
/home/rasp4b/FypPi/main_pi_debug.py

🚀 FypProj 双级推理系统 · 最终调试版

============================================================

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

🎬 正在读取音频并提取特征: heart_sound_1770104436_processed.wav

📦 预处理成功: 已生成 13 个 2 秒切片

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

片段 01: ✨ \[诊断通过\] 结果: Abnormal (异常) \| 置信度: 95.19%

片段 02: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 82.36%

片段 03: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 95.41%

片段 04: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 82.87%

片段 05: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 91.93%

片段 06: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 99.49%

片段 07: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 94.45%

片段 08: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 72.35%

片段 09: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 84.24%

片段 10: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 99.67%

片段 11: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 99.27%

片段 12: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 90.72%

片段 13: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 90.92%

============================================================

📊 性能统计:

⏱ 总运行时间: 5.49 秒

💾 起始内存: 131.97 MB

💾 结束内存: 266.34 MB

📈 当前内存占用: 266.34 MB

✅ 离线验证任务圆满完成。

(.venv) rasp4b@Rasp4B:\~/FypPi \$ /home/rasp4b/FypPi/.venv/bin/python
/home/rasp4b/FypPi/main_pi_debug.py

🚀 FypProj 双级推理系统 · 最终调试版

============================================================

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

🎬 正在读取音频并提取特征: heart_sound_1770104436.wav

📦 预处理成功: 已生成 13 个 2 秒切片

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

片段 01: ✨ \[诊断通过\] 结果: Abnormal (异常) \| 置信度: 96.25%

片段 02: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 62.11%

片段 03: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 86.25%

片段 04: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 70.07%

片段 05: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 87.20%

片段 06: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 98.93%

片段 07: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 86.96%

片段 08: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 55.55%

片段 09: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 65.90%

片段 10: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 99.02%

片段 11: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 97.10%

片段 12: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 84.28%

片段 13: ✨ \[诊断通过\] 结果: Normal (正常) \| 置信度: 73.67%

============================================================

📊 性能统计:

⏱ 总运行时间: 7.97 秒

💾 起始内存: 131.98 MB

💾 结束内存: 264.59 MB

📈 当前内存占用: 264.59 MB

✅ 离线验证任务圆满完成。

有噪声版

(.venv) rasp4b@Rasp4B:\~/FypPi \$ /home/rasp4b/FypPi/.venv/bin/python
/home/rasp4b/FypPi/main_pi_debug.py

🚀 FypProj 双级推理系统 · 最终调试版

============================================================

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

🎬 正在读取音频并提取特征: heart_sound_1773566721_processed.wav

📦 预处理成功: 已生成 11 个 2 秒切片

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

片段 01: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 99.28%

片段 02: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 99.12%

片段 03: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 99.29%

片段 04: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 99.90%

片段 05: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 99.75%

片段 06: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 98.93%

片段 07: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 98.52%

片段 08: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 99.74%

片段 09: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 99.97%

片段 10: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 99.98%

片段 11: ⚠️ \[质量拦截\] 信号干扰过强 \| 噪声概率: 99.99%

============================================================

📊 性能统计:

⏱ 总运行时间: 5.23 秒

💾 起始内存: 131.98 MB

💾 结束内存: 266.14 MB

📈 当前内存占用: 266.14 MB

✅ 离线验证任务圆满完成。

### 结果加权平滑

你说得对，我纠正一下：

1\.
还是用SQA加权平均，不是简单平均------质量稍差的片段贡献小一点，而不是直接丢弃

2\. 0.5只是丢弃极差片段的兜底，不是非黑即白的判断

\-\--

所以完整方案：

三次采样，各自过SQA：

SQA \< 0.5 → 直接丢弃，不参与计算

SQA ≥ 0.5 → 参与加权平均

final_prob_normal = Σ(sqa_i × prob_normal_i) / Σ(sqa_i)

final \> 0.5 → Normal，否则 Abnormal

比如三次结果：

第1次：SQA=0.99，Normal=0.85 → 参与，权重大

第2次：SQA=0.30， → 丢弃

第3次：SQA=0.65，Normal=0.78 → 参与，权重稍小

### BLE 收到的是裸 PCM 字节流，没有任何文件头。 

现在的处理方式：

\# 收到的 raw 是裸 PCM 字节

raw = await collect_segment()

\# 直接用 numpy 解析为 int16 数组

audio = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0

ESP32 发的是 16-bit 小端 PCM，np.frombuffer 直接按 int16 解析，然后除以
32768 归一化到 \[-1, 1\]，就得到可以进预处理管道的 float32 数组。

不需要 WAV 文件头，WAV 头只在最后保存异常音频时用 wave
模块加上去（为了方便事后回放）。

### 蓝牙调试

bluetoothctl remove 80:F1:B2:ED:B4:12

sudo systemctl restart bluetooth

断电重启直接运行模式3

(.venv) rasp4b@Rasp4B:\~/FypPi \$ python ble_debug.py

BLE 调试工具

1\. 扫描设备

2\. 检查 GATT 服务与特征

3\. 监控原始数据（30秒）

4\. 监控原始数据（自定义时长）

请选择 (1-4): 3

=======================================================

\[数据监控\] 连接中，监控时长 30 秒

目标 UUID: beb5483e-36e1-4688-b7f5-ea07361b26a8

=======================================================

/home/rasp4b/FypPi/.venv/lib/python3.13/site-packages/bleak/backends/bluezdbus/client.py:646:
UserWarning: Using default MTU value. Call \_acquire_mtu() or set
\_mtu_size first to avoid this warning.

warnings.warn(

✅ 已连接！MTU: 23 字节

📥 开始接收数据，等待 30 秒\...

包号 大小 \| HEX (前16字节) \| ASCII

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

#0001 \| 128B \| hex: 54 f7 54 f7 54 f7 54 f7 54 f7 54 f7 54 f7 54
f7\... \| ascii: T.T.T.T.T.T.T.T.

#0002 \| 128B \| hex: d2 f1 f0 f1 a4 f2 a4 f2 94 f3 94 f3 0c f4 0c
f4\... \| ascii: \...\...\...\...\....

#0003 \| 128B \| hex: fe f2 fe f2 76 f3 76 f3 76 f3 76 f3 76 f3 76
f3\... \| ascii: \....v.v.v.v.v.v.

#0004 \| 128B \| hex: aa 0a aa 0a e6 0a e6 0a 22 0b 04 0b 04 0b 04
0b\... \| ascii: \...\.....\"\...\....

#0005 \| 128B \| hex: e0 01 e0 01 1c 02 1c 02 58 02 58 02 e0 01 e0
01\... \| ascii: \...\.....X.X\.....

#0006 \| 128B \| hex: ce 04 ce 04 0a 05 0a 05 82 05 82 05 36 06 36
06\... \| ascii: \...\...\...\...6.6.

#0007 \| 128B \| hex: 70 08 70 08 34 08 16 08 da 07 da 07 16 08 16
08\... \| ascii: p.p.4\...\...\.....

#0008 \| 128B \| hex: 2e ff 2e ff 6a ff 6a ff 6a ff 6a ff e2 ff e2
ff\... \| ascii: \....j.j.j.j\.....

#0009 \| 128B \| hex: 74 04 74 04 ec 04 ec 04 ec 04 ec 04 fc 03 fc
03\... \| ascii: t.t\...\...\...\....

#0010 \| 128B \| hex: ec 04 ec 04 38 04 38 04 c0 03 c0 03 48 03 48
03\... \| ascii: \....8.8\.....H.H.

#0011 \| 128B \| hex: 46 f6 46 f6 46 f6 46 f6 82 f6 82 f6 82 f6 82
f6\... \| ascii: F.F.F.F\...\...\...

#0012 \| 128B \| hex: bc f8 bc f8 70 f9 70 f9 24 fa 24 fa d8 fa d8
fa\... \| ascii: \....p.p.\$.\$\.....

#0013 \| 128B \| hex: da 07 da 07 9e 07 9e 07 9e 07 9e 07 08 07 08
07\... \| ascii: \...\...\...\...\....

#0014 \| 128B \| hex: 7c fc 7c fc 04 fc 04 fc 50 fb 50 fb 14 fb 14
fb\... \| ascii: \|.\|\.....P.P\.....

#0015 \| 128B \| hex: ea 06 ea 06 26 07 26 07 9e 07 9e 07 9e 07 9e
07\... \| ascii: \....&.&\...\...\...

#0016 \| 128B \| hex: 5a 00 5a 00 5a 00 5a 00 6a ff 6a ff f2 fe f2
fe\... \| ascii: Z.Z.Z.Z.j.j\.....

#0017 \| 128B \| hex: 34 f9 34 f9 70 f9 70 f9 70 f9 70 f9 70 f9 70
f9\... \| ascii: 4.4.p.p.p.p.p.p.

#0018 \| 128B \| hex: 9a 0b 9a 0b 4e 0c 4e 0c 8a 0c 8a 0c 8a 0c 6c
0c\... \| ascii: \....N.N\...\....l.

#0019 \| 128B \| hex: e8 f9 e8 f9 24 fa 24 fa 60 fa 60 fa d8 fa d8
fa\... \| ascii: \....\$.\$.\`.\`\.....

#0020 \| 128B \| hex: 86 f2 86 f2 4a f2 4a f2 0e f2 0e f2 f0 f1 f0
f1\... \| ascii: \....J.J\...\...\...

#0021 \| 128B \| hex: d2 00 d2 00 4a 01 4a 01 4a 01 4a 01 0e 01 0e
01\... \| ascii: \....J.J.J.J\.....

#0022 \| 128B \| hex: 7c fc 7c fc 04 fc 04 fc 14 fb 14 fb d8 fa d8
fa\... \| ascii: \|.\|\...\...\...\....

#0023 \| 128B \| hex: 84 03 84 03 c0 03 c0 03 0c 03 0c 03 d0 02 d0
02\... \| ascii: \...\...\...\...\....

#0024 \| 128B \| hex: 9c 09 9c 09 50 0a 50 0a 32 0a 32 0a aa 0a aa
0a\... \| ascii: \....P.P.2.2\.....

#0025 \| 128B \| hex: 26 f8 26 f8 62 f8 62 f8 f8 f8 f8 f8 34 f9 34
f9\... \| ascii: &.&.b.b\.....4.4.

#0026 \| 128B \| hex: fe 01 fe 01 86 01 86 01 fe 01 fe 01 86 01 86
01\... \| ascii: \...\...\...\...\....

#0027 \| 128B \| hex: 34 08 34 08 70 08 70 08 70 08 52 08 8e 08 8e
08\... \| ascii: 4.4.p.p.p.R\.....

#0028 \| 128B \| hex: 50 fb 50 fb 8c fb 8c fb b8 fc b8 fc 6c fd 6c
fd\... \| ascii: P.P\...\...\...l.l.

#0029 \| 128B \| hex: f6 fa f6 fa 7e fa 9c fa 24 fa 24 fa 24 fa 24
fa\... \| ascii: \....\~\...\$.\$.\$.\$.

#0030 \| 128B \| hex: d8 fa d8 fa 60 fa 60 fa 9c fa 9c fa 14 fb 14
fb\... \| ascii: \....\`.\`\...\...\...

#0031 \| 128B \| hex: 9c 09 9c 09 9c 09 7e 09 ba 09 ba 09 32 0a 32
0a\... \| ascii: \...\...\~\.....2.2.

#0032 \| 128B \| hex: be e7 be e7 ce e6 ce e6 38 e6 38 e6 48 e5 48
e5\... \| ascii: \...\.....8.8.H.H.

#0033 \| 128B \| hex: 46 f6 46 f6 dc f6 dc f6 dc f6 dc f6 a0 f6 a0
f6\... \| ascii: F.F\...\...\...\....

#0034 \| 128B \| hex: ec 04 ec 04 ec 04 ec 04 ec 04 ec 04 64 05 46
05\... \| ascii: \...\...\...\...d.F.

#0035 \| 128B \| hex: 52 08 52 08 52 08 52 08 da 07 da 07 9e 07 9e
07\... \| ascii: R.R.R.R\...\...\...

#0036 \| 128B \| hex: 70 08 70 08 70 08 70 08 ac 08 ac 08 24 09 06
09\... \| ascii: p.p.p.p\.....\$\...

#0037 \| 128B \| hex: 48 12 48 12 0c 12 0c 12 94 11 76 11 c2 10 c2
10\... \| ascii: H.H\...\....v\.....

#0038 \| 128B \| hex: 94 02 94 02 1c 02 1c 02 58 02 58 02 94 02 94
02\... \| ascii: \...\.....X.X\.....

#0039 \| 128B \| hex: 02 0d e4 0c 20 0d 20 0d 20 0d 20 0d 20 0d 20
0d\... \| ascii: \.... . . . . . .

#0040 \| 128B \| hex: f2 fe f2 fe b6 fe b6 fe f2 fe f2 fe f2 fe f2
fe\... \| ascii: \...\...\...\...\....

#0041 \| 128B \| hex: b4 00 b4 00 78 00 78 00 3c 00 3c 00 00 00 00
00\... \| ascii: \....x.x.\<.\<\.....

#0042 \| 128B \| hex: 24 09 24 09 24 09 24 09 e8 08 e8 08 f8 07 f8
07\... \| ascii: \$.\$.\$.\$\...\...\...

#0043 \| 128B \| hex: 56 04 56 04 92 04 92 04 56 04 56 04 1a 04 1a
04\... \| ascii: V.V\.....V.V\.....

#0044 \| 128B \| hex: 90 e8 90 e8 dc e7 dc e7 a0 e7 be e7 82 e7 82
e7\... \| ascii: \...\...\...\...\....

#0045 \| 128B \| hex: 68 01 68 01 a4 01 a4 01 58 02 58 02 94 02 94
02\... \| ascii: h.h\.....X.X\.....

#0046 \| 128B \| hex: 28 f6 28 f6 28 f6 28 f6 ec f5 ec f5 28 f6 28
f6\... \| ascii: (.(.(.(\.....(.(.

#0047 \| 128B \| hex: b0 04 b0 04 fc 03 fc 03 84 03 84 03 0c 03 0c
03\... \| ascii: \...\...\...\...\....

#0048 \| 128B \| hex: 8a ee 8a ee 8a ee 8a ee 8a ee 8a ee e4 ee e4
ee\... \| ascii: \...\...\...\...\....

#0049 \| 128B \| hex: c4 ff c4 ff 10 ff 10 ff 5c fe 5c fe 6c fd 6c
fd\... \| ascii: \...\.....\\.\\.l.l.

#0050 \| 128B \| hex: 66 f4 66 f4 ee f3 ee f3 c2 f2 c2 f2 f0 f1 f0
f1\... \| ascii: f.f\...\...\...\....

#0051 \| 128B \| hex: 46 05 46 05 be 05 be 05 46 05 46 05 46 05 46
05\... \| ascii: F.F\.....F.F.F.F.

#0052 \| 128B \| hex: d0 02 d0 02 1c 02 1c 02 1c 02 1c 02 58 02 58
02\... \| ascii: \...\...\...\...X.X.

#0053 \| 128B \| hex: b0 04 b0 04 ce 04 ce 04 ce 04 ce 04 0a 05 0a
05\... \| ascii: \...\...\...\...\....

#0054 \| 128B \| hex: 2a 03 2a 03 ee 02 ee 02 76 02 76 02 76 02 76
02\... \| ascii: \*.\*\.....v.v.v.v.

#0055 \| 128B \| hex: 2a f4 2a f4 2a f4 48 f4 c0 f4 c0 f4 fc f4 fc
f4\... \| ascii: \*.\*.\*.H\...\...\...

#0056 \| 128B \| hex: 3e ef 3e ef 3e ef 3e ef a8 ee a8 ee a8 ee a8
ee\... \| ascii: \>.\>.\>.\>\...\...\...

#0057 \| 128B \| hex: 4e fd 4e fd 8a fd 8a fd c6 fd c6 fd 02 fe 02
fe\... \| ascii: N.N\...\...\...\....

#0058 \| 128B \| hex: fe 01 fe 01 fe 01 fe 01 b2 02 b2 02 de 03 de
03\... \| ascii: \...\...\...\...\....

#0059 \| 128B \| hex: 06 fa 06 fa 8e f9 8e f9 52 f9 52 f9 da f8 da
f8\... \| ascii: \...\.....R.R\.....

#0060 \| 128B \| hex: 58 11 58 11 c2 10 c2 10 3a 11 3a 11 76 11 76
11\... \| ascii: X.X\.....:.:.v.v.

#0061 \| 128B \| hex: c0 03 c0 03 84 03 84 03 84 03 84 03 0c 03 0c
03\... \| ascii: \...\...\...\...\....

#0062 \| 128B \| hex: a6 ff a6 ff 1e 00 1e 00 1e 00 1e 00 a6 ff a6
ff\... \| ascii: \...\...\...\...\....

#0063 \| 128B \| hex: 84 12 84 12 c0 12 c0 12 84 12 84 12 2a 12 2a
12\... \| ascii: \...\...\...\...\*.\*.

#0064 \| 128B \| hex: d0 f3 d0 f3 d0 f3 d0 f3 d0 f3 d0 f3 94 f3 b2
f3\... \| ascii: \...\...\...\...\....

#0065 \| 128B \| hex: 90 06 90 06 08 07 08 07 08 07 08 07 ea 06 ea
06\... \| ascii: \...\...\...\...\....

#0066 \| 128B \| hex: 90 06 90 06 cc 06 cc 06 f8 07 f8 07 9e 07 9e
07\... \| ascii: \...\...\...\...\....

#0067 \| 128B \| hex: a4 f2 a4 f2 68 f2 68 f2 68 f2 68 f2 f0 f1 f0
f1\... \| ascii: \....h.h.h.h\.....

#0068 \| 128B \| hex: 74 f5 92 f5 56 f5 56 f5 a2 f4 a2 f4 a2 f4 a2
f4\... \| ascii: t\...V.V\...\...\...

#0069 \| 128B \| hex: 54 06 54 06 90 06 90 06 ea 06 ea 06 26 07 26
07\... \| ascii: T.T\...\...\...&.&.

#0070 \| 128B \| hex: 04 0b 04 0b c8 0a c8 0a e6 0a e6 0a 22 0b 22
0b\... \| ascii: \...\...\...\...\".\".

#0071 \| 128B \| hex: f8 07 f8 07 f8 07 f8 07 9e 07 9e 07 62 07 62
07\... \| ascii: \...\...\...\...b.b.

#0072 \| 128B \| hex: 3c 0f 3c 0f 00 0f e2 0e e2 0e e2 0e 1e 0f 1e
0f\... \| ascii: \<.\<\...\...\...\....

#0073 \| 128B \| hex: 24 fa 24 fa 60 fa 60 fa d8 fa d8 fa 14 fb 14
fb\... \| ascii: \$.\$.\`.\`\...\...\...

#0074 \| 128B \| hex: 14 ec 14 ec 9c eb 9c eb 24 eb 42 eb 42 eb 42
eb\... \| ascii: \...\.....\$.B.B.B.

#0075 \| 128B \| hex: d4 0d b6 0d 3e 0d 3e 0d 2e 0e 2e 0e 2e 0e 2e
0e\... \| ascii: \....\>.\>\...\...\...

#0076 \| 128B \| hex: 62 07 62 07 9e 07 9e 07 bc 07 bc 07 bc 07 bc
07\... \| ascii: b.b\...\...\...\....

#0077 \| 128B \| hex: b4 f1 d2 f1 86 f2 86 f2 86 f2 86 f2 3a f3 3a
f3\... \| ascii: \...\...\...\...:.:.

#0078 \| 128B \| hex: 7a fe 7a fe 7a fe 7a fe f2 fe f2 fe 2e ff 2e
ff\... \| ascii: z.z.z.z\...\...\...

#0079 \| 128B \| hex: 42 fa 42 fa 42 fa 42 fa 42 fa 42 fa 42 fa 42
fa\... \| ascii: B.B.B.B.B.B.B.B.

#0080 \| 128B \| hex: aa 0a aa 0a aa 0a aa 0a 6e 0a 6e 0a 50 0a 50
0a\... \| ascii: \...\.....n.n.P.P.

#0081 \| 128B \| hex: c6 fd c6 fd 8a fd 8a fd c6 fd c6 fd c6 fd c6
fd\... \| ascii: \...\...\...\...\....

#0082 \| 128B \| hex: 70 08 70 08 70 08 70 08 ac 08 ac 08 ac 08 ac
08\... \| ascii: p.p.p.p\...\...\...

#0083 \| 128B \| hex: 72 06 72 06 26 07 26 07 62 07 62 07 62 07 62
07\... \| ascii: r.r.&.&.b.b.b.b.

#0084 \| 128B \| hex: d2 00 d2 00 96 00 96 00 5a 00 5a 00 5a 00 5a
00\... \| ascii: \...\.....Z.Z.Z.Z.

#0085 \| 128B \| hex: f2 fe f2 fe 2e ff 2e ff e2 ff e2 ff 6a ff 6a
ff\... \| ascii: \...\...\...\...j.j.

#0086 \| 128B \| hex: 76 02 76 02 3a 02 3a 02 fe 01 fe 01 d2 00 d2
00\... \| ascii: v.v.:.:\...\...\...

#0087 \| 128B \| hex: 48 03 48 03 84 03 84 03 84 03 84 03 84 03 84
03\... \| ascii: H.H\...\...\...\....

#0088 \| 128B \| hex: e8 f9 e8 f9 e8 f9 e8 f9 e8 f9 e8 f9 24 fa 24
fa\... \| ascii: \...\...\...\...\$.\$.

#0089 \| 128B \| hex: 9e 07 9e 07 bc 07 bc 07 f8 07 f8 07 f8 07 f8
07\... \| ascii: \...\...\...\...\....

#0090 \| 128B \| hex: be 05 be 05 fa 05 fa 05 82 05 82 05 0a 05 0a
05\... \| ascii: \...\...\...\...\....

#0091 \| 128B \| hex: bc f8 bc f8 70 f9 70 f9 34 f9 34 f9 70 f9 70
f9\... \| ascii: \....p.p.4.4.p.p.

#0092 \| 128B \| hex: f4 fc f4 fc 6c fd 6c fd e4 fd e4 fd d4 fe d4
fe\... \| ascii: \....l.l\...\...\...

#0093 \| 128B \| hex: 2e ff 2e ff 6a ff 6a ff 6a ff 6a ff a6 ff a6
ff\... \| ascii: \....j.j.j.j\.....

#0094 \| 128B \| hex: aa fb aa fb 6e fb 6e fb f6 fa 14 fb 14 fb 14
fb\... \| ascii: \....n.n\...\...\...

#0095 \| 128B \| hex: bc 07 bc 07 44 07 44 07 08 07 08 07 cc 06 cc
06\... \| ascii: \....D.D\...\...\...

#0096 \| 128B \| hex: 58 02 58 02 94 02 94 02 d0 02 d0 02 d0 02 d0
02\... \| ascii: X.X\...\...\...\....

#0097 \| 128B \| hex: 5a 00 5a 00 96 00 96 00 4a 01 4a 01 c2 01 c2
01\... \| ascii: Z.Z\.....J.J\.....

#0098 \| 128B \| hex: b0 f5 b0 f5 28 f6 28 f6 64 f6 64 f6 18 f7 36
f7\... \| ascii: \....(.(.d.d\...6.

#0099 \| 128B \| hex: 7c fc 7c fc 9a fc 9a fc d6 fc d6 fc 4e fd 4e
fd\... \| ascii: \|.\|\...\...\...N.N.

#0100 \| 128B \| hex: c6 fd c6 fd 3e fe 3e fe 7a fe 7a fe b6 fe b6
fe\... \| ascii: \....\>.\>.z.z\.....

#0101 \| 128B \| hex: 90 f7 90 f7 18 f7 36 f7 be f6 be f6 be f6 be
f6\... \| ascii: \...\...6\...\...\...

#0102 \| 128B \| hex: 56 f5 56 f5 92 f5 92 f5 b0 f5 b0 f5 28 f6 28
f6\... \| ascii: V.V\...\...\...(.(.

#0103 \| 128B \| hex: 90 06 90 06 54 06 54 06 dc 05 dc 05 dc 05 dc
05\... \| ascii: \....T.T\...\...\...

#0104 \| 128B \| hex: 68 f2 68 f2 68 f2 86 f2 4a f2 4a f2 4a f2 4a
f2\... \| ascii: h.h.h\...J.J.J.J.

#0105 \| 128B \| hex: ac f9 ac f9 e8 f9 e8 f9 e8 f9 e8 f9 ac f9 ac
f9\... \| ascii: \...\...\...\...\....

#0106 \| 128B \| hex: 94 02 94 02 94 02 94 02 d0 02 d0 02 d0 02 d0
02\... \| ascii: \...\...\...\...\....

#0107 \| 128B \| hex: ac 08 ac 08 f8 07 f8 07 70 08 70 08 e8 08 e8
08\... \| ascii: \...\.....p.p\.....

#0108 \| 128B \| hex: 04 0b 04 0b 40 0b 40 0b 7c 0b 7c 0b 30 0c 30
0c\... \| ascii: \....@.@.\|.\|.0.0.

#0109 \| 128B \| hex: 3c 00 3c 00 3c 00 3c 00 88 ff 88 ff b6 fe b6
fe\... \| ascii: \<.\<.\<.\<\...\...\...

#0110 \| 128B \| hex: 6c fd 6c fd e4 fd e4 fd 20 fe 20 fe d4 fe d4
fe\... \| ascii: l.l\..... . \.....

#0111 \| 128B \| hex: b6 fe b6 fe 3e fe 3e fe 3e fe 3e fe 7a fe 7a
fe\... \| ascii: \....\>.\>.\>.\>.z.z.

#0112 \| 128B \| hex: f6 09 f6 09 7e 09 7e 09 06 09 06 09 7e 09 7e
09\... \| ascii: \....\~.\~\.....\~.\~.

#0113 \| 128B \| hex: 82 05 82 05 46 05 46 05 46 05 46 05 0a 05 0a
05\... \| ascii: \....F.F.F.F\.....

#0114 \| 128B \| hex: 04 0b 04 0b c8 0a c8 0a 04 0b 04 0b 32 0a 32
0a\... \| ascii: \...\...\...\...2.2.

#0115 \| 128B \| hex: 6a ff 6a ff 2e ff 2e ff 2e ff 2e ff b6 fe b6
fe\... \| ascii: j.j\...\...\...\....

#0116 \| 128B \| hex: 90 06 90 06 08 07 08 07 80 07 80 07 bc 07 bc
07\... \| ascii: \...\...\...\...\....

#0117 \| 128B \| hex: ac f9 ac f9 ca f9 ca f9 52 f9 52 f9 52 f9 52
f9\... \| ascii: \...\.....R.R.R.R.

#0118 \| 128B \| hex: 46 05 46 05 0a 05 0a 05 0a 05 0a 05 46 05 46
05\... \| ascii: F.F\...\...\...F.F.

#0119 \| 128B \| hex: b2 02 b2 02 ee 02 ee 02 ee 02 ee 02 ee 02 ee
02\... \| ascii: \...\...\...\...\....

#0120 \| 128B \| hex: da f8 da f8 9e f8 9e f8 9e f8 9e f8 26 f8 26
f8\... \| ascii: \...\...\...\...&.&.

=======================================================

统计结果:

接收包数: 120

总数据量: 15360 字节 (15.00 KB)

平均速率: 0.47 KB/s

平均包大小: 128.0 字节

=======================================================

![文本 AI
生成的内容可能不正确。](./media/image32.png){width="6.268055555555556in"
height="1.7166666666666666in"}

### 蓝牙debug与正弦波比较

根本原因：collect_segment() 里用 asyncio.sleep(0.05) 轮询，每秒唤醒 20
次，同时 BLE 通知每秒 125 次，事件循环非常拥挤。dbus_fast
的内部读取协程处理不过来，最终触发了 bluetoothd 发送

disconnect。

修复方案：把轮询循环改成事件驱动，数据够了才唤醒一次：

正弦波做比较

扬声器播音 → INMP441 → I2S

→ remove_dc_offset() ← 直流去除

→ LPF (α=0.05) ← 低通滤波

→ × 30 gain + ±32000 限幅 ← 增益

→ BLE 传输

→ Pi 收到 → raw.wav

50hz

![](./media/image33.png){width="6.268055555555556in"
height="4.513194444444444in"}

100hz

![图表 AI
生成的内容可能不正确。](./media/image34.png){width="6.268055555555556in"
height="4.45625in"}

200hz

![图片包含 日程表 AI
生成的内容可能不正确。](./media/image35.png){width="6.268055555555556in"
height="4.467361111111111in"}

(FypProj) rae@Rae:/mnt/d/FypProj\$ python esp32_debug/pc_analyze_tone.py
WAV_hz_og/50hz_og.wav WAV_record/000_raw.wav 50

OG : 50hz_og.wav fs=44100Hz 时长=10.00s

Received : 000_raw.wav fs=8000Hz 时长=10.00s

Target freq: 50.0 Hz

==================================================

Metric OG Received

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Peak Freq (Hz) 50.00 48.30

SNR (dB) 95.4 -17.6

Purity (%) 100.00 1.70

THD (%) 0.00 74.57

Attenuation (dB) --- -72.6

==================================================

/mnt/d/FypProj/esp32_debug/pc_analyze_tone.py:167: UserWarning: This
figure includes Axes that are not compatible with tight_layout, so
results might be incorrect.

plt.tight_layout()

(FypProj) rae@Rae:/mnt/d/FypProj\$ python esp32_debug/pc_analyze_tone.py
WAV_hz_og/100hz_og.wav WAV_record/001_raw.wav 100

OG : 100hz_og.wav fs=44100Hz 时长=10.00s

Received : 001_raw.wav fs=8000Hz 时长=10.00s

Target freq: 100.0 Hz

==================================================

Metric OG Received

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Peak Freq (Hz) 100.00 100.00

SNR (dB) 95.4 -12.1

Purity (%) 100.00 4.09

THD (%) 0.00 268.18

Attenuation (dB) --- -60.7

==================================================

/mnt/d/FypProj/esp32_debug/pc_analyze_tone.py:167: UserWarning: This
figure includes Axes that are not compatible with tight_layout, so
results might be incorrect.

plt.tight_layout()

(FypProj) rae@Rae:/mnt/d/FypProj\$ python esp32_debug/pc_analyze_tone.py
WAV_hz_og/200hz_og.wav WAV_record/002_raw.wav 200

OG : 200hz_og.wav fs=44100Hz 时长=10.00s

Received : 002_raw.wav fs=8000Hz 时长=10.00s

Target freq: 200.0 Hz

==================================================

Metric OG Received

\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\-\--

Peak Freq (Hz) 200.00 200.00

SNR (dB) 95.4 26.7

Purity (%) 100.00 95.27

THD (%) 0.00 21.79

Attenuation (dB) --- -22.4

==================================================

/mnt/d/FypProj/esp32_debug/pc_analyze_tone.py:167: UserWarning: This
figure includes Axes that are not compatible with tight_layout, so
results might be incorrect.

plt.tight_layout()

I2S 协议本身是固定双声道的，WS（Word Select）引脚在 L/R
之间交替切换，SCK 始终按两个声道计算：

SCK = 采样率 × 2声道 × 位深（slot宽度）

### 归一化后正弦波对比

环境音

![](./media/image36.png){width="6.268055555555556in"
height="1.770138888888889in"}

100hz

![图片包含 图示 AI
生成的内容可能不正确。](./media/image37.png){width="6.268055555555556in"
height="4.468055555555556in"}

![图片包含 图示 AI
生成的内容可能不正确。](./media/image38.png){width="6.268055555555556in"
height="4.458333333333333in"}

200hz

![](./media/image39.png){width="6.268055555555556in"
height="4.464583333333334in"}

![图片包含 日程表 AI
生成的内容可能不正确。](./media/image40.png){width="6.268055555555556in"
height="4.477083333333334in"}

### 归一化后正弦波加回esp32增益

底噪

![](./media/image41.png){width="6.268055555555556in"
height="1.7694444444444444in"}

![日程表 AI
生成的内容可能不正确。](./media/image42.png){width="6.268055555555556in"
height="1.7756944444444445in"}

200hz

![图片包含 图表 AI
生成的内容可能不正确。](./media/image43.png){width="6.268055555555556in"
height="1.775in"}

![图片包含 图形用户界面 AI
生成的内容可能不正确。](./media/image44.png){width="6.268055555555556in"
height="4.475in"}

![图片包含 图示 AI
生成的内容可能不正确。](./media/image45.png){width="6.268055555555556in"
height="4.467361111111111in"}

400hz

![](./media/image46.png){width="6.268055555555556in"
height="1.7673611111111112in"}

![图片包含 图示 AI
生成的内容可能不正确。](./media/image47.png){width="6.268055555555556in"
height="4.478472222222222in"}

![图片包含 图形用户界面 AI
生成的内容可能不正确。](./media/image48.png){width="6.268055555555556in"
height="4.470138888888889in"}

### 同一个音频 不在数据集之内

(.venv) rasp4b@Rasp4B:\~/FypPi \$ python main_pi.py

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

📡 正在连接 ESP32: 80:F1:B2:ED:B4:12\...

✅ 已连接，MTU: 517 字节

🎙️ 第 1/3 次采集中（2s）\...

\[1/1\] SQA → Poor=3.77% \| Good=96.23%

诊断 → Normal \| Normal=51.98%

⏳ 等待 30 秒后进行第 2 次采集\...

🎙️ 第 2/3 次采集中（2s）\...

\[1/1\] SQA → Poor=0.00% \| Good=100.00%

诊断 → Abnormal \| Normal=8.70%

⏳ 等待 30 秒后进行第 3 次采集\...

🎙️ 第 3/3 次采集中（2s）\...

\[1/1\] SQA → Poor=0.01% \| Good=99.99%

诊断 → Normal \| Normal=56.90%

❌ 错误: EOFError()

(.venv) rasp4b@Rasp4B:\~/FypPi \$ python main_pi.py

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

📡 正在连接 ESP32: 80:F1:B2:ED:B4:12\...

✅ 已连接，MTU: 517 字节

🎙️ 第 1/3 次采集中（2s）\...

\[1/1\] SQA → Poor=0.40% \| Good=99.60%

诊断 → Abnormal \| Normal=33.77%

⏳ 等待 30 秒后进行第 2 次采集\...

🎙️ 第 2/3 次采集中（2s）\...

\[1/1\] SQA → Poor=28.13% \| Good=71.87%

⚠️ 质量不足，跳过

⏳ 等待 30 秒后进行第 3 次采集\...

🎙️ 第 3/3 次采集中（2s）\...

\[1/1\] SQA → Poor=0.04% \| Good=99.96%

诊断 → Abnormal \| Normal=3.58%

❌ 错误: EOFError()

(.venv) rasp4b@Rasp4B:\~/FypPi \$ python main_pi.py

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

📡 正在连接 ESP32: 80:F1:B2:ED:B4:12\...

✅ 已连接，MTU: 517 字节

🎙️ 第 1/3 次采集中（2s）\...

\[1/1\] SQA → Poor=24.00% \| Good=76.00%

⚠️ 质量不足，跳过

⏳ 等待 30 秒后进行第 2 次采集\...

🎙️ 第 2/3 次采集中（2s）\...

\[1/1\] SQA → Poor=47.46% \| Good=52.54%

⚠️ 质量不足，跳过

⏳ 等待 30 秒后进行第 3 次采集\...

🎙️ 第 3/3 次采集中（2s）\...

\[1/1\] SQA → Poor=3.36% \| Good=96.64%

诊断 → Normal \| Normal=99.90%

❌ 错误: EOFError()

### 3-22 回校之后，改成流式推理

\[块 001\] 推理中（20s / 19 窗口）\...

w01:0.36✗ w02:0.23✗ w03:0.09✗ w04:0.09✗ w05:0.07✗ w06:0.80✓ w07:0.99✓
w08:0.87✓

w09:0.67✓ w10:0.26✗ w11:1.00✓ w12:0.84✓ w13:0.98✓ w14:0.99✓ w15:0.77✓
w16:0.27✗

w17:0.03✗ w18:0.02✗ w19:0.03✗

\[块 001\] Abnormal 置信度 93.93% (9/19 窗口有效）

\[块 001\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0001_1774172258.wav

\[块 002\] 推理中（20s / 19 窗口）\...

w01:0.62✓ w02:0.16✗ w03:0.00✗ w04:0.00✗ w05:0.01✗ w06:0.01✗ w07:0.04✗
w08:0.02✗

w09:0.18✗ w10:0.02✗ w11:0.01✗ w12:0.01✗ w13:0.07✗ w14:0.19✗ w15:0.17✗
w16:0.85✓

w17:0.12✗ w18:0.03✗ w19:0.78✓

\[块 002\] Abnormal 置信度 79.82% (3/19 窗口有效）

\[块 002\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0002_1774172272.wav

\[块 003\] 推理中（20s / 19 窗口）\...

w01:0.01✗ w02:0.20✗ w03:0.02✗ w04:0.01✗ w05:0.02✗ w06:0.01✗ w07:0.01✗
w08:0.01✗

w09:0.01✗ w10:0.02✗ w11:0.01✗ w12:0.03✗ w13:0.25✗ w14:0.76✓ w15:0.97✓
w16:0.94✓

w17:1.00✓ w18:1.00✓ w19:1.00✓

\[块 003\] Normal 置信度 72.37% (6/19 窗口有效）

\[块 003\] 已保存:
/home/rasp4b/FypPi/debug_records/normal_c0003_1774172292.wav

\[块 004\] 推理中（20s / 19 窗口）\...

w01:0.58✗ w02:0.94✓ w03:0.51✗ w04:0.79✓ w05:0.90✓ w06:0.97✓ w07:0.99✓
w08:0.31✗

w09:0.92✓ w10:0.49✗ w11:0.05✗ w12:0.29✗ w13:0.81✓ w14:0.97✓ w15:0.89✓
w16:0.72✓

w17:0.35✗ w18:0.97✓ w19:0.98✓

\[块 004\] Abnormal 置信度 88.53% (12/19 窗口有效）

\[块 004\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0004_1774172312.wav

\[块 005\] 推理中（20s / 19 窗口）\...

w01:0.78✓ w02:0.99✓ w03:1.00✓ w04:0.06✗ w05:0.10✗ w06:0.62✓ w07:1.00✓
w08:1.00✓

w09:0.81✓ w10:0.11✗ w11:0.99✓ w12:0.65✓ w13:0.81✓ w14:0.26✗ w15:0.97✓
w16:1.00✓

w17:0.94✓ w18:0.21✗ w19:0.21✗

\[块 005\] Abnormal 置信度 74.66% (13/19 窗口有效）

\[块 005\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0005_1774172332.wav

\[块 006\] 推理中（20s / 19 窗口）\...

w01:0.95✓ w02:0.97✓ w03:0.01✗ w04:0.01✗ w05:0.00✗ w06:0.00✗ w07:0.00✗
w08:0.00✗

w09:0.00✗ w10:0.01✗ w11:0.00✗ w12:0.00✗ w13:0.00✗ w14:0.00✗ w15:0.00✗
w16:0.00✗

w17:0.00✗ w18:0.00✗ w19:0.00✗

\[块 006\] Normal 置信度 55.93% (2/19 窗口有效）

\[块 006\] 已保存:
/home/rasp4b/FypPi/debug_records/normal_c0006_1774172352.wav

\[块 007\] 推理中（20s / 19 窗口）\...

w01:0.00✗ w02:0.00✗ w03:0.00✗ w04:0.00✗ w05:0.00✗ w06:0.00✗ w07:0.00✗
w08:0.00✗

w09:0.00✗ w10:0.00✗ w11:0.00✗ w12:0.00✗ w13:0.00✗ w14:0.00✗ w15:0.00✗
w16:0.00✗

w17:0.00✗ w18:0.00✗ w19:0.00✗

\[块 007\] 信号差（0/19 窗口通过 SQA）

\[块 007\] 已保存:
/home/rasp4b/FypPi/debug_records/noise_c0007_1774172372.wav

\[块 008\] 推理中（20s / 19 窗口）\...

w01:0.00✗ w02:0.00✗ w03:0.00✗ w04:0.00✗ w05:0.00✗ w06:0.00✗ w07:0.00✗
w08:0.00✗

w09:0.00✗ w10:0.00✗ w11:0.00✗ w12:0.00✗ w13:0.00✗ w14:0.00✗ w15:0.00✗
w16:0.00✗

w17:0.00✗ w18:0.00✗ w19:0.00✗

\[块 008\] 信号差（0/19 窗口通过 SQA）

\[块 008\] 已保存:
/home/rasp4b/FypPi/debug_records/noise_c0008_1774172392.wav

已用main_pi_debug.py 本地加载

### 改成先切片再归一化

![](./media/image49.png){width="6.268055555555556in"
height="1.2868055555555555in"}

比较来看，per-window
归一化反而更合理------至少每个心音窗口都能被模型正常看到，噪声窗口虽然被拉满，但那是
SQA 该负责过滤的事情。而 chunk
级归一化会直接让好的心音窗口\"消失\"，连SQA 都救不了。

训练时用整段文件归一化之所以没问题，是因为训练数据是干净的录音，没有这种突发大噪声。真实采集环境不同，per-window
更鲁棒。

分别播放了b站正常心音、 c0031、 c0024

B站一个无噪声的心音

(.venv) rasp4b@Rasp4B:\~/FypPi \$ /home/rasp4b/FypPi/.venv/bin/python
/home/rasp4b/FypPi/main_pi_flow.py

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

正在连接 ESP32: 80:F1:B2:ED:B4:12\...

已连接，MTU: 517 字节

流式采集启动（每 20s 一块，滑窗 2.0s / hop 1.0s）

Ctrl+C 停止

\[块 001\] 推理中（20s / 19 窗口）\...

w01:0.33✗ w02:0.24✗ w03:0.42✗ w04:0.54✗ w05:0.66✓ w06:0.16✗ w07:0.01✗
w08:0.30✗

w09:0.98✓ w10:0.86✓ w11:1.00✓ w12:1.00✓ w13:1.00✓ w14:0.55✗ w15:0.18✗
w16:0.04✗

w17:0.99✓ w18:0.93✓ w19:0.71✓

\[块 001\] Abnormal 置信度 65.03% (9/19 窗口有效）

\[块 001\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0001_1774177169.wav

\[块 002\] 推理中（20s / 19 窗口）\...

w01:0.20✗ w02:0.88✓ w03:1.00✓ w04:1.00✓ w05:0.82✓ w06:0.93✓ w07:0.43✗
w08:0.60✓

w09:0.13✗ w10:0.15✗ w11:0.20✗ w12:0.16✗ w13:1.00✓ w14:1.00✓ w15:0.64✓
w16:0.60✗

w17:0.59✗ w18:1.00✓ w19:0.99✓

\[块 002\] Abnormal 置信度 76.72% (11/19 窗口有效）

\[块 002\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0002_1774177187.wav

\[块 003\] 推理中（20s / 19 窗口）\...

w01:0.15✗ w02:0.85✓ w03:0.24✗ w04:0.46✗ w05:0.86✓ w06:0.98✓ w07:1.00✓
w08:0.97✓

w09:0.78✓ w10:0.96✓ w11:0.99✓ w12:0.93✓ w13:0.41✗ w14:0.31✗ w15:0.97✓
w16:1.00✓

w17:0.98✓ w18:1.00✓ w19:1.00✓

\[块 003\] Abnormal 置信度 75.86% (14/19 窗口有效）

\[块 003\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0003_1774177207.wav

\[块 004\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:0.95✓ w05:1.00✓ w06:1.00✓ w07:0.98✓
w08:1.00✓

w09:0.97✓ w10:1.00✓ w11:1.00✓ w12:1.00✓ w13:1.00✓ w14:1.00✓ w15:1.00✓
w16:1.00✓

w17:1.00✓ w18:1.00✓ w19:1.00✓

\[块 004\] Abnormal 置信度 56.53% (19/19 窗口有效）

\[块 004\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0004_1774177227.wav

\[块 005\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:1.00✓ w06:0.98✓ w07:0.99✓
w08:0.36✗

w09:0.70✓ w10:0.97✓ w11:1.00✓ w12:1.00✓ w13:0.95✓ w14:0.99✓ w15:0.98✓
w16:0.91✓

w17:0.99✓ w18:0.99✓ w19:0.79✓

\[块 005\] Abnormal 置信度 77.56% (18/19 窗口有效）

\[块 005\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0005_1774177247.wav

\[块 006\] 推理中（20s / 19 窗口）\...

w01:0.50✗ w02:0.07✗ w03:0.24✗ w04:0.86✓ w05:0.35✗ w06:0.11✗ w07:0.78✓
w08:0.49✗

w09:0.02✗ w10:0.04✗ w11:0.01✗ w12:0.10✗ w13:0.96✓ w14:0.43✗ w15:0.89✓
w16:1.00✓

w17:1.00✓ w18:0.95✓ w19:0.74✓

\[块 006\] Abnormal 置信度 56.51% (8/19 窗口有效）

\[块 006\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0006_1774177267.wav

\[块 007\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:0.95✓ w05:1.00✓ w06:0.93✓ w07:1.00✓
w08:1.00✓

w09:0.90✓ w10:0.02✗ w11:0.01✗ w12:0.10✗ w13:0.20✗ w14:0.05✗ w15:0.10✗
w16:0.03✗

w17:0.01✗ w18:0.02✗ w19:0.60✗

\[块 007\] Abnormal 置信度 85.07% (9/19 窗口有效）

\[块 007\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0007_1774177287.wav

\^C

Ctrl+C --- 等待当前块推理完成后退出\...

已停止。

(.venv) rasp4b@Rasp4B:\~/FypPi \$ /home/rasp4b/FypPi/.venv/bin/python
/home/rasp4b/FypPi/main_pi_flow.py

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

正在连接 ESP32: 80:F1:B2:ED:B4:12\...

已连接，MTU: 517 字节

流式采集启动（每 20s 一块，滑窗 2.0s / hop 1.0s）

Ctrl+C 停止

\[块 001\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:0.20✗ w03:0.00✗ w04:0.95✓ w05:0.68✓ w06:0.72✓ w07:0.12✗
w08:0.18✗

w09:0.78✓ w10:1.00✓ w11:1.00✓ w12:0.98✓ w13:0.34✗ w14:0.79✓ w15:0.20✗
w16:0.99✓

w17:0.74✓ w18:0.90✓ w19:0.84✓

\[块 001\] Abnormal 置信度 91.14% (13/19 窗口有效）

\[块 001\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0001_1774177380.wav

\[块 002\] 推理中（20s / 19 窗口）\...

w01:0.32✗ w02:1.00✓ w03:0.35✗ w04:0.98✓ w05:1.00✓ w06:1.00✓ w07:0.89✓
w08:0.93✓

w09:0.62✓ w10:1.00✓ w11:1.00✓ w12:1.00✓ w13:1.00✓ w14:0.73✓ w15:0.97✓
w16:0.18✗

w17:0.66✓ w18:0.98✓ w19:0.60✓

\[块 002\] Abnormal 置信度 89.34% (16/19 窗口有效）

\[块 002\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0002_1774177398.wav

\[块 003\] 推理中（20s / 19 窗口）\...

w01:0.83✓ w02:0.76✓ w03:1.00✓ w04:0.90✓ w05:0.98✓ w06:1.00✓ w07:1.00✓
w08:0.89✓

w09:0.99✓ w10:0.99✓ w11:0.91✓ w12:1.00✓ w13:0.99✓ w14:0.37✗ w15:0.06✗
w16:0.01✗

w17:0.58✗ w18:0.96✓ w19:0.39✗

\[块 003\] Abnormal 置信度 94.42% (14/19 窗口有效）

\[块 003\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0003_1774177418.wav

\[块 004\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:0.99✓ w04:0.57✗ w05:0.95✓ w06:0.49✗ w07:0.09✗
w08:0.51✗

w09:0.92✓ w10:1.00✓ w11:0.99✓ w12:0.95✓ w13:1.00✓ w14:1.00✓ w15:0.66✓
w16:0.91✓

w17:0.91✓ w18:0.52✗ w19:0.85✓

\[块 004\] Abnormal 置信度 91.03% (14/19 窗口有效）

\[块 004\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0004_1774177438.wav

\[块 005\] 推理中（20s / 19 窗口）\...

w01:0.89✓ w02:0.75✓ w03:0.69✓ w04:0.05✗ w05:0.01✗ w06:0.45✗ w07:0.62✓
w08:0.83✓

w09:0.15✗ w10:1.00✓ w11:1.00✓ w12:1.00✓ w13:0.97✓ w14:0.41✗ w15:0.95✓
w16:0.36✗

w17:0.89✓ w18:0.56✗ w19:0.13✗

\[块 005\] Abnormal 置信度 82.20% (11/19 窗口有效）

\[块 005\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0005_1774177457.wav

\[块 006\] 推理中（20s / 19 窗口）\...

w01:0.90✓ w02:0.98✓ w03:0.64✓ w04:0.44✗ w05:0.36✗ w06:0.95✓ w07:1.00✓
w08:0.98✓

w09:0.99✓ w10:0.91✓ w11:0.90✓ w12:1.00✓ w13:0.99✓ w14:0.82✓ w15:1.00✓
w16:0.99✓

w17:0.29✗ w18:0.81✓ w19:0.04✗

\[块 006\] Abnormal 置信度 89.23% (15/19 窗口有效）

\[块 006\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0006_1774177477.wav

\[块 007\] 推理中（20s / 19 窗口）\...

w01:0.53✗ w02:0.99✓ w03:1.00✓ w04:1.00✓ w05:0.21✗ w06:0.63✓ w07:1.00✓
w08:0.90✓

w09:0.64✓ w10:0.56✗ w11:1.00✓ w12:0.99✓ w13:1.00✓ w14:0.98✓ w15:0.86✓
w16:0.98✓

w17:0.78✓ w18:0.98✓ w19:0.99✓

\[块 007\] Abnormal 置信度 95.29% (16/19 窗口有效）

\[块 007\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0007_1774177497.wav

\^C

Ctrl+C --- 等待当前块推理完成后退出\...

已停止。

(.venv) rasp4b@Rasp4B:\~/FypPi \$ /home/rasp4b/FypPi/.venv/bin/python
/home/rasp4b/FypPi/main_pi_flow.py

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

正在连接 ESP32: 80:F1:B2:ED:B4:12\...

已连接，MTU: 517 字节

流式采集启动（每 20s 一块，滑窗 2.0s / hop 1.0s）

Ctrl+C 停止

\[块 001\] 推理中（20s / 19 窗口）\...

w01:0.52✗ w02:0.01✗ w03:0.00✗ w04:0.06✗ w05:0.08✗ w06:0.00✗ w07:0.04✗
w08:0.01✗

w09:0.02✗ w10:0.60✗ w11:0.02✗ w12:0.19✗ w13:0.06✗ w14:0.04✗ w15:0.48✗
w16:0.22✗

w17:0.05✗ w18:0.05✗ w19:0.00✗

\[块 001\] 信号差（0/19 窗口通过 SQA）

\[块 001\] 已保存:
/home/rasp4b/FypPi/debug_records/noise_c0001_1774177559.wav

\[块 002\] 推理中（20s / 19 窗口）\...

w01:0.88✓ w02:0.01✗ w03:0.03✗ w04:0.94✓ w05:0.01✗ w06:0.02✗ w07:0.21✗
w08:0.68✓

w09:0.84✓ w10:0.77✓ w11:0.19✗ w12:0.30✗ w13:0.02✗ w14:0.70✓ w15:0.81✓
w16:0.01✗

w17:0.08✗ w18:0.88✓ w19:0.11✗

\[块 002\] Abnormal 置信度 87.13% (8/19 窗口有效）

\[块 002\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0002_1774177577.wav

\[块 003\] 推理中（20s / 19 窗口）\...

w01:0.33✗ w02:0.13✗ w03:0.75✓ w04:0.91✓ w05:0.17✗ w06:0.09✗ w07:0.03✗
w08:0.01✗

w09:0.58✗ w10:0.14✗ w11:0.04✗ w12:0.03✗ w13:0.01✗ w14:0.66✓ w15:0.69✓
w16:0.01✗

w17:0.86✓ w18:0.99✓ w19:0.00✗

\[块 003\] Abnormal 置信度 83.82% (6/19 窗口有效）

\[块 003\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0003_1774177597.wav

\[块 004\] 推理中（20s / 19 窗口）\...

w01:0.79✓ w02:0.02✗ w03:0.11✗ w04:0.36✗ w05:0.02✗ w06:0.12✗ w07:0.59✗
w08:0.04✗

w09:0.17✗ w10:0.79✓ w11:0.01✗ w12:0.00✗ w13:0.98✓ w14:0.92✓ w15:0.18✗
w16:0.30✗

w17:0.94✓ w18:0.82✓ w19:0.29✗

\[块 004\] Abnormal 置信度 76.66% (6/19 窗口有效）

\[块 004\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0004_1774177617.wav

\[块 005\] 推理中（20s / 19 窗口）\...

w01:0.64✓ w02:0.96✓ w03:0.20✗ w04:0.01✗ w05:0.85✓ w06:0.07✗ w07:0.01✗
w08:0.60✗

w09:0.22✗ w10:0.24✗ w11:1.00✓ w12:0.50✗ w13:0.94✓ w14:1.00✓ w15:0.09✗
w16:0.95✓

w17:0.99✓ w18:0.68✓ w19:0.42✗

\[块 005\] Abnormal 置信度 76.30% (9/19 窗口有效）

\[块 005\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0005_1774177637.wav

\[块 006\] 推理中（20s / 19 窗口）\...

w01:0.00✗ w02:0.01✗ w03:0.00✗ w04:0.03✗ w05:0.15✗ w06:0.03✗ w07:0.55✗
w08:0.04✗

w09:0.01✗ w10:0.37✗ w11:0.40✗ w12:0.01✗ w13:0.16✗ w14:0.01✗ w15:0.28✗
w16:0.88✓

w17:0.05✗ w18:0.20✗ w19:0.13✗

\[块 006\] Abnormal 置信度 91.49% (1/19 窗口有效）

\[块 006\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0006_1774177657.wav

\[块 007\] 推理中（20s / 19 窗口）\...

w01:0.44✗ w02:0.09✗ w03:0.38✗ w04:0.04✗ w05:0.00✗ w06:0.22✗ w07:0.86✓
w08:0.02✗

w09:0.03✗ w10:0.71✓ w11:0.02✗ w12:0.01✗ w13:0.51✗ w14:0.97✓ w15:0.88✓
w16:0.19✗

w17:0.00✗ w18:0.32✗ w19:0.02✗

\[块 007\] Abnormal 置信度 86.40% (4/19 窗口有效）

\[块 007\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0007_1774177677.wav

(.venv) rasp4b@Rasp4B:\~/FypPi \$ /home/rasp4b/FypPi/.venv/bin/python
/home/rasp4b/FypPi/main_pi.py

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

正在连接 ESP32: 80:F1:B2:ED:B4:12\...

已连接，MTU: 517 字节

流式采集启动（每 20s 一块，滑窗 2.0s / hop 1.0s）

Ctrl+C 停止

\[块 001\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:1.00✓ w06:1.00✓ w07:1.00✓
w08:1.00✓

w09:0.97✓ w10:0.99✓ w11:1.00✓ w12:1.00✓ w13:1.00✓ w14:1.00✓ w15:1.00✓
w16:1.00✓

w17:1.00✓ w18:1.00✓ w19:1.00✓

\[块 001\] Abnormal 置信度 91.28% (19/19 窗口有效）

\[块 001\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0001_1774188053.wav

\[块 002\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:1.00✓ w06:1.00✓ w07:1.00✓
w08:1.00✓

w09:1.00✓ w10:1.00✓ w11:1.00✓ w12:1.00✓ w13:1.00✓ w14:1.00✓ w15:1.00✓
w16:1.00✓

w17:0.06✗ w18:0.00✗ w19:0.00✗

\[块 002\] Abnormal 置信度 90.84% (16/19 窗口有效）

\[块 002\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0002_1774188066.wav

\[块 003\] 推理中（20s / 19 窗口）\...

w01:0.89✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:1.00✓ w06:1.00✓ w07:1.00✓
w08:0.97✓

w09:1.00✓ w10:1.00✓ w11:0.99✓ w12:1.00✓ w13:1.00✓ w14:1.00✓ w15:1.00✓
w16:1.00✓

w17:1.00✓ w18:1.00✓ w19:1.00✓

\[块 003\] Abnormal 置信度 86.45% (19/19 窗口有效）

\[块 003\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0003_1774188086.wav

\[块 004\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:1.00✓ w06:0.99✓ w07:1.00✓
w08:1.00✓

w09:0.99✓ w10:1.00✓ w11:1.00✓ w12:1.00✓ w13:1.00✓ w14:1.00✓ w15:1.00✓
w16:0.96✓

w17:1.00✓ w18:1.00✓ w19:1.00✓

\[块 004\] Abnormal 置信度 89.87% (19/19 窗口有效）

\[块 004\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0004_1774188106.wav

\[块 005\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:1.00✓ w06:1.00✓ w07:1.00✓
w08:1.00✓

w09:0.94✓ w10:0.99✓ w11:0.99✓ w12:1.00✓ w13:1.00✓ w14:0.02✗ w15:0.00✗
w16:0.00✗

w17:0.18✗ w18:1.00✓ w19:1.00✓

\[块 005\] Abnormal 置信度 96.20% (15/19 窗口有效）

\[块 005\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0005_1774188126.wav

\[块 006\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:0.99✓ w06:1.00✓ w07:0.98✓
w08:1.00✓

w09:1.00✓ w10:1.00✓ w11:1.00✓ w12:0.99✓ w13:1.00✓ w14:1.00✓ w15:1.00✓
w16:1.00✓

w17:1.00✓ w18:1.00✓ w19:1.00✓

\[块 006\] Abnormal 置信度 90.14% (19/19 窗口有效）

\[块 006\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0006_1774188146.wav

\[块 007\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:0.97✓ w06:1.00✓ w07:1.00✓
w08:1.00✓

w09:1.00✓ w10:1.00✓ w11:1.00✓ w12:1.00✓ w13:1.00✓ w14:1.00✓ w15:0.99✓
w16:1.00✓

w17:1.00✓ w18:1.00✓ w19:1.00✓

\[块 007\] Abnormal 置信度 91.91% (19/19 窗口有效）

\[块 007\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0007_1774188166.wav

\[块 008\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:1.00✓ w06:1.00✓ w07:1.00✓
w08:1.00✓

w09:0.97✓ w10:0.83✓ w11:0.00✗ w12:0.02✗ w13:0.00✗ w14:0.02✗ w15:0.99✓
w16:1.00✓

w17:1.00✓ w18:1.00✓ w19:1.00✓

\[块 008\] Abnormal 置信度 87.73% (15/19 窗口有效）

\[块 008\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0008_1774188186.wav

\[块 009\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:1.00✓ w06:1.00✓ w07:0.99✓
w08:1.00✓

w09:1.00✓ w10:1.00✓ w11:1.00✓ w12:1.00✓ w13:1.00✓ w14:1.00✓ w15:1.00✓
w16:1.00✓

w17:1.00✓ w18:1.00✓ w19:1.00✓

\[块 009\] Abnormal 置信度 89.48% (19/19 窗口有效）

\[块 009\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0009_1774188206.wav

\[块 010\] 推理中（20s / 19 窗口）\...

w01:1.00✓ w02:1.00✓ w03:1.00✓ w04:1.00✓ w05:1.00✓ w06:1.00✓ w07:1.00✓
w08:1.00✓

w09:0.99✓ w10:0.98✓ w11:1.00✓ w12:1.00✓ w13:1.00✓ w14:1.00✓ w15:1.00✓
w16:1.00✓

w17:1.00✓ w18:1.00✓ w19:1.00✓

\[块 010\] Abnormal 置信度 97.81% (19/19 窗口有效）

\[块 010\] 已保存:
/home/rasp4b/FypPi/debug_records/abnormal_c0010_1774188226.wav

\^C

Ctrl+C --- 等待当前块推理完成后退出\...

==================================================

最终统计: 共 10 块

Normal 0 块

Abnormal 10 块

低质量 0 块（全部窗口未通过 SQA）

正常心音，c0031，c0024

  --------------------------------------------------------------------------------
  **运行批次**   **块编号     **有效窗口数         **最终判定     **置信度
                 (Block)**    (SQA通过/总数)**     (Result)**     (Confidence)**
  -------------- ------------ -------------------- -------------- ----------------
  **Batch 1**    001          9/19                 **Abnormal**   65.03%

                 002          11/19                **Abnormal**   76.72%

                 003          14/19                **Abnormal**   75.86%

                 004          19/19                **Abnormal**   56.53%

                 005          18/19                **Abnormal**   77.56%

                 006          8/19                 **Abnormal**   56.51%

                 007          9/19                 **Abnormal**   85.07%

  \-\--          \-\--        \-\--                \-\--          \-\--

  **Batch 2**    001          13/19                **Abnormal**   91.14%

                 002          16/19                **Abnormal**   89.34%

                 003          14/19                **Abnormal**   94.42%

                 004          14/19                **Abnormal**   91.03%

                 005          11/19                **Abnormal**   82.20%

                 006          15/19                **Abnormal**   89.23%

                 007          16/19                **Abnormal**   95.29%

  \-\--          \-\--        \-\--                \-\--          \-\--

  **Batch 3**    001          0/19                 **信号差**     N/A

                 002          8/19                 **Abnormal**   87.13%

                 003          6/19                 **Abnormal**   83.82%

                 004          6/19                 **Abnormal**   76.66%

                 005          9/19                 **Abnormal**   76.30%

                 006          1/19                 **Abnormal**   91.49%

                 007          4/19                 **Abnormal**   86.40%
  --------------------------------------------------------------------------------

  -------------------------------------------------------------------
  **块编号       **有效窗口数**   **最终判定       **置信度
  (Block)**                       (Result)**       (Confidence)**
  -------------- ---------------- ---------------- ------------------
  001            **19/19**        **Abnormal**     91.28%

  002            16/19            **Abnormal**     90.84%

  003            **19/19**        **Abnormal**     86.45%

  004            **19/19**        **Abnormal**     89.87%

  005            15/19            **Abnormal**     96.20%

  006            **19/19**        **Abnormal**     90.14%

  007            **19/19**        **Abnormal**     91.91%

  008            15/19            **Abnormal**     87.73%

  009            **19/19**        **Abnormal**     89.48%

  010            **19/19**        **Abnormal**     **97.81%**
  -------------------------------------------------------------------

![](./media/image50.png){width="6.268055555555556in"
height="3.2423611111111112in"}

# References

# Appendices

  ---------------------------------------------------------------------
  Appendix 1
  ---------------------------------------------------------------------
  Introduce:

  ---------------------------------------------------------------------

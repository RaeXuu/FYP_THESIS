**rasp4b@Rasp4B**:**~ $** /home/rasp4b/FypPi/.venv/bin/python /home/rasp4b/FypPi/evaluate.py --mode sqa

  

============================================================

SQA 模型评估（test_split_sqa.csv）

  测试录音数：324  Bad(label=0)=32  Good(label=1)=292

  索引约定：SQA_IDX_BAD=1  SQA_IDX_GOOD=0

============================================================

  

  [FP32]  SQA=heart_quality_fp32.tflite

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

    FP32: 100%|█████████████████████████████████████████████████████████████████████| 324/324 [02:22<00:00,  2.27file/s]

    TP=435 TN=4607 FP=1638 FN=46  (skipped=0)

    Accuracy=75.0%  M-Score=82.1%  Se(Bad)=90.4%  Sp(Good)=73.8%  (evaluated=6726 切片)

  

  [INT8]  SQA=heart_quality_quant.tflite

    INT8: 100%|█████████████████████████████████████████████████████████████████████| 324/324 [02:07<00:00,  2.55file/s]

    TP=434 TN=4605 FP=1640 FN=47  (skipped=0)

    Accuracy=74.9%  M-Score=82.0%  Se(Bad)=90.2%  Sp(Good)=73.7%  (evaluated=6726 切片)

  

============================================================

FP32 vs INT8 对比（SQA 模型）

============================================================

  Metric               FP32       INT8     Change

  --------------------------------------------

  M-Score             82.1%      82.0%      -0.1%

  Se(Bad)             90.4%      90.2%      -0.2%

  Sp(Good)            73.8%      73.7%      -0.0%

  Accuracy            75.0%      74.9%      -0.0%

============================================================

  

**rasp4b@Rasp4B**:**~ $** /home/rasp4b/FypPi/.venv/bin/python /home/rasp4b/FypPi/evaluate.py --mode diag

  

============================================================

诊断模型评估（解耦，无 SQA 门控，test_split.csv）

  测试录音数：288

============================================================

  

  [FP32]  DIAG=heart_model_fp32.tflite

INFO: Created TensorFlow Lite XNNPACK delegate for CPU.

    FP32: 100%|█████████████████████████████████████████████████████████████████████| 288/288 [02:04<00:00,  2.32file/s]

    Accuracy=83.3%  M-Score=89.1%  Se=98.0%  Sp=80.2%  (evaluated=288, skipped=0)

    推理耗时 mean=431ms  min=124ms  max=3141ms

  

  [INT8]  DIAG=heart_model_quant.tflite

    INT8: 100%|█████████████████████████████████████████████████████████████████████| 288/288 [01:58<00:00,  2.42file/s]

    Accuracy=83.3%  M-Score=89.1%  Se=98.0%  Sp=80.2%  (evaluated=288, skipped=0)

    推理耗时 mean=412ms  min=116ms  max=1183ms

  

============================================================

FP32 vs INT8 对比（诊断模型，解耦）

============================================================

  Metric               FP32       INT8     Change

  --------------------------------------------

  M-Score             89.1%      89.1%      +0.0%

  Sensitivity         98.0%      98.0%      +0.0%

  Specificity         80.2%      80.2%      +0.0%

  Accuracy            83.3%      83.3%      +0.0%

============================================================
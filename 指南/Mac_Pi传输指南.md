# Mac ↔ Raspberry Pi 文件传输指南

Pi：`rasp4b@Rasp4B.local`

---

## SSH 快捷配置（建议先做）

编辑 `~/.ssh/config`：

```
Host pi
    HostName Rasp4B.local
    User rasp4b
```

之后所有命令用 `pi` 代替完整地址。免密登录：

```bash
ssh-keygen -t ed25519      # 已有则跳过
ssh-copy-id pi
```

---

## scp — 单文件传输

```bash
# Mac → Pi
scp 文件名 pi:~/FypPi/

# Pi → Mac（下载到当前目录）
scp pi:~/FypPi/文件名 .

# 一次下载多个文件
scp "pi:~/FypPi/{confusion_matrix_diag.pdf,confusion_matrix_sqa.pdf}" .

# 传文件夹加 -r
scp -r pi:~/FypPi/results/ ./results/
```

---

## rsync — 目录同步（批量/反复同步用这个）

```bash
# Mac → Pi（上传目录）
rsync -avz --exclude='__pycache__' --exclude='.DS_Store' \
  scripts/ pi:~/FypPi/scripts/

# Pi → Mac（拉回结果）
rsync -avz pi:~/FypPi/results/ ./results/

# 只拉 PDF
rsync -avz --include='*.pdf' --exclude='*' pi:~/FypPi/ ./figures/
```

---

## 本项目常用命令

```bash
# 上传脚本
scp plot_confusion_matrix.py pi:~/FypPi/

# 拉回图表
scp "pi:~/FypPi/*.pdf" .

# 拉回 benchmark 结果
scp pi:~/FypPi/evaluate_benchmark_result.md .
```

---

> **Rasp4B.local 找不到？** 在 Pi 上 `hostname -I` 查 IP，替换掉 `.local` 地址。

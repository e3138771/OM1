# OM1 繁體中文快速入門指南

OM1 是一個專為機器人設計的模組化 AI 運行環境。本指南幫助中文開發者快速設定環境。

## 🛠️ 安裝步驟

### 1. 複製專案
```bash
git clone [https://github.com/OpenMind/OM1.git](https://github.com/OpenMind/OM1.git)
cd OM1
git submodule update --init
uv venv
2. 安裝系統依賴
MacOS: brew install portaudio ffmpeg

Linux: sudo apt-get update && sudo apt-get install portaudio19-dev python-dev ffmpeg

3. 設定 API 金鑰
前往 OpenMind Portal 取得你的 API Key。

執行 cp env.example .env 並將 Key 填入 .env 檔案中。

4. 啟動 Spot 代理
執行以下指令啟動範例：

Bash

uv run src/run.py spot
啟動後，請訪問：http://localhost:8000/ 進入 WebSim 介面。

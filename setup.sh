#!/bin/bash
# macOS/Linux 虛擬環境設定腳本

echo "設定Python虛擬環境..."

# 創建虛擬環境
python3 -m venv venv

echo "虛擬環境創建完成！"
echo ""
echo "請執行以下指令來啟動虛擬環境："
echo "source venv/bin/activate"
echo ""
echo "然後安裝依賴套件："
echo "pip install -r requirements.txt"
echo ""
echo "最後執行程式："
echo "python main.py"
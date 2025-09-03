@echo off
rem Windows 虛擬環境設定批次檔

echo 設定Python虛擬環境...

rem 創建虛擬環境
python -m venv venv

echo 虛擬環境創建完成！
echo.
echo 請執行以下指令來啟動虛擬環境：
echo venv\Scripts\activate
echo.
echo 然後安裝依賴套件：
echo pip install -r requirements.txt
echo.
echo 最後執行程式：
echo python main.py
echo.
pause
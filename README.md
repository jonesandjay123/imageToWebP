# 圖片轉WebP工具

一個簡單的Python GUI應用程式，可以將多種格式的圖片批次轉換為WebP格式。

## 功能特色

- ✅ 支援多種圖片格式：PNG, JPG, JPEG, BMP, TIFF, GIF
- ✅ 批次處理多個檔案  
- ✅ 圖形化使用者介面
- ✅ 可調整輸出品質（10-100）
- ✅ 即時進度顯示
- ✅ 自動產生同名WebP檔案
- ✅ 轉換完成後可直接開啟輸出資料夾

## 系統需求

- Python 3.7 或更新版本
- tkinter（大部分Python安裝都包含）
- Pillow庫

## 快速開始

### 方法一：使用設定腳本（推薦）

#### macOS/Linux：
```bash
# 執行設定腳本
./setup.sh

# 啟動虛擬環境
source venv/bin/activate

# 安裝依賴套件
pip install -r requirements.txt

# 執行程式
python main.py
```

#### Windows：
```cmd
# 執行設定腳本
setup.bat

# 啟動虛擬環境
venv\Scripts\activate

# 安裝依賴套件
pip install -r requirements.txt

# 執行程式
python main.py
```

### 方法二：手動設定虛擬環境

#### macOS/Linux：
```bash
# 1. 創建虛擬環境
python3 -m venv venv

# 2. 啟動虛擬環境
source venv/bin/activate

# 3. 安裝依賴套件
pip install -r requirements.txt

# 4. 執行程式
python main.py
```

#### Windows：
```cmd
# 1. 創建虛擬環境
python -m venv venv

# 2. 啟動虛擬環境
venv\Scripts\activate

# 3. 安裝依賴套件
pip install -r requirements.txt

# 4. 執行程式
python main.py
```

## 疑難排解

### macOS tkinter 問題
如果在macOS上遇到tkinter相關錯誤：

**解決方案一：使用系統內建Python（推薦）**
```bash
# 刪除舊的虛擬環境
rm -rf venv

# 使用系統內建Python創建虛擬環境（通常包含tkinter）
/usr/bin/python3 -m venv venv

# 啟動虛擬環境
source venv/bin/activate

# 安裝依賴套件
pip install -r requirements.txt
```

**解決方案二：安裝支援tkinter的Python**
```bash
# 使用Homebrew安裝支援tkinter的Python
brew install python-tk

# 或者重新安裝Python
brew reinstall python@3.11
```

### Windows tkinter 問題  
Windows用戶通常不會遇到tkinter問題，如果有問題請重新安裝Python並確保勾選「tcl/tk and IDLE」選項。

### 虛擬環境啟動問題
- **macOS/Linux**：確保使用 `source venv/bin/activate` 
- **Windows**：確保使用 `venv\Scripts\activate`
- 如果權限不足，Windows用戶可能需要以管理員身份執行

### 離開虛擬環境
在任何系統上，使用以下指令離開虛擬環境：
```bash
deactivate
```

## 使用方法

### 軟體介面說明

1. **選擇檔案**：點擊「選擇檔案」按鈕選擇要轉換的圖片（支援多選）
2. **選擇輸出資料夾**：點擊「選擇輸出資料夾」選擇WebP檔案的儲存位置
3. **清除選取**：點擊「清除選取」按鈕清空已選擇的檔案清單
4. **品質設定**：使用滑桿調整輸出品質（10-100，預設90）
   - 品質越高，檔案越大，畫質越好
   - 品質越低，檔案越小，但畫質會下降
5. **開始轉換**：點擊「開始轉換」按鈕進行批次轉換
6. **進度顯示**：轉換過程中會顯示進度條和目前處理的檔案
7. **完成後操作**：轉換完成後可選擇開啟輸出資料夾

### 操作流程

1. 啟動程式後，會看到簡潔的圖形介面
2. 使用「選擇檔案」按鈕選取要轉換的圖片（可同時選取多個）
3. 選取的檔案會顯示在檔案清單中
4. 使用「選擇輸出資料夾」指定轉換後檔案的儲存位置
5. 根據需要調整品質設定
6. 點擊「開始轉換」開始批次處理
7. 等待轉換完成，查看結果

## 專案結構

```
imageToWebP/
├── main.py              # 程式入口點
├── gui.py               # GUI介面程式
├── image_converter.py   # 圖片轉換核心邏輯
├── requirements.txt     # 依賴套件清單
├── setup.sh            # macOS/Linux 虛擬環境設定腳本
├── setup.bat           # Windows 虛擬環境設定腳本
└── README.md           # 專案說明文件（本檔案）
```

## 技術特點

- **跨平台支援**：支援 Windows、macOS、Linux
- **虛擬環境隔離**：避免套件版本衝突
- **批次處理**：一次處理多個檔案，提高效率
- **即時回饋**：顯示轉換進度和狀態
- **錯誤處理**：妥善處理各種異常情況
- **使用者友善**：直觀的圖形介面，操作簡單

## 注意事項

- 轉換後的WebP檔案將使用與原始檔案相同的檔名（僅更改副檔名）
- 品質設定會影響檔案大小和畫質，建議根據用途選擇合適的品質
- 程式會自動建立輸出資料夾（如不存在）
- 支援的輸入格式包括：PNG, JPG, JPEG, BMP, TIFF, GIF
- 轉換過程中請勿關閉程式，以免造成檔案損壞

## 常見問題

**Q: 為什麼要使用WebP格式？**
A: WebP格式相比傳統的JPEG和PNG，能在保持相似畫質的情況下顯著減少檔案大小，適合網頁使用。

**Q: 轉換後的檔案在哪裡？**  
A: 檔案會儲存在你選擇的輸出資料夾中，檔名與原始檔案相同但副檔名為.webp。

**Q: 可以同時轉換很多檔案嗎？**
A: 可以，程式支援批次處理，你可以一次選擇多個檔案進行轉換。

**Q: 程式執行時出現錯誤怎麼辦？**
A: 請檢查是否正確設定了虛擬環境，並確保所有依賴套件都已正確安裝。
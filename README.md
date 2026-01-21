[![GitHub stats](https://github-readme-stats.vercel.app/api?username=baihufox3210)]

# Auto Count

一個自動化的 Discord 數字接龍機器人。此工具能夠自動讀取特定頻道中的最新數字訊息，解析其數學表達式，並自動發送下一個數字。

## 🌟 主要功能

- **自動接龍**：即時監控 Discord 頻道，發現新數字後自動接下去。
- **四平方和分解**：發送的數字會自動轉換為最多四個整數的平方和格式（例如：`14` -> `3²+2²+1²`）。
- **強大的表達式解析**：支援多種數學表達式，包括：

    - 標準運算：`+`, `-`, `*`, `/`
    - 上標指數：如 `²`, `³`, `⁴` 等。
    - 全形字元支援：支援全形數字與符號（如 `１＋１`）。
- **防重複發送**：自動記錄最後處理的訊息 ID，避免重複處理。
- **身分識別**：預設排除特定使用者的訊息（如 `baihufox`），防止自我循環。

## 🛠️ 安裝步驟

1. **安裝 Python 依賴**：
   確保您的環境已安裝 Python 3.x，然後執行以下命令：
   ```bash
   pip install requests asteval python-dotenv
   ```

2. **設定環境變數**：
   在專案根目錄下建立 `.env` 檔案，並填入您的資訊：
   ```env
   DISCORD_TOKEN=DISCORD_TOKEN
   CHANNEL_ID=CHANNEL_ID
   ```

3. **設定過濾使用者** (選用)：
   在 `main.py` 中，您可以修改 `user_name` 變數來指定要排除的使用者名稱（預設為 `baihufox`）：
   ```python
   user_name = "user_name"
   ```

## 🚀 使用方法

在專案目錄下執行：
```bash
python main.py
```
程式會開始無限迴圈監控該頻道，並在有新數字出現時自動回覆。

## 📂 專案架構

- `main.py`: 程式進入點，負責主循環邏輯與轉發邏輯。
- `src/Calculate/Calculate.py`: 處理數學表達式的正規化與求值。
- `src/Discord/Discord.py`: 負責與 Discord API 互動（取得訊息與發送訊息）。
- `src/Extension/sum_of_squares.py`: 提供拉格朗日四平方和分解功能，將數字轉換為平方和格式。
- `.env`: 儲存敏感的認證資訊（需自行建立）。

## ⚠️ 注意事項

- 本工具僅供學術研究與自動化測試使用，請遵守 Discord 的服務條款（ToS）。
- 過度頻繁的 API 調用可能會導致帳號受到限制，請謹慎調整 `sleep` 時間。

# Project Gutenberg 中文書爬蟲 📚

這個專案會自動爬取 [Project Gutenberg](https://www.gutenberg.org/browse/languages/zh) 上的**中文書籍**，儲存為純文字檔案（`.txt`），共收錄 **N 本書籍**（實際數量依網頁更新會不同）。

---

## 📦 需要安裝的套件

執行前，請先安裝以下套件，可用 `pip` 或 `conda` 安裝：

| 套件名稱         | 使用版本 | 安裝指令                          |
|------------------|--------------|-----------------------------------|
| `requests`       | 2.32.3          | `pip install requests`           |
| `beautifulsoup4` | 4.13.4          | `pip install beautifulsoup4`     |


> ✅ 可以透過 `pip list` 或 `conda list` 查看安裝版本。

---

## 🧠 程式說明

本程式做了以下幾件事：

1. 進入 Project Gutenberg 的中文書籍頁面
2. 檢查書名是否為純中文（跳過英文書名）
3. 取得書籍編號、對應的 HTML 內容頁
4. 從頁面中取出內文（僅擷取含中文字的段落）
5. 將每本書儲存為 `.txt` 純文字檔，放在 `project_gutenberg/` 資料夾中

---

## ▶️ 如何執行

1. 確保你安裝好 Python 3.6+
2. 將此檔案命名為 `gutenberg_crawler.py`
3. 終端機中執行：

```bash
python gutenberg_crawler.py
```
---
## 📁 結果範例
📂 目錄結構：
```
project_gutenberg/
├── 三國演義.txt
├── 紅樓夢.txt
└── 儒林外史.txt
```
📸 擷取畫面範例：

📹 示範影片：

---

## 📝 其它補充
* 預設會跳過英文書名，僅保存純中文書
* 延遲時間為 0.5~2 秒之間隨機，以降低被封鎖風險

---
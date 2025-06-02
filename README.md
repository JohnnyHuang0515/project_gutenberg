# Project Gutenberg Chinese Book Crawler 📚

This project automatically crawls Chinese-language books from [Project Gutenberg](https://www.gutenberg.org/browse/languages/zh) and saves them as plain text files (`.txt`). A total of `354` books are collected (actual number may vary depending on site updates).

---

## 📦 Required Packages

Before running the script, please make sure the following packages are installed. You can use either `pip` or `conda`:

| Package Name     | Version | Installation Command                     |
|------------------|--------------|-----------------------------------|
| `requests`       | 2.32.3          | `pip install requests`           |
| `beautifulsoup4` | 4.13.4          | `pip install beautifulsoup4`     |


 ✅ You can check installed versions with `pip list` or `conda list`.

---

## 🧠Program Overview

This script performs the following steps:
1. Accesses the Chinese books page on Project Gutenberg
2. Filters out titles that are not fully in Chinese (skipping English titles)
3. Retrieves the book ID and corresponding HTML content page
4. Extracts the content (only paragraphs containing Chinese characters)
5. Saves each book as a `.txt` file in the `project_gutenberg/` directory

---

## ▶️ How to Run

1. Ensure you have Python 3.6 or later installed
2. Save this file as `gutenberg_crawler.py`
3. Run the script in your terminal:

```bash
python gutenberg_crawler.py
```
---

## 📁 Sample Output
📂 Directory structure:
```
project_gutenberg/
├── 三國演義.txt
├── 紅樓夢.txt
└── 儒林外史.txt
```
📸 Screenshot example:

![示範圖片](https://github.com/JohnnyHuang0515/project_gutenberg/blob/main/project_gutenberg/images/demo.png?raw=true)

📹 Demo video:
https://youtu.be/VTZ56Z876JQ

---

## 📝 Additional Notes
* By default, books with English titles are skipped; only fully Chinese titles are downloaded
* A random delay of 0.5 to 2 seconds is used between requests to reduce the risk of being blocked

---

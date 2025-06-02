# Project Gutenberg Chinese Book Crawler 📚

This project automatically crawls Chinese books from Project Gutenberg and saves them as plain text files (.txt). A total of 354 books are fetched (the actual number may vary depending on website updates).

---

## 📦 Required Packages

Before running the script, please install the following packages using either `pip` or `conda`:

| Package Name     | Version | Installation Command                     |
|------------------|--------------|-----------------------------------|
| `requests`       | 2.32.3          | `pip install requests`           |
| `beautifulsoup4` | 4.13.4          | `pip install beautifulsoup4`     |


 ✅ You can check installed versions using `pip list` or `conda list`.

---

## 🧠Program Overview

This script performs the following tasks:

1. Accesses the Chinese book page on Project Gutenberg
2. Checks if the book title is purely in Chinese (skips English titles)
3. Retrieves the book ID and corresponding HTML content page
4. Extracts content from the page (only paragraphs containing Chinese characters)
5. Saves each book as a `.txt` file in the `project_gutenberg/` folder

---

## ▶️ How to Run

1. Make sure you have Python 3.6+ installed
2. Save this file as `gutenberg_crawler.py`
3. Run the script in the terminal:

```bash
python gutenberg_crawler.py
```
---

## 📁 Sample Output
📂 Folder structure:
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
* By default, books with English titles are skipped; only pure Chinese books are saved
* A random delay between 0.5 to 2 seconds is added to reduce the risk of being blocked

---

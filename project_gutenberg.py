import re
import requests as req
from bs4 import BeautifulSoup as bs
import os, random
from time import sleep
#創建資料夾
folderPath = "project_gutenberg"
if not os.path.exists(folderPath):
    os.makedirs(folderPath)
#抓取文章編號
url = "https://www.gutenberg.org/browse/languages/zh"
my_header = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.0.0 Safari/537.36 Edg/136.0.0.0"
}
res = req.get(url, headers=my_header)
soup = bs(res.text, "lxml")
#自訂一個檢查中文字的規則
chinese_check = re.compile(r'[\u4E00-\u9FFF]+')
#取得書名並檢查是不是中文字
for li in soup.select("li.pgdbetext > a[href]"):
    title = li.get_text()
    if not chinese_check.fullmatch(title):
        continue
#取得書籍編號
    book_num = re.findall(r'\d+', li["href"])
    if not book_num:
        continue
    book_num = book_num[0]
#抓取文章內容
    url_p = f"https://www.gutenberg.org/cache/epub/{book_num}/pg{book_num}-images.html"
    res_p = req.get(url_p, headers=my_header)
    soup_p = bs(res_p.text, "lxml")
#取得所有是數字的id標籤
    contents_id = soup_p.find_all(id=re.compile(r'\d+'))
#把id的內容取出來檢查是不是都是中文字，將通過篩選的文字換行並接起來
    content_chinese = "\n".join([line.get_text(strip=True) for line in contents_id if chinese_check.search(line.get_text())])
    file_path = os.path.join(folderPath, f"{title}.txt")
#寫入檔案
    with open(file_path, "w", encoding='<utf-8>') as f:
        f.write(content_chinese)
    print(f"檔名:{title},儲存成功")

    sleep(random.uniform(0.5,2))

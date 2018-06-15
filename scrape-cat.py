import requests
from bs4 import BeautifulSoup

r = requests.get("replace URL")
soup = BeautifulSoup(r.content, "html.parser")

div = soup.find("div", class_="readingContent01")
for li in div.find_all("li"): #divタグ内の全liタグを取得
    url = li.a["href"] #liタグ内のaタグのhref属性値を取得
    date, text = li.a.text.split(maxsplit=1) #日付とタイトルに分割
    print("{},{},{}".format(date, text, url))

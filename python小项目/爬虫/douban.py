import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0"}
respones = requests.get("https://movie.douban.com/chart", headers=headers)
html = respones.text
soup = BeautifulSoup(html, "html.parser")
all_titles=soup.find_all("a")
for i in all_titles:
    i1=i.get_text()
    print(i1)


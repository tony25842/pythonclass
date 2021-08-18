import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/Stock/index.html"
for times in range(5):
    res = requests.get(url)
    html = BeautifulSoup(res.text, 'html.parser')
    articles = html.select('.title a')
    paging = html.select('.btn-group.btn-group-paging a')
    next_url = "https://www.ptt.cc/" + paging[1]["href"]
    url = next_url
    for each_title in articles:
        print(each_title.text)
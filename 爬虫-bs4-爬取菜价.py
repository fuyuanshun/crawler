from bs4 import BeautifulSoup
import requests

if __name__ == '__main__':
    url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
    resp = requests.get(url)
    bs4_page = BeautifulSoup(resp.text, "html.parser")
    trs = bs4_page.find_all("tr", attrs={"class": "tr_color"})
    for tr in trs:
        tds = tr.find_all("td")
        for j in tds:
            print(j.text, end=' ')
        print()
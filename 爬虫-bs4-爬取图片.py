import requests
from bs4 import BeautifulSoup
import os

if __name__ == '__main__':
    base_url = "http://www.tuku.com.cn"
    url = base_url + "/photo/3/1.html"
    resp = requests.get(url)
    page = BeautifulSoup(resp.text, "html.parser")
    find = page.find("table", attrs={"id": "DataList1"})
    result_list = []
    # print(find)
    for i in find.find_all("a"):
        result_list.append(base_url + i.get("href"))
    i = 0;
    dir = "img/"
    if not os.path.exists(dir):
        os.makedirs(dir)
    for one in result_list:
        i = i+1
        one_resp = requests.get(one)
        # print(one_resp.text)
        # break;
        img = BeautifulSoup(one_resp.text, "html.parser").find("div", class_="main").find("img")
        src = img.get("src")

        with open (dir + img.get("alt") + str(i) + '.' + src.split(".")[-1], 'wb') as f:
            f.write(requests.get(src).content)
            print("ok! " + img.get("alt") + str(i))


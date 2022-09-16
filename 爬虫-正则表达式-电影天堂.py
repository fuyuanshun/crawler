import requests
import re

if __name__ == '__main__':
    base_url = "https://www.dytt8.net/"
    index = base_url + "html/gndy/index.html" # 主页
    regexIndex = re.compile('<strong>国内电影</strong>.*?<table width="100%" border="0" cellspacing="0" cellpadding="0">(?P<content>.*?)</table>', re.S)
    regexChild = re.compile("\[<a href=\"/html/gndy/china/index.html\">国内电影</a>]<a href='(?P<url>.*?)'>(?P<name>.*?)</a>", re.S)
    regexChildDownload = re.compile("◎片　　名(?P<name>.*?)<br />.*?href=\"(?P<url>.*?)\"", re.S)
    resp = requests.get(index)
    resp.encoding = "gb2312"
    it = regexIndex.finditer(resp.text)
    itChild = regexChild.finditer(it.__next__().group("content"))
    child_url_list = []
    for oneChild in itChild:
        # print(oneChild.group("name"))
        child_url_list.append(base_url + oneChild.group("url"))

    for url in child_url_list:
        child_resp = requests.get(url)
        child_resp.encoding = "gb2312"
        i = regexChildDownload.finditer(child_resp.text).__next__()
        print(i.group("name"))
        print(i.group("url"))

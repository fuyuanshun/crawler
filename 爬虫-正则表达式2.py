import requests
import re
import csv

if __name__ == '__main__':
    url = "https://movie.douban.com/chart"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    resp = requests.get(url, headers = headers)
    content = resp.text
    obj = re.compile(r'<table width="100%" class="">.*?<a class="nbg" href="(?P<url>.*?)"\s+title="(?P<title>.*?)".*?<span style="font-size:13px;">(?P<alias>.*?)</span>.*?<p class="pl">(?P<info>.*?)</p>', re.S) #  re.S 把整个HTML当作一个字符串
    it = obj.finditer(content)
    f = open("info.csv", mode="a", encoding="utf-8")
    csvWriter = csv.writer(f)
    for i in it:
        # print (i.group("title") + "/" + i.group("alias"))
        # print (i.group("url"))
        # print (i.group("info"))
        csvWriter.writerow(i.groupdict().values())
    resp.close()
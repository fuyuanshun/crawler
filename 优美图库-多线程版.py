import requests
from concurrent.futures import ThreadPoolExecutor
from lxml import etree
import os

baseurl = "https://www.umei.cc"

def get_all_tag_html():
    tag_index = baseurl + "/tags/"
    resp = requests.get(tag_index)
    resp.encoding = "utf-8"
    html = etree.HTML(resp.text)
    return html.xpath("/html/body/div[2]//a[position()>1]/@href")

def download_img(url, name):
    resp = requests.get(url)
    if not os.path.exists(os.getcwd() + os.sep + '图片2'):
        os.mkdir(os.getcwd() + os.sep + '图片2')
    with open(os.getcwd() + os.sep + '图片2' + os.sep + name+".jpg", 'wb') as f:
        f.write(resp.content)
    print(name + " success!")

def get_img_src():
    hrefs = get_all_tag_html()
    for href in hrefs:
        resp = requests.get(baseurl + href)
        resp.encoding = "utf-8"
        html = etree.HTML(resp.text)
        lis = html.xpath("/html/body/div[2]/div[7]/ul/li")
        with ThreadPoolExecutor(100) as t:
            for li in lis:
                src = li.xpath("./a/img/@src")[0]
                name = li.xpath("./a/div/text()")[0]
                t.submit(download_img, url=src, name=name)

if __name__ == '__main__':
    get_img_src()
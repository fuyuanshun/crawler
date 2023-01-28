import requests
import aiohttp
import aiofiles
import asyncio
from lxml import etree
import time
import os

baseurl = "https://www.umei.cc"

def get_all_tag_html():
    tag_index = baseurl + "/tags/"
    resp = requests.get(tag_index)
    resp.encoding = "utf-8"
    html = etree.HTML(resp.text)
    return html.xpath("/html/body/div[2]//a[position()>1]/@href")

async def download_img(url, name,session):
    try:
        async with session.get(url) as resp:
            content = await resp.content.read()
            if not os.path.exists(os.getcwd() + os.sep + '图片'):
                os.mkdir(os.getcwd() + os.sep + '图片')
            async with aiofiles.open(os.getcwd() + os.sep + '图片' + os.sep + name+".jpg",'wb') as f:
                await f.write(content)
                print(url + " success!")
    except Exception:
        print(url + " error")

async def get_img_src(lis):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for li in lis:
            src = li.xpath("./a/img/@src")[0]
            try:
                name = li.xpath("./a/div/text()")[0]
            except IndexError:
                name = time.time()
            tasks.append(download_img(src, name,session))
        await asyncio.wait(tasks)

if __name__ == '__main__':
    hrefs = get_all_tag_html()
    for href in hrefs:
        resp = requests.get(baseurl + href)
        resp.encoding = "utf-8"
        html = etree.HTML(resp.text)
        lis = html.xpath("/html/body/div[2]/div[7]/ul/li")
        print(href + " 源代码抓取完毕.")
        asyncio.run(get_img_src(lis))
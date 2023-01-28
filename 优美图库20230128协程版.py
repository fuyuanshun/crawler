import asyncio
import datetime
import time

import aiofiles
import aiohttp
from lxml import html

from concurrent.futures import ThreadPoolExecutor
import requests
import os

# 爬取的网址
url = "http://www.umei.cc/"
# 下载文件的存储路径
download_path = "D:/mt/"

# 多线程处理下载任务
async def download_image(image_url, name, session):
    try:
        print("图片地址：{}", image_url)
        async with session.get(image_url) as resp:
            content = await resp.content.read()
            if not os.path.exists(download_path):
                os.mkdir(download_path)
            async with aiofiles.open(download_path + os.sep + name + ".jpg", 'wb') as f:
                await f.write(content)
    except ConnectionError as e:
        print(e)
    else:
        print(name + " success!")

# 使用协程处理每个子页面
async def get_child_html(xpath_href):
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
        tasks = []
        for x in xpath_href:
            if x.endswith(".htm"):
                child_url = url + x
                print("子页面：{}", child_url)
                requests_request = requests.request("GET", child_url)
                child_html_content = requests_request.text
                # print(child_html_content)
                xpath_images = html.etree.HTML(child_html_content).xpath("//img/@src")

                for image_url in xpath_images:
                    # 获取文件名
                    name = image_url.split("/")[-1]
                    if not image_url.startswith("http"):
                        image_url = url + image_url
                    tasks.append(download_image(image_url, name, session))
        await asyncio.wait(tasks)

def main():
    request = requests.request("GET", url)
    # 不是200则表示请求失败
    if request.status_code != 200:
        print("请求出现异常：")
        return
    # 获取html源码
    html_content = request.text
    # 转为xpath对象
    xpath_data = html.etree.HTML(html_content)
    xpath_href = xpath_data.xpath("//a/@href")
    # 使用异步协程处理
    # asyncio.run(get_child_html(xpath_href))

    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_child_html(xpath_href))

if __name__ == "__main__":
    print("*****************开始******************")
    start_time = time.time()
    main()
    print("*****************结束******************")
    print("耗时总计：{} 秒".format(time.time() - start_time))
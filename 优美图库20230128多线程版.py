import datetime
import time

from lxml import html

from concurrent.futures import ThreadPoolExecutor
import requests
import os

# 爬取的网址
url = "http://www.umei.cc/"
# 下载文件的存储路径
download_path = "D:/mt/"

# 多线程处理下载任务
def download_image(image_url, name):
    try:
        print("图片地址：{}", image_url)
        resp = requests.get(image_url)
        if not os.path.exists(download_path):
            os.mkdir(download_path)
        with open(download_path + os.sep + name + ".jpg", 'wb') as f:
            f.write(resp.content)
    except ConnectionError as e:
        print(e)
    else:
        print(name + " success!")


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
    for x in xpath_href:
        if x.endswith(".htm"):
            child_url = url + x
            print("子页面：{}", child_url)
            requests_request = requests.request("GET", child_url)
            child_html_content = requests_request.text
            # print(child_html_content)
            xpath_images = html.etree.HTML(child_html_content).xpath("//img/@src")
            with ThreadPoolExecutor(100) as tpe:
                for image_url in xpath_images:
                    # 获取文件名
                    name = image_url.split("/")[-1]
                    if not image_url.startswith("http"):
                        image_url = url + image_url
                    # 提交给线程池执行
                    tpe.submit(download_image, image_url, name)


if __name__ == "__main__":
    print("*****************开始******************")
    start_time = time.time()
    main()
    print("*****************结束******************")
    print("耗时总计：{} 秒".format(time.time() - start_time))
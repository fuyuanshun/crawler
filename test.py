import requests
import re

if __name__ == '__main__':
    url = 'https://www.baidu.com'
    resp = requests.get(url)
    resp.encoding = 'utf-8'
    # print(resp.text)
    result = re.finditer(f'<html>(?P<content>.*?)</html>', resp.text, re.S)
    for i in result:
        print(i.group())
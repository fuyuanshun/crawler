import requests
import re

if __name__ == "__main__" :
    url = "https://movie.douban.com/chart"
    headers = {
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    resp = requests.get(url, headers = headers)
    a = re.finditer(f'https://\w+\.\w+\.\w+/\w+/\d+/', resp.text)  #   *?表示非贪婪匹配
    with open("movie.txt", 'w', encoding = 'utf-8') as f:
        for i in a:
            f.write(i.group() + "\n")
    resp.close()
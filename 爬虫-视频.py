import requests

url = "https://www.google.com"

if __name__ == '__main__':
    proxies = {
        "https":"https://dxgy1.lanlan.site:10000"
    }
    resp = requests.get(url, proxies=proxies, verify=False)
    print(resp.text)
import requests
from lxml import html

if __name__ == '__main__':
    url = "https://shanghai.zbj.com/search/f/?type=new&kw=saas"
    resp = requests.get(url)
    # print(resp.text)
    # etree = etree.HTML(resp.text)
    etree = html.etree
    html = etree.HTML(resp.text)
    div_list = html.xpath("/html/body/div[6]/div/div/div[2]/div[4]/div[1]/div")
    for div in div_list:
        try:
            price = div.xpath("./div/div/a[1]/div[2]/div[1]/span[1]/text()")[0].strip("￥")
            content = "saas".join(div.xpath("./div/div/a[1]/div[2]/div[2]/p[1]/text()"))
            name = div.xpath("./div/div/a[2]/div[1]/p/text()")[0]
            location = div.xpath("./div/div/a[2]/div[1]/div/span/text()")[0]
        except:
            continue
        # print(price)
        # print(content)
        # print(name)
        print(location)
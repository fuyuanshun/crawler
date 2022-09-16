import requests

if __name__ == '__main__':
    url = "https://user.17k.com/www/bookshelf/"
    headers = {
        "user-agent":"Mozilla/5.0 (Macintosh; IntelMac OS X 10_15_4) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/87.0.4280.141 Safari/537.36",
        "Cookie" : "GUID=a6450ce9-deae-436a-a4dc-d4567dc4a768; Hm_lvt_9793f42b498361373512340937deb2a0=1616850158; sajssdk_2015_cross_new_user=1; c_channel=0; c_csc=web; Hm_lpvt_9793f42b498361373512340937deb2a0=1616850835; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22a6450ce9-deae-436a-a4dc-d4567dc4a768%22%2C%22%24device_id%22%3A%2217873c782a5709-0d305174ee5f2b-5771031-2359296-17873c782a6a0a%22%2C%22props%22%3A%7B%7D%2C%22first_id%22%3A%22a6450ce9-deae-436a-a4dc-d4567dc4a768%22%7D; accessToken=avatarUrl%3Dhttps%253A%252F%252Fcdn.static.17k.com%252Fuser%252Favatar%252F14%252F14%252F45%252F76434514.jpg-88x88%253Fv%253D1616850244000%26id%3D76434514%26nickname%3Dnumberone23423%26e%3D1632404296%26s%3D26ade46b84325368"
    }
    # data = {
    #     "loginname" : "17839002230",
    #     "password" : "nJW7EPM5y6kYhh7"
    # }
    session = requests.session()
    resp = session.post(url, headers = headers)
    resp.encoding = "UTF-8"
    print(resp.text)

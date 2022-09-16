import requests
if __name__ == '__main__':
    videoId = "1724597"
    url = "https://www.pearvideo.com/video_" + videoId
    videoStatus = "https://www.pearvideo.com/videoStatus.jsp?contId="+ videoId +"&mrd=0.42688790293791823"

    headers = {
        "Referer" : "https://www.pearvideo.com/video_1724597",
        "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
    }
    # resp = requests.get(url)
    resp = requests.get(videoStatus, headers = headers)
    json = resp.json()
    systemTime = json.get("systemTime")
    srcUrl = json.get("videoInfo").get("videos").get("srcUrl")
    srcUrl = srcUrl.replace(systemTime, "cont-"+videoId)
    resp2 = requests.get(srcUrl)
    with open("video/"+srcUrl.split("/")[-1], "wb") as f:
        f.write(resp2.content)
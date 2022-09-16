import requests
import time
import re
import asyncio
import aiohttp
import aiofiles
import os
from Crypto.Cipher import AES

baseurl = 'https://vod3.buycar5.cn/'
url = baseurl + "20210308/MQkP4Lgn/index.m3u8"

def download_m3u8():
    resp = requests.get(url)
    with open('first_m3u8.txt', 'w') as f:
        for line in resp.text.splitlines():
            f.write(line)
            if not line.startswith("#"):
                resp2 = requests.get(baseurl + line)
                with open('second_m3u8.txt', 'w') as f2:
                    f2.write(resp2.text)

async def download_m3u8_url(url, session, aes):
    async with session.get(url) as resp:
        if resp.status == 200:
            async with aiofiles.open('m3u8/'+url.split('/')[-1], 'wb') as f:
                await f.write(aes.decrypt(await resp.content.read()))
                # print(url + ' success')

async def main(key):
    tasks = []
    aes = AES.new(key, IV=b'0000000000000000', mode=AES.MODE_CBC)
    async with aiohttp.ClientSession() as session:
        with open('second_m3u8.txt', 'r') as f:
            for line in f:
                if not line.startswith('#') and line.strip() != '':
                    tasks.append(download_m3u8_url(line.strip(), session, aes))
            await asyncio.wait(tasks)

def get_key():
    key = ''
    reg = re.compile('URI="(?P<keypath>.*?)"')
    with open('second_m3u8.txt') as f:
        for line in f:
            if line.startswith("#EXT-X-KEY"):
                key = reg.search(line.strip()).group("keypath")
                break
    resp = requests.get(key)
    return resp.text

def merge_m3u8():
    urls = []
    temp = ''
    with open('second_m3u8.txt', 'r') as f:
        for line in f:
            if not line.startswith('#') and line.strip() != '':
                urls.append(os.getcwd()+'\\m3u8\\'+line.split('/')[-1].strip())
                if temp == '':
                    temp = os.getcwd()+'\\m3u8\\'+line.split('/')[-1].strip()
                else:
                    temp = temp + '+' + os.getcwd()+'\\m3u8\\'+line.split('/')[-1].strip()
                    os.system(f'copy /b {temp} ' + os.getcwd() + '\\aa.mp4')
                    temp = os.getcwd() + '\\aa.mp4'

    # str = "+".join(urls)
    # print(f'copy /b {str} aa.mp4')
    # os.system(f'copy /b '+os.getcwd()+'\m3u8\*.ts aa.mp4')
    # print(f'copy /b {str} '+os.getcwd()+'\\aa.mp4')
    # os.system(f'copy /b {str} '+os.getcwd()+'\\aa.mp4')

if __name__ == '__main__':
    # download_m3u8()
    # key = get_key()
    # asyncio.run(main(key))
    merge_m3u8()

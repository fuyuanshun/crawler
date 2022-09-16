import aiohttp
import asyncio

urls = {
    "http://i1.shaodiyejin.com/uploads/tu/201911/9999/446d0ec3f4.jpg",
    "http://i1.shaodiyejin.com/uploads/tu/201911/9999/c18405ba1c.jpg",
    "http://i1.shaodiyejin.com/uploads/tu/201911/9999/33a6d7ac7f.jpg"
}

async def download(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            with open('img/' + url.rsplit("/", 1)[1], 'wb') as f:
                f.write(await resp.content.read())

async def main():
    tasks = []
    for url in urls:
        tasks.append(download(url))
    await asyncio.wait(tasks)

if __name__ == '__main__':
    asyncio.run(main())
import aiohttp
import asyncio

BASH_URL = 'http://bash.im/random'


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


def parse(html_body):
    pass


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, BASH_URL)
        print(html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
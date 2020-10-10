import aiohttp
import asyncio

from bs4 import BeautifulSoup, NavigableString

BASH_URL = 'http://bash.im/random'


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


def parse(html_body: str) -> str:
    output = []
    soup = BeautifulSoup(html_body, 'html.parser')
    for element in soup.find("div", class_="quote__body").children:
        if type(element) == NavigableString:
            output.append(element.string.strip())
        elif element.name == "br":
            output.append("\n")

    return "".join(output)


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, BASH_URL)
        quote = parse(html)
        print(quote)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
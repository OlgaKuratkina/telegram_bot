import aiohttp
import asyncio

from bs4 import BeautifulSoup, NavigableString
from bs4.element import Tag

BASH_URL = 'http://bash.im/random'


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


def parse_body(soup: Tag) -> str:
    output = []
    # soup = BeautifulSoup(html_body, 'html.parser')
    for element in soup.children:
        if type(element) == NavigableString:
            output.append(element.string.strip())
        elif element.name == "br":
            output.append("\n")

    return "".join(output)


def parse_quote_number(soup: Tag) -> str:
    number = soup.find("a", class_="quote__header_permalink")
    return number.string.strip()


def parse_quote_votes(soup: Tag) -> str:
    number = soup.find("div", class_="quote__total")
    return number.string.strip()


def parse_quote_date(soup: Tag) -> str:
    number = soup.find("div", class_="quote__header_date")
    return number.string.strip()


def parse(html_body: str) -> str:
    # TODO: catch exception for unexpected structure of quotes
    soup = BeautifulSoup(html_body, 'html.parser')
    quote = soup.find("div", class_="quote__frame")
    quote_number = parse_quote_number(quote.find("header"))
    quote_date = parse_quote_date(quote.find("header"))
    quote_votes = parse_quote_votes(quote.find("footer"))
    quote_body = parse_body(quote.find("div", class_="quote__body"))
    return f"{quote_number} [{quote_votes} votes]\n{quote_date}\n{quote_body}"


async def main():
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, BASH_URL)
        quote = parse(html)
        print(quote)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
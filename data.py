import asyncio
import random
import aiohttp
from bs4 import BeautifulSoup, SoupStrainer
import requests

from entry import Entry
from wordlist_file_access import WordlistFileAccess


async def get_definition(word, session):
    url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"
    headers = {'user-agent': 'x-infinity/0.0.1'}
    async with session.get(url, headers=headers) as response:
        def_elements = SoupStrainer(attrs=["class", "def"])
        definition = BeautifulSoup(await response.text(), "lxml", parse_only=def_elements).span

    if not definition:
        return None
    return definition.text


async def get_multiple_definitions(words):
    definitions = []
    async with aiohttp.ClientSession() as session:
        for word in words:
            definitions.append(get_definition(word, session))
        definitions = await asyncio.gather(*definitions)
    return definitions


def generate_wordlist():
    url = "https://raw.githubusercontent.com/MichaelWehar/Public-Domain-Word-Lists/master/5000-more-common.txt"
    response = requests.get(url)
    words = response.text.split()
    long_words = [word for word in words if len(word) >= 4]
    saved_words = random.sample(long_words, 100)

    definitions = asyncio.run(get_multiple_definitions(saved_words))
    return [Entry(saved_words[i], definitions[i]) for i in range(len(definitions)) if definitions[i]]


def main():
    results = generate_wordlist()

    db = WordlistFileAccess()
    db.set_wordlist("wordlist", results)


if __name__ == "__main__":
    main()

import asyncio
import json
from typing import List
import aiohttp
from bs4 import BeautifulSoup, SoupStrainer
import requests

from entry import Entry
from wordlist_file_access import as_json

WORD_SOURCE = "https://raw.githubusercontent.com/MichaelWehar/Public-Domain-Word-Lists/master/5000-more-common.txt"


class WordScraper:
    async def get_definition(self, word: str, session: aiohttp.ClientSession):
        url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"
        headers = {'user-agent': 'x-infinity/0.0.1'}
        async with session.get(url, headers=headers) as response:
            def_elements = SoupStrainer(attrs=["class", "def"])
            definition = BeautifulSoup(await response.text(), "lxml", parse_only=def_elements).span

        if not definition:
            return None
        return definition.text

    async def get_multiple_definitions(self, words: List[str]):
        definitions = []
        async with aiohttp.ClientSession() as session:
            for word in words:
                definitions.append(self.get_definition(word, session))
            definitions = await asyncio.gather(*definitions)
        return definitions

    def download_full_sample(self):
        response = requests.get(WORD_SOURCE)
        words = response.text.split()
        long_words = [word for word in words if len(word) >= 4]

        definitions = asyncio.run(self.get_multiple_definitions(long_words))
        return [Entry(long_words[i], definitions[i]) for i in range(len(definitions)) if definitions[i]]


def main():
    results = WordScraper().download_full_sample()

    with open('full_data.json', 'w') as file:
        file.write(json.dumps(as_json(results), indent=4))


if __name__ == "__main__":
    main()

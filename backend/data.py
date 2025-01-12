import asyncio
from typing import List
import aiohttp
from bs4 import BeautifulSoup, SoupStrainer
import requests

from backend.entry import Entry

WORD_SOURCE = "https://raw.githubusercontent.com/MichaelWehar/Public-Domain-Word-Lists/master/5000-more-common.txt"


class WordScraper:
    """A class responsible for handling entries fetched from the web."""

    async def get_definition(self, word: str, session: aiohttp.ClientSession):
        """
        Fetches the `word`'s definition from the Oxford Learner's Dictionary.
        Returns `None` if cannot find the definition.
        """
        url = f"https://www.oxfordlearnersdictionaries.com/definition/english/{word}"
        headers = {'user-agent': 'x-infinity/0.0.1'}
        async with session.get(url, headers=headers) as response:
            def_elements = SoupStrainer(attrs=["class", "def"])
            definition = BeautifulSoup(await response.text(), "lxml", parse_only=def_elements).span

        if not definition:
            return None
        return definition.text

    async def get_multiple_definitions(self, words: List[str]):
        """Fetches definitions of `words` asynchronously."""
        definitions = []
        async with aiohttp.ClientSession() as session:
            for word in words:
                definitions.append(self.get_definition(word, session))
            definitions = await asyncio.gather(*definitions)
        return definitions

    def download_full_sample(self):
        """
        Fetches definitions of all words from a public domain list of 5000
        common words.
        """
        response = requests.get(WORD_SOURCE)
        words = response.text.split()
        long_words = [word for word in words if len(word) >= 4]

        definitions = asyncio.run(self.get_multiple_definitions(long_words))
        return [Entry(long_words[i], definitions[i]) for i in range(len(definitions)) if definitions[i]]

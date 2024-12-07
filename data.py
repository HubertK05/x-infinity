import asyncio
import random
import aiohttp
from bs4 import BeautifulSoup, SoupStrainer
import requests


async def get_definition(word, session, i):
    url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
    headers = {'user-agent': 'x-infinity/0.0.1'}
    async with session.get(url, headers=headers) as response:
        divs = SoupStrainer(attrs=["class", "def ddef_d db"])
        definition = BeautifulSoup(await response.text(), "lxml", parse_only=divs).div
    if not definition:
        return None

    definition = definition.text.strip()
    if definition[-1] == ":":
        definition = definition[:-1]
    return definition


async def get_multiple_definitions(words):
    definitions = []
    async with aiohttp.ClientSession() as session:
        for i, word in enumerate(words):
            definitions.append(get_definition(word, session, i))
        definitions = await asyncio.gather(*definitions)
    return definitions


def main():
    url = "https://raw.githubusercontent.com/MichaelWehar/Public-Domain-Word-Lists/master/5000-more-common.txt"
    response = requests.get(url)
    words = response.text.split()
    long_words = [word for word in words if len(word) >= 4]
    saved_words = random.sample(long_words, 100)

    definitions = asyncio.run(get_multiple_definitions(saved_words))
    results = [f"{saved_words[i]},{definitions[i]}" for i in range(len(definitions)) if definitions[i]]

    with open("words.txt", "w") as file:
        file.write("\n".join(results))


if __name__ == "__main__":
    main()

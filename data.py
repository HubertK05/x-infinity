import asyncio
import random
import aiohttp
from bs4 import BeautifulSoup
import requests


async def get_definition(word, session, i):
    url = f"https://dictionary.cambridge.org/dictionary/english/{word}"
    headers = {'user-agent': 'x-infinity/0.0.1'}
    print(f"downloading {i}")
    async with session.get(url, headers=headers) as response:
        print(f"downloaded {i}")
        soup = BeautifulSoup(await response.text(), "html.parser")
    definition = soup.find(attrs=["class", "def ddef_d db"])
    if not definition:
        return None

    definition = definition.text.strip()
    if definition[-1] == ":":
        definition = definition[:-1]
    return "a"


async def get_multiple_definitions(words):
    definitions = []
    async with aiohttp.ClientSession() as session:
        for i, word in enumerate(words):
            print(word)
            definitions.append(get_definition(word, session, i))
        definitions = await asyncio.gather(*definitions)
    return definitions


def main():
    url = "https://raw.githubusercontent.com/MichaelWehar/Public-Domain-Word-Lists/master/5000-more-common.txt"
    response = requests.get(url)
    words = response.text.split()
    long_words = [word for word in words if len(word) >= 4]
    saved_words = random.sample(long_words, 100)

    results = asyncio.run(get_multiple_definitions(saved_words))
    results = [word for word in results if word]

    with open("words.txt", "w") as file:
        file.write("\n".join(results))


if __name__ == "__main__":
    main()

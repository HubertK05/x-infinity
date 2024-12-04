import os
import random
import requests
from dotenv import load_dotenv


def main():
    load_dotenv()
    api_key = os.environ["DICTIONARY_API_KEY"]
    url = "https://raw.githubusercontent.com/MichaelWehar/Public-Domain-Word-Lists/master/5000-more-common.txt"
    response = requests.get(url)
    words = response.text.split()
    long_words = [word for word in words if len(word) >= 4]
    saved_words = random.sample(long_words, 10)
    definitions = []
    for word in saved_words:
        api_url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
        entry_data = requests.get(api_url).json()
        short_definition = entry_data[0]["shortdef"][0]
        definitions.append(f"{word}-{short_definition}")
    with open("words.txt", "w") as file:
        file.write("\n".join(definitions))


if __name__ == "__main__":
    main()

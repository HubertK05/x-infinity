import json

from backend.data import WordScraper


def main():
    results = WordScraper().download_full_sample()
    results = [entry.as_json() for entry in results]

    with open('full_data.json', 'w') as file:
        file.write(json.dumps(results, indent=4))


if __name__ == "__main__":
    main()

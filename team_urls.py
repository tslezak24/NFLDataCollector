import json
import requests
from bs4 import BeautifulSoup as bs
import re

def main():
    with open("settings.json", "r") as jsonfile:
        data = json.load(jsonfile)

    url = 'https://www.nfl.com/teams'

    page = requests.get(url)

    soup = bs(page.content, 'lxml')

    path = soup.findAll('a', href=True, string=re.compile("View Full Site"))

    data['websites'] = [l['href'] for l in path]

    with open("settings.json", "w") as jsonfile:
        json.dump(data, jsonfile)

if __name__ == "__main__":
    main()


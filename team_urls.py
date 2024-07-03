import requests
from bs4 import BeautifulSoup as bs
import re

def main():
    url = 'https://www.nfl.com/teams'

    page = requests.get(url)

    soup = bs(page.content, 'lxml')
    
    print(soup)

    path = soup.findAll('a', href=True, string=re.compile("View Full Site"))

    urls = [l['href'] for l in path]
    
    for url in urls:
        print(url)

    #with open("settings.json", "w") as jsonfile:
    #    json.dump(data, jsonfile)

if __name__ == "__main__":
    main()


import json
import requests
from bs4 import BeautifulSoup as bs
import re


def get_page(url, ptype):
    page = requests.get(url)

    soup = bs(page.content, ptype)

    return soup

def cardinals(url):
    team_roster = {"Cardinals": []}
    soup = get_page(url, 'html.parser')
    for idx, tr in enumerate(soup.find('table', summary='Roster').find_all('tr')):
        row = [td.text.strip('\n') for td in tr.find_all('td')]
    
        if row != []:
            team_roster["Cardinals"].append({
                "Name": row[0],
                "Number": row[1],
                "Position": row[2],
                "Height": row[3],
                "Weight": row[4],
                "Age": row[5],
                "Experience": row[6],
                "College": row[7]
             })

    with open("team_rosters.json", "w") as jsonfile:
        json.dump(team_roster, jsonfile)
    
def get_roster_url(url):
    soup = get_page(url, 'lxml')
    
    path = soup.findAll('a', href=True, string=re.compile("Roster"))
    
    return [url['href'] for url in path] 

def main():
    with open("settings.json", "r") as jsonfile:
        data = json.load(jsonfile)

    roster_url = get_roster_url(data['websites'][0])
    cardinals(roster_url[0])

if __name__ == "__main__":
    main()

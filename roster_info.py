import json
import requests
from bs4 import BeautifulSoup as bs


def get_page(url, ptype):
    page = requests.get(url)

    soup = bs(page.content, ptype)

    return soup

def get_roster(url):
    team_roster = []
    soup = get_page(url, 'html.parser')
    for tr in soup.find('table', summary='Roster').find_all('tr'):
        row = [td.text.strip('\n') for td in tr.find_all('td')]
    
        if row != []:
            team_roster.append({
                "Name": row[0],
                "Number": row[1],
                "Position": row[2],
                "Height": row[3],
                "Weight": row[4],
                "Age": row[5],
                "Experience": row[6],
                "College": row[7]
             })
    return team_roster

def main():
    output = {}
    with open("settings.json", "r") as jsonfile:
        teams = json.load(jsonfile)

    for key, value in teams.items():
        team_roster = get_roster(value['Team_Website'] + 'team/players-roster/')
        output[key] = team_roster
        print(key + ": complete..")

    with open("team_rosters.json", "w") as jsonfile:
        json.dump(output, jsonfile)

    print("Data Extract Complete.")

if __name__ == "__main__":
    main()

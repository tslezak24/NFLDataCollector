import json
import requests
from bs4 import BeautifulSoup as bs
import re

def main():
    url = 'https://www.nfl.com/teams'

    full_team_profile_links = []
    team_website_links = []
    name_to_site_map = {}
    output = {}

    page = requests.get(url)

    soup = bs(page.content, 'lxml')

    team_site_path = soup.findAll('a', href=True, string=re.compile("View Full Site"))
    team_profile_path = soup.findAll('a', href=True, string=re.compile("View Profile"))

    soup.clear()

    print("Setting up team profile links...")

    for link in team_profile_path:
        full_team_profile_links.append('https://www.nfl.com' + link['href'])

    print("Setting up team website links...")

    for link in team_site_path:
        team_website_links.append(link['href'])

    print("Getting team names...")

    for profile in full_team_profile_links:
        profile_page = requests.get(profile)

        profile_soup = bs(profile_page.content, 'html.parser')

        team_name = profile_soup.find('div', class_='nfl-c-team-header__title')

        name_to_site_map[profile] = team_name.get_text()

    for i in range(len(team_website_links)):
        team_name = name_to_site_map[full_team_profile_links[i]]
        output[team_name] = {
                "Profile_Link": full_team_profile_links[i],
                "Team_Website": team_website_links[i]
                }

    with open("settings.json", "w") as jsonfile:
        json.dump(output, jsonfile)

    print("Complete.")

if __name__ == "__main__":
    main()

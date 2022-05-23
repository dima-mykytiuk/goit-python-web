import locale
from datetime import datetime

import aiohttp
import asyncio
from bs4 import BeautifulSoup
from src.store.models import db, NhlResults, EPLResults
from dateutil import parser

locale.setlocale(locale.LC_TIME, "ru_RU")


async def all_football_matches(session):
    async with session.get('https://terrikon.com/football/england/championship/matches', ssl=False) as response:
        soup = BeautifulSoup(await response.text(), "lxml")
        data = soup.find_all('td')
        team_list = []
        done_list = []
        step_1 = 0
        step_2 = 4
        for text in data:
            if text.text != '':
                team_list.append(text.text)
        num = 3
        for item in range(int(len(team_list) / 4)):
            team_list[num] = parser.parse(team_list[num]).date()
            num += 4

        for i in range(int(len(team_list) / 4)):
            done_list.append(tuple(team_list[step_1:step_2]))
            step_1 += 4
            step_2 += 4
        async with db.with_bind('postgresql://postgres:2012@localhost/news') as engine:
            for item in done_list:
                await EPLResults.create(epl_match=f'{item[0]}-{item[2]}', score=item[1], match_date=item[3])


async def nhl_matches(session):
    async with session.get('https://ua.tribuna.com/stanley-cup/calendar/', ssl=False) as response:
        soup = BeautifulSoup(await response.text(), "lxml")
        home_teams = soup.find('table', class_='stat-table').find('tbody').find_all(class_='owner-td')
        away_teams = soup.find('table', class_='stat-table').find('tbody').find_all(class_='guests-td')
        score = soup.find('table', class_='stat-table').find('tbody').find_all(class_='score-td')
        date = soup.find('table', class_='stat-table').find('tbody').find_all(class_='name-td alLeft')
        date_of_matches = []
        nhl_matches = []
        for item in date:
            date_of_matches.append(item.text.strip()[:10])
        step = 0
        for _ in range(len(date_of_matches)):
            date_of_matches[step] = parser.parse(date_of_matches[step]).date()
            step += 1

        tick = 0
        for i in range(len(home_teams)):
            nhl_matches.append({
                'home_team': home_teams[tick].text,
                'away_team': away_teams[tick].text,
                'score': score[tick].text if score[tick].text != '- : -' else "match not played yet",
                'date': date_of_matches[tick]
            })
            tick += 1
        async with db.with_bind('postgresql://postgres:2012@localhost/news') as engine:
            for item in nhl_matches:
                await NhlResults.create(nhl_match=f'{item.get("home_team")}-{item.get("away_team")}',
                                        score=item.get('score'), match_date=item.get('date'))


async def main():
    async with aiohttp.ClientSession() as session:
        await asyncio.gather(all_football_matches(session), nhl_matches(session))


if __name__ == "__main__":
    asyncio.run(main())
    
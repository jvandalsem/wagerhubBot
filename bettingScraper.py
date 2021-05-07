import urllib
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def scrapetheScore():

    baseUrl = 'https://www.thescore.com/nba/events'
    htmlReady = urllib.request.urlopen(baseUrl).read()
    scoreSoup = BeautifulSoup(htmlReady, 'html.parser')
    gameScores = scoreSoup.find_all('div', class_ = 'EventCard__eventCardContainer--3hTGN')
    gamesLod = []

    for b in range(len(gameScores)):

        homeTeam = gameScores[b].find_all('div', class_ = 'EventCard__teamColumn--17asJ')[0]
        awayTeam = gameScores[b].find_all('div', class_ = 'EventCard__teamColumn--17asJ')[1]
        homeScore = gameScores[b].find_all('div', class_ = 'EventCard__scoreColumn--2JZbq')[0]
        awayScore = gameScores[b].find_all('div', class_ = 'EventCard__scoreColumn--2JZbq')[1]
        time = gameScores[b].find('div', class_ = 'EventCard__clockColumn--3lEPz').get_text()

        gamesLod.append({'aateams': homeTeam.get_text().split()[0] + awayTeam.get_text().split()[0], 'homeTeam': homeTeam.get_text(), 'homeScore': homeScore.get_text(), 'awayTeam': awayTeam.get_text(), 'awayScore': awayScore.get_text(), 'time': time})

    return gamesLod

def scrapeoddShark():
    baseUrl = 'https://www.oddsshark.com/nba/computer-picks'
    htmlReady = urllib.request.urlopen(baseUrl).read()
    osSoup = BeautifulSoup(htmlReady, 'html.parser')
    cpicksTables = osSoup.find_all('table', class_ = 'base-table')
    cpicksLod = []
    for a in range(len(cpicksTables)):
        matchUp = cpicksTables[a].find_all('span', class_ = 'name-short')
        teams = [matchUp[c].get_text() for c in range(len(matchUp))]
        tableData = cpicksTables[a].find('tbody')
        tableRows = tableData.find_all('tr')
        gameLod = []
        gameLod.append({'teams': ''.join(teams)})
        for ps in tableRows:
            statCat = ps.find_all('td')[0].get_text()
            atsValue = ps.find_all('td')[1].get_text()
            totalValue = ps.find_all('td')[2].get_text()
            gameLod.append({statCat: {'ATS': atsValue, 'Total': totalValue}})
        cpicksLod.append(gameLod)

    return cpicksLod


# def scrapeoddShark():
baseUrl = 'https://www.sportsinsights.com/nba/'
htmlReady = urllib.request.urlopen(baseUrl).read()
osSoup = BeautifulSoup(htmlReady, 'html.parser')
cpicksTables = osSoup.find('tbody', id = 'oddsBody')
cpicksLod = []
print(cpicksTables)


thescoreDf = pd.DataFrame(scrapetheScore())
for a in scrapeoddShark():
    if a[0]['teams'] in thescoreDf.aateams.value_counts():
        print('yer')
print('\n')
for a in scrapeoddShark():
    for b in a:
        print(b + ':', a[b])
print('\n')
print(thescoreDf[0:1], '\n\n', thescoreDf[1:2])
print(scrapeoddShark())

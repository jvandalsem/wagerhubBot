from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import markdown_strings

class formDriver:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
        self.site = 'https://www.wagerhub888.com/'
    def getSite(self,site):
        self.driver.get(self.site)

    def setCreds(self,user,password):
        self.user = user
        self.password = password

    def login(self):
        self.getSite(self.site)
        self.driver.find_element_by_id("username").send_keys(self.user)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element(By.TAG_NAME, 'button').click()

    def close(self):
        return self.driver.close()

    def getWinnings(self):
        self.login()
        self.winnings = self.driver.find_element_by_id("ctl00_WagerContent_AccountFigures1_lblThisWeek").text
        print('$'+self.winnings)

    def getOpenBets(self):
        self.login()
        self.driver.find_element_by_xpath("//img[@src='/backend/img/User-icon.png']").click()
        self.driver.find_element_by_id("ctl00_AccountFigures1_lnk14").click()
        betList = list()
        for a in self.driver.find_element(By.TAG_NAME,'table').find_elements(By.TAG_NAME,'tr'):
            for b in a.find_elements(By.TAG_NAME,'td')[4:]:
                betList.append(bytes(b.text,'utf-8').decode('unicode_escape').replace('\n',' '))
        discStr = str()
        for c in range(0,len(betList),2):
            discStr+='> '+betList[c]+' Wager: '+betList[c+1]+'\n\n'
        return discStr.replace('Â','')



    def selectBetType(self,type='single'):
        self.betType = type
        self.login()
        if type.lower()=='single':
            self.driver.find_element_by_id("ctl00_SingleTemplateControl2_lnk2").click()
        elif type.lower()=='parlay':
            self.driver.find_element_by_id("ctl00_SingleTemplateControl2_lnk3").click()
        return self

    def getSports(self):
        return 'You can bet on the NBA, MLB, NHL, and EPL'

    def selectSport(self,sport='nba'):
        try:
            sport = sport.lower()
            if sport == 'nba':
                id = 'lg_3'
            elif sport == 'mlb':
                id = 'lg_5'
            elif sport == 'nhl':
                id = 'lg_1166'
            elif sport == 'epl':
                id = 'lg_1699'
            else:
                print("I'm sorry, we don't offer the functionality to place wagers on that sport yet")

            radioElem = self.driver.find_element_by_xpath("//*[@id='%s']"%id)
            self.driver.execute_script("arguments[0].click()",radioElem)
            contElem = self.driver.find_element_by_xpath("//input[@value='Continue']")
            self.driver.execute_script("arguments[0].click()",contElem)

        except:
            print('Looks like there are no games available for that sport right now')
        return self

    def listGames(self,sport):
        self.selectSport(sport)
        gamesList = list()
        elements = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "gamesRow")))
        games = list()
        for a in elements:
            games.append(self.formatBets(bytes(a.text,'utf-8').decode('unicode_escape')))
        return games[0]

    def formatBets(self,element):
        row1 = [a.lstrip() for a in element.split('\n')[:5]]
        row2 = [b.lstrip() for b in element.split('\n')[6:-1]]
        data = [row1,row2]
        if (data[1]!=[]):
            for a,b in zip(data[0],data[1]):
                return(a,b)

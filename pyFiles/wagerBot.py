from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
# os.environ['MOZ_HEADLESS'] = '1'

class formDriver:
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')

    def getSite(self,site):
        self.site = site
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
        print(('{}'+self.winnings).format('$'))

    def selectBetType(self,type='single'):
        self.betType = type
        self.login()
        if type.lower()=='single':
            self.driver.find_element_by_id("ctl00_SingleTemplateControl2_lnk2").click()
        elif type.lower()=='parlay':
            self.driver.find_element_by_id("ctl00_SingleTemplateControl2_lnk3").click()
        return self


    def getSports(self):
        print('You can bet on the NFL, NBA, MLB, NHL, and EPL')

    def selectSport(self,sport='NBA'):
        if sport.lower() == 'nba':
            self.driver.find_element_by_id('lg_3').click()
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.RETURN)
        # elif sport.lower() == 'nfl':
        # elif sport.lower() == 'mlb':
        # elif sport.lower() == 'nhl':
        # elif sport.lower() == 'epl':
        else:
            print("I'm sorry, we don't offer the functionality to place wagers on that sport yet")

from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        print('You can bet on the NBA, MLB, NHL, and EPL')

    def selectSport(self,sport='NHL'):
        if sport.lower() == 'nba':
            self.driver.find_element_by_id('lg_3').click()
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.RETURN)
        elif sport.lower() == 'mlb':
            WebDriverWait(self.driver,10).until(EC.invisibility_of_element_located((By.XPATH,"//div[@class='col-12 text-center']")))
            el_xp('//*[@id="lg_1166"]').click()
            # element = self.driver.find_element_by_xpath("//div[@class='col-12 text-center']")
            # self.driver.execute_script("arguments[0].style.visibility='hidden'", element)
            # self.driver.find_element_by_xpath('//*[@id="lg_1166"]').click()
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.RETURN)
        elif sport.lower() == 'nhl':
            self.driver.find_element_by_xpath("//label[@for='lg_1166']").click()
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.RETURN)
        elif sport.lower() == 'epl':
            self.driver.find_element_by_id('lg_1699').click()
            self.driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.RETURN)
        else:
            print("I'm sorry, we don't offer the functionality to place wagers on that sport yet")
    def test1(self):
        element = self.driver.find_element_by_xpath("//div[@class='col-12 text-center']")
        print(element)

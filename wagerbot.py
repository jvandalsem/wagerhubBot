from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
os.environ['MOZ_HEADLESS'] = '1'

class formDriver:
    def __init__(self,site):
        self.driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
        self.site = site

    def getSite(self):
        self.driver.get(self.site)

    def setCreds(self,user,password):
        self.user = user
        self.password = password

    def login(self):
        self.getSite()
        self.driver.find_element_by_id("username").send_keys(self.user)
        self.driver.find_element_by_id("password").send_keys(self.password)
        self.driver.find_element(By.TAG_NAME, 'button').click()

    def quitDriver(self):
        self.driver.quit()

    def getWinnings(self):
        self.login()
        self.winnings = self.driver.find_element_by_id("ctl00_WagerContent_AccountFigures1_lblThisWeek").text
        print(('{}'+self.winnings).format('$'))

    def selectBetType(self,type='single'):
        if type.lower()=='single':
            self.driver.find_element_by_id("ctl00_SingleTemplateControl2_lnk2").click()
        elif type.lower()=='parlay':
            self.driver.find_element_by_id("ctl00_SingleTemplateControl2_lnk3").click()
    # TO DO
        # Figure out tree path to iterate through all sports
    def selectSport(self,sport='BASKETBALL'):
        self.driver.find_element_by_id("lg_3").click()
        self.driver.find_element_by_id("ctl00_WagerContent_btn_Continuemod130").click()
        # self.driver.find_elements_by_xpath("//a[text()='BASKETBALL']")
        # print(self.driver.find_elements_by_xpath("//a[text()='BASKETBALL']"))

wager = formDriver('https://www.wagerhub888.com/')
wager.setCreds('jvandal', 'booshy')
wager.getWinnings()
wager.quitDriver()

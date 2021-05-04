import time
from wagerBot import formDriver
wager = formDriver()
wager.getSite('https://www.wagerhub888.com/')
wager.setCreds('jvandal', 'booshy')
wager.selectBetType('parlay').selectSport()

def sleepy(seconds):
    time.sleep(seconds)
    wager.close()
sleepy(5)

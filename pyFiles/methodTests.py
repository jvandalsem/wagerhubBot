from wagerBot import formDriver
wager = formDriver()
wager.getSite('https://www.wagerhub888.com/')
wager.setCreds('jvandal', 'booshy')
wager.selectBetType('parlay').selectSport()

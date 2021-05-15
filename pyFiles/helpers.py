from liveScores import scrapetheScore
import pandas
import numpy as np
import teams
def formatMD_GS(gList):
    s1 = str()
    s2 = str()
    s3 = str()
    s4 = str()
    multiList = list()
    filterList = list()
    for s in gList:
        if s != None:
            try:
                s1='> **Date**: {}, {}\n'.format(s[0][0],s[1][0])
                s2='> **Spread**: *{}* `{}` | *{}* `{}`\n'.format(s[0][1][3:],s[0][2],s[1][1][3:],s[1][2]).replace('Â','')
                s3='> **Total**: {} | {}\n'.format(s[0][3],s[1][3]).replace('Â','')
                s4='> **ML**: *{}* `{}` | *{}* `{}`'.format(s[0][1][3:],s[0][4],s[1][1][3:],s[1][4]).replace('Â','')
                multiStr = ''.join((s1,s2,s3,s4))
                if s[0][1][3:] not in filterList:
                    filterList.append(s[0][1][3:])
                    multiList.append(multiStr)
            except:
                pass
    return multiList

def formatLS(df):
    scores=df.to_numpy().tolist()
    multiList2 = list()
    for a in scores:
        s1='> **{}**: {}\n'.format(a[0],a[1])
        s2='> **{}**: {}\n'.format(a[2],a[3])
        s3='> **{}**\n'.format(a[4])
        multiStr2 = ''.join((s1,s2,s3))
        multiList2.append(multiStr2)
    return multiList2

def checkTeams(league):
    if league.lower() == 'mlb':
        check1 = teams.mlb
    elif league.lower() == 'nba':
        check1 = teams.nba
    elif league.lower() == 'nhl':
        check1 = teams.nhl
    return check1

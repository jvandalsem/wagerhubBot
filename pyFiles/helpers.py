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

firstout = """May 05 1
NASHVILLE PREDATORS
-1�+150
o5�+110
-185
More +
4:08 PM
  2 COLUMBUS BLUE JACKETS
+1�-170
u5�-130
+165"""

fname = 'testoutput.txt'
with open(fname,'w',encoding='utf-8') as f:
    f.write(firstout)

print(firstout.encode('utf-8'))
# May 05
#   7 DALLAS STARS
# +1�-185
# o5-135
# +140
# More +
# 4:08 PM
#   8 TAMPA BAY LIGHTNING
# -1�+165
# u5+115
# -160
#
# May 05
#   9 ANAHEIM DUCKS
# +1�-135
# o5�+120
# +190
# More +
# 5:08 PM
#   10 ST LOUIS BLUES
# -1�+115
# u5�-140
# -245
#
# May 05
#   13 WINNIPEG JETS
# +1�-240
# o5�-105
# +105
# More +
# 6:38 PM
#   14 CALGARY FLAMES
# -1�+190
# u5�-115
# -125
#
# May 05
#   15 LOS ANGELES KINGS
# +1�-220
# o5�+110
# +115
# More +
# 7:08 PM
#   16 ARIZONA COYOTES
# -1�+170
# u5�-130
# -135
#
# May 05
#   17 COLORADO AVALANCHE
# -1�-110
# o6-120
# -300
# More +
# 6:38 PM
#   18 SAN JOSE SHARKS
# +1�-110
# u6EV
# +230
#
# May 05
#   79 MONTREAL CANADIENS
# -1�+165
# o5�-105
# -150
# More +
# 4:08 PM
#   80 OTTAWA SENATORS
# +1�-185
# u5�-115
# +130
#
# May 05
#   5 WASHINGTON CAPITALS
# -1�+170
# o6-115
# -140
# More +
# 4:08 PM
#   6 NEW YORK RANGERS
# +1�-215
# u6-105
# +120
#
# May 05
#   11 VEGAS GOLDEN KNIGHTS
# -1�+195
# o6+105
# -115
# More +
# 5:08 PM
#   12 MINNESOTA WILD
# +1�-250
# u6-125
# -105
#
# May 06
#   21 NEW JERSEY DEVILS
# +1�-115
# o5�EV
# +200
# More +
# 4:08 PM
#   22 NEW YORK ISLANDERS
# -1�-105
# u5�-120
# -265
#
# May 06
#   25 BUFFALO SABRES
# +1�+125
# o6-115
# +275
# More +
# 4:08 PM
#   26 PITTSBURGH PENGUINS
# -1�-145
# u6-105
# -380
#
# May 06
#   27 CHICAGO BLACKHAWKS
# +1�EV
# o6-120
# +220
# More +
# 4:08 PM
#   28 CAROLINA HURRICANES
# -1�-120
# u6EV
# -295
#
# May 06
#   83 VANCOUVER CANUCKS
# +1�-110
# o6-115
# +200
# More +
# 6:08 PM
#   84 EDMONTON OILERS
# -1�-110
# u6-105
# -265

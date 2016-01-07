#cisco centric scripts for parsing out config-------
#------------------------------------
from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse('vg1.router.txt')
blockhead = parse.find_blocks('voice translation')
for item in blockhead:
    print item
#-------------------------------------


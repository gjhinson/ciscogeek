#cisco centric scripts for parsing out config-------
#------------------------------------
from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse('vg1.WASPOK2410.txt')
blockhead = parse.find_blocks('voice translation')
print (blockhead)
#-------------------------------------


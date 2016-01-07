#scratch pad for new scripting
#import math
#squarert = [math.sqrt(x) for x in [1,4,9,16,25,36,49,64]]
#print(squarert)
#-------------------------------------
#import math
#squarert = []
#for x in [1,4,9,16,25,36,49,64]:
#    squarert.append(math.sqrt(x))
#print(squarert)
#------------------------------------
#f = open('GASAVA2283-CTI-Extension-List.csv', 'r')
#f = open('GASAVA2283-Export-AD-Updates.csv', 'r')
#text = f.read()
#print(text)
#
#------------------------------------
#f = open('vg1.WASPOK2410.txt', 'r')
#text = f.read()
#print(text)
#lines = f.readlines()
#lines = [line.rstrip() for line in open('vg1.WASPOK2410.txt','rU') if line[0:5] == 'voice']
#print(lines)
#------------------------------------
#from ciscoconfparse import CiscoConfParse
#parse = CiscoConfParse('vg1.WASPOK2410.txt')
#    
#for obj in parse.find_objects(r'voice translation'):
#    #print ("Object:", obj)
#    #print ('Config text:', obj.text)
#    print (obj.text)
#------------------------------------
from ciscoconfparse import CiscoConfParse
parse = CiscoConfParse('vg1.WASPOK2410.txt')
blockhead = parse.find_blocks('voice translation')
print (blockhead)
#-------------------------------------


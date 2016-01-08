import os
from ciscoconfparse import CiscoConfParse

def process_file(fname):
    with open(fname) as f:
        print '*** %s ***' % fname
        parse = CiscoConfParse(f)
        blockhead = parse.find_blocks('voice translation')

        for item in blockhead:
            print item.rstrip()

def main():
    for root,dirs,files in os.walk('.'):
        for fname in files:
            if fname.endswith('router.txt'):
                process_file(os.path.join(root,fname))
        for dirname in dirs:
            if fname.endswith('router.txt'):
                process_file(os.path.join(root,fname))
        
if __name__ == "__main__":
    main()

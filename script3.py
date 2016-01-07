import os
for root,dirs,files in os.walk('C:\\Users\\hinsong\\Documents\\BACKUPS\\BACKUP-CatTools\\configs'):
    for fname in files:
        with open(fname) as f:
            for line in f:
                if line.startswith('voice translation'):
                    print (line)
#-------------------------------------

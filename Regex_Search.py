from pathlib import Path
import re
p=Path.home()/'Desktop'
allst=list(p.glob('*.txt'))
flag=None
reg=input()
for tfiles in allst:
    fob=open(tfiles)
    ob=re.compile(reg)
    if ob.search(fob.read())!=None:
        print("Match found in ",tfiles)
        flag=True
if flag==None:
    print("No matches found")
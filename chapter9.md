Q1: Relative path is relative to the currrent open directory.
Q2: C:/Users
Q3: It adds to the path-'C:/Users/Al'
Q4: Error occurs because you cant divide strings.
Q5: os.getcwd() returns the path of the current working directory as a string and os.chdir() helps in changing the current working directory.
Q6: ./ means the current directory and ../ means the parent directory.
Q7: C:\bacon\eggs\ is the dir name and spam.txt is the base name.
Q8: write, read and append mode.
Q9: The existing file gets overwritten.
Q10: read() method returns the first line meanwhile readlines() returns all lines in a list of strings.
Q11: Shelf value resembles a dictionary.

PRACTICE PROJECTS

Extending Multi Clipboard
Mad Labs
```from pathlib import Path
choice=input("r-read\nw-write\n")
fob=open(Path.home()/'Desktop'/'spam.txt')
fdata=fob.read()
if choice=='r':
    print(fdata)
elif choice=='w':
    print(fdata)
    for i in fdata.split():
        if i.startswith("NOUN") or i.startswith("VERB") or i.startswith("ADJECTIVE"):
            fdata=fdata.replace(i,input(f"Enter a {i}: "),1)
fob2=Path.home()/'Desktop'/'spamcorrected.txt'
print(fdata)
fob2.write_text(fdata)```

Regex Search
```from pathlib import Path
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
    print("No matches found")```
from pathlib import Path
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
fob2.write_text(fdata)
import shutil,re,os
from pathlib import Path
pref=input()
i=1
lst=sorted(os.listdir(Path("/home/aman/Desktop/textforfills")))
for files in lst:
    ob=re.compile(r"{}".format(pref))
    sp=ob.search(files)
    if int(sp.group(2))!=i:
        shutil.move(Path.home()/'Desktop'/'textforfills'/files,Path("/home/aman/Desktop/textforfills"+'/'+sp.group(1)+'0'*(len(sp.group(2))-len(str(i)))+str(i)+'.txt'))
    i+=1
print("Found and sorted!!")
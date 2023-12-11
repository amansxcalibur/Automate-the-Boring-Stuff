import shutil,os,re
from pathlib import Path
ob=re.compile(r'(\.txt)$')
for folder,subfolder,files in os.walk(Path.home()/'Desktop'/'containstexts'):
    for i in files:
        if ob.search(i)!=None:
           shutil.copy(Path(folder)/i,Path.home()/'Desktop'/'containscopiedtexts')
           print('Copied')

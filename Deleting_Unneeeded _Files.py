import os
from pathlib import Path
for folder,subfolder,files in os.walk(Path.home()/'Desktop'):
    for i in files:
        if os.path.getsize(folder+'/'+i)>100000000:
            os.unlink(folder+'/'+i)
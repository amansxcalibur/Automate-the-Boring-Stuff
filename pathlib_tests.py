'''from pathlib import Path
p=Path.home()/'Desktop'/'spam.txt'
p.write_text("hello wrld")'''
import re
st="^(spam)(\\d\\d\\d)(\\.txt)$"
ob=re.compile(st)
print(ob.search('spam001.txt'))
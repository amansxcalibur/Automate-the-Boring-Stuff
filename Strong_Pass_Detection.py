import re
caps=re.compile("[A-B]")
lows=re.compile("[a-b]")
nos=re.compile("\d")
s=input()
if nos.search(s)!=None and caps.search(s)!=None and lows.search(s)!=None and len(s)>=8:
    print("Strong password!!")
else:
    print("Weak ahh password")
        
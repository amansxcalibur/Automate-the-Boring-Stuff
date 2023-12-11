import re
def regexstrip(S,s):
    if s=='':
        ob=re.compile("( )(.*)( )")
        sp=ob.search(S)
        if sp!=None:
            print(sp.group(2))
        else:
            print(S)
    else:
        ob=re.compile(s)
        ch=ob.search(S)
        if ch!=None:
            print(ob.sub('',S))
        else:
            print(S)
S=input("Enter string")
s=input("Enter strip arguments")
regexstrip(S,s)
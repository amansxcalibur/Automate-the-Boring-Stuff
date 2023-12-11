Q1: re.compile() function creates Regex objects.
Q2: We use rawstrings to make sure '\' are not used as special chars.
Q3: search() returns None if the string pattern is present in the  strings and returns a Match object if the pattern matches.
Q4: Using group() method.
Q5: group(0) gives the whole pattern, group(1) returns the pattern inside the first paranthesis ie. \d\d\d and group(2) gives the pattern inside the second paranthesis ie. \d\d\d-\d\d\d\d.
Q6: Use the escape character \.
Q7: If there are groups in the regex pattern findall() gives values in tuples inside a list. It returns as lists if there arent any extra grouping.
Q8: It acts as OR(???). The pipe function helps in matching one of many expressions and also as a trick to use multiple statements as second arguments in search() method.
Q9: If the string matches a group in the regex pattern, ? char matches it but if it is missing in the string pattern, it matches the rest of the pattern instead of returning None.
Q10: + character matches one or more repetition of the pattern and * character matches 0 or more repetition of the pattern within the group.
Q11: {3} matches only 3 time repertition of the string pattern but {3,5} matches the same but with 3,4 or 5 time repetition.
Q12: \d- The character can be any digits from 0-9
     \w- The character can be letters or digits or special characters
     \s- The character can be spaces, tabs or newline
Q13: \D- The character cannot be any digits from 0-9
     \W- The character cannot be letters or digits or special characters
     \S- The character cannot be spaces, tabs or newline
Q14: .* matches any character except newline.
     .*? does the same but in a non greedy manner.
Q15: ```import re
     ob=re.compile(r"[0-9a-z]+")
     print(ob.findall(',zfbvasAJIJIDH12342'))```
Q16: re.I or re.IGNORCASE can be used.
Q17: . character matches all characters except  newline. re.DOTALL matches all chars including newline.
Q18: X drummers, X pipers, five rings, X hens
Q19: re.VERBOSE helps us to neatly arrange the sections of the regex pattern so it is easy to understand visually.
Q20: import re
     ob=re.compile(r"^(\d){1,3}(,\d\d\d)*$")
Q21: import re
     ob=re.compile("^[a-zA-Z]+ (Watanabi)$")
Q22: import re
     ob=re.compile("(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.")

PRACTICE PROJECTS

Date Detection
```import re,sys
ob=re.compile(r"^((0?[1-9])|([1-2][1-9])|(3[0,1]))/((0?[1-9])|(1[1,2]))/([1,2]\d\d\d)$")
res=ob.search("31/2/2004")
if res==None:
    print('Invalid Date')
else:
    if res.group(5) in ['4','6','5','9','11']==True:
        if int(res.group(1))<31==False:
            print("Invalid Date")
            sys.exit()
    print(res.group())
    if int(res.group(8))%4==0 and int(res.group(8))%100!=0 or int(res.group(8))%400==0:
        if res.group(5)=='02' or res.group(5)=='2':
            if int(res.group(1))<30:
                print("Leap Year")
            else:
                print("Invalid date")
                sys.exit()
        else:
            print("Leap Year")
    else:
        print("Not a Leap Year")```

STRONG PASSWORD DETECTION
```import re
caps=re.compile("[A-B]")
lows=re.compile("[a-b]")
nos=re.compile("\d")
s=input()
if nos.search(s)!=None and caps.search(s)!=None and lows.search(s)!=None and len(s)>=8:
    print("Strong password!!")
else:
    print("Weak ahh password")```

REGEX VESRION OF STRIP()
```def regexstrip(S,s):
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
regexstrip(S,s)```
import re,sys
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
        print("Not a Leap Year")
    
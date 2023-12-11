Q1: No PyInputPlus doesnt come with Python Standard Libarary.
Q2: To avoid typing 'pyinputplus' everytime, instead a shorter 'pyip' is used.
Q3: inputInt() accepts only integers while intFloat() accepts only floating values.
Q4: import pyinputplus as pyip
    print(pyip.inputInt(max=99,min=0))
Q5: The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine what the PyInputPlus function will accept or reject as valid input.
Q6: RetryLinitException gets triggered.
Q7: hello gets taken as input.

SANDWICH MAKER
```import pyinputplus as pyip
lst=[]
lst.append(pyip.inputMenu(['Wheat','White','Sourdough']))
lst.append(pyip.inputMenu(['Chicken','Turkey','Ham','Tofu']))
if pyip.inputYesNo("Do you want cheese?")=='yes':
    lst.append(pyip.inputMenu(['Cheddar','Swiss','Mozzarella']))
if pyip.inputYesNo("Do you want Mayo?")=='yes':
    lst.append('Mayo')
if pyip.inputYesNo("Do you want Mustard?")=='yes':
    lst.append('Mustard')
if pyip.inputYesNo("Do you want Lettuce?")=='yes':
    lst.append('Lettuce')
if pyip.inputYesNo("Do you want Tomato?")=='yes':
    lst.append('Tomato')
no=pyip.inputInt("How many sandwiches do you want",min=1)
menu={'Wheat':4,'White':5,'Sourdough':6,'Chicken':7,'Turkey':8,'Ham':9,'Tofu':10,'Cheddar':2,'Swiss':3,'Mozzarella':2,'Mayo':1,'Mustard':2,"Lettuce":3,"Tomato":1}
def bill(lst,menu):
    count=0
    for i in lst:
        if i in menu:
            count+=menu[i]
    return count
print(no*bill(lst,menu))```

MULTIPLICATION QUIZ
```import time
for i in range(10):
    print(f"{i}X{i}")
    start=time.time()
    for j in range(3):
        ans=int(input("Enter answer within 8secs: "))
        if ans==i*i:
            end=time.time()
            if  (end-start)<=8:
                print("Correct")
                time.sleep(1)
                break
            else:
                print("Time limit exceeded")
                break
        else:
            print("Wrong")```
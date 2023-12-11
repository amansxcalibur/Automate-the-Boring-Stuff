import pyinputplus as pyip
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
print(no*bill(lst,menu))
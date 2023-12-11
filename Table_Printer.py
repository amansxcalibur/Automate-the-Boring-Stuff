'''def printTable(lst):
    for j in lst:
        for i in range(len(lst[0])):
            print(j[i].center(max([len(x[i]) for x in lst])),end=' ')
        print()
printTable([['apples', 'oranges', 'cherries', 'banana'],
            ['Alice', 'Bob', 'Carol', 'David'],
            ['dogs', 'cats', 'moose', 'goose']])'''
'''import re
numRegex = re.compile(r'\d+')
print(numRegex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))'''
'''import re
ob=re.compile(r"^(\d){1,3}(,\d\d\d)*$")
print(ob.search('23,555').group())'''
import re
ob=re.compile("(Alice|Bob|Carol) (eats|pets|throws) (apples|cats|baseballs)\.")
print(ob.search("Alice eats baseballs.").group())
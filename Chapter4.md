Q1: [] is an empty list.
Q2: spam.insert(2,'hello)
Q3: d
Q4: d
Q5: [a, b]
Q6: 1
Q7: [3.14, 'cat', 11, 'cat', True, 99]
Q8: [3.14, 11, 'cat', True]
Q9: + for concatenation and * for replcation.
Q10: append() adds the element at the end of the list while insert() adds the element at the specified index.
Q11: Usong remove() or pop().
Q12: list and strings are ordered sequences of elements and have a lot of common functins like len(), slicing, in, not in, fo rloops, etc.
Q13: Tuples use () and are immutable while lists use [] and are mutable.
Q14: (42,)
Q15: Using tuple() and list() functions respectively.
Q16: They contain references to list values.
Q17: copy.copy() can be used to make a duplicate copy of a mutable value like a list or dictionary, not just a copy of a reference. If the list you need to copy contains lists, deepcopy() is used.

PRACTICE PROJECTS

Comma Code
```lst=list(input().split())
for i in range(len(lst)-1):
    print(lst[i],end=', ')
print('and',lst[i+1])```

Coin Flip Streaks
```streak=0
for i in range(10000):
    lst=[]
    for j in range(100):
        lst.append(random.randint(0,1))
    s=0
    for j in lst:
        if ''.join(map(str,lst[j:j+6]))=="000000" or ''.join(map(str,lst[j:j+6]))=="111111":
            s+=1
    streak+=s
print(streak)```

Character Picture Grid
```import random
lst= [['.', '.', '.', '.', '.', '.'],
      ['.', 'O', 'O', '.', '.', '.'],
      ['O', 'O', 'O', 'O', '.', '.'],
      ['O', 'O', 'O', 'O', 'O', '.'],
      ['.', 'O', 'O', 'O', 'O', 'O'],
      ['O', 'O', 'O', 'O', 'O', '.'],
      ['O', 'O', 'O', 'O', '.', '.'],
      ['.', 'O', 'O', '.', '.', '.'],
      ['.', '.', '.', '.', '.', '.']]
for i in range(len(lst[0])):
    for j in range(len(lst)):
        print(lst[j][i],end='')
    print()```
Q1: A major purpose of functions is to group code that gets executed multiple times. Without a function defined, you would have to copy and paste this code each time.
Q2: only when the function is called.
Q3: def funcname():
Q4: A function is a group of code which does a particular task and a function call executes this set of code.
Q5: One global scope and local scope.
Q6: The values get lost or reset.
Q7: A return value is the value that gets returned after executing a function and it can be an expression.
Q8: None
Q9: using 'global' keyword.
Q10: Boolean
Q11: It imports the module areallyourpetsnamederic
Q12: from spam import bacon()
     bacon()
Q13: Using try-except.
Q14: try clause block executes when there is no error and the except block gets executed when the try block runs into an error.

PRACTICE PROJECTS

The Collatz Sequence
```def collatz(number):
    if number%2==0:
        print(number//2)
        return number//2
    else:
        print(3*number+1)
        return 3*number+1
ret=int(input())
while ret!=1:
    ret=collatz(ret)```

Input Validation
```while True:
    try:
        global s
        s=int(input("Enter an integer: "))
        break
    except:
        print("You re supposed to enter an integer!")```
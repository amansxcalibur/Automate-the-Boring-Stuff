import time
for i in range(10):
    print(f"{i}X{i}")
    start=time.time()
    for j in range(3):
        ans=int(input("Enter answer within 8secs"))
        if ans==i*i:
            end=time.time()
            if (end-start)<=8:
                print("Correct")
                time.sleep(1)
                break
            else:
                print("Time limit exceeded")
                break
        else:
            print("Wrong")
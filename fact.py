a=int(input("Enter a number: "))
fact=1
if a==1 or a==0:
    print(1)
else:    
    for i in range(1,a+1):
        fact*=i
    print(f"factorial of {a} is:",fact)    
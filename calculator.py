a=float(input('Enter first number: '))
b=float(input('Enter second number: '))

print(f'The sum of {a} and {b} is: {a+b}')
print(f'The sub of {a} and {b} is: {a-b}')
print(f'The multi of {a} and {b} is: {a*b}')
print(f'Square Root of {a} is : {a**(0.5)}')
print(f'Square Root of {b} is : {b**(0.5)}')
print(f'Exponentiation : {a**b}')

if b==0:
    print('Division by zero is not possible')    
else:
    print(f'The division of {a} and {b} is: {a/b}')




import random

num=['1','2','3','4','5','6','7','8','9','0','a','b','c','*','%','#','@','$']
length=int(input('Enter number of characters for you password: '))

# password=''.join(random.choice(num) for _ in range(length))
password=''.join(random.sample(num,length))
print(f'Your password is: {password}')

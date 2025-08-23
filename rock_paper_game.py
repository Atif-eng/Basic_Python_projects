import random

computer=random.choice(['r','p','s'])
user_input=input('Enter your choice(r,p,s): ').lower()

dict={"r":'Rock',
      'p':'paper',
      "s":'scissor'}

print(f'you enter: {dict[user_input]}')
print(f'Computer enter: {dict[computer]}')


if (computer=='r' and user_input=='r') or (computer=='p' and user_input=='p') or (computer=='s' and user_input=='s'):
    print("both choose same thing so Graw")

elif (computer=='r' and user_input=='p'):
    print('you lose')

elif (computer=='r' and user_input=='s'):
    print('you lose')

elif (computer=='p' and user_input=='r'):
    print('you win')

elif (computer=='p' and user_input=='s'):
    print('you win')    

elif (computer=='s' and user_input=='r'):
    print('you win')

elif (computer=='s' and user_input=='p'):
    print('you lose')
    
else:
    print('wrong choice')
import random

roll_again='yes'
while roll_again=='yes' or roll_again=='y':
    print('Rolling the dice......')
    dice=random.randint(1,6)
    print(dice)
    roll_again=input('Roll the dice again?')
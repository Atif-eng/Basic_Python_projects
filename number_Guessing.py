from random import randint

random_number=randint(1,100)
my_num=-1
guess=0
while(random_number!=my_num):
    guess+=1
    my_num=int(input('Guess a number: '))

    if my_num<random_number:
        print('Choose a greater number')
    elif my_num>random_number:
        print('Choose a smaller number')
    elif my_num==random_number:
        print('You Guess the right number')
print(f'you guess the right number {random_number} in {guess} attempts')
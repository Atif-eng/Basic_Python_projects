
# using list

import random
random_words=random.choice(['banana','apple','mango','orange'])
user=input('Enter name of a fruit: ')

if user == random_words:
    print('you guess the right fruit')
else:
    print('you did not guess the right one')
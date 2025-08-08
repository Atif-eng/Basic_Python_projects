dict={'School':'A place where you can study.A place where you can learn',
      'Lion':'The king of a jungle.It is an animal.',
      'House':'A place where you live',
      'Industry':'The technology industry is rapidly growing and constantly evolving.',
      "Factory":'The new factory produces thousands of units daily efficiently.'}

a=input('Enter a word: ').capitalize()
b=dict
if a in b:
    print(dict[a])
else:
    print(f'{a} is not found')

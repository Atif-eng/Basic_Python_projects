list=['Ali',"Ahmad",'Hassan']

#add somthing into list
def add():
    a=input('\nEnter a Name:')
    list.append(a)
    print(f'you add {a} in list')
    print(f'your new list is : {list}\n')

#Function to delete somthing from list
def delete():
    a=int(input('Enter index you wanna delete: '))
    del list[a]
    print(f'The list : {list}\n')

# view function
def view():
    for i in list:
        print(i)

# save list elements in a file
def file():
    f=open('project.txt','w')
    for i in list:
        f.write(i)
    f.close()
    print('Your list is saved in a file')

# function call
view()
add()
# delete()
file()
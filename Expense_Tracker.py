def dict_expanses(dict):
    total=0
    for keys in dict:
        a=dict[keys]
        total=total+a
    print(f'Total expanses in dict are: {total}')

def list_sum(list):
    total=0
    for i in list:
        total=total+i
    print(f'Total expanses in list are: {total}')  

d={'a':10,'b':5,'c':5}
dict_expanses(d)

l=[1,2,3,4,5]
list_sum(l)
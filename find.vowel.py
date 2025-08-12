a="aeiou"
b=input("Enter a string: ")
total=0
for char in b:
    if char in a:
        total+=1
print(total)        
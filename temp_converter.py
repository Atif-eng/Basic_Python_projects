
# Celsius to Fahrenheit 
def c_to_f():
    c=float(input("\nEnter temp in Centigrade: "))
    f=(c*(9/5)+32)
    print(f"{c} centigrade is equal to: {f}F")  

# Celsius to Kelvin
def c_to_k():
    c=float(input("\nEnter temp in Centigrade: ")) 
    k = c + 273.15
    print(f"{c} centigrade is equal to: {k}k") 

# Fahrenheit to Celsius
def f_to_c():
    f=float(input("\nEnter temp in Fahrenheit: "))
    c=(f-32)*5/9
    print(f"{f} Fahrenheit is equal to: {c}C")  

# Fahrenheit to Kelvin
def f_to_k():
     f=float(input("\nEnter temp in Fahrenheit: "))
     k=(f - 32)*5/9 + 273.15
     print(f"{f} centigrade is equal to: {k}k")

# function call
c_to_f()
c_to_k()

f_to_c()
f_to_k()
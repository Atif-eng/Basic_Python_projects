weight=int(input('Enter you body weight in kg: '))
height=int(input('Enter you body height in cm: '))
height=height/100
BMI=weight/(height*height)
print(f'your body mass index is: {BMI}')

if (BMI>0):
    if(BMI<=16):
        print('You are severely underweight')
    elif(BMI<=18.5):
        print("You are underweight")
    elif(BMI<=25):
        print('you are healthy')
    elif(BMI<=30):
        print('you are severely overweight')
    else:
        print('you are severely overweight')

else:
    print('Enter valid details')
'''
print("Hello World")

def max_num(num1,num2,num3):
    if num1 >= num2 and num1 >=num3:
        return num1
    elif num2>_num1 and num2>=num3:
        return num2
    else:
        return num3
    
print(max_num(300,40,5))

import useful_tools

print(useful_tools.roll_dice(10))
'''
from Student import Student

student1 = Student("Jim", "Business", 3.1, False)

print(student1.name)

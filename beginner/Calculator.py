def plus(num1, num2):
    print(float(num1) + float(num2))
    return
def minus(num1, num2):
    print(float(num1) - float(num2))
    return
def multiply(num1, num2):
    print(float(num1) * float(num2))
    return
def divide(num1, num2):
    print(float(num1) / float(num2))
    return

num1 = input("Enter a number:")
num2 = input("Enter a number: ")
choice = input(
    """
Select your function:
a. Add
b. Subtract
c. Multiply
d. Divide
""")
#sign = input("Enter operation")
# result = int(num1) + int(num2) #whole numbers
#result = float(num1) + float(num2) #decimal any numbers
if choice=="a":
    print("The answer is:", end="") #the end is to move the answer up
    plus(num1,num2)
elif choice=="b":
    print("The answer is:", end="") #the end is to move the answer up
    minus(num1,num2)
elif choice=="c":
    print("The answer is:", end="") #the end is to move the answer up
    multiply(num1,num2)
elif choice=="d":
    print("The answer is:", end="") #the end is to move the answer up
    divide(num1,num2)

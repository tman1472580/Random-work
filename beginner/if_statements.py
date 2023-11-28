#is_male = True
#is_tall = True
#if is_male and is_tall:
#    print("You are a male and tall")
#elif is_male and not(is_tall):
 #   print("You are a short male")
#elif not(is_male) and is_tall:
#    print("You are not a male but tall")
#else:
 #   print("You are not a male or you are not tall")

def max_num(num1,num2,num3):
    if num1>= num2 and num1 >= num3:
         return num1
    elif num2>= num1 and num2 >= num3:
         return num2
    else:
         return num3


print(max_num(3,67 ,8))

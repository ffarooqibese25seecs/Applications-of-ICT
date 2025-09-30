number=1
for i in range (number):
 a= int(input("enter first number "))
 b= int (input("enter second number "))
 operation = input("enter operation you want to perform")
 if (operation=='+'):
     print("the sum of 2 numbers is ", a+b)
 elif (operation=='-'):
     print("subtraction of 2 number is ", a-b)
 elif (operation=='*'):
     print("multiplication of 2 number is ", a*b)
 elif (operation=='%'):
     print("modulus of 2 number is ", a%b)
 elif (operation=='/'):
     print("division of 2 number is ", a/b)
 elif (operation=='^'):
     print("exponential of 2 number is ", a**b)
 elif (operation=='//'):
     print("integer division of 2 number is ", a//b)

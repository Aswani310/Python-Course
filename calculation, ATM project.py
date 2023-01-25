# Calculation method using function
# Calculation method using function
def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y

def mod(x,y):
    return x % y

def div(x,y):
    return x/y

x=float(input('Enter x value:'))
y=float(input('Enter y value:'))
#mode of operation
'''
options=
    1.add
    2.substract
    3.multiply
    4.module
    5.division
'''
option=int(input("Enter option of your choice:"))

if option == 1:
    print(add(x,y))

elif option == 2:
    print(sub(x-y))

elif option == 3:
    print(multi(x,y))

elif option == 4:
    print(mod(x,y))

elif option == 5:
    print(div(x,y))

else:
    "Not available"






   
   
   # ATM mini project

# name="akshara"
# password="1234"

# user_name=input("Enter the user name:")
# user_pasword=input("Enter password:")

# #b= total balance
# a='''
# 1.credit
# 2.debit
# 3.balance check
# 4.exit
# '''
# b=5000

# if name == user_name and password == user_pasword:

#         while True:
#             print(a)

#             option=int(input("Enter your option:"))

#             def credit():
#                 c=int(input("Enter credit amount:"))
#                 print(b+c)

#             def debit():
#                 d=int(input("Enter debit amount:"))
#                 print(b-d)

#             def balance_check():
#                 print(b)
            
#             if option==1:
        
#                 credit()

#             elif option==2:
#                 debit()

#             elif option==3:
#                 balance_check()

#             elif option==4:
#                 break

# else:
#     print('user name or password is invalid')




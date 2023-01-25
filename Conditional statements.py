# if 2*5<4*5:
#     print("this is right")
# elif 4/2<6/2:
#     print("this is wrong")
# else:
#     print("this is invalid")

# if 10//5>15//5:
#     print("get the discount")
#     if 20%100<=30%120: 
#         print("not eligible for discount")
#     else:
#         print("get additional dscount")
# else:
#     print("Thanks for shopping")

# short hand if practice
# x=10/2
# y=12/3
# print("order created") if x==y else print("order cancelled")





#
# looping statements
# syntax for while loop
'''
while condition:
    statements("any statement like if,elif,ifelif,nested if,ifelse)
'''
'''
syntax:
for i in iterators(like list,string,tuple,range):
    statements("any statement like if,elif,ifelif,nested if,ifelse)
    use(start,stop,skip)method for iterator
    break=stop,continue=skip,pass=pass the current statement
'''
# while 'alexa':
#     print('this is device')

# for i in range(3,70,5):
#     print(i)

for l in "chemistry":
      if l=="s":
         break
         print(l)    
         if l=="s":
          continue
print(l)

# if 12/4!=24/8:
#     pass


# nested for statement

for k in range(2,50):
    for n in range(1,11):
        print(k*n,end=" ")
    print()


 # student address
    a="apple"
    b=40
    fruit=input('enter fruit:')
    price=input('enter price b:')
    if a=="apple" and b==40:
        print("price match")
    else:
        print("doesn't match")      
# Super Market Bill Beneration - Project

from datetime import datetime

# enter the name of the customer
name=input("enter your name:")

# list of items in the store
list='''
Grocery items:

Rice           Rs     50/kg
Atta           Rs     40/kg
Oil            Rs     100/ltr
salt           Rs     30/each
Sugar          Rs     60/kg
Coffe powder   Rs     100/500 gms
Tea powder     Rs     80/500 gms

Health and beauty care items:

Colgate         Rs      80/each
Tooth brush     Rs      30/each
Soap            Rs      40/each
Shampoo         Rs      85/each
Horlicks        Rs      120/each
Hair oil        Rs      100/each
Vimbar          Rs      45/each
Ariel           Rs      90/each

Snacks:

Lays            Rs      10/each
Gooday          Rs      20/each
Maaza           Rs      10/each
Dairy milk      Rs      25/each

'''



# qlist=quantity  ilist=itemslist plist=price
price=0
price_list=[]
total_price=0
final_price=0
ilist=[]
qlist=[]
plist=[]

# actual price of the items

items = {'Rice': 50,
'Atta':40,
'Oil':100,
'salt':30,
'Sugar':60,
'Coffeepowder':100,
'Teapowder':80,
'Colgate':80,
'Toothbrush':30,
'Soap':40,
'Shampoo':85,
'Horlicks':120,
'Hairoil':100,
'Vimbar':45,
'Ariel':90,'Lays':10,
'':20,
'Maaza':10,
'Dairymilk':25}
# print(items)

option = int(input("for list of items press 1:"))

if option == 1:
    print(list)

for i in range(len(items)):
    inp1 = int(input("Press 1 to buy or press 2 for Exit:"))
    if inp1 == 2:
        break
    if inp1 == 1:
        item = input("Enter your item:")
        quantity = int(input("Enter quantity:"))
        if item in items.keys():
            price = quantity*(items[item])
            price_list.append((item,quantity,items,price))
            total_price+= price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst = (total_price*2)/100
            final_ammount = gst + total_price
        else:
            print("item not available")

    else:
        print("entered wrong number")

# bill generation
# 25* al these power is lenth of the = symbol

    inp = input("do you need a print copy of the bill Yes or No:")
    if inp == "Yes":
        pass
    if 'final_ammount' != 0:

        print(25*"=","Akshara Super Market",25*"=" )

        print(28*"=","Ameerpet")

        print("Name:",name,30*" ", "Date:",datetime.now() )

        print(75*"-")

        print("sno",5*" ", "items",8*" ", "quantity",3*" ", "price")


        for j in range(len(price_list)):

            print(j,5*' ',1*' ',ilist[j], 8*' ',qlist[j],8*' ',plist[j])
        
        print(75*"-")

        print(50*"-", 'Total_amount:', 'Rs',total_price)

        print("gst amount", 50*" ", 'Rs',gst)

        print(75*"-")

        print(50*"-", 'final_amount:', 'Rs',final_ammount)

        print(75*"-")

        print(20*"-", "Thanks For Shopping",20*"-")

        print(75*"-")








    
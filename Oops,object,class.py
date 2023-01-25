'''                 object oriented programming                        '''

# class(template)
'''
1.we will define class by using 'class' keyword
2.blue print to create a objects
3.collection of objects is called class
'''
#ex:fruits


# object
# physical entity(real)
'''
1.an instance of a class
2.memory is created when it declared
'''
#ex: apple,orange,mango

# class classname():# class defination
#     # constructors
#     # functions
#     # variables


# attribute (variable) data members
'''
age=20 
color='blue'
'''

# method(behaviour) or functions , member functions
'''
eat() 
sleep()
'''

# class classname():# class defination
# attribute (variable) data members
# method(behaviour) or functions , member functions




class Vijay():                          # class defination
    a="2nd year batch"                  # attribute (variable)
    def College_staff(self):            # method
        print("class lecturer")
Btech=Vijay()                           # obj name=class name()
Btech.College_staff()                   #to call/get output :objectname.method()

print(Btech.a)




class Narayana_school_Toppers():
    a = '10th class'
    b = '9th class'
    c = '8th class'

    def students2022(self):
        print("Geetha","Manasa","Ravi")

    def students2021(self):
        print("dev","vamsi","santhi")

    def student_Ranks(self):
        print(1,2,3)

batch_2022 = Narayana_school_Toppers()
batch_2021 = Narayana_school_Toppers()
Ranks = Narayana_school_Toppers()

batch_2022.students2022()

print(batch_2022.b)

batch_2021.students2021()

print(batch_2021.c)

Ranks.student_Ranks()



class Vegetables():
    x = 40
    y = 60

    def price(self):
        print('brinjal','carrot')

Market = Vegetables()

Market.price()

print(Market.x)

print(Market.y)




class ABC_Company():
    def __init__ (self,Employee_Name,Employee_DOB,Employee_role,Gender):
        self.a = Employee_Name
        self.b = Employee_DOB
        self.c = Employee_role
        self.d = Gender
    
    def Employee_data(self):
        print("Employee_Name:",self.a)
        print("Employee_DOB:",self.b)
        print("Employee_role:",self.c)
        print("Gender:",self.d)
while True:
    name=input("Enter emp name:")
    DOB= input("Enter emp DOB:")
    role=input("Enter emp role:")
    gender=input("Enter emp gender:")

Employee_details = ABC_Company('name','DOB','role','gender')

Employee_details.Employee_data()


















# self keyword
'''
we can access the attributes and methods of the class(current class only)
'''
# # # __init__

# # '''
# # Constructors are generally used for instantiating an object. 
# # The task of constructors is to initialize(assign values)
# # to the data members of the class when an object of the class 
# # is created.
# # In Python the __init__() method is called the constructor
# # and is always called when an object is created

# # does'nt support multiple constructor
# # '''
# self keyword use in class

'''
syntax: class classname():

object=classname()
to call/get output :objectname.method()
'''


# class Bikes():
#     def __init__(self,Bike_Brand_Name,Bike_Model,Bike_Milage,Bike_Price):

#         self.x = Bike_Brand_Name
#         self.y = Bike_Model
#         self.z = Bike_Milage
#         self.d = Bike_Price

#     def Bikes_data(self):
#         print("Bike_Brand_Name:",self.x)
#         print("Bike_Model:",self.y)
#         print("Bike_Milage:",self.z)
#         print("Bike_Price:",self.d)

# while True:
#     name=input("Enten the Bike Name:")
#     model=int(input("Enter Bike Model Num:"))
#     milage=input("Enter Bike Milage:")
#     price=float(input("Enter Bike Price:"))

#     Bike_object = Bikes(name,model,milage,price)
#     Bike_object.Bikes_data()
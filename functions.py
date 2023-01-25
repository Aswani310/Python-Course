# students marks list
# s= total marks
# l= lab marks

def smarks(s,l):
    print(s/l)
# smarks(576,6)
smarks(479,6)
smarks(548,8)
smarks(345,5)

#orbitary function
def students(*name):
     print("10th grade students",name)
students('radha','suma','rani')
students('ramu',432,'ravi',546,'usha',47.5,'sruthi',43.68)

def smarks(marks):
    print(marks)
    vani=int(input("10th class marks:"))
smarks('vani')

#keyword function
def students(**sname):
    print("balance student account",sname)
students(sname=[('ravi',3560),('kumar',890),('sonu',1089)])

def outer_function():
    print("qualified students")
    def inner_function():
        print("failed student")
    inner_function()
outer_function()



    


 








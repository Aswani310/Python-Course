# list means sequencing of diff types of data 
# we can create empty list in 2 methods


# institute students marks list
# narayana=[] #empty list
# print(narayana) method 1

# narayana=list() #empty list
# print(type(narayana)) # method
# students list
# narayana=["madhu","sudha","latha","rajesh"]
# print(type(narayana))
# # students individual marks
madhu=[88,76,89.5,92,67,55,78.54,"fail"]
sudha=[75,87.4,58,64,91,"pass",74.34]
latha=[98,86,84,55,63,46.88,44.22,79,65,73,98,87.5]

# madhu=[88,76,89.5,92,67,55,78.54,"fail"]
madhu2=list([88,76,89.5,92,67,55,78.54,"fail"])
# print(madhu)
# print(madhu2)

# print(madhu[5])
# print(madhu[-1])
# print(sudha[0])

#slicing the data 
#syntax [start:stop:skip] or s***3

# print(madhu[1:7:3])
# print(latha[0:10:4])
# print(latha[:])
# print(latha[:6])
# print(latha[:-1])
# print(latha[-1:-8:-2])
# print(sudha[::])
# print(sudha[::-1])
# print(latha[:4])
# print(latha[-3:])
# print(madhu[3:3])


# madhu2[2]="fail"
# print(madhu2)
# madhu2[7]=72
# print(madhu2)

# # list methods:syntax:variable.method()
# # variable extend takes bulk data only means we have to give[]to enter data.
# # count variable gives how many times the paricular data that we give in the list
# #for index if tha data repeats in multiple times result will be the first occurance of the data we give

# sudha=[75,91,87.4,58,64,91,"pass",74.34]
# sudha.append(58)
# print(sudha)
# # sudha.append([58])
# sudha.extend([79])
# print (sudha)
# print(sudha.count(75))
# # print(len(latha))
# print(sudha.index(91))
# sudha.clear()
# print(sudha)

# radha=madhu2.copy()
# print(radha)
# madhu2.append(49)
# print(madhu2)
# print(radha)
# madhu2.insert(0,"fail")
# print(madhu2)
# # pop() takes index and removes elements 
# #remove() takes elements and removes index
# madhu2.pop(2)
# madhu2.remove(55)
# print(madhu2)
# madhu2.reverse()
# print(madhu2)
# sort print elements from assending to desending order
# sort(reverse=true) gives from desending to asending order
# latha.sort()
# print(latha)
# latha.sort(reverse=True)
# print(latha)






# list comprehension
# syntax [expression for item in iterable] like [x**2 for x in[1,2,3,4,5]]
# we use short hand ifelse and for loop method

 
a=[475,550,535,400,320,492,380,555]
G=['B' if i/6 <= 75 else 'A+' for i in a]
print(G)

slist=["pass" if i*5>=25 else "fail" for i in range(15)]
print(slist)


shapes=["circle","triangle","sqare","diamond"]
N=[x for x in shapes if "i" in x]
print(N)

h=[98,86,84,55,98,88,44.22,79,65,98,98,87.5]
for j in range(len(h)):
    if h[j]==98:
        print(j)
#elimination of repeated particular element using list comprehension

l=[98,86,84,55,98,88,44.22,65,98,98,87.5]
k=[]
for i in l:
    if i==98:
        continue
    else:
        k.append(i)    
print(k)
# '', "" ,''' ''' used to declare string
#'s can't write in '' but its posible using ""
# but paragraph writing is not posible in "" its posible using '''
#Example:
# suresh='Python'
# durga="python's"
# madhu='''python
# fsdgfdsg
# dgdgd
# dgdgd
# fd
# gd
# dg
# '''
# print(type(suresh),type(durga),type(madhu))
#syntax: variable.method


#upper() returns string in upper case letters
#lower()returns string in lower case letters

# health = "Fruits and Vegetable are good for health"
 
# print(health.upper())
# print(health.lower())

# print(health.find('good')) # both find() and index() both returns the word index in the string
# print(health.index('good'))

# #if the word is not found in index returns -1 always but index() throws an error

# print(health.find('is'))

# #print(health.index('is'))

# print(health.startswith('a'))
# print(health.startswith('Fru'))
# print(health.endswith('th'))




# Science_Courses = []

# for i in ("zoology","maths","computers","opthmology","physics","cardiology"):
#     if i.endswith("gy"):
#         Science_Courses.append(i)
# print(Science_Courses)


# # format() returns entire string in same format
# customers = ["suman","rohit","priya","sonu","venu"]
# for i in customers:
#     print("hi {} get an extra 40% off on sale items!!! hurry up!!". format(i) )


# # isalpha() checks if string in alphabetical, isalnum() checks if string is in alphabets/ numeric or both
# vishal = "VSL567"
# geetha= "geethakumari"
# print(vishal.isalpha())
# print(vishal.isalnum())

# print(geetha.isalnum())
# print(geetha.isalpha())

# # isalnum() returns false to the float numbers
# rj="34666.67"
# print(rj.isalnum())


# len() gives lenth of the string with spaces
# strip() removes the spaces gives the lenth of the string without space count
# lstrip() removes the left side spaces
# rstrip() removes the right side spaces


# P ="  Python general-purpose  programming language   "

# print(len(P))
# G = P.strip()
# print(len(G))

# G = P.lstrip()
# print(len(G))

# G = P.rstrip()
# print(len(G))



# B= " Python is a high-level, general-purpose programming language"

# print(B.title())


# B= " Python is a high-level, general-purpose programming language"
# A = B.replace("is","are")
# # print(A)

# C = B.replace("a","the").replace("is","is one of")
# print(C)

# D = "Slack is an instant messaging program designed by Slack Technologies and owned by Salesforce. Although Slack was developed for professional and organizational communications, it has also been adopted as a community platform."
# #E = D.replace("an","the")
# #print(E)
# #E = D.replace("an ","the ")
# #print(E)
# F = D.replace("and","plus")
# # print(F)

# F1 = D.replace("Slack","sLack",2) # replace working for number of time the repeated data here 2 times slack replaced
# print(F1)
# F2 = D.replace("Slack","sLack",1)
# print(F2)





'''
split() converts string into new list
for split method we must write the looping method
join() converts the list into sting
'''

# B= " Python is a high-level, general-purpose programming language"
# G = B.split()
# #print(G)
# L=[]
# for i in G:
#     if i == 'a':
#         i = 'the'
#     L.append(i)    
# else:
#     L.append(i)
#     print(L)

# #join() converts the list into sting and in the place of " " we can give anything like  "*".join() "2".join() ",".join() etc

# j = "Chemistry is the scientific study of the properties and behavior of matter."
# k = j.split()

# print(k)
# print(j)

# m=" ".join(k)
# print(m)

# q=":".join(k)
# print(q)

# n="!".join(k)
# print(n)














R = "Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming"
P = R.replace("is","are").replace("the","that")
#print(R)

print(P)
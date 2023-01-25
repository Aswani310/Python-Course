
'''

A lambda function is a small anonymous function.

A lambda function can take any number of arguments,
 but can only have one expression.

lambda arguments : expression

'''
# lambda function
#syntax: variable=lambda arguments : expression

std= lambda x,y : (x**2)+(y**2)+2*(x*y)
print(std(5,6))

s=[5,8,9,2]
n=[]
for k in s:
    j=lambda t:(t**2)+5
    n.append(j(k))
print(n)


'''
The filter() method filters the given sequence with the help 
of a function that tests each element in the sequence 
to be true or not.

'''
'''
syntax:

filter(function, sequence)
Parameters:
function: function that tests if each element of a 
sequence true or not.
sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.
Returns:
returns an iterator that is already filtered.
'''
# syntax:filter(function, sequence)
# filter() function

a=(2,4,6,8,2,6,2,1)
b=[9,5,2,62,4,2,8,29,7,2,10,34]
def myfunc(n):
    if n > 2:
        return True
    else:
        return False
d= filter (myfunc, a)
print(tuple(d))
f= filter (myfunc,b)
print(list(f))



# map() function
'''
The python map() function is used to return a list of results
after applying a given function to each item of an iterable(list, tuple etc.)

syntax : map(function, iterables)

'''

def calculatemultiplication(x):
    return x*5
y=[2,3,4,5]
output = map(calculatemultiplication, y)

print(list(output))

def caldivision (x):
    return x / 2
z=(16,32,56,44,98,61,29)

r = map(caldivision,z)

print(tuple(r))


# reduce()function
'''
The reduce() function, as the name describes,
applies a given function to the iterables and returns a single value.
'''
from functools import reduce
# reduce(function,sequence)

z = reduce(lambda x,y:x+y , (2,5,8,3))
print(z)


# filter(),map() diff

def value(n):
    if n % 5 == 0:
        print(n)

data=(25,36,40,44,75,16,6,20,4)

f = filter(lambda n:n/2>10, data)
print(tuple(f))


m = map(lambda n: n-1, data)
print(list(m))


# A Python program to demonstrate use of
# generator object with next()

# A generator function
# def simpleGeneratorFun():
# 	yield 1
# 	yield 2
# 	yield 3

# # x is a generator object
# x = simpleGeneratorFun()

# Iterating over the generator object using next
# print(x.__next__()) # In Python 3, __next__()
# print(x.__next__())
# print(x.__next__())





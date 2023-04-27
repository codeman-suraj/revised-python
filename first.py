print('hello world')
print('*' * 10)

# data types
a = 10
A = "suraj"
print(a, A)

# type casting
x = str(3)
y = int(3)
z = float(3)
print(x, y, z)
print(type(x), type(y), type(z))

# case sensitive
z = 10
Z = 20
print(z, Z)

# many value to multiple variables

j, k, l = 10, 20, 30
print(j, k, l)

# one value to ultiple variables

x = y = z = "orange"
print(x)
print(y)
print(z)


# global variables

x = "awesome"

def myfunct():
    print("python is " + x)
    
myfunct()

def yourfunct():
    print("i love " + x)
    
yourfunct()

# local variables

def localvariables():
    global l
    l = "python"
    print("everyone loves " + l)
localvariables()
    
print("***********************************")
    
print("globaly declared variable " + l)

x = ["apple", "banana", "cherry"]
print(type(x))
    
x = True
print(type(x))

# Below is docstring

'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''

x = "Hello World"	#str	
x = 20	#int	
x = 20.5	#float	
x = 1j	#complex	
x = ["apple", "banana", "cherry"]	#list	
x = ("apple", "banana", "cherry")	#tuple	
x = range(6)	#range	
x = {"name" : "John", "age" : 36}	#dict	
x = {"apple", "banana", "cherry"}	#set	
x = frozenset({"apple", "banana", "cherry"})	#frozenset	
x = True	#bool	
x = b"Hello"	#bytes	
x = bytearray(5)	#bytearray	
x = memoryview(bytes(5))	#memoryview	
x = None	#NoneType

# random function

import random
print(random.randint(0, 20))



# python strings
a = "Hello python"
print(a[0])

# looping through a string
print("****************************************************")

a = "banana"
for i in a:
    print(i)
    
txt = "The best things in life are free!"
print("free" in txt)

if "free" in txt:
    print('Yes, "free" is present in txt')
    
if "expenive" not in txt:
    print('No, "expenive" is not present in txt')
    
    
# string slicing
name = "suraj sanjay otari"
print(name[0:])  #all string starting from zero end with all
print(name[2:])  #string starting with 2nd index and end with all
print(len(name)) #finding lenght of string
print(name[6:12][2:4])


# changing string to uppercase and vice versa
a = "suraj"
print(a.upper()) #upper case
b = "OTARI"
print(b.lower()) #lower case

# remove whitespace
a = "          hello suraj how are you        "
print(a.strip()) #remove whitespace
print(a.replace("suraj", "dhiraj"))

# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello suraj how are you"
print(a.split(",")) #

#string concatination
a = "Hello"
b = "World"
c = a + " " + b
print(c)


#string formatting
a = "suraj"
print("hello " + a , "how are you?")

age = 36
txt = "My name is John, and I am{}"
print(txt.format(age))



quantity = 3
itemno = 567
price = 49.95
print(f"I want to pay {quantity} dollars for {itemno} pieces of item {price}")

a = ["teju", "suraj", "dhiraj"]
print(f"my name is {a[1]} and i have one elder sister who's name is {a[0]} she is married. and i have on younger brother {a[2]}.")

#escape charachter
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

a = ["teju", "suraj", "dhiraj", "teju"]
print(a.count("teju"))

a = 0
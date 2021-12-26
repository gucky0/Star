'''  Python Tutorial: Lesson 2  '''
'''
python tutorial

Lesson 1 recap:
basic output: hello world
'''
##print("Hello World")
"""
line by line
functions - syntax, parameters
variables - box
comments - #, \"""
complications - mistakes
formatting print: f'{}'
input output  - string
shortcuts f5, alt+3, ctrl+c, alt+g
"""
##while True:
##    print("annoying")
"""
mindset - hands-on, read doc

application: swap variables
"""
##a = input("a: ")
##b = input("b: ")
##a,b = b,a
##print(f"""
##a = {a}
##b = {b}""")

"""
feedback: pace too fast
hw: create a script to find out whether a variable is a valid one.

variable = value













what is a valid variable?
https://www.geeksforgeeks.org/python-variables/

Rules for creating variables in Python:
- A variable name must start with a letter or the underscore character.
- A variable name cannot start with a number.
- A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _).
- Variable names are case-sensitive (name, Name and NAME are three different variables).
- The reserved words(keywords) cannot be used naming the variable, eg: class.
"""

"Good Examples:"

##_variable = 1
##vald_variable = 1
##variableName = 1




"Bad Examples:"

##1variable = 1




















##try:
##    #code goes in here
##    eval("1variable = 1")
##except SyntaxError as e:
##    print(e)

##try:
##    eval("variable! = 1")
##except SyntaxError as e:
##    print(e)

##try:
##    eval("class = 1")
##except SyntaxError as e:
##    print(e)


'''  if it is too much to remember, just use var1, var2, etc. '''

'''  <  short break  >  '''























##variable = 'hafiz'
##print(  variable.isidentifier()  )










##variable = 'class'
##print(  variable.isidentifier()  )










'functions'
def cls():
    print("\n"*38)








from keyword import iskeyword



dir()
__builtins__            #module
dir(__builtins__)[116:] #look into module




def is_valid_variable_name(name):
    return name.isidentifier() and not iskeyword(name)











##variable = 'class'
##print(  is_valid_variable_name(variable)  )



































"""
Lesson 2:
other var types: lists, tuples and dictionaries
"""
##elements = "persian", "siamese", "ragdoll"

##list_cat = ["ragdoll"]
##print(list_cat)






##tuple_cat = () #fixed list
##print(tuple_cat)










##dict_animals = {"cat": "persian", "dog": "shiba", "fish": "koi"}
##print(dict_animals)































"""
are they the same? are they ordered? can they be changed? are they mutable? lets test them!

ordered / indexed: can be referenced by numbers


lists and tuples can but dicts can not.


lets try:
"""


##list_cat = ["persian", "siamese", "ragdoll"]
##tuple_cat = ("persian", "siamese", "ragdoll")
##dict_animals = {"cat": "persian", "dog": "shiba", "fish": "koi"}



##print(list_cat[0])










##print(tuple_cat[0])












##print(dict_animals[0]) #error

















"""
mutable / modifiable: items can be added or removed. can be changed
lists and dicts can be modified, tuples can not
lets try:
"""


list_cat = ["persian", "siamese", "ragdoll"]
tuple_cat = ("persian", "siamese", "ragdoll")
dict_animals = {"cat": "persian", "dog": "shiba", "fish": "koi"}










##list_cat[0] = "munchkin"


















##tuple_cat[0] = "munchkin" #error
















##dict_animals[0] = "munchkin" 
##print(dict_animals) #no error but incorrect























'''
dictionary value is called by its key
format:
dictinary_name = {key : value}
'''

##dict_animals["cat"] = "munchkin"
##print(dict_animals)




























""" ---< short break >--- """
''' task: create a madlibs game '''



























'''  <  call stack  >  '''
import sys
print("\n"+"<\tCall\tStack\t>".center(35).replace(" ", "-"))
for k,v in locals().copy().items():
    if k.startswith("__") == 0 and k not in sys.modules and not hasattr(eval(k), '__call__'):
        print(f"{k:13}: {v}")

#extra: globals()[name] = count


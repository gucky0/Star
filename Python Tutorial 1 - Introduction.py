## #variable type , operators and functions

print(1) #display 1 on the shell

"""
variable types

user_string = input('prompt?: ')

nstring ( str ) , number ( int ) , decimal ( float ) , bool
    'abc'      ,      100       ,       12.22       , True

list       ( [] ): mutable , variable size
tuple      [ () ]: immutable , fixed size
dictionary ( { key : value } ): mutable , variable size 
 

#1b) operators
 sum() , max() , min() #int * float = float
 17 % 7  = 3
 4**2    = 16
 8//5    = 1
 -9//5   = -2
 BODMAS: brackets , orders (power and roots) ,
         division and multiply (@ , // , %) ,
         add and subtract , left to right
 8 == 5  = False

#1c) function
def function_name(parameter_1):
        return parameter_1
 
#takeaway 1 - which variable names are valid? : 
 - cannot start with a digit or underscore (special meaning)
 - cannot end with underscore
 - cannot have special char
 - cannnot be keyword





























#takeaway 1b - groups :
lowercase = [chr(i) for i in (range(97,123))] or string.ascii_lowercase
uppercase = [chr(i) for i in (range(65,91))] or string.ascii_uppercase
letters = lowercase + uppercase
numbers   = ['0','1','2','3','4','5','6','7','8','9'] or [chr(i) for i in (range(48,58))] or string.digits
keywords = ['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']











#research
 func ( class )
 type / isinstance()

#projects
 multi-inputs

#extra
 _ = last value (shell)

#extra related functions
 islower(), isupper(), isalpha()
 .append()
"""

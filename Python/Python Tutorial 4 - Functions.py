' Python Task 4: Creating Your Own Functions '

# create a function to say "hello" whenever it is called





































def greet():
    print("Hello!")

# create a function to say "hello <user>" whenever it is called






























def greetMe():
    name = input("What is your name?: ")
    print(f"Hello, {name}!")

# create a function that:
# takes in a number as a parameter
# adds one to it
# displays the output







































def addOne(num):
    num = num + 1
    print(num)

'  <<< short break >>>  '

# creates a function that:
# takes in 2 numbers as parameters
# adds them together
# displays the output






































def add(num1, num2):
    num = num1 + num2
    print(num)

# creates a function that:
# takes in 2 numbers as parameters
# takes in a string (operator) as parameter
# perform said operation
# displays the output











































def op(num1, op, num2):
    num = eval(f"{num1} {op} {num2}")
    print(num)

# Using this Function, and Test Cases, Generate the factors of Input Parameter

def Generate_Factors(num):
    myList = []
    for i in range(1 , num+1):
        if num % i == 0:
            myList.append(i)
    return myList

y = [20 , 31 , 140 , 222 , 517]

##for i in y:
##    print(f"The Factors of {i} is:")
##    print(Generate_Factors(i))

##for i in y:
##    if len(Generate_Factors(i))==2:
##           print(i,'is prime')
##    else:
##           print(i,"is not prime")







' thus edit the function to find prime numbers '






































def find_prime(num):
    if len(Generate_Factors(num)) == 2:
        print(f"{num} is prime")
    else:
        print(f"{num} is not prime")




##example_range = range(5)
##example_range = range(1,5) 
##example_range = range(-2, 2)
##example_range = range(1, 5, 3)
##example_range = range(20, 10, -5)

##for i in example_range:
##    print(i)

















''' Lesson: Daniel: Lesson 3 '''

##variable is descriptorName
##everything is a bulld-on from the prev lesson, like a pyramid
##make ur own functions (myFunc) and put in settings import path
##
##python games
##madlib (io)
##triangle builder (slicing)
##smarter calculator (switch)
##higher lower (if)
##
##'Previous Task: Madlib'
##
##characterName = "Jim"
##characterAge = 12
##
####lines = [f"There once was a man named {characterName}.",\
####         f"He was {characterAge} years old.",\
####         f"He really liked the name {characterName}.",\
####         f"But he didn't like being {characterAge}."]
####
####for line in lines:
####    print(f"{line}".ljust(len(max(lines))))
##
##def checkDifference0(guess):
##    answer = 23
##    if guess > answer:
##        return "Too High. Guess Again: "
##    elif guess < answer:
##        return "Too Low. Guess Again: "
##
##def checkDifference(guess, answer):
##    if guess > answer:
##        return "Too High. Guess Again: "
##    elif guess < answer:
##        return "Too Low. Guess Again: "
##
##def higher_lower():
##    from random import randrange
##    answer = randrange(1,101)
##    print(answer)
##    guess = int ( input("guess the number: ") )
##    guessCount = 1
##    while (guess != answer):
##        prompt = checkDifference(guess, answer)
##        guess = int ( input(prompt) )
##        guessCount += 1
##    print(f"You Won in {guessCount} guesses")
##
####higher_lower()
##
##def validInput(prompt,desiredOutput):
##    output = input(prompt)
##    if desiredOutput == "a":
##        while (not output.isalpha()):
##            output = input(prompt)
##            
##    elif desiredOutput == "0":
##        while (not output.isdigit()):
##            output = input(prompt)
##    return output
##
####characterName = validInput("Who: ","a")
####characterAge = validInput("Age: ","0")
##
####lines = [f"There once was a man named {characterName}.",\
####         f"He was {characterAge} years old.",\
####         f"He really liked the name {characterName}.",\
####         f"But he didn't like being {characterAge}."]
####
####for line in lines:
####    print(f"{line}".ljust(len(max(lines))))
##
####print('''
####Roses are {}
####{} are Blue
####I love {}
####'''.format("Yellow" if input("Color: ")=="" else input("Color: "),\
####           "Pancakes" if input("Plural Noun: ")=="" else input("Plural Noun: "),\
####           "Emma Watson" if input("Celebrity: ")=="" else input("Celebrity: ")))
##
##
##
##
####print("/_____|")
##
##
##
##
##
##
####print("     /|")
####print("    /_|")
####print("   /__|")
####print("  /___|")
####print(" /____|")
####print("/_____|")
##
##
##
##trBase = "/_____|"
##
##
##
##
####while len(trBase >= 2):
####    print(trBase)
##
##
##
##
##
##triBase     = "_"
##triSlope    = "/"
##triHeight   = "|"
##space       = " "
##height      = 5
##
####for i in range(height):
####    print(space * ( height - i )  +\
####          triSlope  +\
####          triBase * i    +\
####          triHeight)
##
##def makeTri(height):
##    height = int(height)
##    for i in range(height):
##        print(space * ( height - i )  +\
##              triSlope  +\
##              triBase * i    +\
##              triHeight)
##
##
####makeTri(input ("how big do you want your Triangle?: ") )

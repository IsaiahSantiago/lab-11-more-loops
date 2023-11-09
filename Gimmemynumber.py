
#use a while loop to reach a number less than 100
userInput = int(input("Gimme a number that is greater than 100... ")) #creating an ouput of an integer with a base 

while userInput <= 100:
    print(str(userInput), " is less than 100, try again... ")
    userInput = int(input("Nope not what I asked forGimme a number that is greater than 100... "))

#imagine that the condition has been satisfied... exited the loop...
    print(str(userInput), " is greater than 100; good Job! ")


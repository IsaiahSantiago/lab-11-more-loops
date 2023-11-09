maximum_stories = 60
usernum = int(input("On what floor of the building is your office?"))

while (usernum > maximum_stories):
#"statement for the termination condition is NOT true, which keeps the loop going..."
    print("You entered: " + str(usernum) + " but there are only " + str(maximum_stories) + " floors in this building. Try again..." )
    usernum = int(input("On what floor of the building is your office?"))

print("Congrats! You work on floor number: " + str(usernum))

##There are two solutions to this challenge
# first :
print("Numbers from 1 to 10")
target_number = 4
while  True:
    guess_number = int(input("Guess the number: "))
    if guess_number == target_number :
       print("Great! You did it!")
       break


# second :

print("Numbers from 1 to 10")
target_number = 4
condation = target_number
while  True:
    guess_number = int(input("Guess the number: "))
    if guess_number > 0 and guess_number < 11 :
        if guess_number == target_number :
            print("Great! You did it!")
            break
        else:
            print("Your guess is wrong try again")
    else:
        print("you guess number out of range -- note our range from 1 to 10 ")
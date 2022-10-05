import random

def guess():
    random_number = random.randint(1, 5)
    i = 1
    limit = 3

    while i <= limit:

        guessed_number = int(input("Enter a Number between 1 & 5: "))
        
        if guessed_number > 5:
            print("The number should be less than 6.")
            continue

        elif guessed_number < 1:
            print("The number should be greater than 0.")
            continue
        
        if guessed_number == random_number:
            print("WOW, Congratulations you own! ")
            break
        else:
            print(f"Try again, You got {limit - i} chance.")
        i += 1

    else:
        print(f"Sorry, you lost. The number was {random_number}")
        
guess()            




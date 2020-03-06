import random
number = random.randint(0,10)
def enter_number():
    return int(input("Guess a random number between 0 and 10:\n"))

user_number = enter_number()

if user_number == number:
    print("you Guessed right!")
elif user_number < number:
    print("Too low")
    print("The random number was: " + str(number))
    print("your guess was: " + str(user_number))
elif user_number > number:
    print("Too high")
    print("The random number was " + str(number))
    print("your guess was: " + str(user_number))

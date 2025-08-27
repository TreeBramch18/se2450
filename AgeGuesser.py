import random

print("Hello there, I'm going to try and guess your age")
name = input("What's your name?")
while True: 
    ageGuess = random.randint(15,30)
    result = input(f"Are you {ageGuess} years old? Y or N?")
    if result in "Y y":
        print(f"Yay, {name} is {ageGuess} years old")
        break
    print("Rats")
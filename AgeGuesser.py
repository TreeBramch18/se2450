import random

print("Hello there, I'm going to try and guess your age")
name = input("What's your name?")

# Runs a random age guess until correct age reached
while True: 
    MinAge = 15
    MaxAge = 30
    ageGuess = random.randint(MinAge,MaxAge)
    result = input(f"Are you {ageGuess} years old? Y or N?")
    if result in "Y y":
        print(f"Yay, {name} is {ageGuess} years old")
        break
    print("Rats")
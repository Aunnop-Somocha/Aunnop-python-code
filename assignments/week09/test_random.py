import random

#refactor != debug

def test_random():
    random_number = random.randint(1, 100)

    guess_number = input("What is your guess number?: ")
    guess_number = int(guess_number)

    if random_number == guess_number:
        print("Congratulation")
    
    elif random_number < guess_number:
        print("Too much")

    elif random_number > guess_number:
        print("Too low")

    print(random_number)
    
test_random()

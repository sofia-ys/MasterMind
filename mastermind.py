#libraries
import random

#game text
print("I have a code with 4 colours, each different. Each colour is represented by a number 1-6, as there are 6 possible colours in total.")
print("Attempt to guess the code within 10 times using my score of your guess.")

#generate code
balls = [1,2,3,4,5,6]

while True: 
    
    code = random.sample(balls, 4)
    guesses = 0 

    for guesses in range(10):
        guess_str = input("Guess: ")
        guess = [int(x) for x in guess_str if x.isdigit()]

        num_correct = sum(1 for num in guess if num in code)
        pos_correct = sum(1 for i in range(4) if guess[i] == code[i])

        if guess == code:
            print("Yes, the code is ", code, "You win!")
            break
        elif guess != [int(x) for x in guess_str if x.isdigit() and int(x) in balls]:
            print("Invalid input: choose numbers between 1 and 6")
            continue
        elif len(guess) != 4:
            print("Invalid input: guess must have four numbers")
            continue
        elif len(guess) != len(set(guess)):
            print("Invalid input: choose unique numbers")
        else:
            num_correct -= pos_correct
            print(pos_correct, "good and", num_correct, "good number but in wrong position")
    else:
        print("You ran out of guesses, the correct code was", code)
     
    again = input("Do you want to play again? Y/N: ")

    if again == 'Y' or again == 'y' or again == 'Yes' or again == 'yes' or again == '':
        guesses = 0
    else:
        break
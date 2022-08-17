'''
Number guesser!  LEARN   THE WHILE-ELSE HERE!
    The else statement allows us to run a block of code once when the condition no longer is true:
'''

secret_num = 2
correctGuess = False
lives = 3

while lives > 0:
    guess = input("Make your guess! ")
    lives = lives - 1
    if int(guess) == secret_num:
        print("You win!")
        break
    print(f"That's the wrong number! Current lives is {lives} \n")
else:
    print("You bad!")


import random

min = 1
max = 6

computer_score = 0
player_score = 0

while True:
    print("Can you beat the computer?")
    print("Please type 'yes' to find out!")
    
    roll = str(input())
    roll = roll.lower()

    player_roll = random.randint(min,max)
    computer_roll = random.randint(min,max)
    
    if roll == "yes":
        print("Currently rolling the dice...")
        print("Drum roll please...")
        print("You rolled:", player_roll)
        print("The computer rolled:", computer_roll)
        if player_roll == computer_roll:
            print("We have a tie!")
            computer_score = computer_score+1
            player_score = player_score+1
            print("Computer:", computer_score, "- Player:", player_score)
            print()

        if player_roll > computer_roll:
            print("Congratulations! You win!")
            player_score = player_score+1
            print("Computer:", computer_score, "- Player:", player_score)
            print()
            
        if player_roll < computer_roll:
            print("Sorry boss! You lose!")
            computer_score = computer_score+1
            print("Computer:", computer_score, "- Player:", player_score)
            print()
else:
    print("Hey! We couldn't quite get that!")

    roll = input("Would you like to roll the dices again?")

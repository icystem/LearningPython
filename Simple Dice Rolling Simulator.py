import random

def roll (sides=6) :
    num_rolled = random.randint (1,sides)
    return num_rolled

def main():
    sides = 6
    rolling= True
    while rolling:
        roll_again = input ("Ready to roll? ENTER=Roll. Q=Quit. ")
        if roll_again.lower() !="q":
            dice1 = roll(sides)
            dice2 = roll(sides)
            player1total = dice1 + dice2
            dice3 = roll(sides)
            dice4 = roll(sides)
            player2total = dice3 + dice4
            #print("You rolled a", str(dice1) +".", "You rolled a", str(dice2) +".")
            #print("The sum of the two die values is", str(dice1 + dice2) +".")
            print("Player 1's total is", str(player1total) +".", "Player 2's total is", str(player2total) +".")
            if player1total > player2total:
                print("Player 1 wins.")
            elif player2total > player1total:
                print("Player 2 wins.")
            else:
                print("It was a tie. Try again.")
        else:
            rolling = False

            print("Thanks for playing.")

main()
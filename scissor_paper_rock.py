import random

choice = ["scissor", "paper", "rock"]
print("ENTER:\nSCISSOR\nPAPER\nROCK\n-1 TO QUIT ")
def game():
    for i in range(0, 10000000):
        
        print(f"Round {i+1}")
        player = (input("Your turn: ")).lower()
        
        if player == "-1":
            print("You quit the game.")
            break
        
        elif player not in choice:
            print("The choice is invalid. Try again! ")
        
        else:
            computer = random.choice(choice)
            print(f"Opponent chooses {computer}")
            
            if player == computer:
                print("The game is draw.")
            
            elif (player == "scissor" and computer == "paper") or (player == "paper" and computer== "rock") or (player == "rock" and computer == "scissor"):
                print("You won.")
            
            else: 
                print("You loose. Better luck next time.")

game()
                
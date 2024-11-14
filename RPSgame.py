import random
options = ("rock","paper","scissor")
running = True
while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        
    
        player = input("enter the choice (rock,paper,scissor)" )
   
    print(f"player:{player}")
    print(f"Computer:{computer}")
    if player == computer:
        
        print("its a tie")
    elif player == "rock" and computer == "scissor" :
        print("You WIN")
    
    elif player == "paper" and computer == "rock":
    
        print("you win")
    
    elif player == "scissor" and computer == "paper":
        print("you win")

    else:
        print("you lose")

    playagain = input("play agaain(y/n): ").lower()
    if not playagain == "y":
        running = False
print("Thanks for Playing")       


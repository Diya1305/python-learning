import random
while True:
    options=('rock','paper','scissors')
    player=input(" Rock?Paper?Scissors?  ").lower()
    computer=random.choice(options)

    while player not in options:
        print(" Invalid")
        player=input(" Rock?Paper?Scissors?  ").lower()

    print(f"Player: {player}")
    print(f"Computer:  {computer}")

    if player==computer:
        print("Draw")
    elif player == "rock" and computer =="scissors":
        print("Player wins")
    elif player== 'paper' and computer=="rock":
        print("player wins")
    elif player== 'scissors' and computer=="paper":
        print("Player wins")
    else:
        print("Computer wins")
    
    again= input('Play again???(yes/no)').lower()
    if again=='no':
        break   

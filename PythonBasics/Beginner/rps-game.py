import random

def get_choices():
    player=input("Enter choice: (Rock,Scissors,Paper)")
    options=["Rock","Scissors","Paper"]
    computer=random.choices(options)
    return {"player":player,"computer":computer}

def check_win(player,computer):
    print(f"You chose {player} & Computer chose {computer}")
    if player==computer:
        return "It's a tie"
    elif player=="Rock":
        if computer=="Scissors":
            return "Rock hits Scissors! You win!"
        else:
            return "Paper wraps Rock, You Lose!"
    elif player=="Scissors":
        if computer=="Paper":
            return "Scissors cut Paper, You WIN!"
        else:
            return "Rock smashes Scissors, You Lose!"
    elif player=="Paper":
        if computer=="Rock":
            return "Paper swallows Rock, You Win!"
        else:
            return "Scissors cut Paper, You Lose!"

choices=get_choices()

print(check_win(choices["player"],choices["computer"]))
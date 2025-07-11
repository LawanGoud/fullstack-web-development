player_score = int(input())
opponent_score = int(input())

if player_score > opponent_score:
    print("Win")
elif player_score == opponent_score:
    print("Draw")
else:
    print("Lose")
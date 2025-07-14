# Read what Abhinav showed
abhinav_choice = input()

# Read what Anjali showed
anjali_choice = input()

# Check the result of the game
if abhinav_choice == anjali_choice:
    print("Tie")
elif abhinav_choice == "Rock" and anjali_choice == "Scissors":
    print("Abhinav Wins")
elif abhinav_choice == "Scissors" and anjali_choice == "Paper":
    print("Abhinav Wins")
elif abhinav_choice == "Paper" and anjali_choice == "Rock":
    print("Abhinav Wins")
else:
    print("Anjali Wins")

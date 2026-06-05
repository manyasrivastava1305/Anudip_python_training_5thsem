# PLAYER SCORE
player_score = []
# input of score form user
for i in range(11):
    score = int(input("Enter the score of player {}: "))
    player_score.append(score)
# display the score of player
print("\n---- Player Scores -----")
print ("score of 11 players: ", player_score)
#finding the highest score
highest_score = max(player_score)

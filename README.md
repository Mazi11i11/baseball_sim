# baseball_sim
A simulation of a 9-inning baseball game using batting average functions for two teams. To run the simulation add batting averages to the simulate_game function followed by the number of innings. Example:

 print("Team 1:", team1_score)
 print("Team 2:", team2_score)

# Example usage
player1 = Player("Player 1", 0.300)
player2 = Player("Player 2", 0.275)
team1 = [player1, player2]

player3 = Player("Player 3", 0.320)
player4 = Player("Player 4", 0.290)
team2 = [player3, player4]

simulate_game(team1, team2, 9)

Future development will incorporate batting and potching statistic databases. feel free to add.

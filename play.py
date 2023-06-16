import random

class Player:
    def __init__(self, name, batting_avg):
        self.name = name
        self.batting_avg = batting_avg

def simulate_at_bat(player):
    # Simulate a single at-bat for a specific player and return the outcome
    if random.random() < player.batting_avg:
        return "Hit"
    else:
        return "Out"

def simulate_inning(team):
    outs = 0
    runs = 0

    # Simulate at-bats until three outs occur
    while outs < 3:
        # Select a player randomly from the team's roster
        batter = random.choice(team)
        outcome = simulate_at_bat(batter)
        if outcome == "Hit":
            runs += 1
        else:
            outs += 1

    return runs

def simulate_game(team1, team2, innings):
    team1_score = 0
    team2_score = 0

    # Simulate innings and update scores
    for _ in range(innings):
        team1_score += simulate_inning(team1)
        team2_score += simulate_inning(team2)

    # Display final scores
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

import random

def simulate_at_bat(batter_avg):
    # Simulate a single at-bat and return the outcome
    if random.random() < batter_avg:
        return "Hit"
    else:
        return "Out"

def simulate_inning(batter_avg):
    outs = 0
    runs = 0

    # Simulate at-bats until three outs occur
    while outs < 3:
        outcome = simulate_at_bat(batter_avg)
        if outcome == "Hit":
            runs += 1
        else:
            outs += 1

    return runs

def simulate_game(team1_avg, team2_avg, innings):
    team1_score = 0
    team2_score = 0

    # Simulate innings and update scores
    for _ in range(innings):
        team1_score += simulate_inning(team1_avg)
        team2_score += simulate_inning(team2_avg)

    # Display final scores
    print("Team 1:", team1_score)
    print("Team 2:", team2_score)

# Example usage
simulate_game(0.300, 0.275, 9)

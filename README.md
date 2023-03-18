# upset-bracket-scoring
A simple scoring program for upset-weighted bracket games. A bracket scores `n` points if they get the winner correct for a game. `n` is the team's seed times 2^(round - 1). Example: 13 seeds in round 1, if you picked it you get 13 * 2^(1-1) = 13 points. 10 seed wins in round 3, if you picked it you get 10 * 2^(3-1) = 40 points.

to run: `python main.py`

Based on a 64 team tournament with 4 regions. Each region has 16 teams seeded 1-16. 

Each number represents a team. The team is the seed for the given number in the commented region. Each round represents the round's winners. Key must be updated for scores to be accurate.

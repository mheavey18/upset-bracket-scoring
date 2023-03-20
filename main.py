key = [
    [
        # Round 1
        [1, 8, 5, 13, 6, 3, 7, 15], # South
        [16, 9, 5, 4, 6, 3, 7, 2], # East
        [1, 9, 5, 4, 11, 3, 10, 2], # Midwest
        [1, 8, 5, 4, 6, 3, 7, 2], # West
    ],
    [
        # Round 2 (Sweet 16)
        [1, 5, 6, 15], # South
        [9, 4, 3, 7], # East
        [1, 5, 3, 2], # Midwest
        [8, 4, 3, 2], # West
    ],
    [
        # Round 3 (Elite 8)
        [0, 0], # South
        [0, 0], # East
        [0, 0], # Midwest
        [0, 0], # West
    ],
    [
        # Round 4 (Final 4)
        [0], # South
        [0], # East
        [0], # Midwest
        [0], # West
    ],
    [
        # Round 5 (Finals)
        [0], # South
        [0], # East
        [0], # Midwest
        [0], # West
    ],
    [
        # Round 6 (Champion)
        [0], # South
        [0], # East
        [0], # Midwest
        [0], # West
    ],
]

brackets = {
    "Marty": [
        [
            # Round 1
            [1, 9, 12, 13, 11, 3, 10, 2], # South
            [1, 8, 12, 13, 11, 3, 10, 2], # East
            [1, 9, 12, 4, 11, 3, 7, 2], # Midwest
            [1, 8, 12, 13, 11, 3, 10, 2], # West
        ],
        [
            # Round 2 (Sweet 16)
            [1, 12, 3, 2], # South
            [8, 12, 11, 10], # East
            [9, 12, 3, 7], # Midwest
            [1, 13, 11, 2], # West
        ],
        [
            # Round 3 (Elite 8)
            [1, 3], # South
            [12, 10], # East
            [12, 7], # Midwest
            [1, 2], # West
        ],
        [
            # Round 4 (Final 4)
            [1], # South
            [10], # East
            [12], # Midwest
            [2], # West
        ],
        [
            # Round 5 (Finals)
            [1], # South
            [0], # East
            [0], # Midwest
            [2], # West
        ],
        [
            # Round 6 (Champion)
            [0], # South
            [0], # East
            [0], # Midwest
            [2], # West
        ],
    ],
    "Jack C.": [
        [
            # Round 1
            [1, 9, 5, 13, 11, 3, 10, 2], # South
            [1, 9, 5, 4, 6, 3, 10, 2], # East
            [1, 9, 12, 13, 11, 3, 10, 2], # Midwest
            [1, 8, 12, 4, 11, 3, 7, 2], # West
        ],
        [
            # Round 2 (Sweet 16)
            [9, 5, 11, 2], # South
            [1, 4, 6, 10], # East
            [1, 12, 3, 2], # Midwest
            [8, 12, 3, 2], # West
        ],
        [
            # Round 3 (Elite 8)
            [5, 11], # South
            [4, 6], # East
            [1, 3], # Midwest
            [8, 3], # West
        ],
        [
            # Round 4 (Final 4)
            [5], # South
            [4], # East
            [1], # Midwest
            [8], # West
        ],
        [
            # Round 5 (Finals)
            [0], # South
            [4], # East
            [0], # Midwest
            [8], # West
        ],
        [
            # Round 6 (Champion)
            [0], # South
            [4], # East
            [0], # Midwest
            [0], # West
        ],
    ],
    "Jack H.": [
        [
            # Round 1
            [1, 8, 12, 4, 11, 14, 7, 2], # South
            [1, 8, 5, 4, 11, 3, 10, 2], # East
            [1, 9, 5, 4, 6, 3, 10, 2], # Midwest
            [1, 9, 5, 4, 11, 3, 7, 2], # West
        ],
        [
            # Round 2 (Sweet 16)
            [1, 12, 11, 2], # South
            [1, 5, 3, 2], # East
            [1, 5, 3, 2], # Midwest
            [1, 5, 11, 2], # West
        ],
        [
            # Round 3 (Elite 8)
            [1, 2], # South
            [5, 3], # East
            [5, 3], # Midwest
            [5, 2], # West
        ],
        [
            # Round 4 (Final 4)
            [2], # South
            [5], # East
            [5], # Midwest
            [2], # West
        ],
        [
            # Round 5 (Finals)
            [0], # South
            [5], # East
            [0], # Midwest
            [2], # West
        ],
        [
            # Round 6 (Champion)
            [0], # South
            [0], # East
            [0], # Midwest
            [2], # West
        ],
    ],
    "Buddy": [
        [
            # Round 1
            [1, 9, 12, 13, 11, 14, 10, 2], # South
            [1, 8, 12, 4, 11, 3, 7, 2], # East
            [1, 9, 12, 13, 11, 3, 10, 2], # Midwest
            [1, 8, 12, 13, 11, 3, 10, 15], # West
        ],
        [
            # Round 2 (Sweet 16)
            [1, 13, 11, 10], # South
            [8, 12, 11, 7], # East
            [9, 12, 11, 10], # Midwest
            [8, 13, 3, 15], # West
        ],
        [
            # Round 3 (Elite 8)
            [1, 11], # South
            [8, 11], # East
            [9, 10], # Midwest
            [8, 3], # West
        ],
        [
            # Round 4 (Final 4)
            [11], # South
            [11], # East
            [10], # Midwest
            [8], # West
        ],
        [
            # Round 5 (Finals)
            [0], # South
            [11], # East
            [0], # Midwest
            [8], # West
        ],
        [
            # Round 6 (Champion)
            [0], # South
            [0], # East
            [0], # Midwest
            [8], # West
        ],
    ],
    "chalk": [
        [
            # Round 1
            [1, 8, 5, 4, 6, 3, 7, 2], # South
            [1, 8, 5, 4, 6, 3, 7, 2], # East
            [1, 8, 5, 4, 6, 3, 7, 2], # Midwest
            [1, 8, 5, 4, 6, 3, 7, 2], # West
        ],
        [
            # Round 2 (Sweet 16)
            [1, 4, 3, 2], # South
            [1, 4, 3, 2], # East
            [1, 4, 3, 2], # Midwest
            [1, 4, 3, 2], # West
        ],
        [
            # Round 3 (Elite 8)
            [1, 2], # South
            [1, 2], # East
            [1, 2], # Midwest
            [1, 2], # West
        ],
        [
            # Round 4 (Final 4)
            [1], # South
            [1], # East
            [1], # Midwest
            [1], # West
        ],
        [
            # Round 5 (Finals)
            [1], # South
            [0], # East
            [1], # Midwest
            [0], # West
        ],
        [
            # Round 6 (Champion)
            [1], # South
            [0], # East
            [0], # Midwest
            [0], # West
        ],
    ],
}

def score(bracket):
    total = 0
    for round in range(6):
        for region in range(4):
            for team in range(len(bracket[round][0])):
                if bracket[round][region][team] == key[round][region][team]:
                    total += bracket[round][region][team] * 2**round
    return total


if __name__ == "__main__":
    for name, bracket in brackets.items():
        print("{}: {}".format(name, score(bracket)))

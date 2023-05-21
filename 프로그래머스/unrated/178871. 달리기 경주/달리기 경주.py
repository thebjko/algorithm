def solution(players, callings):
    rank = {j: i for i, j in enumerate(players)}
    for call in callings:
        players[rank[call]], players[rank[call]-1] = players[rank[call]-1], players[rank[call]]
        rank[players[rank[call]]] += 1
        rank[call] -= 1 
        # rank[call], rank[players[rank[call]]] = rank[players[rank[call]]], rank[call]   # doesn't work
    return players

if __name__ == '__main__':
    test_cases = [
        [["mumu", "soe", "poe", "kai", "mine"], ["kai", "kai", "mine", "mine"]]
    ]
    for tc in test_cases:
        print(solution(*tc))
from typing import List


def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
    players_outcome, players = {}, set()
    res = [[], []]

    for match in matches:
        players_outcome[match[1]] = players_outcome.get(match[1], 0) + 1
        players.add(match[0])
        players.add(match[1])

    for player in players:
        if players_outcome.get(player, 0) == 1:
            res[1].append(player)
        if player not in players_outcome:
            res[0].append(player)

    res[0].sort()
    res[1].sort()
    return res


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    losses_count = [-1] * 100001

    for winner, loser in matches:
        if losses_count[winner] == -1:
            losses_count[winner] = 0
        if losses_count[loser] == -1:
            losses_count[loser] = 1
        else:
            losses_count[loser] += 1

    answer = [[], []]

    for i in range(100001):
        if losses_count[i] == 0:
            answer[0].append(i)
        if losses_count[i] == 1:
            answer[1].append(i)

    return answer


def findWinners(matches: List[List[int]]) -> List[List[int]]:
    winners, losers, multi_losers = set(), set(), set()

    for winner, loser in matches:
        winners.add(winner)

        if loser in losers:
            multi_losers.add(loser)
        else:
            losers.add(loser)

    winners = list(winners - losers)
    losers = list(losers - multi_losers)

    winners.sort()
    losers.sort()

    return [winners, losers]

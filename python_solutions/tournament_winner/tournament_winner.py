
"""
  There's an algorithms tournament taking place in which teams of programmers compete
  against each other to solve algorithmic problems as fast as possible.

  Teams compete in a round robin, where each team faces off against all other teams.
  Only two teams compete against each other at a time, and for each competition,
  one team is designated the home team, while the other team is the away team.

  In each competition there's always one winner and one loser; there are no ties.
  A team receives 3 points if it wins and 0 points if it loses.
  The winner of the tournament is the team that receives the most amount of points.

  Given an array of pairs representing the teams that have competed against each
  other and an array containing the results of each competition, write a
  function that returns the winner of the tournament.

  The input arrays are named competitions and results, respectively.
  The competitions array has elements in the form of [homeTeam, awayTeam], where each
  team is a string of at most 30 characters representing the name of the team.

  The results array contains information about the winner of each corresponding
  competition in the competitions array. Specifically, results[i] denotes the winner
  of competitions[i], where a 1 in the results array means that the home team in the
  corresponding competition won and a 0 means that the away team won.
"""

# (hash_tables): This is an implementation using Two For-loops
# Time Complexity:     |    Space Comaplexity:


def tournamentWinner(competitions, results):
    if len(competitions) > 0:
        totalTeamPoints = []
        loopTracker = 0
        points = 3
        while loopTracker < len(competitions):
            if results[loopTracker] == 1:
                # totalTeamPoints.append([competitions[loopTracker][0], points])
                # if totalTeamPoints[loopTracker][0] in totalTeamPoints[loopTracker]:
                #     points + 3
                totalTeamPoints.append(competitions[loopTracker][0])
            else:
                # totalTeamPoints.append([competitions[loopTracker][1], points])
                # if totalTeamPoints[loopTracker][1] in totalTeamPoints[loopTracker]:
                #     points + 3
                totalTeamPoints.append(competitions[loopTracker][1])

            loopTracker += 1
            i = 0
            winner = []
        while i < len(totalTeamPoints):
            j = totalTeamPoints.count(totalTeamPoints[i]) * 3
            f = totalTeamPoints[i]
            winner.append(f)
            winner.append(j)
            i += 1

    return winner


if __name__ == "__main__":
    competitions = [
        ["HTML", "C#"],
        ["Python", "C#"],
        ["Python", "HTML"],
    ]

    results = [0, 1, 1]

    print(tournamentWinner(competitions, results))

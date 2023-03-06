from typing import List, Union
from dataclasses import dataclass
import copy


@dataclass
class TeamScore:
    name: str
    points: int
    place: int


def take_input():
    teams_num = int(input())
    data: List[TeamScore] = []
    for place in range(1, teams_num + 1):
        name, points = input().split()
        data.append(TeamScore(name=name, points=int(points), place=place))
    return data


def find_place(first_team: str,
               second_team: str,
               data: List[TeamScore],
               first_team_won: Union[bool, None] = True
               ):
    if first_team_won:
        for team_score in data:
            if team_score.name == first_team:
                team_score.points += 3

        data.sort(key=lambda x: (-x.points, x.name))
        for team in data:
            team.place = data.index(team) + 1

    elif first_team_won is False:
        for team_score in data:
            if team_score.name == second_team:
                team_score.points += 3

        data.sort(key=lambda x: (-x.points, x.name))
        for team in data:
            team.place = data.index(team) + 1

    else:
        for team_score in data:
            if team_score.name in (first_team, second_team):
                team_score.points += 1

        data.sort(key=lambda x: (-x.points, x.name))
        for team in data:
            team.place = data.index(team) + 1

    for t in data:
        if t.name == first_team:
            return t.place


def main():
    teams_scores: List[TeamScore] = take_input()
    team_a, team_b = input().split(sep="-")

    win = find_place(first_team=team_a, second_team=team_b, data=copy.deepcopy(teams_scores), first_team_won=True)
    draw = find_place(first_team=team_a, second_team=team_b, data=copy.deepcopy(teams_scores), first_team_won=None)
    lose = find_place(first_team=team_a, second_team=team_b, data=copy.deepcopy(teams_scores), first_team_won=False)
    return " ".join(map(str, (win, draw, lose)))


if __name__ == '__main__':
    print(main())

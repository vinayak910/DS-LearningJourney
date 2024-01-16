#data analysis

import pandas as pd
import numpy as np

matches = pd.read_csv("IPL_Matches_2008_2022 - IPL_Matches_2008_2022.csv")


def teamsAPI():
     teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
     teams_dict = {
         'teams':teams
     }
     return teams_dict


def team_vs_teamAPI(team1, team2):
    temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (
                matches['Team2'] == team1)]
    total_matches = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (
                matches['Team2'] == team1)].shape[0]

    matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
    matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]

    draws = total_matches - (matches_won_team1 + matches_won_team2)

    response = {
        'total matches': total_matches,
        team1 + ' won': matches_won_team1,
        team2 + ' won': matches_won_team2,
        'draw': draws
    }
    response = {(key): str(value) for key, value in response.items()}
    return response
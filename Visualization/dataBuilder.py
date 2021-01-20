#!/usr/bin/env python3

import numpy as np
import pandas as pd
import plotly.graph_objects as go


_dataset = '../dataset/athlete_events.csv'

_sports = list()
_teams = list()
_medals = ["Gold", "Silver", "Bronze", "nan"]

def newSport(test):
    for sport in _sports:
        if sport == test:
            return False
    return True

def getDisciplines(csv):
    global _sports
    for line in csv['Sport']:
        if (newSport(line) == True):
            _sports.append(line)

def newTeam(test):
    for team in _teams:
        if team == test:
            return False
    return True

def getCountries(csv):
    global _teams
    for line in csv['NOC']:
        if (newTeam(line) == True):
            _teams.append(line)

def dataSelector():
    try:
        with open(_dataset, 'r') as f:
            print("open")
            filtered_csv = pd.read_csv(_dataset, usecols=['NOC', 'Year', 'Sport', 'Medal'])
            print("filtered")
            getDisciplines(filtered_csv)
            getCountries(filtered_csv)
            f.close()
            return filtered_csv
    except:
        print(f'The program could not find the dataset.\nPlease make sure the archive has been unzipped, and that the dataset is located at the following path : \'{_dataset}\'')
        exit(1)

def visualizer(team, year, sport, medal):
    fig = go.Figure(data=
        go.Parcoords(
            line = dict(color = year,
                    colorscale = 'Electric',
                    showscale = True,
                    cmin = 1900,
                    cmax = 2020),
            dimensions = list([
                dict(label = 'Medal',
                    tickvals = list(range(0, len(_medals))),
                    ticktext = ["Gold", "Silver", "Bronze", "nan"],
                    values = medal),
                dict(label = "Country",
                    tickvals = list(range(0, len(_teams))),
                    ticktext = _teams,
                    values = team),
                dict(label = 'Sport',
                    tickvals = list(range(0, len(_sports))),
                    ticktext = _sports,
                    values = sport),
                dict(label = 'Year',
                    values = year),
            ])
        )
    )
    fig.show()

def dataTranslator(csv):
    colTeam = list()
    colYear = list()
    colSport = list()
    colMedal = list()
    for line in csv['NOC']:
        colTeam.append(_teams.index(line))
    for line in csv['Year']:
        colYear.append(int(line))
    for line in csv['Sport']:
        colSport.append(_sports.index(line))
    for line in csv['Medal']:
        if type(line) is str:
            colMedal.append(_medals.index(line))
        else:
            colMedal.append(3)

    visualizer(colTeam, colYear, colSport, colMedal)

    data = np.column_stack((colTeam, csv['Year']))
    data = np.column_stack((data, colSport))
    data = np.column_stack((data, colMedal))
    return data

def buildData():
    filtered_csv = dataSelector()
    data = dataTranslator(filtered_csv)
    np.save("data", data)

#!/usr/bin/env python3

import numpy as np
import pandas as pd
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

    data = np.column_stack((colTeam, csv['Year']))
    data = np.column_stack((data, colSport))
    data = np.column_stack((data, colMedal))
#    print(data)
    return data

def buildData():
    filtered_csv = dataSelector()
    data = dataTranslator(filtered_csv)

    column_1 = np.random.uniform(3, 5, 10)
    noise_2 = np.random.normal(0, 0.01, 10)
    column_2 = 4*column_1+noise_2
    noise_3 = np.random.normal(0, 0.1, 10)
    column_3 = 50 - 2*column_2+noise_3
    noise_4 = np.random.normal(0, 5, 10)
    column_4 = 10+column_1+noise_4

    doto = np.column_stack((column_1, column_2))
    doto = np.column_stack((doto, column_3))
    doto = np.column_stack((doto, column_4))
    print(doto)

    np.save("data", data)

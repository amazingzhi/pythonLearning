# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 14:47:24 2020

@author: amazi
"""
import pandas as pd
import numpy as np
gamedetails = pd.read_csv(r'C:\Users\amazi\OneDrive\Desktop\NBA data\games and player from 2004 to 2020\games_details.csv')



gameid=0
teamid=0
abilityindex=0
sumPlus1={}
sumPlus2={}
gamedetails=gamedetails.fillna(0)

for index,row in gamedetails.iterrows():
    if gameid==row['GAME_ID']:
        if teamid==row['TEAM_ID']:
            abilityindex=abilityindex+row['PLUS_MINUS']
        elif teamid!=row['TEAM_ID']:
            print (abilityindex)
            sumPlus1[gameid]=abilityindex
            abilityindex=row['PLUS_MINUS']
            teamid=row['TEAM_ID']
    elif gameid!=row['GAME_ID']:
        sumPlus2[gameid]=abilityindex
        teamid=row['TEAM_ID']
        gameid=row['GAME_ID']
        abilityindex=row['PLUS_MINUS']
        

sumPlus_away = sumPlus1
sumPlus_home = sumPlus2

print (sumPlus_away)

from collections import defaultdict


sumPlus_ha = defaultdict(list)

for d in (sumPlus_home, sumPlus_away): # you can list as many input dicts as you want here
    for key, value in d.items():
        sumPlus_ha[key].append(value)

print(sumPlus_ha)

sumPlus_ha_csv = pd.DataFrame(list(sumPlus_ha.items()),columns = ['Game_ID','sumPlus'])

print (sumPlus_ha_csv)

sumPlus_ha_csv=sumPlus_ha_csv.drop(sumPlus_ha_csv.index[[0,23096]],axis = 0)
print(sumPlus_ha_csv)

sumPlus_ha_csv['sumPlus'].float.split(expand=True)
















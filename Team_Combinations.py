import pandas as pd
import itertools
import csv 

FILENAME = "FPL_Defence_FDR.csv"
RATINGS = pd.read_csv(FILENAME)
DEF_IN_SQUAD = 4

GAMEWEEK = "GW{}".format(1)
TEAM_COMB = list(itertools.combinations(RATINGS['TEAM'], DEF_IN_SQUAD))

file = open('Teams_4.csv', 'w+', newline ='') 
with file:     
    write = csv.writer(file) 
    write.writerows(TEAM_COMB)
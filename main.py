import pandas as pd
import itertools
import csv

FILENAME = "FPL_Defence_FDR.csv"
RATINGS = pd.read_csv(FILENAME)
DEF_IN_SQUAD = 4 #including two Goalkeepers
DEF_IN_XI = 2
STARTING_GW = 1
ENDING_GW = 11 #GW10 (Increment)

def validCombinations(GAMEWEEK):
  TOTAL_COMB = list(itertools.combinations(RATINGS[GAMEWEEK], DEF_IN_SQUAD))
  VALID_COMB = [(sum(sorted(x)[:DEF_IN_XI])) for x in TOTAL_COMB]
  return(VALID_COMB)

TEAM_COMB = RATINGS.columns

for i in range(STARTING_GW, ENDING_GW, 1):
  GW = "GW{}".format(i)
  a = validCombinations(GW)
  # print(len(a))
  TEAM_COMB = TEAM_COMB.insert(i, a)

file = open('GW10.csv', 'w+', newline ='')  
with file:     
    write = csv.writer(file) 
    write.writerows(TEAM_COMB) 
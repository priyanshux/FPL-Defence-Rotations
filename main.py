import pandas as pd
import itertools

FILENAME = "FPL_Defence_FDR.csv"
RATINGS = pd.read_csv(FILENAME)
DEF_IN_SQUAD = 5 #including two Goalkeepers
DEF_IN_XI = 3
STARTING_GW = 1
ENDING_GW = 11 #GW10 (Increment)

def validCombinations():
  for i in range(STARTING_GW, ENDING_GW, 1):
    GAMEWEEK = "GW{}".format(i)
    TOTAL_COMB = list(itertools.combinations(RATINGS[GAMEWEEK], DEF_IN_SQUAD))
    VALID_COMB = [(sum(sorted(x)[:DEF_IN_XI])) for x in TOTAL_COMB]
    yield(VALID_COMB)

for i in validCombinations():
  FINAL = [i[j] + i[j] for j in range(len(i)) if i[j] > 0]


print(FINAL)
import pandas as pd
import itertools

FILENAME = "FPL_Defence_FDR.csv"
RATINGS = pd.read_csv(FILENAME)

DEF_IN_SQUAD = 5 #Including 2 Goalkeepers
DEF_IN_XI = 2

# GAMEWEEK = "GW1"
# RATINGS = pd.read_csv(FILENAME)
# TOTAL_COMB = list(itertools.combinations(RATINGS[GAMEWEEK], DEF_IN_SQUAD))
# TOTAL_COMB = [(sorted(x)[:DEF_IN_XI]) for x in TOTAL_COMB]
# print(TOTAL_COMB)

def validCombinations():
  for i in range(1,39,1):
    GAMEWEEK = "GW{}".format(i)
    TOTAL_COMB = list(itertools.combinations(RATINGS[GAMEWEEK], DEF_IN_SQUAD))
    VALID_COMB = [(sum(sorted(x)[:DEF_IN_XI])) for x in TOTAL_COMB]
    yield(VALID_COMB)

for i in validCombinations():
  print(i)


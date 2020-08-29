import pandas as pd
import itertools

filename = "FPL_Defence_FDR.csv"

# my_csv = pd.read_csv(filename, usecols = [i])

# print(my_csv)

DEF_IN_SQUAD = 7 #including two Goalkeepers
DEF_IN_XI = 4



for i in range(1,39):
  GAMEWEEK = "GW{}".format(i)
  my_csv = pd.read_csv(filename)
  TOTAL_COMB = list(itertools.combinations(my_csv[GAMEWEEK], DEF_IN_SQUAD))
  VALID_COMB = (sorted(TOTAL_COMB)[:DEF_IN_XI])
  print(VALID_COMB)
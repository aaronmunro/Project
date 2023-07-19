import pandas as pd
records = pd.read_csv('Bundesliga_Results.csv')

# Cleaning:

records = records[~records.isna().any(axis=1)]

# Which team/(s) has been in the BuLi the most? (from 95/96 to 17/18)
# Checking prevalence in number of games played with groupby

homes = records.groupby(['HomeTeam']).agg({'Date':'count'})

homes.columns = ['countOfHomeGames']

homes = homes.reset_index()

# homes.rename({'Date':'countOfHomeGames'}, axis=1, inplace=True)

homes = homes.reset_index().sort_values(by='countOfHomeGames', ascending=False)

print(homes.head(10))

# Hamburg, Bayern, Werder Bremen, Schalke, Leverkusen and Dortmund have played the maximum amount of games at their home stadiums.

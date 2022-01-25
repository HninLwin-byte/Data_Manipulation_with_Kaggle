import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib

sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'
matches_raw_df=pd.read_csv('D:\data download\matches.csv')
#print(matches_raw_df.shape)
#print(matches_raw_df.columns)
#print(matches_raw_df.info())
#print(matches_raw_df.result.value_counts())
matches_df=matches_raw_df.drop('umpire3',axis=1)
#print(matches_df)

matches_per_season=matches_df.groupby("season").id.count()

#plt.figure(figsize=(12,6))
#plt.xticks(rotation=75)
#plt.title("Matches Per Season")
#matches_per_season_plot=sns.barplot(x=matches_per_season.index,y=matches_per_season)
#matches_per_season_plot.set(xlabel="Seasons",ylabel="number of matches")
toss_decision_percentage = matches_df.groupby('season').toss_decision.value_counts() / matches_per_season * 100

#print(matches_per_season)
#print(toss_decision_percentage.unstack())
#toss_decision_percentage.unstack().plot(kind='bar',figsize=(12,6),title='Toss decision',xlabel='Season',ylabel='Percentage')

filter_1=(matches_df.result=='normal')&(matches_df.win_by_wickets==0)
wins_batting_first=matches_df[filter_1].groupby('season').winner.count()/matches_per_season * 100
filter_2=(matches_df.win_by_runs==0) & (matches_df.result=='normal')
wins_fielding_first=matches_df[filter_2].groupby('season').winner.count()/matches_per_season * 100

combined_wins_df=pd.concat([wins_batting_first,wins_fielding_first],axis=1)
combined_wins_df.columns = ['batting_first','field_first']
#print(combined_wins_df)

#combined_wins_df.plot(kind='bar',figsize=(12,6),title='Wins',xlabel='Season',ylabel="Percentage")
'''total_matches_played = (matches_df.team2.value_counts() + matches_df.team1.value_counts()).sort_values(ascending= False)'''
#print(total_matches_played)
'''plt.figure(figsize=(12,6))
plt.title("Total matches")
total_matches_played_plot=sns.barplot(y=total_matches_played.index,x=total_matches_played)
total_matches_played_plot.set(xlabel='Teams',ylabel='no of matches')
#plt.show()'''

#most_wins = matches_df.winner.value_counts()
#print(most_wins)

#win_percentage= (most_wins/total_matches_played).sort_values(ascending=False)*100
#print(win_percentage)

#plt.figure(figsize=(12,6))
#plt.title('Win percentage')

#win_percentage_plot=sns.barplot(y=win_percentage.index,x=win_percentage)

#win_percentage_plot.set(xlabel='Percentage',ylabel="Teams")



#plt.show()

'''ipl_win=matches_df.groupby('season').tail(1).sort_values('season',ascending = True)
print(ipl_win)

ipl_win_winner=ipl_win.winner.value_counts()
print(ipl_win_winner)'''

'''plt.figure(figsize=(18,4))
plt.xlabel('Teams')
plt.ylabel('No of wins')
plt.title('IPL championship')

sns.barplot(x=ipl_win_winner.index,y=ipl_win_winner)
plt.show()'''

matches_won_each_season=pd.crosstab(matches_df['winner'],matches_df['season'])
#print(matches_won_each_season)

'''plt.figure(figsize=(16,10))
plt.xlabel('Season')
plt.ylabel('Teams')
plt.title("Matches won per season")

sns.heatmap(matches_won_each_season, annot = True, cmap = 'rocket_r', fmt = 'd', cbar_kws={"orientation": "horizontal"})
plt.show()'''

mivcsk_df = matches_df[((matches_df.team1 == 'Mumbai Indians') & (matches_df.team2 == 'Chennai Super Kings')) | ((matches_df.team1 == 'Chennai Super Kings') & (matches_df.team2 == 'Mumbai Indians')) ]
mivcsk = mivcsk_df.winner.value_counts()
print(mivcsk)




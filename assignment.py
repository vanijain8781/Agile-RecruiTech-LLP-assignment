import pandas as pd

# read the two Excel sheets
df1 = pd.read_excel('Input 1.xlsx')
df2 = pd.read_excel('Input 2.xlsx')
# code for Output 1
# merge the two dataframes based on the User ID/uid column for Output 1
df_merged = pd.merge(df1[['Team Name', 'User ID']], df2[['uid','total_statements', 'total_reasons']], left_on='User ID', right_on='uid')
df_merged = df_merged.drop(columns=['uid', 'User ID'])

# group the merged dataframe by Team Name and calculate the average statements and reasons
grouped_df = df_merged.groupby('Team Name').agg({'total_statements': 'mean', 'total_reasons': 'mean'})

# add a new column for the sum of 'total_statements' and 'total_reasons'
grouped_df['rank'] = grouped_df['total_statements'] + grouped_df['total_reasons']

# sort the dataframe based on 'rank' in descending order
grouped_df = grouped_df.sort_values(by='rank', ascending=False)

# reset the index of the sorted dataframe and re-assign the ranks from 1 to 10
grouped_df = grouped_df.reset_index().rename(columns={'Team Name': 'Thinking Teams Leaderboard'})
grouped_df = grouped_df.reset_index().rename(columns={'total_statements': 'Average Statements'})
grouped_df = grouped_df.reset_index().rename(columns={'total_reasons': 'Average Reasons'})
grouped_df['Team Rank'] = range(1, 10)

# select the required columns and display the updated dataframe
grouped_df = grouped_df[['Team Rank', 'Thinking Teams Leaderboard', 'Average Statements', 'Average Reasons']]
print(grouped_df)
grouped_df.to_excel('output_file1.xlsx', index=False)


#code for Output 2
df_merged = pd.merge(df1[['Name','User ID']], df2[['uid','total_statements', 'total_reasons']], left_on='User ID', right_on='uid')
df_merged = df_merged.drop(columns=['User ID'])
df_merged['rank'] = df_merged['total_statements'] + df_merged['total_reasons']

# sort the dataframe based on 'rank' in descending order
df_merged = df_merged.sort_values(by='rank', ascending=False)
df_merged = df_merged.reset_index().rename(columns={'total_statements': 'No. of Statements'})
df_merged = df_merged.reset_index().rename(columns={'total_reasons': 'No. of Reasons'})
df_merged['Rank'] = range(1, 22)
df_merged = df_merged[['Rank', 'Name','uid', 'No. of Statements', 'No. of Reasons']]

print(df_merged)
df_merged.to_excel('output_file2.xlsx', index=False)


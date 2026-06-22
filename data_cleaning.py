import pandas as pd

df = pd.read_csv('raw_data.csv')
df.drop_duplicates(inplace=True)
df.fillna('Not Available', inplace=True)
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
df['Email_Valid'] = df['Email'].str.contains('@')
df.to_csv('cleaned_data.csv', index=False)
print('Data Cleaning Completed Successfully!')

import pandas as pd

df = pd.read_csv('query.csv', sep=',')

print(len(df['personLabel'].unique()))
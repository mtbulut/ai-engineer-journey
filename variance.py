import pandas as pd
df = pd.read_csv("actuals_budget.csv")
# print(df)
print()
# print(df.dtypes) there is no need to use this for now 
# Varience calculation below
# df['variance'] = df['actual'] - df['budget']
# print(df)
df['budget*actual^2'] = df['budget'] * df['actual']+df['actual']
print(df)
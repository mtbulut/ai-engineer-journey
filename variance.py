import pandas as pd
df = pd.read_csv("actuals_budget.csv")
# print(df)
print()
# print(df.dtypes) there is no need to use this for now 
# Varience calculation below
# df['variance'] = df['actual'] - df['budget']
# print(df)
# Variance calculation
df["variance"] = df["actual"] - df["budget"]
df["variance_pct"] = (df["variance"] / df["budget"] * 100).round(2)
print(df)
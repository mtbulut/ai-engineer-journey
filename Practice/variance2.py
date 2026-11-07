import pandas as pd
import numpy as np
df = pd.read_csv("actuals_budget.csv")
# print(df)
df['Varience'] = df['actual'] - df['budget']
df["Net Sales"] = df['Varience'] * df['budget']

# print(df)
df["Flag"]= np.where((df['account'] == "Opex") & (df['Varience']) <= 0,
                     "1",
                     "2"
                     )
print(df)

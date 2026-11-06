import pandas as pd
import numpy as np

df = pd.read_csv("actuals_budget.csv")
# print(df)
print()
# print(df.dtypes) there is no need to use this for now 
# Varience calculation below
# df['variance'] = df['actual'] - df['budget']
# print(df)
# Variance calculation
df["variance"] = df["actual"] - df["budget"]
df["variance_pct"] = (df["variance"] / df["budget"] * 100).round(1)


#Revenue: Positive varience is good. Opex: negative varience is good. 

df["favorable"] = np.where(
    df["account"] == "Revenue",
    df["variance"] >= 0,
    df["variance"] <=0
)
df['flag'] = np.where((df['favorable'] == False) & (df['variance_pct'].abs()>5),
                      "FLAG", 
                      ""
                      )

print(df)
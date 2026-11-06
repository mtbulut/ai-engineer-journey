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
df['flag'] = np.where((~df['favorable'] & (df['variance_pct'].abs()>5)),
                      "FLAG", 
                      ""
                      )
# print(df)
# now CFP team 8 satirlik ozeti gormek istediklerini belirttiler ve Soru: Temmuzda North bolgesi toplamda nasillardi?
summary = df.groupby(['month','region'])[['actual', 'budget','variance']].sum()
# print(df)
# print(summary)
#  Her group ta kac flag var ona bakilmali.. 
df['is_flag'] = df['flag'] == 'FLAG'
print(df)

Flag_count = df.groupby(['month','region'])[['actual','budget','variance','is_flag']].sum()
print(Flag_count)
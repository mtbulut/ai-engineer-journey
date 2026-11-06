import pandas as pd
df = pd.read_csv("Customer.csv")

df["sqrtt"] = df["Code"] + df["Code"]

print(df)
# Bolge bazinda toplam actual
import pandas as pd
from pathlib import Path
# This is the parent part of it below
BASE_DIR = Path(__file__).parent  
# Buda tam dosyanin yeri 
path = BASE_DIR/"actuals_budget.csv"
df = pd.read_csv(path)
# print(df)

# test = df[df['region'] == 'North']
# print(test)
#	Soru	İpucu	Kontrol için cevap
# 1	Bölge bazında toplam actual	groupby + sum	North = 257000

by_region = df.groupby(['region','account']).agg(
    total_actual = ('actual', 'sum')
)

print(by_region)
print(df)

	# Ay bazında toplam budget	groupby + sum	2026-07 = 299000

by_month = df.groupby('month').agg(
    total_buget = ("budget", "sum")
)

print(by_month)

print(df.groupby("month")[['budget']].sum())

# diger yollarin hepsini deniyelim 
budget_by_month = df.groupby('month')[['budget']].sum()
print(budget_by_month)
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
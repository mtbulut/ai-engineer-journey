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

by_region = df.groupby(['region',]).agg(
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
# print(df)

print(df.groupby('account')[['actual','budget']].sum())
#4. Only the Opex row
print(df[df['account'] == "Opex"])
#5. Rows where actual is greater than 100000
print(df[df['actual'] > 100000])
# 6. Revenue for the south region only
print(df[(df['region'] == 'South') & (df['account'] == 'Revenue')] )

# 7. Average actual by region by data Frame seklinde yazmis oldum
print(df.groupby('region')[['actual']].mean())

# 8. Lowest and highest actual by account
#    Hint: agg                      | Check: Revenue min = 91000

account_by = df.groupby('account').agg(
    lowest_actual = ('actual','min'),
    highest_actual = ('actual','max')
)
print(account_by)


# print(pd.concat([df.groupby('account')[['actual']].max(), df.groupby('account')[['actual']].min()],ignore_index=True))

# 9. Opex pivot: regions in rows, months in columns, with totals
#    Hint: pivot_table              | Check: Opex grand total = 170000
# aslinda burada filitreleme yapiliyor
opex = df[df["account"] == "Opex"] 
print(opex)
pivot = pd.pivot_table(opex, values='actual',index='region',columns='month',aggfunc='sum', margins=True)
print(pivot)
print(df)


# 10. Pivot with accounts in rows, regions in columns, showing budget
#     Hint: pivot_table
budget_pivot = pd.pivot_table(df, values= 'budget', index='account', columns='region', margins= True, aggfunc='sum')
print(budget_pivot)
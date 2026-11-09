from pathlib import Path
import pandas as pd
import numpy as np
BASE_DIR = Path(__file__).parent
path = BASE_DIR / "actuals_budget.csv"

df = pd.read_csv(path)
# df = pd.read_csv("actuals_budget.csv")  Bu sorun teskil eder.. cunku path olusturulmadi. 
print(df)
# Hesap basinda ozet: Toplam, ortalama, en yuksek, adet
# Hesap bazında özet: toplam, ortalama, en yüksek, adet
by_account = df.groupby("account").agg(
    total_actual=("actual", "sum"),
    avg_actual=("actual", "mean"),
    max_actual=("actual", "max"),
    row_count=("actual", "count"),
)
print()
# print(by_account)

without_agg_sum = df.groupby("account")["actual"].sum()
without_agg_mean = df.groupby("account")["actual"].mean()
without_agg_max = df.groupby("account")["actual"].max()
without_agg_count = df.groupby("account")["actual"].count()
print(without_agg_mean,without_agg_sum)

combined = pd.DataFrame({
    "total_actual": without_agg_sum,
    "avg_actual" :without_agg_mean,
    "max_actual" : without_agg_max,
    "count_actual" : without_agg_count
})

print(combined)

combined_2 = pd.DataFrame()

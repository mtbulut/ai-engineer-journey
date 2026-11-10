import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).parent
path = Path(BASE_DIR/'monthly_revenue.csv')
# print(path.exists())

df = pd.read_csv(path)


# 1. Metni gerçek tarihe çevir
df['month'] = pd.to_datetime(df['month'])
print(df)

# 2. Önce bölgeye, sonra aya göre sırala
df = df.sort_values(["region", "month"])
print(df)

# 3. YTD: Her bölge için kümülatif toplam
df["ytd"] = df.groupby("region")["revenue"].cumsum()
print(df)

# north_march = df.groupby(["month","region"])["revenue"].cumsum()
# print(north_march)
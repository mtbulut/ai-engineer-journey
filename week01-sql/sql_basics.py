import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent.parent
csv_path = (BASE_DIR / "week01-pandas" / "actuals_budget.csv")
df = pd.read_csv(csv_path)
print(csv_path.exists())
print(df)

#2. veritabanina baglan dosya yoksa olustutur (finance.db done!)
conn = sqlite3.connect(BASE_DIR/"week01-sql"/"finance.db")
print(conn)

#3.csv tablosunu db ye yazditma zamani 

df.to_sql("actuals_budget", conn, if_exists="replace", index= False)
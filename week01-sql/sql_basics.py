import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent.parent
csv_path = (BASE_DIR / "week01-pandas" / "actuals_budget.csv")
df = pd.read_csv(csv_path)
# print(csv_path.exists())
# print(df)

#2. veritabanina baglan dosya yoksa olustutur (finance.db done!)
conn = sqlite3.connect(BASE_DIR/"week01-sql"/"finance.db")
print(conn)

#3.csv tablosunu db ye yazditma zamani 

df.to_sql("actuals_budget", conn, if_exists="replace", index= False)

# ilk SQL sorgusunu yazalim. 
# query = "SELECT * FROM actuals_budget"
# result = pd.read_sql_query(query, conn)
# print(result)

#5 baglatiyi kapat 
conn.close()
print()

conn = sqlite3.connect(BASE_DIR/"week01-sql"/"finance.db")
# query = "SELECT * FROM actuals_budget"
# result = pd.read_sql_query(query, conn)
# print(result)

query = """
SELECT month, region, actual,budget, actual, actual
FROM actuals_budget
"""
query = """
SELECT *
FROM actuals_budget
WHERE region = 'North' AND account = 'Revenue'
"""

query = """
SELECT month, region, account, actual
FROM actuals_budget
WHERE actual > 100000
"""

query = """
SELECT month, region, account, actual, budget,
       actual - budget AS variance
FROM actuals_budget
"""
query = """
SELECT region,AVG(budget) AS avg_budget, SUM(actual) AS total_actual
FROM actuals_budget
GROUP BY region
"""

query = """
SELECT account,
       SUM(actual) AS total_actual,
       SUM(budget) AS total_budget,
       SUM(actual) - SUM(budget) AS variance,
       COUNT(*) AS row_count
FROM actuals_budget
GROUP BY account
"""
query = """
SELECT * FROM actuals_budget
"""
# 1. All Opex rows
#    Check: 4 rows
query = """
SELECT *
FROM actuals_budget
WHERE account = 'Opex'
"""
# 2. Rows where budget is greater than 100000
#    Check: 4 rows

query = """
SELECT *
FROM actuals_budget
WHERE budget > 100000
"""
# 3. South rows where actual is less than budget
#    Hint: WHERE ... AND ...   | Check: 3 rows
query = """ 
SELECT * 
FROM actuals_budget
WHERE region = 'South' AND actual < budget

"""
# 4. Total actual by month
#    Check: 2026-07 = 301000, 2026-08 = 303000

query = """
SELECT month, account, SUM(actual) AS tl_actual, SUM(budget) AS tl_budget
FROM actuals_budget
GROUP BY month
"""

# 5. Total budget by region
#    Check: North = 314000, South = 290500
query = """
SELECT region, SUM(budget) AS tl_budget
FROM actuals_budget
GROUP BY region
"""
# 6. Average actual by account
#    Check: Revenue = 108500, Opex = 42500
query = """
SELECT account, 
AVG(actual) AS avg_actual
FROM actuals_budget
GROUP BY account
"""
# 7. All rows sorted by actual, highest first
#    Hint: ORDER BY ... DESC   | Check: first row = 125000
query = """
SELECT *
FROM actuals_budget
ORDER BY actual DESC
"""
# 8. Variance (actual - budget) by month AND region
#    Hint: GROUP BY month, region   | Check: 2026-08 South = -15500
query = """
SELECT region, month, SUM(actual)- SUM(budget) AS Variance
FROM actuals_budget
GROUP BY region, month
"""
# 9. Revenue only: total actual and total budget by region
#    Hint: WHERE + GROUP BY   | Check: South actual = 189000, budget = 212000
query = """
SELECT region, 
SUM(actual) AS Total_actual,
SUM(budget) AS Total_budget
FROM actuals_budget
WHERE account = 'Revenue'
GROUP BY region
"""
# 10. Rows with negative variance, worst first
#     Hint: WHERE actual - budget < 0, then ORDER BY   | Check: 3 rows, first = -16000
query = """
SELECT account, region, 
actual - budget AS Neg_Variance 
FROM actuals_budget
WHERE actual - budget < 0 
ORDER BY  Neg_Variance ASC
"""

# denemeler 
query = """
SELECT month, account, SUM(actual) AS tl_actual, SUM(budget) AS tl_budget
FROM actuals_budget
GROUP BY month
"""

query = """
SELECT account, 
AVG(actual) AS avg_actual
FROM actuals_budget
GROUP BY account
"""
result = pd.read_sql_query(query, conn)
print(result)
conn.close()
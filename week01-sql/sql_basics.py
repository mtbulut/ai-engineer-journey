import sqlite3
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent.parent
csv_path = (BASE_DIR / "week01-pandas" / "actuals_budget.csv")
df = pd.read_csv(csv_path)
print(csv_path.exists())
print(df)
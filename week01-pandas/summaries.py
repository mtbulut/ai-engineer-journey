from pathlib import Path
import pandas as pd
BASE_DIR = Path(__file__).parent
path = BASE_DIR / "actuals_budget.csv"

df = pd.read_csv(path)
# df = pd.read_csv("actuals_budget.csv")  Bu sorun teskil eder.. cunku path olusturulmadi. 
print(df)





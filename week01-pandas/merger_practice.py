import pandas as pd
from pathlib import Path
import numpy as np

BASE_DIR = Path(__file__).parent
path_actuals = BASE_DIR/'actuals.csv'
path_budget = BASE_DIR/'budget.cssv'
print(path_actuals.exists())
print(path_budget.exists())

actuals = pd.read_csv(path_actuals)
budget = pd.read_csv(BASE_DIR/"budget.csv")
print(actuals)


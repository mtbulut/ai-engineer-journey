import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).parent
path_actuals = BASE_DIR/'actuals.csv'
path_budget = BASE_DIR/'budget.csv'
print(path_actuals.exists())
print(path_budget.exists())

actuals = pd.read_csv(path_actuals)
budget = pd.read_csv(BASE_DIR/"budget.csv")
# print(actuals)

merged_data = pd.merge(actuals, budget, on=['month', 'region', 'account'], how= 'outer')
merged_data = merged_data.fillna(0)



merged_data['variance'] = merged_data['actual'] - merged_data['budget']
# merged_data =abs(merged_data)
print(merged_data)


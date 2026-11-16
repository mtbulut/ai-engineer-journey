from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).parent

df = pd.read_csv(BASE_DIR / "actuals_budget.csv")

def varience(actual, budget):
    return actual - budget

print("Varinece sonucu:",varience( 10000, 8020))

def variance_prc(actual, budget):
    return round((actual - budget)/budget *100, 1)

print(variance_prc(80, 90))

def check_data(df):
    print("--- 1. ilk 5 satir ---")
    print(df.head())
    print()
    print("--- 2. Sutun bilgileri ---")
    print(df.info())
    print(" --- 3. Bosluk degerleri ---")
    print(df.isna().sum())
    print("--- 4. Tekrarlanan Satir ---")
    print(df.duplicated().sum())

def check_data(df):
    print('--- 5. Metin sutunlarindaki farkli degerler ---')
    for col in df.select_dtypes(include=["object", "string"]).columns:
        print(col, ":", df[col].unique())
    
check_data(df)

from pathlib import Path
import pandas as pd 

BASE_DIR = Path(__file__).parent
path = (BASE_DIR/"messy_sales.csv")
df = pd.read_csv(path)
print()
print(df)
print()
# print(path.exists())

# sutun tiplerive bos deger sayilari
df.info()

# 2. Her stunda kac bos deger var?
print(df.isna().sum())
print() 

# 3. Kaç tekrarlanan satır var?
print("Tekrarlanan satır:", df.duplicated().sum())
print()

# 4. Region ve account sütunlarında hangi farklı değerler var? Bu datanin ne kadar sikintili oldugunu gosterir.. Unique ile
print(df["region"].unique())
print(df["account"].unique())
print()
print(repr(df.loc[3, "region"]))    # → ' north'
print()
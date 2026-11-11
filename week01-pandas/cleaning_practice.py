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

print(df.head())
df.info()

# --- TEMİZLİK ---

# Region ve account: boşlukları sil, ilk harfi büyük yap
df["region"] = df["region"].str.strip().str.title()
df["account"] = df["account"].str.strip().str.title()

print(df["region"].unique())
print(df["account"].unique())

df['actual'] = df['actual'].str.replace(",","")
df['actual'] = pd.to_numeric(df["actual"], errors ="coerce")
df.info()
print(df)
print("Toplam actual:", df["actual"].sum())

print("toplam Actual", df["actual"].sum())

print("Once satir sayisi:", len(df))
df = df.drop_duplicates()
print("Sonra satir sayisi:", len(df))
print("Actual Toplam(iki kayit eksik):", df['actual'].sum())

# df['actual'] = df['actual']..replace(",","")

print(df)

# Eksik olanları işaretle, silme
df["data_status"] = df["actual"].isna().map({True: "MISSING", False: "OK"})

print(df)
print("Toplam actual (eksikler hariç):", df["actual"].sum())
print("Eksik kayıt sayısı:", (df["data_status"] == "MISSING").sum())
print()
df.to_csv(BASE_DIR / "clean_sales.csv", index=False)
import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent
THRESHOLD_PCT = 5

# =========================
def load_data(filename):
    return pd.read_csv(BASE_DIR/filename)

print()
def calculate_variance(df):
     df["variance"] = df["actual"] - df["budget"]
     df["variance_pct"] = (df["variance"] / df["budget"] * 100).round(1)
     df["variance_mult"] = df["variance"] * df["variance"]/100 
     return df

df = load_data("actuals_budget.csv") 
df = calculate_variance(df)  
print(df)      

#Revenue: Positive variance is good. Opex: negative variance is good. 

def add_favorable(df):
    df["favorable"] = np.where(
        df["account"] == "Revenue",
        df["variance"] >= 0,
        df["variance"] <=0
    )
    return df
df = add_favorable(df)
print(df)

print("------- check below 1----------")
def add_flag(df):

    df['flag'] = np.where((~df['favorable'] & (df['variance_pct'].abs()>5)),
                         "FLAG", 
                        ""
                          )

    return df

df = add_flag(df)
print(df)
print(" === 1_check the answer_1 =======")

# now CFP team 8 satirlik ozeti gormek istediklerini belirttiler ve Soru: Temmuzda North bolgesi toplamda nasillardi?

#  Her group ta kac flag var ona bakilmali.. 
df['is_flag'] = df['flag'] == 'FLAG'
print(df)

flag_count = df.groupby(['month','region'])[['actual','budget','variance','is_flag']].sum()
print(flag_count)

# simdi bunu ekledim. evet simdi bakalim.. 
# Sonuclari bir soyaya kaydet e geldik
df.to_csv(BASE_DIR /'variance_report.csv')
flag_count.to_csv(BASE_DIR / 'variance_summary.csv')

import pandas as pd
import numpy as np
from pathlib import Path

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

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


def add_flag(df):

    df['flag'] = np.where((~df['favorable'] & (df['variance_pct'].abs()>5)),
                         "FLAG", 
                        ""
                          )

    return df

df = add_flag(df)
print(df)


# now CFP team 8 satirlik ozeti gormek istediklerini belirttiler ve Soru: Temmuzda North bolgesi toplamda nasillardi?

#  Her group ta kac flag var ona bakilmali..
# 
def is_flag(df): 
    df['is_flag'] = df['flag'] == 'FLAG'
    return df
df = is_flag(df)
print(df)
print(" === 33333331_check the answer_1 =======")

def summrize(df):
    summary = df.groupby(['month','region'])[['actual','budget','variance','is_flag']].sum()
    return summary
summary = summrize(df)
print(summary)
print(" === 1_check the answer_1 =======")
# simdi bunu ekledim. evet simdi bakalim.. 
# Sonuclari bir soyaya kaydet e geldik
df.to_csv(BASE_DIR /'variance_report.csv')
df.to_csv(BASE_DIR / 'variance_summary.csv')

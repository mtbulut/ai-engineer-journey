import pandas as pd
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).parent
df = pd.read_csv(BASE_DIR / "actuals_budget.csv")
print(df)
print()

df["variance"] = df["actual"] - df["budget"]
df["variance_pct"] = (df["variance"] / df["budget"] * 100).round(1)


#Revenue: Positive varience is good. Opex: negative varience is good. 

df["favorable"] = np.where(
    df["account"] == "Revenue",
    df["variance"] >= 0,
    df["variance"] <=0
)
df['flag'] = np.where((~df['favorable'] & (df['variance_pct'].abs()>5)),
                      "FLAG", 
                      ""
                      )

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

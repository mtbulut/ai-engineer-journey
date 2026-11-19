import pandas as pd
import numpy as np

d = {"cal_1":[1, 2, 34, 12,22 ], "cal_2": [3,4, 0, 55, 22]}
df = pd.DataFrame(data=d)
print(df)
print(df.isna().sum())

# for s in "sss34343434": 
#     print(s)

# for n in [1,3,5,6]:
#     print(n)

# tuple (1,3,5,7) 
for t in (1,3,5,7): 
    print(t)

a = [3,5 ,6, 11]
a[-1]= 44
a[0] = 77
print(a)

for z in a:
    print(z)
# listenin sonuna ekleme yapiyor.. 
a.append(99)
a.append(444)
print(a)

tul = (34, 55, 37)
tul[0]

s = {3, 5, 7, 88, 23}
# for s in s:
#     print(s)
s.add(5)
print(s)
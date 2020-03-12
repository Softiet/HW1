import os
import sys

env_p = sys.prefix  # path to the env
"""print("Env. path: {}".format(env_p))
"""
new_p = ''
for extra_p in (r"Library\mingw-w64\bin",
    r"Library\usr\bin",
    r"Library\bin",
    r"Scripts",
    r"bin"):
    new_p +=  os.path.join(env_p, extra_p) + ';'

os.environ["PATH"] = new_p + os.environ["PATH"]  # set it for Python
os.putenv("PATH", os.environ["PATH"])  # push it at the OS level

import pandas as pd

df = pd.read_csv('./106061216.csv')

df = df.set_index("PRES")

try:
    df = df.drop(-99, axis=0)
except:
    None
try:
    df = df.drop(-999, axis=0)
except:
    None
df = df.reset_index()

target_list = ["C0A880","C0F9A0","C0G640","C0R190","C0X260"]
answer = []
    
for i in target_list:
    k = df[['PRES']].where(df[['station_id']].values == i).stack().mean()
    answer.append([i , None if k != k else k])

print(answer)
import pandas as pd

df = pd.read_excel("sample.xlsx")

for i, row in df.iterrows():
    assert row["金額"] >= 0, f"{i}行目 金額NG: {row['金額']}"

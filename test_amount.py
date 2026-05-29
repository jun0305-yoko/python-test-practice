import pandas as pd

def test_amount():
    df = pd.read_excel("sample.xlsx")

    for i, row in df.iterrows():
        assert row["金額"] >= 0

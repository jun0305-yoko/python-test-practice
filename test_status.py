import pandas as pd

def test_status():
    df = pd.read_excel("sample.xlsx")

    for i, row in df.iterrows():
        assert row["ステータス"] in ["active", "inactive"]

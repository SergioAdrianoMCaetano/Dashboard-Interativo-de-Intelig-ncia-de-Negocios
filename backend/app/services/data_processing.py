import pandas as pd

def load_real_estate_data():
    df = pd.read_csv("data/real_estate.csv", sep="\t", parse_dates=["date"])

    df["Valor (R$)"] = (
        df["Valor (R$)"]
            .str.replace("R$", "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .astype(float)
    )

    return df

import pandas as pd

def load_real_estate_data():
    try:
        df = pd.read_csv("data/real_estate.csv", encoding="utf-8")
        df.columns = df.columns.str.strip()

        if "Valor (R$)" not in df.columns:
            raise ValueError("Coluna 'Valor (R$)' não encontrada no CSV")

        df["Valor (R$)"] = (
            df["Valor (R$)"]
            .str.replace("R$", "", regex=False)
            .str.replace(".", "", regex=False)
            .str.replace(",", ".", regex=False)
            .astype(float)
        )

        return df
    except Exception as e:
        print("Erro ao carregar dados:", e)
        raise

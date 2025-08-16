from fastapi import APIRouter, Query
import pandas as pd

router = APIRouter()

@router.get("/kpis")
def get_kpis(start: str = Query(None), end: str = Query(None)):
    df = pd.read_csv("data/sales_data.csv", parse_dates=["date"])

    if start:
        df = df[df["date"] >= pd.to_datetime(start)]
    if end:
        df = df[df["date"] <= pd.to_datetime(end)]

    receita_total = df["revenue"].sum()
    produtos_vendidos = len(df)
    ticket_medio = receita_total / produtos_vendidos if produtos_vendidos else 0

    return {"receita_total": f"R$ {receita_total:, .2f}", "produtos_vendidos": produtos_vendidos, "ticket_medio": f"R$ {ticket_medio:,.2f}"}

# Este arquivo faz parte da API de backend do painel de vendas para KPIs.
# Ele define um endpoint para recuperar indicadores-chave de desempenho (KPIs), como receita total,
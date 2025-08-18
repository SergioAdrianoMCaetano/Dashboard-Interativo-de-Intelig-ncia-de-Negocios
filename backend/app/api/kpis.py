from fastapi import APIRouter, Query
from app.services.data_processing import load_real_estate_data
import pandas as pd

router = APIRouter()

@router.get("/kpis")
def get_kpis_from_real_estate():
    df = load_real_estate_data()
    total_valor = df["Valor (R$)"].sum()
    total_imoveis = len(df)
    valor_medio = total_valor / total_imoveis if total_imoveis > 0 else 0

    return {"valor_total": f"R$ {total_valor:,.2f}",
            "total_imoveis": total_imoveis,
            "valor_medio": f"R$ {valor_medio:,.2f}"}

# Este arquivo faz parte da API de backend do painel de vendas para KPIs.
# Ele define um endpoint para recuperar indicadores-chave de desempenho (KPIs), como receita total,
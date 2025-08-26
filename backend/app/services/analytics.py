import pandas as pd
from fastapi.responses import JSONResponse
from app.services.data_processing import load_real_estate_data

# Gráfico de valor médio por localização
def generate_sales_chart():
    df = load_real_estate_data()
    grouped = df.groupby("Localização", as_index=False)["Valor (R$)"].mean()

    data = [
        {
            "x": grouped["Localização"].tolist(),
            "y": grouped["Valor (R$)"].tolist(),
            "type": "bar",
            "name": "Valor Médio por Localização",
            "marker": {"color": "rgb(102, 197, 204)"}
        }
    ]

    layout = {
        "title": "Valor Médio por Localização",
        "xaxis": {"title": "Localização"},
        "yaxis": {"title": "Valor Médio (R$)"}
    }

    return JSONResponse(content={"data": data, "layout": layout})


# Gráfico filtrado por tipo, preço, região e quartos
def generate_filtered_chart(property_type=None, min_price=None, max_price=None, region=None, bedrooms=None):
    df = load_real_estate_data()

    if property_type:
        df = df[df["Tipo"] == property_type]
    if min_price:
        df = df[df["Valor (R$)"] >= min_price]
    if max_price:
        df = df[df["Valor (R$)"] <= max_price]
    if region:
        df = df[df["Localização"] == region]
    if bedrooms:
        df = df[df["Quartos"] == bedrooms]

    grouped = df.groupby("Localização", as_index=False)["Valor (R$)"].mean()

    data = [
        {
            "x": grouped["Localização"].tolist(),
            "y": grouped["Valor (R$)"].tolist(),
            "type": "bar",
            "name": "Valor Médio Filtrado",
            "marker": {"color": "rgb(255, 127, 14)"}
        }
    ]

    layout = {
        "title": "Valor Médio por Localização (Filtrado)",
        "xaxis": {"title": "Localização"},
        "yaxis": {"title": "Valor Médio (R$)"}
    }

    return JSONResponse(content={"data": data, "layout": layout})


# Gráfico comparativo por região
def generate_region_comparison_chart():
    df = load_real_estate_data()
    grouped = df.groupby("Localização", as_index=False)["Valor (R$)"].mean()

    data = [
        {
            "x": grouped["Localização"].tolist(),
            "y": grouped["Valor (R$)"].tolist(),
            "type": "bar",
            "name": "Comparação por Região",
            "marker": {"color": "rgb(44, 160, 44)"}
        }
    ]

    layout = {
        "title": "Comparação de Valor Médio por Região",
        "xaxis": {"title": "Localização"},
        "yaxis": {"title": "Valor Médio (R$)"}
    }

    return JSONResponse(content={"data": data, "layout": layout})


# Gráfico por número de quartos
def generate_bedroom_price_chart():
    df = load_real_estate_data()
    grouped = df.groupby("Quartos", as_index=False)["Valor (R$)"].mean()

    data = [
        {
            "x": grouped["Quartos"].tolist(),
            "y": grouped["Valor (R$)"].tolist(),
            "type": "bar",
            "name": "Valor Médio por Quartos",
            "marker": {"color": "rgb(214, 39, 40)"}
        }
    ]

    layout = {
        "title": "Valor Médio por Número de Quartos",
        "xaxis": {"title": "Quartos"},
        "yaxis": {"title": "Valor Médio (R$)"}
    }

    return JSONResponse(content={"data": data, "layout": layout})

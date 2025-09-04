from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.charts import router as charts_router
from app.api.kpis import router as kpis_router
from fastapi.responses import HTMLResponse
from app.services.data_processing import load_real_estate_data
import pandas as pd
import os

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    return "<h1>API do Dashboard de Vendas</h1><p>Use <code>/docs</code> para acessar a documentação.</p>"

@app.get("/api/data")
def get_real_estate_data():
    df = load_real_estate_data()
    return df.to_dict(orient="records")


#Libera acesso do frontend
app.add_middleware(CORSMiddleware, allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(charts_router, prefix="/api")
app.include_router(kpis_router, prefix="/api")
# Este arquivo é o ponto de entrada da API FastAPI para o painel de vendas.

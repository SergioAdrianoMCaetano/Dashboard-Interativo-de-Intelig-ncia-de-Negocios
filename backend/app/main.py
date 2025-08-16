from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.charts import router as charts_router
from app.api.kpis import router as kpis_router

app = FastAPI()

#Libera acesso do frontend
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

app.include_router(charts_router)
app.include_router(kpis_router)
# Este arquivo é o ponto de entrada da API FastAPI para o painel de vendas.

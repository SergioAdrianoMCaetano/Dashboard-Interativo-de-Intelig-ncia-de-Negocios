from fastapi import APIRouter
from app.services.analytics import generate_sales_chart
import json

#Prefixo para todas as rotas deste arquivo
router = APIRouter(prefix="/api")

@router.get("/chart")
def get_chart():
    #Retorna um JSON sting
    chart_data = generate_sales_chart()
    return chart_data
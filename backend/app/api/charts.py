from fastapi import APIRouter
from app.services.analytics import generate_sales_chart 
from app.services.analytics import generate_filtered_chart
from app.services.analytics import generate_region_comparison_chart
import json

#Prefixo para todas as rotas deste arquivo
router = APIRouter(prefix="/api")

@router.get("/chart")
def get_chart():
    #Retorna um JSON string
    chart_data = generate_sales_chart()
    return chart_data

@router.get("/chart/filter")
def get_filtered_chart(property_type: str = None, min_price: float = None, max_price: float = None, region: str = None):
    chart_data = generate_filtered_chart(property_type, min_price, max_price, region)
    return chart_data

@router.get("/chart/region-comparison")
def get_region_comparison_chart():
    chart_data = generate_region_comparison_chart()
    return chart_data
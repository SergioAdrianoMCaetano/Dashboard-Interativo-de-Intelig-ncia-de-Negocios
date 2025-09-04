from fastapi import APIRouter
from app.services.analytics import (
    generate_sales_chart,
    generate_filtered_chart,
    generate_region_comparison_chart,
    generate_bedroom_price_chart
)
import pandas as pd

router = APIRouter()

@router.get("/data")
def get_raw_data():
    df = pd.read_csv("backend/data/real_estate.csv")
    return df.to_dict(orient="records")

@router.get("/chart")
def get_chart():
    print("Chamando o endpoint /chart")
    return generate_sales_chart()

@router.get("/chart/filter")
def get_filtered_chart(property_type: str = None, min_price: float = None, max_price: float = None, region: str = None, bedrooms: int = None):
    print("Chamando o endpoint /chart/filter")
    return generate_filtered_chart(property_type, min_price, max_price, region, bedrooms)

@router.get("/chart/region-comparison")
def get_region_comparison_chart():
    print("Chamando o endpoint /chart/region-comparison")
    return generate_region_comparison_chart()

@router.get("/chart/bedrooms")
def get_bedroom_price_chart():
    print("Chamando o endpoint /chart/bedrooms")
    return generate_bedroom_price_chart()

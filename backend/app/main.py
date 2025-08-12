from fastapi import FastAPI
from app.api import charts

app = FastAPI()
app.include_router(charts.router)

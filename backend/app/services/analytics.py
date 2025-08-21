import pandas as pd
import plotly.express as px
import json
from app.services.data_processing import load_real_estate_data

#Carrega e limpa os dados de vendas
def generate_sales_chart():
    df = load_real_estate_data()
    grouped = df.groupby("Localização", as_index=False)["Valor (R$)"].mean()

    fig = px.bar(grouped,x="Localização", y="Valor (R$)", title="Valor Médio por Localização", color="Localização", labels={"Valor (R$)": "Valor Médio (R$)"})

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', xaxis_title="Localização", yaxis_title="Valor Médio (R$)", font=dict(family="Arial", size=12, color="#333"), xaxis=dict(tickangle=-45), margin=dict(l=50, r=50, t=80, b=150), hovermode="x unified")

    fig.update_traces(marker_color=px.colors.qualitative.Pastel, marker_line_color="#333", marker_line_width=1.5, opacity=0.9)

    return json.loads(fig.to_json())

#Aplica os filtros no "real_estate.csv" antes de gerar o gráfico
def generate_filtered_chart(property_type=None, min_price=None, max_price=None, region=None, bedrooms=None):
    df = load_real_estate_data()

    #Aplicar filtros
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

    #Gerar Gráfico
    fig = px.histogram(df, x="Valor (R$)", color="Localização", title="Distribuição de Valores dos Imóveis")

    return json.loads(fig.to_json())


#Gráficos Comparativos entre Regiões
def generate_region_comparison_chart():
    df = load_real_estate_data()
    grouped = df.groupby("Localização", as_index=False)["Valor (R$)"].mean()

    fig = px.bar(grouped, x="Localização", y="Valor (R$)", title="Comparação de Valores por Região", color="Localização", labels={"Valor": "Valor Médio"})
    
    return json.loads(fig.to_json())

#Grafico por número de quartos
def generate_bedroom_price_chart():
    df = load_real_estate_data()
    
    fig = px.box(df, x="Quartos", y="Valor (R$)", title="Distribuição de Preços por Número de Quartos", labels={"Quartos": "Número de Quartos", "Valor (R$)": "Valor do Imóvel"}, color="Quartos")

    fig.update_layout(plot_bgcolor='rgba(0, 0, 0, 0)', paper_bgcolor='rgba(0, 0, 0, 0)', font=dict(family="Arial", size=12, color="#333"), margin=dict(l=50, r=50, t=80, b=150), hovermode="x unified")

    return json.loads(fig.to_json())

    ################################################################################################################################################ 
#     # #Gráfico de barras 
# df = load_real_estate_data()

# fig = px.bar(df.groupby("Localização", as_index=False)["Valor (R$)"].mean(),x="Localização", y="Valor (R$)", title="Valor Médio por Localiação", color="Localização", labels={"Valor (R$)" : "Valor Médio (R$)"}) 
    
# #     # Controle do Layout do Gráfico 
# #     # Fundo transparente f
# fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0, 0, 0, 0)', xaxis_title="Localização", yaxis_title="Valor Médio (R$)",font=dict(family="Arial", size=12,color='#333'), xaxis=dict(tickangle=-45), margin=dict(l=50, r=50, t=80, b=150), hovermode="x unified") 
    
#     # --- PERSONALIZAÇÃO DE CORES --- # 
#     # Opção A: Paleta pré-definida (ex: 'Viridis', 'Plasma', 'Inferno') 
#     fig.update_traces(marker_color=px.colors.qualitative.Pastel, marker_line_color='#333', marker_line_width=1.5, opacity=0.9) 
    
#     # Opção B: Cores manuais (lista de HEX/RGB) 
#     # fig.update_traces(marker_color=['#4CAF50', '#2196F3', '#FF5722', '#9C27B0']) 
    
#     # # Opção C: Mapear cores por categoria (usando color_discrete_map) 
#     # fig.update_traces( # marker_color=[px.colors.qualitative.Pastel[i] for i in range(len(df['Localização'].unique())) # ) 
#     # 

#     # --- SALVAR O GRÁFICO --- 
#     # # Salva como HTML (interativo) 
# fig.write_html("grafico_valor_medio.html") 
    
#     # Convertendo para dict ao invés de string JSON 
#     return json.loads(fig.to_json()) 

# # Salva como imagem (PNG/JPEG - requer kaleido) 
# # --- SALVAR O GRÁFICO --- 
# # Salva como HTML (interativo) 
# #fig.write_html("grafico_valor_medio.html") 
# # # Convertendo para dict ao invés de string JSON 
# # return json.loads(fig.to_json())
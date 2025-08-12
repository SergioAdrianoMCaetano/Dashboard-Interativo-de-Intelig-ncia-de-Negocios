import pandas as pd
import plotly.express as px
import json

#Carrega e limpa os dados de vendas
def generate_sales_chart():
    df = pd.read_csv("data/sales_data.csv")
    df['Valor (R$)'] = df['Valor (R$)'].str.replace('R$', '').str.replace('.', '').str.replace(',', '.').astype(float)

#Gráfico de barras
    fig = px.bar(df.groupby('Localização', as_index=False)['Valor (R$)'].mean(),x='Localização', y='Valor (R$)', title='Valor Médio por Localiação', color='Localização', labels={'Valor (R$)' : 'Valor Médio (R$)'})

# Controle do Layout do Gráfico    
    # Fundo transparente
    fig.update_layout(plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0, 0, 0, 0)', xaxis_title="Localização", yaxis_title="Valor Médio (R$)",font=dict(family="Arial", size=12,color="#333"), xaxis=dict(tickangle=-45), margin=dict(l=50, r=50, t=80, b=150), hovermode="x unified")
    
    # --- PERSONALIZAÇÃO DE CORES ---
    # Opção A: Paleta pré-definida (ex: 'Viridis', 'Plasma', 'Inferno')
    fig.update_traces(marker_color=px.colors.qualitative.Pastel, marker_line_color='#333', marker_line_width=1.5, opacity=0.9)

    # Opção B: Cores manuais (lista de HEX/RGB)
    # fig.update_traces(marker_color=['#4CAF50', '#2196F3', '#FF5722', '#9C27B0'])

    # Opção C: Mapear cores por categoria (usando color_discrete_map)
    # fig.update_traces(
    #     marker_color=[px.colors.qualitative.Pastel[i] for i in range(len(df['Localização'].unique()))
    # )

    # --- SALVAR O GRÁFICO ---
    # Salva como HTML (interativo)
    fig.write_html("grafico_valor_medio.html")

    # Salva como imagem (PNG/JPEG - requer kaleido)
    # fig.write_image("grafico_valor_medio.png", engine="kaleido")

    # Convertendo para dict ao invés de string JSON
    return json.loads(fig.to_json())
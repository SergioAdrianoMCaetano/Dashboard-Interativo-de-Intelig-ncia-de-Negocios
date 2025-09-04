🏠 Dashboard Imobiliário - Análise de Mercado em Tempo Real









Uma plataforma completa de business intelligence para análise do mercado imobiliário, proporcionando insights visuais e ferramentas de filtragem avançada para corretores, investidores e gestores.

✨ Funcionalidades

📊 Visualizações Interativas

- Mapa de Calor Geográfico: Distribuição espacial dos imóveis com tooltips informativos
- Gráfico de Barras: Distribuição de imóveis por localização
- Gráfico de Pizza: Proporção por tipo de imóvel (Apartamento, Casa, Loja, Sala)
- KPIs Dinâmicos: Valor total, quantidade e valor médio em tempo real

🔍 Sistema de Filtros Avançados

- Localização: Busca por bairro/região
- Tipo de Imóvel: Filtro por categoria
- Quartos: Filtro numérico específico
- Valor Máximo: Filtro por faixa de preço
- Filtros Combinados: Aplicação simultânea de múltiplos critérios

📤 Exportação de Dados

- Download em CSV dos dados filtrados
- Relatórios personalizáveis para apresentações
- Compatibilidade com Excel e outras ferramentas

🛠️ Stack Tecnológica

Frontend

- React 18 com Hooks
- Plotly.js para visualizações gráficas
- React-Leaflet para mapas interativos
- Styled Components para estilização
- Vite para build e desenvolvimento

Backend

- FastAPI para API RESTful
- Pandas para processamento de dados
- Python 3.11+ para lógica de negócio
- Uvicorn como servidor ASGI

🚀 Como Executar

Pré-requisitos

- Node.js 18+
- Python 3.11+
- pip ou poetry

Instalação e Execução

Backend

    cd backend
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    # ou venv\Scripts\activate  # Windows
    
    pip install -r requirements.txt
    uvicorn main:app --reload --port 8000

Frontend

    cd frontend
    npm install
    npm run dev

Variáveis de Ambiente

Crie um arquivo .env na pasta frontend:

    VITE_API_URL=http://localhost:8000

📁 Estrutura do Projeto

    imobiliaria-dashboard/
    ├── backend/
    │   ├── main.py                 # Aplicação FastAPI
    │   ├── services/
    │   │   ├── data_processing.py  # Processamento de dados
    │   │   └── analytics.py        # Geração de gráficos
    │   ├── api/
    │   │   ├── charts.py           # Rotas de gráficos
    │   │   └── kpis.py             # Rotas de KPIs
    │   └── data/
    │       └── real_estate.csv     # Dados de exemplo
    ├── frontend/
    │   ├── src/
    │   │   ├── components/
    │   │   │   ├── HeatMap/        # Mapa de calor
    │   │   │   ├── PieChart/       # Gráfico de pizza
    │   │   │   ├── ExportButton/   # Botão de exportação
    │   │   │   └── PropertyFilter/ # Componente de filtros
    │   │   ├── utils/
    │   │   │   └── geoData.js      # Coordenadas geográficas
    │   │   └── Dashboard.jsx       # Componente principal
    │   └── package.json
    └── README.md

🎯 Exemplos de Uso

Caso 1: Análise por Localização

    // Filtro: Asa Sul - Apartamentos - 2 quartos - até R$ 850.000
    {
      location: "Asa Sul",
      type: "Apartamento", 
      bedrooms: "2",
      amount: "850000"
    }

Caso 2: Identificação de Oportunidades

    // Filtro: Taguatinga - Casas - 3+ quartos - até R$ 600.000
    {
      location: "Taguatinga",
      type: "Casa",
      bedrooms: "3", 
      amount: "600000"
    }

🔧 API Endpoints

GET /api/data

Retorna todos os dados de imóveis em formato JSON

    [
      {
        "Localização": "Asa Sul",
        "Tipo": "Apartamento",
        "Quartos": 2,
        "Valor (R$)": 850000.00,
        "latitude": -15.8306,
        "longitude": -47.9132
      }
    ]

GET /api/chart

Retorna dados para gráficos de distribuição

GET /api/kpis

Retorna indicadores-chave de performance

📈 Estrutura de Dados

Arquivo CSV de Entrada

    Localização,Tipo,Quartos,Valor (R$)
    Asa Sul,Apartamento,2,R$ 850.000,00
    Taguatinga,Casa,3,R$ 550.000,00

Dados Processados

    {
      Localização: "asa sul",
      Tipo: "apartamento", 
      Quartos: 2,
      valor: 850000.00,
      latitude: -15.8306,
      longitude: -47.9132
    }

🎨 Personalização

Adicionar Novas Localizações

Edite src/utils/geoData.js:

    export const bairrosGeo = {
      "nova-localizacao": { 
        lat: -15.0000, 
        lng: -47.0000 
      }
    };

Modificar Estilos

Os componentes utilizam Styled Components para fácil customização:

    const CustomChart = styled(Plot)`
      background-color: #your-color;
      border-radius: 8px;
    `;

🤝 Contribuição

1. Faça o fork do projeto
2. Crie uma branch para sua feature (git checkout -b feature/AmazingFeature)
3. Commit suas mudanças (git commit -m 'Add some AmazingFeature')
4. Push para a branch (git push origin feature/AmazingFeature)
5. Abra um Pull Request

📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para detalhes.

🏆 Próximas Melhorias

- [ ] Autenticação de usuários
- [ ] Dashboard responsivo para mobile
- [ ] Integração com APIs imobiliárias reais
- [ ] Sistema de favoritos e comparações
- [ ] Relatórios PDF automatizados
- [ ] Modo escuro/claro

📞 Contato

Desenvolvido por [Sérgio Adriano] - [sergioadrianomc@gmail.com]





---

⭐️ Se este projeto foi útil, deixe uma estrela no GitHub!

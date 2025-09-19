import jwt
from datetime import datetime, timedelta
from typing import Dict, Any, Optional
import os
from dotenv import load_dotenv

load_dotenv()

#Configurações (em produção, use variáveis de ambiente)
SECRET_KEY = os.getenv
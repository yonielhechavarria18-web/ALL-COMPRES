"""
CONFIGURACIÓN DEL BOT
Rellena estos valores directamente aquí antes de subir el proyecto a GitHub.

Obtén API_ID y API_HASH en https://my.telegram.org
Obtén BOT_TOKEN hablando con @BotFather.
OWNER_ID es tu ID numérico de Telegram.
"""

from pathlib import Path

# Credenciales de Telegram
API_ID = 20446108                # Reemplaza por tu API ID numérico
API_HASH = "025f6661faa3e16c1461f8aa4f4f94ce"
BOT_TOKEN = "9057540007:AAGXGrLJhm2iM3FjEq_heuR_zlZcZeseCIE"
OWNER_ID = 7133137250             # Reemplaza por tu ID numérico de Telegram

# Opcional: ID o username del canal usado por el bot para almacenar/reenviar.
# Déjalo vacío si no utilizas esa función.
DATABASE_CHANNEL_ID = ""

# Carpeta de datos del bot.
# Render usa almacenamiento efímero por defecto. Para conservar los JSON,
# añade un Persistent Disk montado en /var/data y cambia esta ruta a "/var/data".
DATA_DIR = Path("./data")

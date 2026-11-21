# Video Compressor Telegram Bot — Render Web Service

## 1. Configurar el bot
Abre `config.py` y rellena:
- `API_ID`
- `API_HASH`
- `BOT_TOKEN`
- `OWNER_ID`

`DATABASE_CHANNEL_ID` es opcional. No es necesario configurar variables secretas en el panel Environment de Render.

## 2. Desplegar
1. Sube el contenido de esta carpeta a la raíz de un repositorio de GitHub.
2. En Render selecciona **New + → Web Service**.
3. Conecta el repositorio y selecciona **Docker**.
4. Dockerfile Path: `./Dockerfile`; Docker Context: `.`.
5. Render utilizará automáticamente el puerto asignado mediante `PORT`.

También puedes crear el servicio como Blueprint usando `render.yaml`.

## 3. Archivos mínimos
- `main.py`: bot Pyrogram y servidor HTTP para Render.
- `config.py`: credenciales y configuración.
- `Dockerfile`: Python y FFmpeg.
- `requirements.txt`: dependencias Python.
- `render.yaml`: definición del Web Service.

Los JSON de estado se crean automáticamente al ejecutarse el bot.

## 4. Persistencia
Render puede borrar los archivos locales al reemplazar el contenedor. Para conservar los JSON:
1. Añade un Persistent Disk al Web Service con punto de montaje `/var/data`.
2. En `config.py`, cambia `DATA_DIR = Path("./data")` por `DATA_DIR = Path("/var/data")`.

## 5. Seguridad
`config.py` contiene el token y las claves. No publiques el repositorio como público mientras tenga credenciales reales. Si ya publicaste un token, revócalo con @BotFather y genera otro.

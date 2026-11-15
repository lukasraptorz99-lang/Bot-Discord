# Usamos una imagen oficial de Python ligera
FROM python:3.10-slim

# Instalamos las dependencias del sistema operativo, incluyendo la librería libopus para la voz
RUN apt-get update && apt-get install -y \
    libopus0 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Creamos y nos movemos a la carpeta de trabajo
WORKDIR /app

# Copiamos e instalamos los requerimientos de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código del bot
COPY . .

# Comando para arrancar el bot (Railway lee el puerto automáticamente)
CMD ["python", "Bot.py"]

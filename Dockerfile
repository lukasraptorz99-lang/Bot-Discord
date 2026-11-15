FROM python:3.10-slim

# Instalar dependencias del sistema necesarias para audio y PyNaCl
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libopus0 \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar archivos del proyecto
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "Bot.py"]
#Comentario Nuevo :D

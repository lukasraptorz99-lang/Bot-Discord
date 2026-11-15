FROM python:3.10-slim

# Instalar dependencias del sistema y herramientas de compilación para PyNaCl y audio
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libopus0 \
    build-essential \
    libffi-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del bot
COPY . .

# Comando de ejecución
CMD ["python", "Bot.py"]

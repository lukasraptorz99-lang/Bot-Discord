FROM python:3.10-slim

# Instalar dependencias del sistema y PyNaCl directamente desde los paquetes de Debian (evita errores de compilación)
RUN apt-get update && apt-get install -y \
    ffmpeg \
    libopus0 \
    python3-pynacl \
    build-essential \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "Bot.py"]

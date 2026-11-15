import discord
import asyncio
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

print(">>> [INICIO] El script se está ejecutando correctamente...")

# --- Mini servidor web invisible para Render ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_web_server():
    port = int(os.getenv("PORT", 10000))
    print(f">>> [WEB] Iniciando servidor web en el puerto {port}...")
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

# Lanzamos el servidor web en segundo plano
threading.Thread(target=run_web_server, daemon=True).start()

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

client = discord.Client(intents=intents)
CANAL_VOZ_ID = 1546286007308255239

@client.event
async def on_ready():
    print(f'>>> [DISCORD] ¡Sesión iniciada con éxito como {client.user}!')
    await asyncio.sleep(3)
    try:
        print(f'>>> [VOZ] Buscando canal ID: {CANAL_VOZ_ID}...')
        channel = await client.fetch_channel(CANAL_VOZ_ID)
        if channel:
            print(f'>>> [VOZ] ¡Canal encontrado ({channel.name})! Conectando...')
            await channel.connect()
            print('>>> [VOZ] ¡ÉXITO! El bot ya entró al canal de voz.')
        else:
            print('>>> [VOZ] Error: No se encontró el canal.')
    except Exception as e:
        print(f'>>> [ERROR CRÍTICO] {e}')

token = os.getenv("DISCORD_TOKEN")
if not token:
    print(">>> [ERROR] Falta la variable DISCORD_TOKEN en Render.")
else:
    print(">>> [DISCORD] Conectando a la pasarela de Discord...")
    client.run(token)
    

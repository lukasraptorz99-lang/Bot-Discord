import discord
import asyncio
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- Mini servidor web invisible para que Render no apague el bot ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_web_server():
    port = int(os.getenv("PORT", 10000))
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()
# -------------------------------------------------------------------

intents = discord.Intents.all()
client = discord.Client(intents=intents)

CANAL_VOZ_ID = 1546286007308255239

@client.event
async def on_connect():
    print(">>> [CONECTADO] El bot ha establecido conexión con los servidores de Discord.")

@client.event
async def on_ready():
    print(f'>>> [LISTO] Sesión iniciada como {client.user.name}')
    try:
        print(f'>>> Buscando canal ID: {CANAL_VOZ_ID}...')
        channel = await client.fetch_channel(CANAL_VOZ_ID)
        if channel:
            print(f'>>> ¡Canal encontrado: {channel.name}! Conectando a voz...')
            await channel.connect()
            print('>>> ¡ÉXITO! El bot ya está en el canal de voz.')
        else:
            print('>>> Error: No se encontró el canal.')
    except Exception as e:
        print(f'>>> ERROR AL CONECTAR A VOZ: {e}')

token = os.getenv("DISCORD_TOKEN")
if not token:
    print(">>> ERROR: No se encontró la variable de entorno DISCORD_TOKEN.")
else:
    client.run(token)
    

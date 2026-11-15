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

# Usamos intents por defecto para evitar el error de privilegios
intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

client = discord.Client(intents=intents)
CANAL_VOZ_ID = 1546286007308255239

@client.event
async def on_ready():
    print(f'>>> [LISTO] Conectado como {client.user}')
    await asyncio.sleep(3)
    try:
        print(f'>>> Buscando canal de voz...')
        channel = await client.fetch_channel(CANAL_VOZ_ID)
        if channel:
            print(f'>>> ¡Canal encontrado ({channel.name})! Entrando a voz...')
            await channel.connect()
            print('>>> ¡ÉXITO TOTAL! El bot ya está dentro del canal.')
        else:
            print('>>> Error: Canal no encontrado.')
    except Exception as e:
        print(f'>>> ERROR AL CONECTAR A VOZ: {e}')

client.run(os.getenv("DISCORD_TOKEN"))


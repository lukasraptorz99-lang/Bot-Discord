import discord
import asyncio
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- Mini servidor web falso para mantener vivo a Fly.io ---
class DummyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_server():
    server_address = ('0.0.0.0', 8080)
    httpd = HTTPServer(server_address, DummyHandler)
    httpd.serve_forever()

# Arrancamos el servidor web en un hilo separado
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()
print(">>> [WEB] Servidor dummy activo en el puerto 8080", flush=True)

# --- Configuración del Bot de Discord ---
intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

client = discord.Client(intents=intents)
CANAL_VOZ_ID = 1546286007308255239

@client.event
async def on_ready():
    print(f'>>> [DISCORD] ¡Sesión iniciada con éxito como {client.user}', flush=True)
    await asyncio.sleep(3)
    try:
        print(f'>>> [VOZ] Buscando canal ID: {CANAL_VOZ_ID}...', flush=True)
        channel = await client.fetch_channel(CANAL_VOZ_ID)
        if channel:
            print(f'>>> [VOZ] ¡Canal encontrado ({channel.name})! Conectando...', flush=True)
            await channel.connect()
            print(f'>>> [VOZ] ¡ÉXITO! El bot ya entró al canal de voz.', flush=True)
        else:
            print(f'>>> [VOZ] Error: No se encontró el canal.', flush=True)
    except Exception as e:
        print(f'>>> [ERROR CRÍTICO] {e}', flush=True)

token = os.getenv("DISCORD_TOKEN")
if not token:
    print(">>> [ERROR] Falta la variable DISCORD_TOKEN.", flush=True)
else:
    print(">>> [DISCORD] Conectando a la pasarela de Discord...", flush=True)
    client.run(token)
    

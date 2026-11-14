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

# Arrancamos el servidor web en segundo plano
threading.Thread(target=run_web_server, daemon=True).start()
# -------------------------------------------------------------------

# Configuramos los intents básicos
intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

client = discord.Client(intents=intents)

CANAL_VOZ_ID = 1546286007308255238

@client.event
async def on_ready():
    print(f'¡Conectado con éxito como {client.user}!')
    
    # Esperamos unos segundos a que carguen los canales
    await asyncio.sleep(5)
    
    # Búsqueda del canal de voz
    for guild in client.guilds:
        found_channel = guild.get_channel(CANAL_VOZ_ID)
        if found_channel:
            try:
                await found_channel.connect()
                print(f'¡Éxito! El bot ya entró al canal de voz: {found_channel.name}')
                return
            except Exception as e:
                print(f'Error al conectar: {e}')
    
    print('No se pudo encontrar el canal de voz. Revisa el ID.')

client.run(os.getenv("DISCORD_TOKEN"))

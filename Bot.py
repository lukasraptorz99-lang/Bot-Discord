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

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

client = discord.Client(intents=intents)
CANAL_VOZ_ID = 1546286007308255239

@client.event
async def on_ready():
    print(f'--> ¡Sesión iniciada correctamente como {client.user}!')
    print('--> Intentando conectar al canal de voz inmediatamente...')
    
    # Esperamos 3 segunditos para asegurar estabilidad de la red
    await asyncio.sleep(3)
    
    try:
        channel = await client.fetch_channel(CANAL_VOZ_ID)
        if channel:
            print(f'--> ¡Canal encontrado: {channel.name}! Entrando...')
            await channel.connect()
            print('--> ¡ÉXITO TOTAL! El bot ya está en el canal de voz.')
        else:
            print('--> Error: El canal devolvió None.')
    except Exception as e:
        print(f'--> ERROR CRÍTICO al conectar a la voz: {e}')

client.run(os.getenv("DISCORD_TOKEN"))

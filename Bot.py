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

async def join_voice_channel():
    await client.wait_until_ready()
    print("El bot está listo, buscando canal de voz directamente en la API...")
    
    while not client.is_closed():
        try:
            # Verificamos si ya está conectado a algún canal de voz
            if client.voice_clients:
                for vc in client.voice_clients:
                    if vc.channel.id == CANAL_VOZ_ID and vc.is_connected():
                        print("El bot ya se encuentra en el canal de voz correctamente.")
                        await asyncio.sleep(30)
                        continue

            # Buscamos el canal directamente usando la API (ignorando la memoria caché)
            channel = await client.fetch_channel(CANAL_VOZ_ID)
            
            if channel:
                print(f"Canal encontrado: {channel.name}. Intentando conectar...")
                # Si ya hay otra conexión fantasma, la cerramos primero
                for vc in client.voice_clients:
                    await vc.disconnect()
                
                await channel.connect()
                print(f'¡ÉXITO TOTAL! El bot se ha metido al canal de voz: {channel.name}')
            else:
                print('No se pudo encontrar el canal.')
                
        except Exception as e:
            print(f'Error al intentar conectar a la voz: {e}')
        
        # Espera 30 segundos antes de reintentar o verificar estado
        await asyncio.sleep(30)

@client.event
async def on_ready():
    print(f'Sesión iniciada como {client.user}')
    client.loop.create_task(join_voice_channel())

client.run(os.getenv("DISCORD_TOKEN")

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
    print("El bot está completamente listo, buscando canal de voz...")
    while not client.is_closed():
        channel = client.get_channel(CANAL_VOZ_ID)
        if channel:
            try:
                if not client.voice_clients:
                    await channel.connect()
                    print(f'¡ÉXITO TOTAL! Conectado al canal: {channel.name}')
                else:
                    print('Ya está conectado a un canal de voz.')
            except Exception as e:
                print(f'Error al intentar conectar a la voz: {e}')
        else:
            print('Buscando el canal en los servidores del bot...')
            for guild in client.guilds:
                g_channel = guild.get_channel(CANAL_VOZ_ID)
                if g_channel:
                    try:
                        await g_channel.connect()
                        print(f'¡ÉXITO en servidor {guild.name}! Conectado a: {g_channel.name}')
                    except Exception as e:
                        print(f'Error en bucle secundario: {e}')
        
        # Espera 30 segundos antes de volver a comprobar
        await asyncio.sleep(30)

@client.event
async def on_ready():
    print(f'Sesión iniciada como {client.user}')
    client.loop.create_task(join_voice_channel())

client.run(os.getenv("DISCORD_TOKEN"))
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
    print("El bot está completamente listo, buscando canal de voz...")
    while not client.is_closed():
        channel = client.get_channel(CANAL_VOZ_ID)
        if channel:
            try:
                if not client.voice_clients:
                    await channel.connect()
                    print(f'¡ÉXITO TOTAL! Conectado al canal: {channel.name}')
                else:
                    print('Ya está conectado a un canal de voz.')
            except Exception as e:
                print(f'Error al intentar conectar a la voz: {e}')
        else:
            print('Buscando el canal en los servidores del bot...')
            for guild in client.guilds:
                g_channel = guild.get_channel(CANAL_VOZ_ID)
                if g_channel:
                    try:
                        await g_channel.connect()
                        print(f'¡ÉXITO en servidor {guild.name}! Conectado a: {g_channel.name}')
                    except Exception as e:
                        print(f'Error en bucle secundario: {e}')
        
        # Espera 30 segundos antes de volver a comprobar
        await asyncio.sleep(30)

@client.event
async def on_ready():
    print(f'Sesión iniciada como {client.user}')
    client.loop.create_task(join_voice_channel())

client.run(os.getenv("DISCORD_TOKEN"))

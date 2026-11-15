import ctypes
import ctypes.util
import discord
import asyncio
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# Intentamos cargar opus manualmente para evitar el error de la librería
if not discord.opus.is_loaded():
    for lib in ["libopus.so.0", "libopus.so", "libopus-0.dll", "libopus"]:
        try:
            discord.opus.load_opus(lib)
            print(f">>> [OPUS] ¡Librería {lib} cargada con éxito manualmente!", flush=True)
            break
        except Exception:
            pass

print(">>> [INICIO] El script se está ejecutando correctamente...", flush=True)

# --- Mini servidor web invisible para Render ---
class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is alive!")

def run_web_server():
    port = int(os.getenv("PORT", 10000))
    print(f">>> [WEB] Iniciando servidor web en el puerto {port}...", flush=True)
    server = HTTPServer(('0.0.0.0', port), SimpleHandler)
    server.serve_forever()

threading.Thread(target=run_web_server, daemon=True).start()

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

client = discord.Client(intents=intents)
CANAL_VOZ_ID = 1546286007308255239

@client.event
async def on_ready():
    print(f'>>> [DISCORD] ¡Sesión iniciada con éxito como {client.user}!', flush=True)
    await asyncio.sleep(3)
    try:
        print(f'>>> [VOZ] Buscando canal ID: {CANAL_VOZ_ID}...', flush=True)
        channel = await client.fetch_channel(CANAL_VOZ_ID)
        if channel:
            print(f'>>> [VOZ] ¡Canal encontrado ({channel.name})! Conectando...', flush=True)
            await channel.connect()
            print('>>> [VOZ] ¡ÉXITO! El bot ya entró al canal de voz.', flush=True)
        else:
            print('>>> [VOZ] Error: No se encontró el canal.', flush=True)
    except Exception as e:
        print(f'>>> [ERROR CRÍTICO] {e}', flush=True)

token = os.getenv("DISCORD_TOKEN")
if not token:
    print(">>> [ERROR] Falta la variable DISCORD_TOKEN en Render.", flush=True)
else:
    print(">>> [DISCORD] Conectando a la pasarela de Discord...", flush=True)
    client.run(token)
    

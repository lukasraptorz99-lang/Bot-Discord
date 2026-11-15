import os
import asyncio
import discord
from discord.ext import commands
from aiohttp import web

# Configuración básica de intents
intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# ID de tu canal de voz (el mismo que mencionaste en los logs)
VOICE_CHANNEL_ID = 1546286007308255239

@bot.event
async def on_ready():
    print(f"[DISCORD] ¡Sesión iniciada con éxito como {bot.user}")
    
    # Tarea en segundo plano para conectar al canal de voz y mantenerse ahí
    bot.loop.create_task(connect_to_voice())

async def connect_to_voice():
    await bot.wait_until_ready()
    print(f"[VOZ] Buscando canal ID: {VOICE_CHANNEL_ID} ...")
    
    channel = bot.get_channel(VOICE_CHANNEL_ID)
    if channel is not None and isinstance(channel, discord.VoiceChannel):
        print(f"[VOZ] ¡Canal encontrado ({channel.name})! Conectando ...")
        try:
            if not channel.guild.voice_client:
                await channel.connect()
                print("[VOZ] ¡Conectado al canal de voz con éxito!")
            else:
                print("[VOZ] El bot ya estaba conectado.")
        except Exception as e:
            print(f"[ERROR DE VOZ] No se pudo conectar: {e}")
    else:
        print("[ERROR CRÍTICO] No se encontró el canal de voz o el ID es incorrecto.")

# Servidor HTTP dummy para mantener el proceso vivo en Fly.io
async def handle(request):
    return web.Response(text="Bot de Discord activo 24/7 en Fly.io")

async def start_web_server():
    app = web.Application()
    app.router.add_get("/", handle)
    runner = web.AppRunner(app)
    await runner.setup()
    port = int(os.getenv("PORT", 8080))
    site = web.TCPSite(runner, "0.0.0.0", port)
    await site.start()
    print(f"[WEB] Servidor dummy activo en el puerto {port}")

async def main():
    # Inicia el servidor web auxiliar y el bot en paralelo
    await start_web_server()
    token = os.getenv("DISCORD_TOKEN")
    if not token:
        print("[ERROR] No se encontró la variable de entorno DISCORD_TOKEN.")
        return
    await bot.start(token)

if __name__ == "__main__":
    asyncio.run(main())
    

import discord
import asyncio
import os

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
    print(">>> [ERROR] Falta la variable DISCORD_TOKEN.", flush=True)
else:
    print(">>> [DISCORD] Conectando a la pasarela de Discord...", flush=True)
    client.run(token)
    

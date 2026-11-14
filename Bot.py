import discord
import asyncio
import os

# Configuramos los intents básicos
intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

client = discord.Client(intents=intents)

CANAL_VOZ_ID = 1546286007308255238

@client.event
async def on_ready():
    print(f'¡Conectado con éxito como {client.user}!')
    
    # Esperamos unos segundos a que la caché de Discord cargue por completo los servidores y canales
    print('Esperando a sincronizar canales...')
    await asyncio.sleep(5)
    
    channel = client.get_channel(CANAL_VOZ_ID)
    
    if channel is not None:
        try:
            await channel.connect()
            print(f'¡Éxito! El bot ya entró al canal de voz: {channel.name}')
        except Exception as e:
            print(f'Error al intentar conectar al canal: {e}')
    else:
        print('Buscando canal en todos los servidores...')
        # Búsqueda alternativa por si el caché directo falló
        for guild in client.guilds:
            found_channel = guild.get_channel(CANAL_VOZ_ID)
            if found_channel:
                try:
                    await found_channel.connect()
                    print(f'¡Éxito encontrado en servidor {guild.name}! Entró a: {found_channel.name}')
                    return
                except Exception as e:
                    print(f'Error al conectar en bucle: {e}')
        print('No se encontró el canal de voz en ningún servidor. Revisa el ID.')

client.run(os.getenv("DISCORD_TOKEN"))

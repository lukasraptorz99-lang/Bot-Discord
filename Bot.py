import discord
import os

# Configuramos los intents básicos
intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True

# Creamos la instancia del cliente
client = discord.Client(intents=intents)

# ID de tu canal de voz convertido a número entero
CANAL_VOZ_ID = 1546286007308255238

@client.event
async def on_ready():
    print(f'¡Conectado con éxito como {client.user}!')
    
    # Esperamos a que el bot reconozca los servidores en los que está
    for guild in client.guilds:
        print(f'- Conectado al servidor: {guild.name}')
    
    # Buscamos el canal de voz
    channel = client.get_channel(CANAL_VOZ_ID)
    
    if channel is not None:
        try:
            # Nos conectamos al canal de voz
            await channel.connect()
            print(f'¡Éxito! El bot ya entró al canal de voz: {channel.name}')
        except Exception as e:
            print(f'Error al intentar conectar al canal: {e}')
    else:
        print('No se encontró el canal de voz. Asegúrate de que el bot esté en el servidor y el ID sea correcto.')

client.run(os.getenv("DISCORD_TOKEN"))

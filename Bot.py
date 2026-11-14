import discord
from discord.ext import commands

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
    
    # Buscamos el canal de voz usando su ID
    channel = client.get_channel(CANAL_VOZ_ID)
    
    if channel is not None:
        try:
            # Nos conectamos al canal de voz
            await channel.connect()
            print(f'¡Éxito! El bot ya entró al canal de voz: {channel.name}')
        except Exception as e:
            print(f'Error al intentar conectar al canal: {e}')
    else:
        print('No se encontró el canal de voz. Revisa que el ID sea correcto y que el bot esté en el servidor.')

# AQUÍ PEGAS TU TOKEN (Reemplaza este texto por tu token real o el nuevo que restaures)
client.run('MTU3MTIwNzc5NzYzNzUxMzI1Ng.Gh0Slq.btN7i5wAOC8MWY9-qLXVCncg86v_rIVPAaLbvo')

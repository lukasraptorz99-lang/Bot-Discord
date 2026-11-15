client = discord.Client(intents=intents)
CANAL_VOZ_ID = 1546286007308255239

@client.event
async def on_ready():
    print(f'>>> [DISCORD] ¡Sesión iniciada con éxito como {client.user}', flush=True)
    try:
        print(f'>>> [VOZ] Buscando canal ID: {CANAL_VOZ_ID}...', flush=True)
        channel = await client.fetch_channel(CANAL_VOZ_ID)
        if channel:
            print(f'>>> [VOZ] ¡Canal encontrado ({channel.name})! Conectando...', flush=True)
            await channel.connect()
            print(f'>>> [VOZ] ¡ÉXITO! El bot ya entró al canal de voz.', flush=True)
        else:
            print(f'>>> [VOZ] Error: No se encontró el canal.', flush=True)
    except Exception as e:
        print(f'>>> [ERROR CRÍTICO] {e}', flush=True)

# Al final solo va esto para mantenerlo vivo 24/7:
token = os.getenv("DISCORD_TOKEN")
if token:
    client.run(token)
else:
    print(">>> [ERROR] Falta la variable DISCORD_TOKEN.")
    

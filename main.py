# Imports
import aternosAPI
import minecraftAPI
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from discord import app_commands

# Variables
load_dotenv()
token = os.getenv("token")
intents = discord.Intents.all()

activity = discord.Activity(type=discord.ActivityType.listening, name="/help")
bot = commands.Bot(command_prefix="!", intents=intents, activity=activity, status=discord.Status.idle)


@bot.event
async def on_ready():
    print("✔️ Le bot est prêt.")
    try:
        synced = await bot.tree.sync()
        print(f"🔄 {len(synced)} commande(s) slash détectée(s)")
    except Exception as e:
        print(f"🔴 Erreur : {e}")


@bot.tree.command(name="help", description="Affiche un message d'aide pour utiliser le bot")
async def help(interaction: discord.Interaction):
    await interaction.response.send_message(
        f"Liste des commandes disponible {interaction.user.mention} : \n`/serveur`\n`/aternos`\n`/statuts`")


@bot.group(name="aternos")
async def aternos(interaction: discord.Interaction):
    await interaction.response.send_message("test")


@bot.tree.command(name="aternos-start", description="Permet de gérer votre serveur aternos")
@app_commands.describe(username="username", password="password", server_id="server_id")
async def aternos_start(interaction: discord.Interaction, username: str, password: str, server_id: str):
    print("🔀 Aternos Start...")
    try:
        aternosAPI.start(username, password, int(server_id))
    except Exception as e:
        await interaction.response.send_message(
            f"L'identifiant, le mot de passe ou l'id du serveur n'est pas le bon {interaction.user.mention}. \n `{e}`")
    print("✔️ Serveur lancé !")
    await interaction.response.send_message(f"✔️ Le serveur est lancé {interaction.user.mention} !")


@bot.tree.command(name="statuts", description="Permet de voir si un serveur est ouvert avec une ip")
@app_commands.describe(ip="Ip de votre serveur", port="Port de votre serveur")
async def status(interaction: discord.Interaction, ip: str, port: str):
    print("🔀 Serveur Statuts...")
    x = minecraftAPI.statuts(ip, int(port))
    await interaction.response.send_message(f"Le serveur dont l'ip est `{ip}`, est `{x}`  {interaction.user.mention}.")

    print("✔️ Serveur Statuts a marché sans erreur.")

bot.run(token)

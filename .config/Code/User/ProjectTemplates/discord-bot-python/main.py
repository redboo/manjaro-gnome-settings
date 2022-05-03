#!/usr/bin/python
"""TVP bot discord."""
from datetime import datetime
from discord.ext import commands
from discord import Intents
import config
import sqlite3
import os


bot = commands.Bot(command_prefix=config.PREFIX,
                   intents=Intents.all())


@bot.event
async def on_ready() -> None:
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f'✅ {current_time} Бот запущен')

    global base, cur
    base = sqlite3.connect(config.DB_NAME)
    cur = base.cursor()
    if base:
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f'✅ {current_time} DB connected')


@bot.command(aliases=['l'])
@commands.is_owner()
async def load(ctx, ext: str) -> None:
    """Подключает модуль к боту."""
    bot.load_extension(f'cogs.{ext}')
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f'✅ {current_time} {ext} loaded')
    await ctx.send(f'✅ {ctx.author.mention} `{ext}` is loaded')


@bot.command(aliases=['u'])
@commands.is_owner()
async def unload(ctx, ext: str) -> None:
    """Отключает модуль от бота."""
    bot.unload_extension(f'cogs.{ext}')
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f'✅ {current_time} {ext} unloaded')
    await ctx.send(f'✅ {ctx.author.mention} `{ext}` is unloaded')


@bot.command(aliases=['r'])
@commands.is_owner()
async def reload(ctx, ext: str) -> None:
    """Перезагружает модуль бота."""
    bot.unload_extension(f'cogs.{ext}')
    bot.load_extension(f'cogs.{ext}')
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f'✅ {current_time} {ext} reloaded')
    await ctx.send(f'✅ {ctx.author.mention} `{ext}` is reloaded')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(config.TOKEN)

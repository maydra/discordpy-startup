from discord.ext import commands
import os
import traceback
import random ##運勢リストからランダムに出力するために必要

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)
    
       if message.content == "占い":
#レスポンスされる運勢のリストを作成
        unsei = ["大吉", "中吉", "吉", "末吉", "小吉", "凶", "大凶"]
        choice = random.choice(unsei) #randomモジュール使用
        await message.send_message(message.channel, choice)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')


bot.run(token)

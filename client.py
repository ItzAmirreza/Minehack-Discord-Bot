from json import load
import discord
from discord import embeds
from discord.ext import commands, tasks
import json
from difflib import SequenceMatcher
import aiohttp
import youtube_dl
from youtube_dl import YoutubeDL
import json
import bs4
import asyncio
import random
from functools import partial
from bs4 import BeautifulSoup

TOKEN = "NzgwNDk3MDk3ODk5NTA3NzU0.X7v8kQ.yWtAJ6ZNcJz_yhlY5DJEf2iz_74"
intents = discord.Intents.all()
intents.members = True
client = commands.Bot(command_prefix="-", help_command=None, intents=intents)
count = 0

@client.event
async def on_ready():
    changing.start()
    print('im ready!@ :DD')
    await playsong()
    print("voice ready dude")


async def playsong():
    minehack = client.get_guild(771435036468838451)
    vcchannel = minehack.get_channel(827272150095233054)
    

    def playagain(source, vc):
        source = discord.FFmpegPCMAudio(
            f'sound.mp3')
        vc.play(source, after=lambda e: playagain(source, vc))

    try:
        vc = await vcchannel.connect()
        source = discord.FFmpegPCMAudio(
            f'sound.mp3')
        vc.play(
            source, after=lambda e: playagain(source, vc))
    except Exception as ex:
        print(ex)

@tasks.loop(minutes=30)
async def changing():
    global count
    guild = client.get_guild(771435036468838451)
    count = guild.member_count
    await client.change_presence(status=discord.Status.dnd,
                                 activity=discord.Activity(type=discord.ActivityType.watching,
                                                           name=f" {str(count)} Members in MineHack"))


@client.event
async def on_member_join(member):
    channel = client.get_channel(771438539178639383)
    rules = client.get_channel(771443829999665192)
    embed = discord.Embed(
        title="خوش اومدی به جامعه ی ماین هک!",
        description=f"""قبل از شروع حتما چنل ({rules.mention}) رو مطلعه کن \n امیدوارم لحظات خوبی رو سرپی کنی.""",
        color=0x1C2732
    )
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text="By MineHack Community")
    await channel.send(embed=embed, content=f"{member.mention}")


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title="راهنمای استفاده از بات",
        description="-info [تاپیک] \n -thx تشکر کردن زیبا \n -noobsanj [ @Member (optional) ] \n -addpand [pand] \n -google [سرچ]",
        color=0x1C2732
    )
    await ctx.send(embed=embed)




@client.command()
async def thx(ctx):
    embed = discord.Embed(
        title="ممون که به سوالم جواب دادی",
        description="اینم به افتخار شما",
        color=0xf47fff
    )
    embed.set_image(url="https://cdn.discordapp.com/attachments/771804409981567016/824733947316928513/7c57-ezgif-com-gif-maker-1-.gif")
    await ctx.send(embed=embed)




@client.command()
# https://www.spigotmc.org/search/235/?q={key}&t=resource_update&o=relevance&c[title_only]
async def search(ctx, *, key=None):
    # params={
    #         "api_key": "KHQTJ01Y4LQVFL65GIM0XP6BD0GL6FLK8FNACWN57N5XOC8OJSAQF42NJUR8YRVQFLD8SI03E9BHUMZ6",
    #         "url": f"https://www.spigotmc.org/search/235/?q={key}&t=resource_update&o=relevance&c[title_only]",
    #         "premium_proxy": "true", 
    #         "country_code":"se"
    #     }
    # async with aiohttp.request("GET", f"https://app.scrapingbee.com/api/v1/", params=params) as r:
    #     response = await r.read()
    
    # print(response)

    # embed = discord.Embed(
    #     title="در حال جستجو....",
    #     description="در حال جستجوی پلاگین ها در اسپیگات، لطفا کی صبر کنید.",
    #     color=0x1C2732
    # )
    # embed.set_footer(text=f"By Minehack Community - Seach requested by: {ctx.author.name}")
    # msg = await ctx.send(embed=embed)
    
    # searches = {}

    # soup = BeautifulSoup(response, "html.parser")
    # all = soup.find_all('h3', class_="title")
    # authors = soup.find_all('a', class_="username")
    # count = -1
    # for i in all:
    #     count = count + 1
    #     title = i.a.text
    #     link = "https://www.spigotmc.org/" + i.a["href"]
    #     searches[title] = {}
    #     searches[title]["link"] = link
    #     searches[title]["author"] = authors[count].text
    

    # if len(authors) == 0:
    #     embed = discord.Embed(
    #         title="چیزی پیدا نکردم...",
    #         description="متاسفانه نتونستم پلاگینی با این اسم پیدا کنم.",
    #         color=0x1C2732
    #     )
    #     embed.set_footer(text=f"By Minehack Community - Seach requested by: {ctx.author.name}")
    #     await msg.edit(embed=embed)
    # else:
    #     laststring = ""
    #     for i in searches:
    #         title = i
    #         link = searches[i]["link"]
    #         author = searches[i]["author"]
    #         if not len(laststring + f"[{title}]({link}) | **By {author}** \n ") > 2048:
    #             laststring = laststring + f"[{title}]({link}) | **By {author}** \n "
        

    #     embed = discord.Embed(
    #         title=f"{str(len(authors))} نتیجه پیدا کردم.",
    #         description=laststring,
    #         color=0x1C2732
    #     )
    #     embed.set_footer(text=f"By Minehack Community - Seach requested by: {ctx.author.name}")
    #     await msg.edit(embed=embed)
    await ctx.send("این قابلیت به دلیل مطابقت نداشتن با قوانین اسپیگات حذف شد.")




async def getHelpEmbed(ctx):
    embed = discord.Embed(
        title="راهنمای استفاده:",
        description="""
        
        دیدن توضیحات یک تاپیک
        ``-info اسم تاپیک``

        Topic Managers Role:

        اینجاد توضیحات درباره یک تاپیک
        ``-info create [اسم تاپیک ( 1 کلمه)] [توضیحات تاپیک]``

        پاک کردن یک تاپیک:
        ``-info delete [اسم تاپیک]``

        ادیت تاپیک:
        ``-info edit [اسم تاپیک ( 1 کلمه)] [توضیحات تاپیک]``
        
        """,
        color=0x1C2732
    )
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
    embed.set_footer(text="By Minehack Community - Author: Dead_Light")
    return embed


async def checkForOtherArguments(usage, key, description):
    if usage == "create" or usage == "edit":

        if key == "" or description == "":
            return False
        else:
            return True
    elif usage == "delete":
        if key == "":
            return False
        else:
            return True

async def rightPerm(ctx):
    roles = [771437443755802664, 780513428799356951, 758428780422496280, 771437918857199617]
    roleids = ctx.author.roles
    memberid = ctx.author.id
    result = False

    if memberid in roles:
        result = True
    for i in roleids:
        if i.id in roles:
            result = True

    return result

async def rightpandgiver(ctx):
    roles = [824736294176555008]
    roleids = ctx.author.roles
    memberid = ctx.author.id
    result = False

    if memberid in roles:
        result = True
    for i in roleids:
        if i.id in roles:
            result = True

    return result


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

#info create login aodpmawpdawpdawdo
@client.command()
async def info(ctx, usage="", key="", *, description=""):
    #help command
    if usage == "":
        embed = await getHelpEmbed(ctx)
        await ctx.send(embed=embed)
    elif usage.lower() == "create":
        if await checkForOtherArguments(usage.lower(), key, description) == False:
            await ctx.send(embed=await getHelpEmbed())
        else:
            if await rightPerm(ctx):

                with open("data.json", "r") as f:
                    loaded = json.load(f)
                
                if key.lower() in loaded:
                    await ctx.send("این تاپیک قبلا به ثبت رسیده!")
                else:
                    loaded[key.lower()] = {}
                    loaded[key.lower()]["description"] = description
                    loaded[key.lower()]["by"] = ctx.author.name

                    with open('data.json', 'w') as f:
                        json.dump(loaded, f)
                
                    embed = discord.Embed(
                        title=f"تاپیک ({key}) با موفقیت ثبت شد",
                        description=f"""
                        
                        توضیحات تاپیک:
                        \n

                        {description}
                        


                        ``-info {key}``
                        """
                    )
                    embed.set_footer(text=f"By Minehack Community - {ctx.author.name}")
                    await ctx.send(embed=embed)
            else:
                await ctx.send("دسترسی این کار برای شما وجود ندارد.")

    elif usage.lower() == "delete":
        if await checkForOtherArguments(usage.lower(), key, description) == False:
            await ctx.send(embed=await getHelpEmbed(ctx))
        else:
            if await rightPerm(ctx):

                with open("data.json", "r") as f:
                    loaded = json.load(f)
                
                if not key.lower() in loaded:

                    await ctx.send("این تاپیک وجود ندارد.")
                else:

                    del loaded[key.lower()]

                    with open('data.json', 'w') as f:
                        json.dump(loaded, f)

                    await ctx.send("این تاپیک با موفقیت حذف شد.")
            else:
                await ctx.send("دسترسی این کار برای شما وجود ندارد.")
        
    elif usage.lower() == "edit":
        if await checkForOtherArguments(usage.lower(), key, description) == False:
            await ctx.send(embed=await getHelpEmbed(ctx))
        else:
            if await rightPerm(ctx):
            
                with open("data.json", "r") as f:
                    loaded = json.load(f)

                if not key.lower() in loaded:
                    await ctx.send("این تاپیک وجود ندارد.")
                else:

                    loaded[key.lower()]["description"] = description
                    loaded[key.lower()]["by"] = ctx.author.name

                    with open('data.json', 'w') as f:
                        json.dump(loaded, f)
                

                    await ctx.send("توضیحات این تاپیک ادیت شد.")
            else:
                await ctx.send("دسترسی این کار برای شما وجود ندارد.")
    else:
        usage = usage.lower()
        with open("data.json", "r") as f:
            loaded = json.load(f)
        
        if usage in loaded:
            description = loaded[usage]["description"]
            by = loaded[usage]["by"]


            embed = discord.Embed(
                title=f"درباره تاپیک: {usage}",
                description=description,
                color=0x1C2732
            )
            embed.set_footer(text=f"By Minehack Community - {by}")
            await ctx.send(embed=embed)
        else:
            list = []
            results = []
            for i in loaded:
                list.append(i)
            
            for i in list:
                if i in usage or usage in i:
                    results.append(i)
                

            description = ''
            if len(results) != 0:

                for i in results:
                    description = description + f"\n ``-info {i}``"

                embed = discord.Embed(
                    title="منظور شما این بود؟",
                    description=description,
                    color=0x1C2732
                )
                embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                embed.set_footer(text="By Minehack Community - Author: Dead_Light")
                await ctx.send(embed=embed)
            else:
                
                results = []
                for i in list:
                    if similar(i, usage.lower()) >= 0.5:
                        results.append(i)
                
                if len(results) != 0:


                    for i in results:
                        description = description + f"\n ``-info {i}``"

                    embed = discord.Embed(
                        title="منظور شما این بود؟",
                        description=description,
                        color=0x1C2732
                    )
                    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
                    embed.set_footer(text="By Minehack Community - Author: Dead_Light")
                    await ctx.send(embed=embed)
                else:
                    await ctx.send("این تاپیک وجود ندارد.")
      
                
@commands.cooldown(1, 30, commands.BucketType.user)
@client.command()
async def noobsanj(ctx, member : discord.Member = None):
    num1 = random.randint(0, 100)
    randompand = await getArandomPand()
    randompand = randompand.replace("*", f"{num1}")
    if member is None:
        member = ctx.author
    if num1 > 80:

        embed = discord.Embed(
            title=f"شما مرز های نوبیت رو رد کردید!",
            description=randompand,
            color=0xFF5733
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/771804409981567016/824725361915854848/sticker4webp.webp")
        
        await ctx.send(content=member.mention, embed=embed)
    elif num1 > 50:
        embed = discord.Embed(
            title=f"شما به طور نا متعادلی نوب هستید",
            description=randompand,
            color=0xFF5733
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/771804409981567016/824725309144039445/sticker2.webp")
        
        await ctx.send(content=member.mention, embed=embed)
    elif num1 > 20:
        embed = discord.Embed(
            title=f"شما فقط نوبی با درصد کم هستید",
            description=randompand,
            color=0xFF5733
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/771804409981567016/824725280005423194/sticker.webp")
        
        await ctx.send(content=member.mention, embed=embed)
    elif num1 > 0:
        embed = discord.Embed(
            title=f"شما درصد نوبیت قابل قبولی دارید",
            description=randompand,
            color=0xFF5733
        )
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/771804409981567016/824725337074040862/sticker3.webp")
        
        await ctx.send(content=member.mention, embed=embed)



# @client.event
# async def on_message(message):
#     if message.guild.id == 771435036468838451:
#         print(message.content)

async def getArandomPand():
    with open("noobsanj.json", "r") as f:
        loaded = json.load(f)
    pands = len(loaded["pands"])
    randnum = random.randint(0, pands - 1)
    
    return loaded["pands"][randnum]

@commands.cooldown(1, 3600, commands.BucketType.user)
@client.command()
async def addpand(ctx):
    result = await rightpandgiver(ctx)
    if result:
        if "*" in ctx.message.content:
            with open("noobsanj.json", "r") as f:
                loaded = json.load(f)
            loaded["pands"].append(ctx.message.content.replace("-addpand", ""))
            with open('noobsanj.json', 'w') as f:
                json.dump(loaded, f)
            await ctx.send("پند شما اضافه شد")
        else:
            await ctx.send("حتما در پند خود از * به عنوان درصد نوبیت فرد استفاده کنید")

    else:
        await ctx.send("شما رول پند دهنده را ندارید! - برای دریافت این رول به ماین هک در سایت دیسکورد فا رای دهید")

@noobsanj.error
async def noobsanjerror(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = "شما هر 30 ثانیه میتوانید از نوب سنج استفاده کنید"
        await ctx.send(msg)
    else:
        raise error

@addpand.error
async def addpanderror(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = "شما هر 1 ساعت می توانید 3 پند اضافه کنید."
        await ctx.send(msg)
    else:
        raise error


@client.command()
async def google(ctx, *, content):
    link = f"https://letmegooglethat.com/?q={content}".replace(" ", "+")
    embed = discord.Embed(
        title="جواب سوال شما پیدا شد - کلیک کنید",
        url=link
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/771804409981567016/825030603740938281/3.jpg")
    
    await ctx.send(embed=embed)

@client.command()
async def bego(ctx, *, content):
    channel = client.get_channel(771438539178639383)
    await channel.send(content)

client.run(TOKEN)
import discord, os
from discord.ext import commands
from discord.ext.commands import Bot

Bot = commands.Bot(command_prefix= 'h!')

@Bot.event
async def on_ready():
   print ("Я онлайн")

Bot.remove_command('help')

@Bot.command(pass_context= True)
async def Зиллиакс(ctx):
    hen = discord.Embed(title= "**Единство! Точность! Совершенство!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/568746965739896852/maxresdefault_1.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Альакир(ctx):
    hen = discord.Embed(title= "**Ветра! Повинуйтесь моей воле!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/568749568750256129/83c014c5ab8d7978.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Вольджин(ctx):
    hen = discord.Embed(title= "**Духи не знают усталости!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/568754277401624616/1497439905136192573.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Принц_Галливикс(ctx):
    hen = discord.Embed(title= "**Перед вами торговый Принц Галливикс!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569486517718745088/f6dfbb3e1353e29e009e8686560d4677_1.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Блескотрон_3000(ctx):
    hen = discord.Embed(title= "**Кому подарочков?**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569498781528358942/Blingtron-3000-art.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Газлоу(ctx):
    hen = discord.Embed(title= "**Быстрее! Я не хочу тут вечно торчать!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569504395432165376/GVG_117.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Врагорез_4000(ctx):
    hen = discord.Embed(title= "**Предохранительный механизм отключён! Начинаю калибровку!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569530819660742676/GVG_113_1_1_1_1.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Архимаг_Антонидас(ctx):
    hen = discord.Embed(title= "**Тебе нужна моя помощь?**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569533126796378113/maxresdefault.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Пророк_Велен(ctx):
    hen = discord.Embed(title= "**Все, кто ищут путь, потеряли свой!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569535612856827914/529839_velena.png")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Эдвин_ванКлиф(ctx):
    hen = discord.Embed(title= "**Справедливость восторжествует!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569759520537051139/1497257596118322253.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Громмаш_АдскийКрик(ctx):
    hen = discord.Embed(title= "**Не могу больше ждать!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569820668716384287/WarCraft_Raneman021c_1.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Магкрови_Талнос(ctx):
    hen = discord.Embed(title= "**Мы жаждем мести!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569821232300818447/images.jpeg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Миллхаус_Манашторм(ctx):
    hen = discord.Embed(title= "**Приготовьтесь сразиться с могущественным Миллхаусом Манаштормом!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569872152627642369/Millhouse-Manastorm-art.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Нат_Пэгл(ctx):
    hen = discord.Embed(title= "**Я могу рыбачить весь день!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569873681757503499/EX1_557_1.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Хранительистории_Чо(ctx):
    hen = discord.Embed(title= "**Нефритовая змея направляет тебя!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569880858396327946/hranitel-istorii-cho.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)

@Bot.command(pass_context= True)
async def Мехмастер_Замыкалец(ctx):
    hen = discord.Embed(title= "**На этот раз всё получится!**", color= 0xca8ef1 )
    hen.set_image(url= "https://cdn.discordapp.com/attachments/505360396866158593/569882428156542976/Tinkmaster-art_1.jpg")
    await Bot.say(embed= hen)
    await Bot.delete_message(ctx.message)


@Bot.command(pass_context= True)
async def помоги(ctx):
    await Bot.say("```Зиллиакс,  Альакир,  Вольджин,  Принц_Галливикс,  Блескотрон_3000,  Газлоу,  Врагорез_4000,  Архимаг_Антонидас,  Пророк_Велен,  Эдвин_ванКлиф,  Громмаш_АдскийКрик,  Магкрови_Талнос,  Миллхаус_Манашторм,  Нат_Пэгл,  Хранительистории_Чо,  Мехмастер_Замыкалец```")


token = os.onviron.get('BOT_TOKEN')
Bot.run(str(token))

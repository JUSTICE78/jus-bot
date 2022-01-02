import discord
import COVID19Py
import random
import requests
from bs4 import BeautifulSoup
from discord import Member

import os
from discord.ext import commands
from discord import *
from discord import Status

covid19 = COVID19Py.COVID19()

client=commands.Bot(command_prefix=['jus ', 'Jus ', 'JUS '])
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Game(name="jus help", type=10)
    await client.change_presence(status=discord.Status.idle, activity=activity)

    
@client.command()
async def covidstats(contex, country):
    
    covid19 = COVID19Py.COVID19()
    
    #print(cases)
    #string="Number of cases in "+ country+ "is: "+ cases
    #await contex.send(string)
    try:
        cases1 = covid19.getLocationByCountryCode(country)
        cases=str(cases1[0]['latest']['confirmed'])
        string="Number of cases in "+ country+ " is: "+ cases
        await contex.send(string)
    except:
        await contex.send("wrong ID")
@client.command()
async def allstats(contex):
    covid19 = COVID19Py.COVID19()
    latest = covid19.getLatest()
    await contex.send(latest)
@client.command()
async def lastest(contex):
    changes = covid19.getLatestChanges()
    await contex.send(changes)
@client.command()
async def story(contex):
    enemy = random.choice (["chihuahua", "border collie", "wolf"])
    father = random.choice (["John", "Mr.Pickles", "Hairyface", "Willy Wonka", "Steve", "Bob"])
    enemyadj = ["grimy", "muddy", "awful", "grotesque", "hideous", "adorable", "cute"]
    intro1 = "I was sitting on the edge of the rocky cliff beside my favourite tree."
    intro2 = "Alone in the searing desert, I was wondering why I was leaning against a cactus."
    intro3 = "Staring out my apartment window, I saw my reflection staring back at me."
    intro4 = "I was sitting in middle of aspire zone under a tree."
    char1 = "As I looked out into the distance, I thought about my past and all of the drama in it."
    char2 = "I wondered if this was my destiny- trying to find happiness."
    char3 = "I pulled out the photo of my long lost mother and where on earth she could be."
    prob1 = "Suddenly I was covered from head to toe with darkness. I couldn't breathe or see. Everything went black..."
    prob2 = "All of a sudden a psychopathic " + enemy + " grinned at me,showing all his razor sharp teeth. Suddenly it started"
    prob3 = "I suddenly felt a sharp needle sink into my flesh. It was a tranquilizer. But before I knew it I started feeling "
    sol1 = "I forced my drowsy eyes open my eyes to see a bright light."
    sol2 = "I forced my drowsy eyes open to find myself on the back of a massive dragon and a man in front of me."
    sol3 = "I forced my drowsy eyes open to the sounds of a " + random.choice(enemyadj) + " " +enemy + " licking my face."
    end1 = "A man came to my side with a knife. It was my friend!" + father + "!" "'Go to sleep young one...'"
    end2 = "It was difficult to keep my eyes open as I stuggled to breathe. "
    end3 = "A Man came and shoot a 3 bullets using a ak-47 . . ."

    intros = [intro1, intro2, intro3]
    characters = [char1, char2, char3]
    problems = [prob1, prob2, prob3]
    solutions = [sol1, sol2, sol3]
    endings = [end1, end2, end3]
    stor = (random.choice(intros) + random.choice(characters) + random.choice(problems) + random.choice(solutions) + random.choice(endings))
    print(random.choice(intros)),
    print(random.choice(characters)),
    print(random.choice(problems)),
    print(random.choice(solutions)),
    print(random.choice(endings))
    await contex.send(stor)



    
@client.command()
async def Id(contex):
    await contex.send("You can find IDs on this wikipedia article: https://en.wikipedia.org/wiki/ISO_3166-1")
    covid19 = COVID19Py.COVID19()
    
    #print(cases)
    #string="Number of cases in "+ country+ "is: "+ cases
    #await contex.send(string)
    try:
        cases1 = covid19.getLocationByCountryCode(country)
        cases=str(cases1[0]['latest']['confirmed'])
        string="Number of cases in "+ country+ " is: "+ cases
        await contex.send(string)
    except:
        await contex.send("wrong ID")
anime_list = ["Re:Zero − Starting Life in Another World.", "Death Note.", "Naruto.", "Ghost in the Shell.", "Steins;Gate.", "Fullmetal Alchemist.", "Samurai Champloo.", "Darker Than Black", "Magic kaito", "Konosuba", "Astolfo", "91 Days", "ACCA 13", "Aiura", "Ajin", "Akame ga Kill", "Amagi Brilliant Park", "Angel Beats", "Ano Natsu de Matteru", "Another", "B the Beginning", "Baka and Test", "Barakamon", "Ben-to", "Black Cat", "Black Lagoon", "Erased", "Bokura wa Minna Kawai-sou", "Bungou Stray Dogs", "Chuunibyo", "I don't understand What my Husband is Saying", "Daily Lives of Highschool Boys", "Darker than Black", "Death Note", "D-frag", "Fate stay night", "Millionaire Detective", "Full Metal Panic", "Fullmetal Alchemist", "Gakuen Babysitters", "Gate", "Gekkan Shoujo", "Ghost Hunt", "Gin no Saji", "Grisaia", "Hanasaku Iroha", "Demon Lord is a Part Timer", "Hellsing", "Hinamatsuri", "Hyouka", "Inou-battle", "Inu x Boku", "How not to Summon a Demon Lord", "One Week Friends", "Bofuri", "Kaguya Sama", "Maid Sama", "The World God Only Knows", "Kaze no Stigma", "Kekkai Sensen", "Kokoro Connect", "Konosuba", "Ghost in the Shell", "Beyond the Boundary", "Log Horizon", "Irregular at Magic High School", "Engaged to the Unidentified", "Minami-ke", "Problem Children", "Monster", "Musaigen no Phantom World", "Nanatsu no Taizai", "Nejimaki", "Net-juu", "No Game no Life", "Noragami", "Nurarihyon", "Wolf Children", "Overlord", "Papa no Iukoto wo Kikinasai", "Psycho-pass", "Re:Zero", "ReLife", "Rental Magica", "Rokka no Yuusha", "Rosario + Vampire", "Saenai Heroine (Saekano)", "School Days", "Seiken Tsukai mo World Break", "Your Lie in April", "Steins Gate", "Summer Wars", "SAO", "Tada Kun Never Falls in Love", "Tamako Market", "Slime Isekai", "The Pilot's Love Song", "The Princess and the Pilot", "To Aru Majutsu no Index", "To Aru Kagaku no Railgun", "To Aru Kagaku no Accelerator", "The Girl who leapt through time", "Tokyo Ravens", "Trigun", "Working", "Wotakoi", "Oregairu", "Tanya the Evil", "Toradora", "Arifureta", "Bottom tier character Tomozaki Kun", "The Day I Became a God", "Talentless Nana", "Tonari no Kaibutsu Kun", "Tokyo Ghoul", "Death Parade", "Parasyte the Maxim", "Hortensia Saga", "Isekai no Seikishi Monogatari"]

@client.command()
async def hello(message):
    await message.channel.send('Hello!')
@client.command()
async def hi(message):
    await message.channel.send('Hello!')
@client.command(help="suggest an anime for You")
async def anime(message):
    await message.channel.send(random.choice(anime_list))

# @client.command()
# async def spam(message):
#     await message.channel.send('no spaming')
@client.command(pass_context=True, name='status')
async def status(ctx, member: Member):
    await ctx.send(str(member.status))

from discord.utils import get

# @client.command()
# async def gulag(message):
@client.command(pass_context=True)
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    member = member or ctx.message.author
    await client.add_roles(member, role)
# @client.event
# async def on_message(message, ctx):
#     mention = f'<@!{client.user.id}>'
#     mention1 = (ctx.author.mention)
#     if mention in message.content:
#         await message.channel.send("Iam here")
#     if message.content.startswith('Hi'):
#         msg = 'Hi {0.author.mention} Hope to hear that You are fine'.format(message)
#         await message.channel.send(msg)

@client.command(help="credits of this Bot")
async def credit(message):
    await message.channel.send("""made by justice#6010 github page:https://github.com/boris-is-here-red
    idk2706#3688(Mod of kian brose server)
    lonely weeb#2101 github page:https://github.com/Skyoathzero
    Chris7#9250(Mod of kian brose server)""")



#     if message.content.startswith('hello'):
#         await message.channel.send(f'Hello! How are U {message.author.mention}')
#     if message.content.startswith('hi'):
#         await message.channel.send(f'Hello! How are U {message.author.mention}')
#     if message.content.startswith('Hello'):
#         await message.channel.send(f'Hello! How are U {message.author.mention}')
#     if message.content.startswith('Hi'):
#         await message.channel.send(f'Hello! How are U {message.author.mention}')
#     if message.content.startswith(str.lower('brb')):
#         await message.channel.send(f'tyt {message.author.mention} take your time')
#     if message.content.startswith(str.lower('bye')):
#         await message.channel.send(f'bye {message.author.mention} we wish You come back')
#     if message.content.startswith(str.lower('back')):
#         await message.channel.send(f'welcome {message.author.mention}')
    


#     #arabic    
#     if message.content.startswith('السلام عليكم'):
#         await message.channel.send(f' وعليكم السلام ورحمة الله وبركاته منور/ه يا {message.author.mention}')
#     if message.content.startswith('برب'):
#         await message.channel.send(f' تيت خذ وقتك بس لا تطول {message.author.mention}')
#     if message.content.startswith('اهلا'):
#         await message.channel.send(f' هلا ايش اخبارك {message.author.mention}')
#     if message.content.startswith('باك'):
#         await message.channel.send(f' ولكم {message.author.mention}')

        
        


# @client.command()
# async def guess(message, num, content):
#     randomlist = []
#     n = random.randint(1,int(num))
#     randomlist.append(str(n))
#     print(str(n))
#     counter=5
#     await message.channel.send(" I guessed a number from 1 to "+ str(num))
     
    
    
#     if message.author.bot:
#         return
#         return n
#     counter=5
#     if "n" in message.content:
#         await message.channel.send("nice")
#     else:
#         counter -=1
#         await message.channel.send(f"Try again you have {counter} trys")
#         print(str(n))

@client.command(help="kick members that they dont have 'roles'")
async def kick(self, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    
@client.command(help="ban members that they dont have 'roles'")
async def ban(self, member: discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await message.channel.send(f"{member} banned")

# @client.command()
# async def ban(ctx, *, member):
#     banned_users = await ctx.guild.bans()
#     member_name, member_di

@client.command(help="Give You anime news by number")
async def animenews(message, number):
    import re
    URL = 'https://www.animenewsnetwork.com'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('a', attrs={'href': re.compile('/news/20.+')})[:int(number)]
    for r in results:
        print(r.text)
        print(URL + r['href'])
    await message.channel.send(r.text)
    await message.channel.send(URL + r['href'])


# @client.command()
# async def turgot_is_best(message):
#     await message.channel.send("https://www.youtube.com/watch?v=tKRotg4o9aE")

@client.command(help="say what u put after say command")
async def say(ctx ,message): 
    await ctx.send(message)
    await ctx.send(ctx.author.mention)
    #to get a member from a 'ctx' object is ctx.author
	#from there its .mention will mention (ping) the user
	#also there are others like .id
@client.command(help="ask u a ques in english")
async def ask(message): 
    await message.channel.send(random.choice(ques_list))
# async def on_message(self, message):
#     # we do not want the bot to reply to itself
#     if message.author.id == self.user.id:
#         return
#     if message.content.startswith('jus guess'):
#         await message.channel.send('Guess a number between 1 and 10.')
#         def is_correct(m):
#             return m.author == message.author and m.content.isdigit()
#         answer = random.randint(1, 10)
#         try:
#             guess = await self.wait_for('message', check=is_correct, timeout=5.0)
#         except asyncio.TimeoutError:
#             return await message.channel.send(f'Sorry, you took too long it was {answer}.')
#         if int(guess.content) == answer:
#             await message.channel.send('You are right!')
#         else:
#             await message.channel.send(f'Oops. It is actually {answer}.')
@client.command(help="ask u a ques in arabic")
async def ask_ar(message): 
    await message.channel.send(random.choice(ques_list_arab))
ques_list=["1. What’s your favorite way to spend a day off?", "What type of music are you into?", "What was the best vacation you ever took and why?", "Where’s the next place on your travel bucket list and why?", "What are your hobbies, and how did you get into them?", "What was your favorite age growing up?", "Was the last thing you read?", "Would you say you’re more of an extrovert or an introvert?", "What's your favorite ice cream topping?", " What was the last TV show you binge-watched?", " Are you into podcasts or do you only listen to music?", " Do you have a favorite holiday? Why or why not?", " If you could only eat one food for the rest of your life, what would it be?", " Do you like going to the movies or prefer watching at home?", " What’s your favorite sleeping position?", " What’s your go-to guilty pleasure?", " In the summer, would you rather go to the beach or go camping?", " What’s your favorite quote from a TV show/movie/book?", " How old were you when you had your first celebrity crush, and who was it?", " What's one thing that can instantly make your day better?", " Do you have any pet peeves?", "what is your favourite anime?", "how many mangas You read?"] 
ques_list_arab=[" ما هي طريقتك المفضلة لقضاء يوم عطلة؟" , " ما نوع الموسيقى التي تحبها؟" , " ما هي أفضل إجازة أخذتها ولماذا؟" , " أين المكان التالي في قائمة مجموعة السفر الخاصة بك ولماذا ؟", " ما هي هواياتك , وكيف دخلت إليها؟" , " ما هو عمرك المفضل عندما نشأت؟" , " هل كان آخر شيء قرأته؟", " هل تقول أنك أكثر انفتاحًا أو انطوائيًا؟", " ما هي كريمة الآيس كريم المفضلة لديك؟" , " ما هو آخر برنامج تلفزيوني شاهدته بنهم ؟", " هل تحب البودكاست أم تستمع إلى الموسيقى فقط؟", " هل لديك عطلة مفضلة؟ لما و لما لا؟", " إذا كان بإمكانك تناول طعام واحد فقط لبقية حياتك , فماذا سيكون؟ ", " هل تحب الذهاب إلى السينما أو تفضل مشاهدتها في المنزل؟ ", " ما هو وضعك المفضل في النوم؟" , " ما هو سعادتك بالذنب؟ ", "في الصيف , هل تفضل الذهاب إلى الشاطئ أم الذهاب للتخييم ؟", " ما هو الاقتباس المفضل لديك من برنامج تليفزيوني / فيلم / كتاب؟" , "كم كان عمرك عندما حظيت بأول سحق لك , ومن كان؟ ", "ما هو الشيء الوحيد الذي يمكن أن يجعل يومك أفضل؟ ", "هل لديك أي حيوان أليف يزعجك؟",
]

#fssdsd
@client.event
async def on_member_update(before, after):
    if str(after.status) == "offline":
        print("{} has gone {}.".format(after.name,after.status))
# @client.event
# async def on_message(message):
#     if message.author == client.user:
#         return
#     if "ty" in message.content:
        
#         await message.add_reaction("w")

@commands.command()
async def game(self, ctx):
    number = random.randint(0, 100)
    for i in range(0, 5):
        await ctx.send('guess')
        response = await self.bot.wait_for('message')
        guess = int(response.content)
        if guess > number:
            await ctx.send('bigger')
        elif guess < number:
            await ctx.send('smaller')
        else:
            await ctx.send('true')

client.run("")


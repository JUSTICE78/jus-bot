import discord
import COVID19Py
import random

import os
from discord.ext import commands
covid19 = COVID19Py.COVID19()

client=commands.Bot(command_prefix='jus ')
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def covidStats(contex, country):
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
async def ID(contex):
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
anime_list = ["Re:Zero − Starting Life in Another World.",
"Death Note.",
"Naruto.",
"Ghost in the Shell.",
"Steins;Gate.",
"Fullmetal Alchemist.",
"Samurai Champloo.",
"Darker Than Black"]

@client.command()
async def hello(message):
    await message.channel.send('Hello!')
@client.command()
async def hi(message):
    await message.channel.send('Hello!')
@client.command()
async def anime(message):
    await message.channel.send(random.choice(anime_list))

@client.command()
async def spam(message):
    await message.channel.send('no spaming')
    





client.run('')






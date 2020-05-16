import discord
import random

client = discord.Client()

#Data

test = 0

races = {
    '0':'Space Marines',
    '1':'Chaos',
    '2':'Eldar',
    '3':'Dark Eldar',
    '4':'Tau',
    '5':'Orks',
    }

#Functions

def ChooseRace(races):
    chosenRace = random.choice(list(races.values()))
    return chosenRace

def BuildRaceList(players = 2):

    count = 0
    racelist = []
    while count < players:
        racelist.append(ChooseRace(races))
        count += 1

    return racelist

def SelectFromTxtFile():
#Function will return a random word from word_list.txt

    wordList = open("data/vocab.txt").readlines()

    chosenWord = random.choice(wordList)
    return chosenWord

#Run Logic

@client.event
async def on_ready():
    print('Reporting for duty sir!... {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user: 
        return

    if message.content.startswith('tp match'):
        print('Im on it {0.user}'.format(client))
        await message.channel.send('I have completed the task... \n  '+ str(BuildRaceList()))

    if message.content.startswith('tp qoute'):
        await message.channel.send(SelectFromTxtFile())

    if message.content.startswith('tp help'):
        await message.channel.send('Help File Here.')

    else:
        await message.channel.send('My will falters.')

#Execute Server

print("Debug" + " " + str(ChooseRace))
client.run('NzA5ODcwMzkwMjA1MzQ5OTUx.XrsNBQ.xZpu2bBRznl_XlDFQ5vNX4jl74Y')


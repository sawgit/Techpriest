import discord
import random

client = discord.Client()

#Data

debug = 0
pathRaceList = 'data/races.txt'
pathVocab = 'data/vocab.txt'
pathSecretBotKey = 'secrets/appKey.txt'

races = open(pathRaceList).readlines()
secretBotKey = open(pathSecretBotKey).read()

#Functions

def ChooseRace(races):
    chosenRace = random.choice(races)
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

    wordList = open(pathVocab).readlines()

    chosenWord = random.choice(wordList)
    return chosenWord

#Run Logic

@client.event
async def on_ready():
    print('\n  ==== Techpriest Discord Bot v0.1 ==== \n\n Thankyou machine spirit for our safe arrival. \n {0.user}'.format(client))
    # await client.send_message('I am honoured that you require my skills... \n type "tp help" for commands.')

@client.event
async def on_message(message):
    if message.author == client.user: 
        return

    elif message.content.startswith('tp match'):
        await message.channel.send('I have completed the task... \n  '+ str(BuildRaceList()))

    elif message.content.startswith('tp quote'):
        await message.channel.send(SelectFromTxtFile())

    elif message.content.startswith('tp help'):
        await message.channel.send(str(open("data/help.txt").read()))

    elif message.content.startswith('tp ldr'):
        await message.channel.send('***Coming soon to a chat near you***')

#Execute Server

print("Debug" + " " + str(ChooseRace))
client.run(secretBotKey)


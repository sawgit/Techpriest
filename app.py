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

def BuildRaceList(players = 2, teams = 2):
#Function will distribute a number of players to a set number of teams.

    def calcTeamsize(players, teams):
    #Function will recieve a number of players and divide that by the number of teams.
    #Will produce an error if number is not divisable.
        modulo = teams / players

        if isinstance(modulo, float) == True:
            modulo = 0

        return modulo

    playerCount = 0
    teamSize = calcTeamsize(players, teams)
    teamList0 = []
    teamList1 = []
    teamList2 = []

    while playerCount < players:
        print("Debug: " + str(playerCount) + str(players) + str(teamSize))

        while playerCount < teamSize:
            print("DebugX02: " + str(playerCount) + str(players))
            teamList0.append(ChooseRace(races))
            playerCount += 1

        while playerCount < teamSize:
            print("DebugX03: " + str(playerCount) + str(players))
            teamList1.append(ChooseRace(races))
            playerCount += 1

        while playerCount < teamSize:
            teamList2.append(ChooseRace(races))
            playerCount += 1

    #This section will receive the individual racelists, collate then format them for output.
    formattedOutput = 'Team 1: ' + str(teamList0) + 'Team 2: ' + str(teamList1) + 'Team 3: ' + str(teamList2)

    return formattedOutput

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
        await message.channel.send('I have completed the task... \n  '+ BuildRaceList())

    elif message.content.startswith('tp quote'):
        await message.channel.send(SelectFromTxtFile())

    elif message.content.startswith('tp help'):
        await message.channel.send(str(open("data/help.txt").read()))

    elif message.content.startswith('tp ldr'):
        await message.channel.send('***Coming soon to a chat near you***')

#Execute Server

print("Debug" + " " + str(ChooseRace))
client.run(secretBotKey)


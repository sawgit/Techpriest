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

def BuildRaceArray(playerNum):

    def ChooseRace(races):
        chosenRace = random.choice(races)
        return chosenRace

    playerArray = []
    i = 0

    while i < playerNum:
        
        playerArray.append(ChooseRace(races))
        i += 1

    return playerArray

def BuildRaceList(raceArray, teamSize):
#Function will distribute a number of players to a set number of teams.

    print("debugBRL01: " + str(raceArray))

    def chunks(l, n):
        #"""Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    #random.shuffle(n)

    formattedOutput = list(chunks(raceArray, teamSize))
    # [['B', 'H', 'G'], ['D', 'A', 'C'], ['E', 'F', 'I'], ['J', 'K']]

    print("debugBRL02: " + str(formattedOutput))

    return formattedOutput

def SelectFromTxtFile():
#Function will return a random word from word_list.txt

    wordList = open(pathVocab).readlines()

    chosenWord = random.choice(wordList)
    return chosenWord

def OutputRaceList(list):

    outputString = ""
    teamCount = 1

    for i in range(len(list)):
        for x in list[i]:
            outputString = outputString + "```" + "Team " + str(teamCount) + ": " + str(x) + "```"
        teamCount += 1
        #outputString = outputString + "```vs```"

    return outputString

#Run Listeners and chat logic.

@client.event
async def on_ready():
    print('\n  ==== Techpriest Discord Bot v0.1 ==== \n\n Thankyou machine spirit for our safe arrival. \n {0.user}'.format(client))
    # await client.send_message('I am honoured that you require my skills... \n type "tp help" for commands.')

@client.event #Creates listener.
async def on_message(message):
    if message.author == client.user: 
        return

    elif message.content.startswith('tp match'):
        await message.channel.send('I have completed the task... \n  ' + OutputRaceList(BuildRaceList(BuildRaceArray(6), 3)))

    elif message.content.startswith('tp quote'):
        await message.channel.send(SelectFromTxtFile())

    elif message.content.startswith('tp help'):
        await message.channel.send(str(open("data/help.txt").read()))

    elif message.content.startswith('tp ldr'):
        await message.channel.send('***Coming soon to a chat near you***')

#Execute Server

client.run(secretBotKey)

#


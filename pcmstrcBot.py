import urllib.request

##------------------------VARIABLES AND DECLARATIONS------------------------##

#bot token for Telegram Bot API
botToken = "bot309515186:AAEK6vQS-rPR-O3ahDCYclc9e_7-MwRBZDc"

#Telegram API bot website
url = "https://api.telegram.org/"

#Bot URL
botURL = url + botToken

#COMMANDS
getMeCMD = "/getMe"
getUpdateCMD = "/getupdates"
sendMessageCMD = "/sendmessage"

#CHAT IDs
pcmstrcID = "-1001095327132"
caroRodriguezID = "8869779"
chemaID = "275473930"
julioID = "252442498"
joshuaID = "222735823"
davidID = "295691591"


##------------------------METHODS------------------------##

def sendMessage(message , chatID):
    link = botURL + sendMessageCMD + "?chat_id=" + chatID + "&text=" + message
    with urllib.request.urlopen(link) as response:
        update = response.read()

        print(update)

        a = "asdfasdfasdfasdfasdf"


def getUpdate():
    link = botURL + getUpdateCMD + "?limit=1000"
    with urllib.request.urlopen(link) as response:
        update = response.read()

    print(update)
    b = "ioagoiqgpioqbgioq"

"""
    update = update[::-1]

    updateLen = len(update)

    for i in range(updateLen):
        if update[i] == "d":
            if update[i+1] == "i":
                if update[i+2] == "_":
                    if update[i+3] == "e":
                        if update[i+4] == "t":
                            update = update[i+4::-1]
                            print(update)





    print("error")

"""

##------------------------EXECUTE------------------------##

#sendMessage("testerino" , pcmstrcID)

getUpdate()

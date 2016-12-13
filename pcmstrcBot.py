import urllib.request
import json
from collections import OrderedDict
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
serruchoID = "-151480946"

caroRodriguezID = "8869779"
chemaID = "275473930"
julioID = "252442498"
joshuaID = "222735823"
davidID = "295691591"


##------------------------METHODS------------------------##

def sendMessage(message , chatID):
    link = botURL + sendMessageCMD + "?chat_id=" + chatID + "&text=" + message
    with urllib.request.urlopen(link) as response:
        update = response.read().decode('utf-8')

        jsonUpdate = json.loads(update)

        print(jsonUpdate)

def getUpdate():
    link = botURL + getUpdateCMD + "?limit=5"
    with urllib.request.urlopen(link) as response:
        update = response.read().decode('utf-8')

    jsonUpdate = json.loads(update)
    print(json.dumps(jsonUpdate , sort_keys=False , indent=1))




##------------------------EXECUTE------------------------##

#sendMessage("chema, please program me, i will be ur sex slave" , pcmstrcID)

getUpdate()

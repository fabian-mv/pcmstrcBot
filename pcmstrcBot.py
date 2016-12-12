import urllib.request

##------------------------VARIABLES AND DECLARATIONS------------------------##

#bot token for Telegram Bot API
botToken = "309515186:AAEK6vQS-rPR-O3ahDCYclc9e_7-MwRBZDc"

#Telegram API bot website
url = "https://api.telegram.org/bot" + botToken

#COMMANDS
getMeCMD = "/getMe"
updateCMD = "/getupdates"
sendmessageCMD = "/sendmessage"

#CHAT IDs
pcmstrcID = "-1001095327132"
caroRodriguezID = "8869779"
chemaID = "275473930"
julioID = "252442498"
joshuaID = "222735823"
davidID = "295691591"


##------------------------METHODS------------------------##

def sendMessage(message , chatID):
   link = url + sendmessageCMD + "?chat_id=" + chatID + "&text=" + message
   with urllib.request.urlopen(link) as response:
      update = response.read()

   print(update)


##------------------------EXECUTE------------------------##

sendMessage("test, you are a faggot lol" , davidID)

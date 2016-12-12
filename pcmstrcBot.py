import urllib.request


#bot token for Telegram Bot API
botToken = "309515186:AAEK6vQS-rPR-O3ahDCYclc9e_7-MwRBZDc"

#Telegram API bot website
url = "https://api.telegram.org/bot" + botToken

#COMMANDS
getMe = "/getMe"
update = "/getupdates"
sendmessage = "/sendmessage"

#CHAT IDs
pcmstrc = "-1001095327132"



with urllib.request.urlopen(url + sendmessage + "?chat_id=-1001095327132&text=test") as response:
   update = response.read()



print(update)
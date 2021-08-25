'''
--|~|--|~|--|~|--|~|--|~|--|~|--

██  ████        ██████        ██
████    ██     ██           ████
██      ██   ████████     ██  ██
████████       ██       ██    ██
██             ██       █████████
██             ██             ██
██
.codé en : UTF-8
.langage : python 3
--|~|--|~|--|~|--|~|--|~|--|~|--
'''

#import
import discord, sys

# bot
client = discord.Client()


@client.event
async def on_ready():
    ch = client.get_channel(880053539110522910)
    messages = await ch.history(limit=1).flatten()
    for each_message in messages:
        drmsg = each_message.content
    temp = ""
    for guild in client.guilds: temp += guild.name+": " + str(guild.member_count)+" membres" + "\n"
    temp = temp.split("\n")

    # saute de ligne automatique
    drmsgn = drmsg
    drmsg = list(drmsg)
    if len(drmsg) > 20:
        drmsgn = ""
        for x in range(len(drmsg)):
            if x > 56:
                drmsgn += "."
            else:
                drmsgn += drmsg[x]
            if x == 20 or x == 39:
                if len(drmsg) != 21 and len(drmsg) != 40:
                    drmsgn += "\n| "
            


    msg = temp[0] +  "\nnvifgudhihgifukdh" + drmsgn
    fil = open("/home/pi/nas-kit-master/data.txt", "w")
    fil.write(str(msg))
    fil.close()
    sys.exit()


client.run("ODY4MTg2NTAwOTgwOTU3MjM1.YPr_rw.WKRq1tM4Bw_4a4F5qszDd5XAq74")
import os
import random
import discord
import csv
import sys
import decimal
import pandas as pd
import aiohttp
import textwrap
import asyncio

from discord.ext import commands


msglist = []



TOKEN = 'put bot token here'

with open('prefix.txt', 'r') as pfx:
    prefix = pfx.readline()
    print('The prefix is', prefix)


bot = commands.Bot(command_prefix=prefix, help_command=None)

content = 0

rarechannel = 786751841374830604



'''
def await ctx.send(response):
    await ctx.send(response)
    print(f'responded with {response}')
'''

def balance(ctx):
    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    usrbalance = alldata[0]
    return(int(usrbalance))


def writebalance(ctx, newbalance):
    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    alldata[0] = f'{newbalance}\n'

    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(alldata)


def addbalance(ctx, newbalance):
    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    alldata[0] = f'{int(alldata[0]) + newbalance}\n'
    alldata[1] = f'{int(alldata[1]) + newbalance}\n'

    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(alldata)


def subtractbalance(ctx, newbalance):
    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    alldata[0] = f'{int(alldata[0]) - newbalance}\n'

    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(alldata)

def formatprice(oldprice):
    num = int(oldprice)
    num = decimal.Decimal(num)/100
    num = "${:,.2f}".format(num)
    num = str(f'{num}')
    return(num)

def output(ctx):
    print(f'Command {ctx.command.qualified_name} from {bot.get_user(ctx.author.id)} in {ctx.channel.name}')


def getbadge(ctx):
    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    badgenum = alldata[3]
    return(int(badgenum))


















@bot.event
async def on_ready():
    with open('status.txt', 'r') as pfx:
        status = pfx.readline()
    await bot.change_presence(activity=discord.Game(name=status))
    print('Status is', status)
    
    print(f'{bot.user.name} has connected to Discord!')

    with open('lastchannel.txt', 'r') as pfx:
        lastchannel = int(pfx.readline())
        channel = bot.get_channel(lastchannel)
    
    await channel.send('The bot is online!')


    

@bot.command(name='test')
async def test(ctx):
    output(ctx)
    
    await ctx.send('frick off and leave me alone')



@bot.command(name='prefix')
async def prefixchange(ctx, new_pfx):
    output(ctx)

    if ctx.author.id == 256247035265548298:
        if len(new_pfx) > 1:
            await ctx.send('The prefix must be only one character')
        else:

            with open('prefix.txt', 'w') as pfx:
                pfx.seek(0)
                pfx.write(new_pfx)

            with open('prefix.txt', 'r') as pfx:
                prefix = pfx.readline()
            
            bot = commands.Bot(command_prefix=prefix, help_command=None)
            print('The prefix has been changed to', prefix)
            await ctx.send('The prefix has been changed.')
    else:
        await ctx.send(f'You are not a bot administrator')


@bot.command(name='GameStatus')
async def statuschange(ctx, *, new_status):
    output(ctx)

    with open('status.txt', 'w') as pfx:
        pfx.truncate(0)
        pfx.seek(0)
        pfx.write(new_status)

    with open('status.txt', 'r') as pfx:
        status = pfx.readline()
    
    await bot.change_presence(activity=discord.Game(name=status))
    print('Status has been changed to', status)
    await ctx.send('Status has been changed.')

@bot.command(name='wisdom')
async def wisdom(ctx):
    output(ctx)
    with open('wisdom.csv') as f:
        reader = csv.reader(f)
        chosen_row = random.choice(list(reader))
        chosen_row = str(chosen_row)
        chosen_row = chosen_row.replace("'",'')
        chosen_row = chosen_row.replace("[",'')
        chosen_row = chosen_row.replace("]",'')
        chosen_row = chosen_row.replace('"','')
        await ctx.send(chosen_row)


@bot.command(name='addwisdom')
async def addwisdom(ctx, *, newentry):
    output(ctx)
    added = 0
    with open('wisdom.csv', 'r') as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                for j, column in enumerate(row):
                    if newentry in column:
                        added = 1
    
    if added == 1:
        await ctx.send(f'That wisdom has already been added.')
    else:
        if '@' in newentry:
            await ctx.send(f'That wisdom is not allowed')
        else:
            print('received new wisdom "',newentry,'"')
            with open('wisdom.csv','a') as fd:
                fd.write(f"\n{newentry}")
            await ctx.send(f'Added wisdom "{newentry}"')

@bot.command(name='r')
async def restart(ctx):
    output(ctx)
    print('Received command to restart')
    await ctx.send('restarting...')
    print()

    with open('lastchannel.txt', 'w') as pfx:
        pfx.truncate(0)
        pfx.seek(0)
        lastchannel = str(ctx.message.channel.id)
        pfx.write(lastchannel)
    exit()


@bot.command(name='help')
async def help(ctx):
    output(ctx)

    em = discord.Embed(title="Help", description="I am the real Mr. Lauchu, you have absolutley no reason to suspect that I am not", colour= 3447003)
    
    em.add_field(name=f"{prefix}test", value="Test if the bot is working correctly", inline=False)

    em.add_field(name=f"{prefix}prefix [new prefix]", value=f'Change the bot`s command prefix, currently "{prefix}"', inline=False)

    em.add_field(name=f"{prefix}GameStatus [new game status]", value="Set the bot's current game status", inline=False)

    em.add_field(name=f"{prefix}wisdom", value='If you are ever in need of wisdom and direction in life, simply consult Mr. Lauchu.', inline=False)

    em.add_field(name=f"{prefix}addwisdom [new wisdom here]", value="Contribute to the bot's pool of knowledge ($addwisdom your wisdom here)", inline=False)

    em.add_field(name=f"{prefix}meme", value='Grabs a random meme from Reddit', inline=False)

    em.add_field(name=f"{prefix}echo", value='Make the bot say something', inline=False)
    
    em.add_field(name=f"{prefix}connectfour", value='Play the classic game connect four, right in a discord channel!', inline=False)

    em.add_field(name=f"{prefix}store", value="Access the store to buy items and special roles (Currently the only ways to get money are to be active on the server or open cases, however I will add more ways to get money such as winning games of connect four and getting bonuses from admins for being helpful members, but you start with $100, and I'll add more items soon)", inline=False)

    em.add_field(name=f"{prefix}bank", value='Check your current balance as well as how much total money you have earned and spent', inline=False)

    em.add_field(name=f"{prefix}case", value='Open a CS:GO weapon case. (Yes, this is gambling, but I have tweaked the odds so they are mostly fair. You start with 10 free cases.)', inline=False)

    em.add_field(name=f"{prefix}pay @[user] [amount]", value='Send money to another member, no questions asked about what it is for.', inline=False)

    await ctx.send(embed=em)

    print('responded with help embed')

chosen_skin = 'none'

@bot.command(name='meme')
async def meme(ctx):
    output(ctx)
    subreddits = ['dankmemes','memes','memeeconomy']
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f'https://www.reddit.com/r/{random.choice(subreddits)}/hot.json?sort=hot') as r:
            res = await r.json()
            post = random.randint(0, 25)
            header = res['data']['children'] [post]['data']['title']
            header = str(header)
            header = textwrap.fill(header, 38)
            embed = em = discord.Embed(title=header,description="", colour= 0xffffff)
            embed.set_image(url=res['data']['children'] [post]['data']['url'])
            await ctx.send(embed=embed)
            print('sent meme')

@bot.command(name='nuke')
async def nuke(ctx):
    output(ctx)
    if ctx.author.id == 256247035265548298:
        await ctx.channel.clone(reason="none")
        await ctx.channel.delete()
    else:
        await ctx.send(f'You are not a bot administrator')

@bot.command(name='echo')
async def echo(ctx, *, content):
    output(ctx)
    if '@everyone' in content:
        await ctx.send(f'{ctx.author.mention} sucks donkey dick')
        return
    if '@here' in content:
        await ctx.send(f'{ctx.author.mention} sucks donkey dick')
        return
    await ctx.channel.purge(limit=1)
    await ctx.send(content)


#async def writedata():
    '''authordata[0] = f'{str(authorhp)}\n'
    authordata[1] = f'{str(authorslapcool)}\n'
    authordata[2] = f'{str(authorhealcool)}\n'

    slapdata[0] = f'{str(slaphp)}\n'
    slapdata[1] = f'{str(slapslapcool)}\n'
    slapdata[2] = f'{str(slaphealcool)}\n'

    with open(f'data/{author}.txt', 'w') as file:
            file.writelines(authordata)
    
    with open(f'data/{slapid}.txt', 'w') as file:
            file.writelines(slapdata)'''



@bot.command(name='connectfour')
async def connectfour(ctx):
    
    output(ctx)
    rows = 10
    columns = 10
    noColumns = 10
    noRows = 10
    winLength = 4

    def isInteger(n):
        result = True
        try:
            int(n)
            result = True
        except ValueError:
            print("That was not an Integer!")
            result = False
        return result

    def inputInLimitCheck(x,min, max):
        response = True
        if x < min:
            print("That is too low! Must be at least %d" % min)
            response = False
        elif x > max:
            print("That is too high! Cannot be higher than %d" % max)
            response = False
        return response

    def createGrid(columns, rows) :
        grid = []
        for row in range(0,rows):
            newRow = []
            for column in range(0,columns):
                newRow.append(0)
            grid.append(newRow)
        return grid

    def printGrid(aGrid) :
        topline = "|"
        #for n in range(0,len(aGrid)):
            #topline += "-" + str(n) + "-|"
        #print(topline)
        lines = ''
        for row in aGrid:
            line = "  ⠀ |  "
            for x in row:
                if (x == 0) :
                    x = "⬛️"
                elif (x == 1) :
                    x = "🔴"
                elif (x == 2) :
                    x = "🟡"
                line = line + str(x) + "  |  "
            lines += f'{line}\n'
        return lines

    def dropCoin(noColumns, grid, player, slotnum) :
        global selectedColumn
        selectedColumn =  slotnum
        if isValidCoinDrop(selectedColumn, grid)==False :
            newGrid = grid
        else :
            for x in range(1,len(grid)+1) :
                if (x==len(grid)):
                    grid[x-1][selectedColumn] = player
                    newGrid = grid
                elif (grid[x][selectedColumn]!=0):
                    grid[x-1][selectedColumn] = player
                    newGrid = grid
                    break
        return newGrid

    def isValidCoinDrop(columnNo, grid):
        result = True
        if (grid[0][columnNo]!=0) :
            print("Column is already full!")
            result = False
        return result

    def horizontalWinCheck(x,y,grid, player):
        streak = 0
        xleft = x
        xright = x + 1
        while (xleft>=0):
            if grid[y][xleft] == player:
                streak += 1
                xleft -= 1
            else:
                break
        while (xright<len(grid[0])):
            if grid[y][xright] == player:
                streak += 1
                xright += 1
            else:
                break
        return streak

    def verticalWinCheck(x,y,grid,player):
        streak = 0
        yup = y
        ydown = y + 1
        while (yup>=0):
            if grid[yup][x] == player:
                streak += 1
                yup -= 1
            else:
                break
        while (ydown<len(grid)):
            if grid[ydown][x] == player:
                streak += 1
                ydown += 1
            else:
                break
        return streak

    def NWSEWinCheck(x,y,grid,player):
        streak = 0
        yup = y
        ydown = y + 1
        xleft = x
        xright = x + 1
        while (yup>=0) and (xleft>=0):
            if grid[yup][xleft] == player:
                streak += 1
                yup -= 1
                xleft -= 1
            else:
                break
        while (ydown<len(grid)) and (xright<len(grid[0])):
            if grid[ydown][xright] == player:
                streak += 1
                ydown += 1
                xright += 1
            else:
                break
        return streak

    def NESWWinCheck(x,y,grid,player):
            streak = 1
            yup = y
            ydown = y + 1
            xleft = x - 1
            xright = x
            while (yup>=0) and (xright<len(grid[0])):
                if grid[yup][xleft] == player:
                    streak += 1
                    yup -= 1
                    xright += 1
                else:
                    break
            while (ydown<len(grid)) and (xleft>=0):
                if grid[ydown][xleft] == player:
                    streak += 1
                    ydown += 1
                    xleft -= 1
                else:
                    break
            return streak

    def winCheck(player, selectedColumn, grid, winlength):
        winner = 0
        x = selectedColumn
        y = findLastRow(selectedColumn, grid)
        win = False
        if (horizontalWinCheck(x,y, grid, player)>=winlength) :
            win = True
        elif (verticalWinCheck(x,y,grid,player)>=winlength) :
            win = True
        elif (NESWWinCheck(x,y,grid,player)>=winlength) :
            win = True
        elif (NWSEWinCheck(x,y,grid,player)>=winlength) :
            win = True
        if (win == True):
            print("Player %d Wins!" % player)
            
        return win

    def drawCheck(grid):
        result = True
        for x in grid[0]:
            if x == 0:
                result = False
                break
        if result == True:
            print("The Game is a Draw!")
            ctx.send("The Game is a Draw!")
        return result

    def findLastRow(selectedColumn, grid) :
        for n in range(0,len(grid)):
            if grid[n][selectedColumn] != 0:
                result = n
                break
        return result

    isbot = 1

    startmsg = ctx.message

    await startmsg.add_reaction("✅")

    hostid = str(ctx.author.id)

    
    
    

    grid = createGrid(noColumns, noRows)
    reciept = [grid, winLength]

    grid = reciept[0]
    winlength = reciept[1]
    printGrid(grid)

    confmessage = await ctx.send(f"Waiting for player to accept game...")

    def checkone(reaction, user):
        return user != ctx.author

    print('started checking reactions')

    
    try:
        print('loop started')
        reaction, user = await bot.wait_for("reaction_add", timeout=120, check=checkone)
        # waiting for a reaction to be added - times out after x seconds
        
        ('reaction received')


        if str(reaction.emoji) == "✅":
            guestid = str(user.id)
            print('reaction received')


    except asyncio.TimeoutError:
        await ctx.send('❌ Player took too long to make a move')
        return
        # ending the loop if user doesn't react after x seconds

    print('ended first loop')
    
    
    await confmessage.edit(content=f"<@!{guestid}> has accepted the match!")
    
    
    
    
    
    
    await confmessage.add_reaction("1️⃣")
    await confmessage.add_reaction("2️⃣")
    await confmessage.add_reaction("3️⃣")
    await confmessage.add_reaction("4️⃣")
    await confmessage.add_reaction("5️⃣")
    await confmessage.add_reaction("6️⃣")
    await confmessage.add_reaction("7️⃣")
    await confmessage.add_reaction("8️⃣")
    await confmessage.add_reaction("9️⃣")
    await confmessage.add_reaction("🔟")
    noColumns = len(grid[0])
    player = 2
    complete = False
    
    await confmessage.edit(content=f"<@!{hostid}>'s turn\n\n  ⠀ |  1️⃣  |  2️⃣  |  3️⃣  |  4️⃣  |  5️⃣  |  6️⃣  |  7️⃣  |  8️⃣  |  9️⃣  |  🔟  |\n{printGrid(grid)}")

    print('reactions done')

    isbot = 1
    
    currentplayer  = hostid
    
    while(complete==False) :
        
        try:

            loop = 1
            while True:
                try:
                    
                    print('started checking for reactions in main board')
                    loop += 1

                    if loop > 50:
                        await ctx.send('Loop length exceeded, quitting loop')
                        return
                    reaction, user = await bot.wait_for("reaction_add", timeout=120)
                    # waiting for a reaction to be added - times out after x seconds

                    print('reaction received')
                    #if isbot == 1:
                        #isbot = 0
                        #continue
                    if str(user.id) != str(currentplayer):
                        print(user.id)
                        print(currentplayer)
                        #await ctx.send('❌ It is not your turn')
                        await confmessage.remove_reaction(reaction, user)
                        continue

                    if str(reaction.emoji) == "1️⃣":
                        usermove = 0
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "2️⃣":
                        usermove = 1
                        await confmessage.remove_reaction(reaction, user)
                        break
                        
                    elif str(reaction.emoji) == "3️⃣":
                        usermove = 2
                        await confmessage.remove_reaction(reaction, user)
                        break
                    
                    elif str(reaction.emoji) == "4️⃣":
                        usermove = 3
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "5️⃣":
                        usermove = 4
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "6️⃣":
                        usermove = 5
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "7️⃣":
                        usermove = 6
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "8️⃣":
                        usermove = 7
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "9️⃣":
                        usermove = 8
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "🔟":
                        usermove = 9
                        await confmessage.remove_reaction(reaction, user)
                        break

                    elif str(reaction.emoji) == "🔄":
                        await confmessage.remove_reaction(reaction, user)
                        continue

                        
                except asyncio.TimeoutError:
                    await ctx.send('❌ Player took too long to make a move')
                    break
                    # ending the loop if user doesn't react after x seconds


            
            #print("It is Player %d Turn!" % player)
            grid = dropCoin(noColumns, grid, player, usermove)
            complete = winCheck(player, selectedColumn, grid, winlength)
            
            player = (player%2)+1
            if player == 1:
                currentplayer = guestid
                pturn = f"<@!{guestid}>'s turn"
            else:
                currentplayer = hostid
                pturn = f"<@!{hostid}>'s turn"
            
            if (complete==True):
                if player == 1:
                    await ctx.send(f"<@!{hostid}> won $200!")
                    await confmessage.edit(content=f"<@!{hostid}> won against <@!{guestid}>!\n\n  ⠀ |  1️⃣  |  2️⃣  |  3️⃣  |  4️⃣  |  5️⃣  |  6️⃣  |  7️⃣  |  8️⃣  |  9️⃣  |  🔟  |\n{printGrid(grid)}")
                    try:
                        with open(f'bank/{str(hostid)}.txt', 'r') as file:
                            pass
                    except:
                        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
                        with open(f'bank/{str(hostid)}.txt', 'w') as file:
                            file.writelines(newdata)

                    with open(f'bank/{str(hostid)}.txt', 'r') as file:
                        alldata = file.readlines()
                    
                    alldata[0] = f'{int(alldata[0]) + 20000}\n'
                    alldata[1] = f'{int(alldata[1]) + 20000}\n'

                    with open(f'bank/{str(hostid)}.txt', 'w') as file:
                            file.writelines(alldata)
                else:
                    await ctx.send(f"<@!{guestid}> won $200!")
                    await confmessage.edit(content=f"<@!{guestid}> won against <@!{hostid}>!\n\n  ⠀ |  1️⃣  |  2️⃣  |  3️⃣  |  4️⃣  |  5️⃣  |  6️⃣  |  7️⃣  |  8️⃣  |  9️⃣  |  🔟  |\n{printGrid(grid)}")
                    try:
                        with open(f'bank/{str(guestid)}.txt', 'r') as file:
                            pass
                    except:
                        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
                        with open(f'bank/{str(guestid)}.txt', 'w') as file:
                            file.writelines(newdata)

                    with open(f'bank/{str(guestid)}.txt', 'r') as file:
                        alldata = file.readlines()
                    
                    alldata[0] = f'{int(alldata[0]) + 20000}\n'
                    alldata[1] = f'{int(alldata[1]) + 20000}\n'

                    with open(f'bank/{str(guestid)}.txt', 'w') as file:
                            file.writelines(alldata)
                
            
            if (complete!=True):
                
                result = True
                for x in grid[0]:
                    if x == 0:
                        result = False
                        break
                if result == True:
                    print("The Game is a Draw!")
                    await ctx.send
                    pass
                
                complete = result
            
            
                topline = "|"
                #for n in range(0,len(aGrid)):
                    #topline += "-" + str(n) + "-|"
                #print(topline)
                lines = ''
                for row in grid:
                    line = "  ⠀ |  "
                    for x in row:
                        if (x == 0) :
                            x = "⬛️"
                        elif (x == 1) :
                            x = "🔴"
                        elif (x == 2) :
                            x = "🟡"
                        line = line + str(x) + "  |  "
                    lines += f'{line}\n'
                    #print(lines)
                
                

                #boardem = discord.Embed(title="Connect Four", description=lines, colour= 3447003)
                await confmessage.edit(content=f"{pturn}\n\n  ⠀ |  1️⃣  |  2️⃣  |  3️⃣  |  4️⃣  |  5️⃣  |  6️⃣  |  7️⃣  |  8️⃣  |  9️⃣  |  🔟  |\n{printGrid(grid)}")
        except:
            pass
    


chosen_skin = 'none'

#case command
@bot.command(name='case')
async def case(ctx):

    output(ctx)

    try:
        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
            pass
    except:
        newdata = ['100\n','100\n','10\n','0\n','0\n','0\n','0\n','0\n']
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(newdata)
    

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    cases = int(alldata[2])

    if cases == 0:
        await ctx.send('You are out of cases. You can buy more at the store.')
        print(cases)
    if cases > 0:
        print(cases)
        cases -= 1
        alldata[2] = f'{cases}\n'
        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
            file.writelines(alldata)

    
        #generate number
        probability = random.randrange(0, 183)

        rare = 0

        #probability = 182

        print(probability)

        loop = 0

        colors = [0xffffff, 0x0099cc, 0x0033cc, 0x6600cc, 0xff00ff, 0xff0000, 0xffcc00]

        

        #get rarity, remove unnessesary characters, skin name, and define embed with colors
        if probability < 50:
            rarity = 'consumer'
            with open('skins_consumer.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')
            
            np = random.randrange(30,500)

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            
            colournum = 0
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour=colors[colournum])    
        elif probability < 130:
            rarity = 'industrial'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')

            np = random.randrange(30,500)

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            
            colournum = 1
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
        elif probability < 155:
            rarity = 'Mil-Spec'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')

            np = random.randrange(300,1000)
            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            colournum = 2
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
            
        elif probability < 170:
            rarity = 'restricted'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            colournum = 3
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
            
            np = random.randrange(700,2000)
        elif probability < 180:
            rarity = 'Classified'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            colournum = 4
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
            
            np = random.randrange(1000,10000)

        elif probability < 183:
            rarity = 'Covert'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            colournum = 5
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
            
            np = random.randrange(5000,30000)

        elif probability < 184:
            rarity = 'Knife'
            with open(f'{rarity}.csv') as f:
                reader = csv.reader(f)
                chosen_skin = random.choice(list(reader))
                chosen_skin = str(chosen_skin)
                chosen_skin = chosen_skin.replace("'",'')
                chosen_skin = chosen_skin.replace("[",'')
                chosen_skin = chosen_skin.replace("]",'')
            
            np = random.randrange(30000,300000)

            print(chosen_skin)

            skin_name = chosen_skin
            skin_name = skin_name.replace(".png",'')

            print(skin_name)

            
            colournum = 6
            em = discord.Embed(title="CS:GO Case⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
            rare = 1
        else:
            print('bruh')


        
        

        price = 'No Price Available'


        #get price from file
        try:
            with open('fullprice.csv', 'r') as f:
                reader = csv.reader(f)
                for i, row in enumerate(reader):
                    for j, column in enumerate(row):
                        if skin_name in column:
                            print((i,j))
                            price = row[1]
                            print(price)
        except:
            price = np

        if price == 'No Price Available':
            price = np

        price = str(price)

        price = price.replace(',','')

        price = int(price)

        #generate float and format price
        try:
            fl = random.randrange(0, 800000)

            finalfl = decimal.Decimal(fl)/1000000

            prfl = 1 - finalfl

            prfl = prfl * 1000000


            price = int(price)
            price= price * 3
            price= price * prfl
            price = decimal.Decimal(price)/100000000
            price = round(price, 2)
            price = str("${:,.2f}".format(price))
            price = str(f'{price}')
        except:
            pass
        else:
            pass
        
        #add fields
        em.add_field(name="Rarity:", value=rarity, inline=False)
        em.add_field(name="Price:", value=price, inline=False)
        em.add_field(name="Wear:", value=finalfl, inline=False)
        em.add_field(name="Cases left:", value=cases, inline=False)
        await ctx.send(embed=em, file=discord.File(f'{rarity}/{chosen_skin}'))
        #await ctx.send(file=discord.File(f'{rarity}/{chosen_skin}'))
        
        price = price.replace(',','')

        #price integer for storage
        if price != "No Price Available":
            intprice = price.replace(',','')
            intprice = intprice.replace('.','')
            intprice = intprice.replace('$','')
            print(intprice)
            intprice  = int(intprice)
            if intprice > 30000:
                rare = 1
        

        prettyprice = formatprice(intprice)


        #rare skin in rare skin channel
        if rare == 1:
            chl = bot.get_channel(rarechannel)
            await chl.send(f'{ctx.author.mention} got a {rarity} {skin_name} worth {prettyprice} in <#{ctx.message.channel.id}>', embed=em, file=discord.File(f'{rarity}/{chosen_skin}'))
        


        #save data

        #setup file
        try:
            with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                pass
        except:
            newdata = ['0\n','0\n','0\n','0\n','0\n','0\n','0\n','0\n']
            with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                file.writelines(newdata)
        else:

            #add earnings to bank file
            with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                newearnings = file.readlines()

            #print(newearnings[0])


            try:
                newearnings[0] = f'{int(newearnings[0]) + intprice}\n'
                newearnings[1] = f'{int(newearnings[1]) + intprice}\n'
            except:
                print('No Price')
                return

            with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                file.writelines(newearnings)


            with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                totalwinnings = file.readlines()

            #print(totalwinnings[0])


            try:
                totalwinnings[0] = f'{int(totalwinnings[0]) + intprice}\n'
            except:
                print('No Price')
                return

            with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                file.writelines(totalwinnings)





            with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                mostvaluable = file.readlines()

            #print(mostvaluable[1])

            if intprice > int(mostvaluable[1]):
                mostvaluable[1] = f'{str(intprice)}\n'

                with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                    file.writelines(mostvaluable)

                with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                    storedat = file.readlines()

                storedat[2] = str(f'{rarity}\n')
                storedat[3] = str(f'{skin_name}\n')
                storedat[4] = str(f'{chosen_skin}\n')
                storedat[5] = str(f'{finalfl}\n')
                storedat[7] = str(f'{colournum}\n')

                with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                    file.writelines(storedat)
            
            with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
                totalcases = file.readlines()

            totalcases[6] = f'{int(totalcases[6]) + 1}\n'
            
            with open(f'data/{str(ctx.author.id)}.txt', 'w') as file:
                file.writelines(totalcases)


        
@bot.command(name='casestats')
async def casestats(ctx):
    output(ctx)
    with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
        stats = file.readlines()
    
    print(stats)

    colors = [0xffffff, 0x0099cc, 0x0033cc, 0x6600cc, 0xff00ff, 0xff0000, 0xffcc00]

    totalvalue = str(stats[0])
    rawtotal = int(stats[0])
    price= str(stats[1])
    rawprice = int(stats[1])
    rarity = str(stats[2])
    skin_name = str(stats[3])
    chosen_skin = str(stats[4])
    finalfl = str(stats[5])
    totalcases = str(stats[6])
    rawcases = int(stats[6])
    colournum = int(stats[7])


    price = decimal.Decimal(price)/100
    price = "${:,.2f}".format(price)
    price = str(f'{price}')


    totalvalue = decimal.Decimal(totalvalue)/100
    totalvalue = "${:,.2f}".format(totalvalue)
    totalvalue = str(f'{totalvalue}')

    luck = decimal.Decimal(rawtotal)/rawcases
    luck = str(luck)
    luck = str(luck.split('.', 1)[0])

    em2 = discord.Embed(title=f"{ctx.author}'s Case Stats",description='', colour= colors[1])
    em2.add_field(name="Total skin value", value=totalvalue, inline=False)
    em2.add_field(name="Amount of cases opened", value=totalcases, inline=False)
    em2.add_field(name="Most valueable skin", value=skin_name, inline=False)
    em2.add_field(name="Luck", value=luck, inline=False)



    em = discord.Embed(title="Most Valueable Skin⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name, colour= colors[colournum])
    
    
    
    em.add_field(name="Rarity:", value=rarity, inline=False)
    em.add_field(name="Price:", value=price, inline=False)
    em.add_field(name="Wear:", value=finalfl, inline=False)
    await ctx.send(embed=em2)
    path = str(f'{rarity}/{chosen_skin}').replace('\n','')
    await ctx.send(embed=em, file=discord.File(path))


@bot.command(name='bank')
async def bank(ctx):
    output(ctx)
    currentbal = balance(ctx)

    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    cases = int(alldata[2])

    totalearn = int(alldata[1])
    totalspent = int(totalearn) - int(currentbal)

    em = discord.Embed(title="Bank Info", description="", colour= 3447003)
    
    em.add_field(name=f"Current Balance", value=formatprice(currentbal), inline=False)
    em.add_field(name=f"Total Earnings", value=formatprice(totalearn), inline=False)
    #em.add_field(name=f"Total Money Spent", value=formatprice(totalspent), inline=False)
    em.add_field(name=f"Inventory", value=f'Cases: {cases}', inline=False)

    await ctx.send(embed=em)

@bot.event
async def on_message(message):
    
    addbalance(message, 50)

    await bot.process_commands(message)

cooldown = []
@bot.command(name='store')
async def store(ctx):

    global cooldown

    if cooldown.count(ctx.author.id) == 0:
        cooldown.append(ctx.author.id)

        usrbal = balance(ctx)
                
        formattedbalance = formatprice(usrbal)


        em = discord.Embed(title="Store", description="Purchase items and and special roles", colour= 3447003)
        em.add_field(name=f"Current Balance:", value=formattedbalance, inline=False)
        em.add_field(name=f"🎁 - CS:GO Case ($10)", value=f'1 CS:GO weapon case. (Yes, this is gambling, but I have tweaked the odds so they are mostly fair.)', inline=False)
        


        check_role = discord.utils.get(ctx.guild.roles, name= '★ VIP ★')
        if check_role in ctx.author.roles:
            hasVIP = True
        else:
            hasVIP = False
            em.add_field(name=f"⭐ - VIP Access ($2000)", value=f'Grants you access to the VIP lounge as well as other perks', inline=False)


        if getbadge(ctx) == 0:
            em.add_field(name=f"<:Silver:787796126614814720> - Silver Badge ($100)", value=f'Grants you Silver badge.', inline=False)
        elif getbadge(ctx) == 1:
            em.add_field(name=f"<:gold:688558927377727517> - Upgrade Badge to Gold ($500)", value=f'Grants you the Gold badge.', inline=False)
        elif getbadge(ctx) == 2:
            em.add_field(name=f"<:Platinum:787796126119493633> - Upgrade Badge to Platinum ($1,800)", value=f'Grants you the Platinum badge.', inline=False)
        elif getbadge(ctx) == 3:
            em.add_field(name=f"<:Mithril:787796126492655677> - Upgrade Badge to Mithril ($20,000)", value=f'Grants you the Mithril badge.', inline=False)
        elif getbadge(ctx) == 4:
            em.add_field(name=f"<:Ternion:787796127063343154> - Upgrade Badge to Ternion ($50,000)", value=f'Grants you the Ternion badge.', inline=False)

        # getting the message object for editing and reacting

        message = await ctx.send(embed = em)

        

        if not hasVIP:
            await message.add_reaction("⭐")


        await message.add_reaction("🎁")

        def check(reaction, user):
            return user == ctx.author
            # This makes sure nobody except the command sender can interact with the "menu"

        while True:
            
            try:
                
                if getbadge(ctx) == 0:
                    await message.add_reaction('<:Silver:787796126614814720>')
                elif getbadge(ctx) == 1:
                    await message.add_reaction("<:gold:688558927377727517>")
                elif getbadge(ctx) == 2:
                    await message.add_reaction("<:Platinum:787796126119493633>")
                elif getbadge(ctx) == 3:
                    await message.add_reaction("<:Mithril:787796126492655677>")
                elif getbadge(ctx) == 4:
                    await message.add_reaction("<:Ternion:787796127063343154>")
                
                usrbal = balance(ctx)
                
                formattedbalance = formatprice(usrbal)

                print(formattedbalance)
                em = discord.Embed(title="Store", description="Purchase items and and special roles", colour= 3447003)
                em.add_field(name=f"Current Balance:", value=formattedbalance, inline=False)
                em.add_field(name=f"🎁 - CS:GO Case ($10)", value=f'1 CS:GO weapon case. (Yes, this is gambling, but I have tweaked the odds so they are mostly fair.)', inline=False)
                
                

                if not hasVIP:
                    em.add_field(name=f"⭐ - VIP Access ($2,000)", value=f'Grants you access to the VIP lounge as well as other perks', inline=False)

                
                print(getbadge(ctx))
                
                if getbadge(ctx) == 0:
                    em.add_field(name=f"<:Silver:787796126614814720> - Silver Badge ($100)", value=f'Grants you Silver badge.', inline=False)
                elif getbadge(ctx) == 1:
                    em.add_field(name=f"<:gold:688558927377727517> - Upgrade Badge to Gold ($500)", value=f'Grants you the Gold badge.', inline=False)
                elif getbadge(ctx) == 2:
                    em.add_field(name=f"<:Platinum:787796126119493633> - Upgrade Badge to Platinum ($1,800)", value=f'Grants you the Platinum badge.', inline=False)
                elif getbadge(ctx) == 3:
                    em.add_field(name=f"<:Mithril:787796126492655677> - Upgrade Badge to Mithril ($20,000)", value=f'Grants you the Mithril badge.', inline=False)
                elif getbadge(ctx) == 4:
                    em.add_field(name=f"<:Ternion:787796127063343154> - Upgrade Badge to Ternion ($50,000)", value=f'Grants you the Ternion badge.', inline=False)


                await message.edit(embed = em)

                reaction, user = await bot.wait_for("reaction_add", timeout=120, check=check)


                if str(reaction.emoji) == "⭐":
                    usrbal = balance(ctx)
                    if usrbal < 200000:
                        await ctx.send('❌ You do not have enough money ($2,000)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="★ VIP ★")
                        await ctx.author.add_roles(role)
                        hasVIP = True
                        subtractbalance(ctx, 200000)
                        await ctx.send('✅ Transaction successful! You now have VIP access.')
                    #await message.remove_reaction(reaction, user)
                    await message.clear_reaction("⭐")
            


                elif str(reaction.emoji) == "<:Silver:787796126614814720>":
                    usrbal = balance(ctx)
                    if usrbal < 10000:
                        await ctx.send('❌ You do not have enough money ($100)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="Silver")
                        await ctx.author.add_roles(role)
                        subtractbalance(ctx, 10000)
                        await ctx.send('✅ Transaction successful! You now have the Silver badge.')
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    
                    alldata[3] = f'{int(alldata[3]) + 1}\n'

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)
                    await message.clear_reaction("<:Silver:787796126614814720>")



                elif str(reaction.emoji) == "<:gold:688558927377727517>":
                    usrbal = balance(ctx)
                    if usrbal < 50000:
                        await ctx.send('❌ You do not have enough money ($500)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="Gold")
                        await ctx.author.add_roles(role)
                        subtractbalance(ctx, 50000)
                        await ctx.send('✅ Transaction successful! You have upgraded your badge to Gold.')
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    
                    alldata[3] = f'{int(alldata[3]) + 1}\n'

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)
                    await message.clear_reaction("<:gold:688558927377727517>")

                elif str(reaction.emoji) == "<:Platinum:787796126119493633>":
                    usrbal = balance(ctx)
                    if usrbal < 180000:
                        await ctx.send('❌ You do not have enough money ($1,800)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="Platinum")
                        await ctx.author.add_roles(role)
                        subtractbalance(ctx, 180000)
                        await ctx.send('✅ Transaction successful! You have upgraded your badge to Platinum.')
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    alldata[3] = f'{int(alldata[3]) + 1}\n'

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)
                    await message.clear_reaction("<:Platinum:787796126119493633>")

                elif str(reaction.emoji) == "<:Mithril:787796126492655677>":
                    usrbal = balance(ctx)
                    if usrbal < 2000000:
                        await ctx.send('❌ You do not have enough money ($20,000)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="Mithril")
                        await ctx.author.add_roles(role)
                        subtractbalance(ctx, 2000000)
                        await ctx.send('✅ Transaction successful! You have upgraded your badge to Mithril.')
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    alldata[3] = f'{int(alldata[3]) + 1}\n'

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)
                    await message.clear_reaction("<:Mithril:787796126492655677>")

                elif str(reaction.emoji) == "<:Ternion:787796127063343154>":
                    usrbal = balance(ctx)
                    if usrbal < 5000000:
                        await ctx.send('❌ You do not have enough money ($50,000)')
                    else:
                        role = discord.utils.get(ctx.author.guild.roles, name="Ternion")
                        await ctx.author.add_roles(role)
                        subtractbalance(ctx, 5000000)
                        await ctx.send('✅ Transaction successful! You have upgraded your badge to Ternion.')
                    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                        alldata = file.readlines()
                    alldata[3] = f'{int(alldata[3]) + 1}\n'

                    with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)
                    await message.clear_reaction("<:Ternion:787796127063343154>")


                elif str(reaction.emoji) == "🎁":
                    usrbal = balance(ctx)
                    if usrbal < 1000:
                        await ctx.send('❌ You do not have enough money ($10)')
                    else:
                        with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                            alldata = file.readlines()
                        
                        cases = int(alldata[2])

                        print(cases)
                        cases += 1
                        alldata[2] = f'{cases}\n'
                        with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                            file.writelines(alldata)

                        subtractbalance(ctx, 1000)
                        await ctx.send(f'✅ Transaction successful! You now have {cases} case(s).')
                    await message.remove_reaction(reaction, user)

                else:
                    await message.remove_reaction(reaction, user)
                    # removes reactions if the user tries to go forward on the last page or
                    # backwards on the first page
            except asyncio.TimeoutError:
                break
                # ending the loop if user doesn't react after x seconds
        
        await asyncio.sleep(30)
        cooldown.remove(ctx.author.id)
    else:
        await ctx.send('❌ You cannot use this command again yet. You have to wait 30 seconds every time you open the store, but the old store message will still work until the cooldown is over.')

@bot.command(name='pay')
async def pay(ctx, member, amount):
    id = str(member)
    id = id.replace('<','')
    id = id.replace('@','')
    id = id.replace('!','')
    id = id.replace('>','')
    id = id.replace('&','')
    id = int(id)

    floatamount = float(amount)
    amount = floatamount * 100
    amount = int(amount)

    if amount < 1 or amount > balance(ctx):
        await ctx.send(f'❌ Invalid amount.')
        return

    if str(ctx.author.id) == str(id):
        await ctx.send(f"❌ You can't pay yourself.")
        return


    try:
        with open(f'bank/{str(id)}.txt', 'r') as file:
            pass
    except:
        await ctx.send(f'❌ User not found. If they have not sent any messages since the bot update, a file may not have been created for them.')
        return


    with open(f'bank/{str(id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    alldata[0] = f'{int(alldata[0]) + int(amount)}\n'
    alldata[1] = f'{int(alldata[1]) + int(amount)}\n'

    with open(f'bank/{str(id)}.txt', 'w') as file:
            file.writelines(alldata)

    subtractbalance(ctx, amount)

    await ctx.send(f'✅ Paid ${floatamount} to {member}')
    

@bot.command(name='profile')
async def profile(ctx):
    output(ctx)
    usrbal = balance(ctx)
    pfpurl = ctx.author.avatar_url
    
    with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
        alldata = file.readlines()
    
    with open(f'data/{str(ctx.author.id)}.txt', 'r') as file:
        stats = file.readlines()

    cases = int(alldata[2])

    totalearn = int(alldata[1])

    totalvalue = str(stats[0])
    rawtotal = int(stats[0])
    price= str(stats[1])
    rawprice = int(stats[1])
    rarity = str(stats[2])
    skin_name = str(stats[3])
    chosen_skin = str(stats[4])
    finalfl = str(stats[5])
    totalcases = str(stats[6])
    rawcases = int(stats[6])
    colournum = int(stats[7])


    price = decimal.Decimal(price)/100
    price = "${:,.2f}".format(price)
    price = str(f'{price}')


    totalvalue = decimal.Decimal(totalvalue)/100
    totalvalue = "${:,.2f}".format(totalvalue)
    totalvalue = str(f'{totalvalue}')

    luck = decimal.Decimal(rawtotal)/rawcases
    luck = str(luck)
    luck = str(luck.split('.', 1)[0])

    check_role = discord.utils.get(ctx.guild.roles, name= 'Silver')
    if check_role in ctx.author.roles:
        if getbadge(ctx) == 0:
            thumbnailico = 'https://www.redditstatic.com/gold/awards/icon/silver_128.png'
        elif getbadge(ctx) == 1:
            thumbnailico = 'https://www.redditstatic.com/gold/awards/icon/gold_128.png'
        elif getbadge(ctx) == 2:
            thumbnailico = 'https://www.redditstatic.com/gold/awards/icon/platinum_128.png'
        elif getbadge(ctx) == 3:
            thumbnailico = 'https://www.redditstatic.com/gold/awards/icon/Mithril_128.png'
        elif getbadge(ctx) == 4:
            thumbnailico = 'https://www.redditstatic.com/gold/awards/icon/Trinity_128.png'
    else:
        thumbnailico = 'https://cdn.discordapp.com/attachments/784309345822572544/787834374665273364/New_Project.png'

    '''
    em2 = discord.Embed(title=f"{ctx.author}'s Case Stats",description='', colour= colors[1])
    em2.add_field(name="Total skin value", value=totalvalue, inline=False)
    em2.add_field(name="Amount of cases opened", value=totalcases, inline=False)
    em2.add_field(name="Most valueable skin", value=skin_name, inline=False)
    em2.add_field(name="Luck", value=luck, inline=False)
    '''

    embed=discord.Embed(title=f"{ctx.author.display_name}'s stats", color=0x9742ff)
    embed.set_author(name=f"{ctx.author.display_name}", icon_url=pfpurl)
    embed.set_thumbnail(url=thumbnailico)
    embed.add_field(name="----------------------------------Bank-------------------------------", value="earnings", inline=False)
    embed.add_field(name="test", value=totalearn, inline=True)
    embed.add_field(name="Total Earnings", value=totalearn, inline=True)
    embed.add_field(name="-------------------------------Inventory----------------------------", value="12 cases \n Gold Badge", inline=False)
    embed.add_field(name="-------------------------------Case Stats----------------------------",value='test', inline=False)
    embed.add_field(name="Cases opened", value=totalcases, inline=True)
    embed.add_field(name="Total case value", value=totalvalue, inline=True)
    embed.add_field(name="Luck", value=luck, inline=True)
    await ctx.send(embed=embed)
    
    
    em = discord.Embed(title="Most Valueable Skin⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",description=skin_name,)
    
    em.add_field(name="Rarity:", value=rarity, inline=False)
    em.add_field(name="Price:", value=price, inline=False)
    em.add_field(name="Wear:", value=finalfl, inline=False)
    #await ctx.send(embed=em2)
    path = str(f'{rarity}/{chosen_skin}').replace('\n','')
    await ctx.send(embed=em, file=discord.File(path))







@bot.command(name='bulkcase')
async def bulkcase(ctx, casenum):
    casenum = int(casenum)
    usrbal = balance(ctx)
    caseprice = casenum * 1000
    caseprice = int(caseprice)
    caseprice = decimal.Decimal(caseprice)/100
    caseprice = "${:,.2f}".format(caseprice)
    caseprice = str(f'{caseprice}')

    if casenum > 0:
        if usrbal < 1000 * casenum:
            await ctx.send(f'❌ You do not have enough money ({caseprice})')
        else:
            with open(f'bank/{str(ctx.author.id)}.txt', 'r') as file:
                alldata = file.readlines()
            
            cases = int(alldata[2])

            print(cases)
            cases += casenum
            alldata[2] = f'{cases}\n'
            with open(f'bank/{str(ctx.author.id)}.txt', 'w') as file:
                file.writelines(alldata)

            subtractbalance(ctx, 1000*casenum)
            await ctx.send(f'✅ Transaction successful! You now have {cases} case(s).')
    else:
        await ctx.send(f'❌ Invalid integer')



bot.run(TOKEN)

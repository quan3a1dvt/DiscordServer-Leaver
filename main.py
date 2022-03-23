import discord

client = discord.Client()
token = "" # your token

@client.event
async def on_ready():
    print("1. Leave All Server\n2. Leave Manual\n")
    choice = input("Choice: ")
    
    if choice == "1":
        print("Are you sure want to leave all server?")
        x = input("(y: Yes, n: No) : ")
        if x == "y":
            for guild in client.guilds:
                server = client.get_guild(guild.id)
                await server.leave()
            print("Done")
    elif choice == "2":
        for guild in client.guilds:
            print(guild.name)
            choice = input("y: leave, n: stay, exit: e\nChoice: ")
            print("\n-----------\n")
            if choice == "y":
                server = client.get_guild(guild.id)
                await server.leave()
                print("You left " + guild.name)
            elif choice == "e":
                break
client.run(token, bot=False)


import discord
import sys
class MyClient(discord.Client):
	async def on_ready(self):
		print(f'Online as {self.user}')

	async def on_message_delete(self,message):
		print("message deleted")
		print(f"{message.author}-({message.channel}):{message.content}")
	if sys.argv[2]=="all":
		async def on_message(self,message):
			print("message created")
			print(f"{message.author}-({message.channel}):{message.content}")

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
print('''  _____  _     _                            
 |  __ \\(_)   | |                           
 | |  | |_ ___| | ___   __ _   _ __  _   _  
 | |  | | / __| |/ _ \\ / _` | | '_ \\| | | | 
 | |__| | \\__ \\ | (_) | (_| |_| |_) | |_| | 
 |_____/|_|___/_|\\___/ \\__, (_) .__/ \\__, | 
                        __/ | | |     __/ | 
                       |___/  |_|    |___/''')
client.run(sys.argv[1])

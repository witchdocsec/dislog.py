import discord
import sys
import random
class DislogClient(discord.Client):
	async def on_ready(self):
		print(f'Online as {self.user}')

	async def on_message_delete(self,message):
		print("message deleted")
		print(f"{message.author}-({message.channel}):{message.content}")
		if len(sys.argv) >= 4:
			if sys.argv[3]=="roast":
				await message.channel.send(f"message deleted by{message.author}-({message.channel}):`{message.content}` :skull: isn't this message cringe?")
	if len(sys.argv) >= 3:
		if sys.argv[2]=="all":
			async def on_message(self,message):
				print("message created")
				print(f"{message.author}-({message.channel}):{message.content}")

intents = discord.Intents.default()
intents.message_content = True
client = DislogClient(intents=intents)
print('''
\033[49m            \033[38;5;63;49m▄▄▄\033[38;5;63;48;5;63m▄\033[48;5;63m  \033[38;5;63;49m▄\033[49m            \033[38;5;63;49m▄\033[48;5;63m  \033[38;5;63;48;5;63m▄\033[38;5;63;49m▄▄▄\033[49m            \033[m
\033[49m       \033[38;5;63;49m▄▄\033[48;5;63m          \033[38;5;63;49m▄\033[38;5;63;48;5;63m▄\033[48;5;63m        \033[38;5;63;48;5;63m▄\033[38;5;63;49m▄\033[48;5;63m          \033[38;5;63;49m▄▄\033[49m       \033[m
\033[49m      \033[38;5;63;49m▄\033[48;5;63m                                    \033[38;5;63;49m▄\033[49m      \033[m
\033[49m     \033[38;5;63;48;5;63m▄\033[48;5;63m                                      \033[38;5;63;48;5;63m▄\033[49m     \033[m
\033[49m    \033[38;5;63;48;5;63m▄\033[48;5;63m                                         \033[49m    \033[m
\033[49m   \033[38;5;63;48;5;63m▄\033[48;5;63m                                           \033[49m   \033[m
\033[49m  \033[38;5;63;49m▄\033[48;5;63m                                            \033[38;5;63;49m▄\033[49m  \033[m
\033[49m  \033[48;5;63m              \033[38;5;63;48;5;63m▄▄\033[48;5;63m              \033[38;5;63;48;5;63m▄▄\033[48;5;63m              \033[49m  \033[m
\033[49m \033[48;5;63m            \033[49;38;5;63m▀\033[49m     \033[49;38;5;63m▀\033[48;5;63m          \033[49;38;5;63m▀\033[49m     \033[49;38;5;63m▀\033[48;5;63m            \033[49m \033[m
\033[49m \033[48;5;63m           \033[49;38;5;63m▀\033[49m        \033[48;5;63m        \033[49m        \033[49;38;5;63m▀\033[48;5;63m           \033[49m \033[m
\033[38;5;63;48;5;63m▄\033[48;5;63m           \033[49m         \033[48;5;63m        \033[49m         \033[48;5;63m           \033[38;5;63;48;5;63m▄\033[m
\033[48;5;63m             \033[49m       \033[38;5;63;49m▄\033[48;5;63m        \033[38;5;63;49m▄\033[49m       \033[48;5;63m             \033[m
\033[48;5;63m              \033[38;5;63;48;5;63m▄\033[38;5;63;49m▄▄▄▄\033[48;5;63m            \033[38;5;63;49m▄▄▄▄▄\033[48;5;63m              \033[m
\033[48;5;63m                                                  \033[m
\033[48;5;63m                                                  \033[m
\033[49;38;5;63m▀\033[48;5;63m           \033[38;5;63;49m▄\033[49m \033[49;38;5;63m▀▀\033[38;5;63;48;5;63m▄\033[48;5;63m                \033[38;5;63;48;5;63m▄\033[49;38;5;63m▀▀▀\033[38;5;63;49m▄\033[48;5;63m           \033[49;38;5;63m▀\033[m
\033[49m   \033[49;38;5;63m▀\033[38;5;63;48;5;63m▄\033[48;5;63m          \033[49m      \033[49;38;5;63m▀▀▀▀▀▀▀▀\033[49m      \033[48;5;63m          \033[38;5;63;48;5;63m▄\033[49;38;5;63m▀\033[49m   \033[m
\033[49m      \033[49;38;5;63m▀▀▀\033[48;5;63m     \033[49;38;5;63m▀\033[49m                    \033[49;38;5;63m▀\033[48;5;63m     \033[49;38;5;63m▀▀▀\033[49m      \033[m
\033[49m           \033[49;38;5;63m▀▀\033[49m                        \033[49;38;5;63m▀▀\033[49m           \033[m
''')
print('''  _____  _     _                            
 |  __ \\(_)   | |                           
 | |  | |_ ___| | ___   __ _   _ __  _   _  
 | |  | | / __| |/ _ \\ / _` | | '_ \\| | | | 
 | |__| | \\__ \\ | (_) | (_| |_| |_) | |_| | 
 |_____/|_|___/_|\\___/ \\__, (_) .__/ \\__, | 
                        __/ | | |     __/ | 
                       |___/  |_|    |___/''')
client.run(sys.argv[1])

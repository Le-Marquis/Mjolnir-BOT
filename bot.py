import discord
import random
import time
import asyncio


class Bot(discord.Client):



	def __init__(self):
		super().__init__()

	def random_color(self):
		hexa = "0123456789abcdef"
		random_hex = "0x"
		for i in range(6):
			random_hex += random.choice(hexa)
		return discord.Colour(int(random_hex, 16))

	def check_admin_rights(self, message):
		admin_role = discord.utils.get(message.guild.roles, name="Administrateur")
		modo_role = discord.utils.get(message.guild.roles, name="Modérateur")

		return (message.author.top_role != admin_role and message.author.top_role != modo_role)

	def create_embed(self, title, description, color, img=""):
		embed = discord.Embed()
		embed.title = title
		embed.description = description
		embed.colour = color
		if(img != ""):
			embed.set_image(url=img)
		return embed

	async def on_ready(self):
		print('Logged in as')
		print(self.user.name)
		print(self.user.id)
		print('------')
		await self.change_presence(activity=discord.Game(name='pc online')) 
		print('bot ready')

	async def on_message(self, message):

		if(message.author == self.user):
			return

		if(message.content.startswith("!ping")):
			await message.channel.send("pong")

		if(message.content.startswith("!help")):
			await member.send("https://github.com/Syf-dev/Mjolnir-BOT/blob/master/README.md")

		if(message.content.startswith("!clear")):
			
				nbr = message.content.split(" ")[1]
				
				await message.channel.purge(limit=int(nbr))

		if(message.content.startswith("!mp")):

				name = message.content.split(" ")[1]
				mess = message.content.split(" ")[2]

				if(name == "all"):#argument pour envoyer un message a tout les utilisateurs du serveur
						for member in message.guild.members:
								if not member == self.user:#on selectionne que les utilisateurs pas le bot
										try:
												await member.send(mess)
										except discord.Forbidden:
												await message.channel.send(":no_entry: Erreur l'utilisateur " + str(member) + " ne souhaite pas recevoir de message privé a partir de ce serveur")
				else:
						member = discord.utils.get(message.guild.members, name=name)

						try:
								await member.send(mess)
						except discord.Forbidden:
								await message.channel.send(":no_entry: Erreur l'utilisateur " + name + " ne souhaite pas recevoir de message privé a partir de ce serveur")
						except AttributeError:
								await message.channel.send(":warning: Erreur l'utilisateur " + name + " n'existe pas ou mal orthographié")


		if(message.content.startswith("!profile")):
			color = self.random_color()
			description = "voici ton profile"
			embed = self.create_embed(message.author.name, description, color, message.author.avatar_url)

			await message.channel.send(embed=embed)

		
		if(message.content.startswith("!kick")):
			msg = message.content.split(" ")
			if(len(msg) < 2):
				print("erreur nombre d'arguments")
				return
			user = msg[1]
			reason = " ".join(msg[2:])

			member_to_kick = discord.utils.get(message.guild.members, id=int(user[3:-1]))

			await message.guild.kick(member_to_kick, reason=reason)


		if(message.content.startswith("!ban")):
			msg = message.content.split(" ")
			if(len(msg) < 2):
				print("erreur nombre d'arguments")
				return
			user = msg[1]
			reason = " ".join(msg[2:])

			member_to_ban = discord.utils.get(message.guild.members, id=int(user[3:-1]))

			await message.guild.ban(member_to_ban, reason=reason)



if(__name__ == "__main__"):

	bot = Bot()
	bot.run("")	#votre token

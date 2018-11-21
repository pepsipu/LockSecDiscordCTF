import discord
from discord.ext import commands
import json

class Solve:
	def __init__(self, client):
		self.client = client

#Converts the given key into another value by CTF 1's algorithm.

	async def check_key1(self, key):
		char_sum = 0
		for c in key:
			char_sum += ord(c)
		return char_sum

#Converts the given key into another value by CTF 2's algorithm.

	async def check_key2(self, key):
		char_sum = 0
		for c in key:
			char_sum += ord(c) + ord(c)
			if ord(c) > 50:
				char_sum -= ord(c)
			else:
				char_sum += ord(c) / 2
		return char_sum

#This deserves a class itself due to it's size and complexity
#This function checks your ctf is wrong or not.

	@commands.command(pass_context=True)
	async def solve(self, ctx, ctfid, attempt):
		with open("users.json", "r") as f:
			users = json.load(f)
		ctfid = int(ctfid)
		if ctfid == 1:
			if users[ctx.message.author.id]["ctf1"] == 0:
				input_sum = await self.check_key1(attempt)
				if input_sum == 900:
					embed = discord.Embed(
						title = "0x01 - KeyGen Solved",
						description = "The lock snaps open as you enter the key and hit enter. You are awarded $1000.",
						colour = discord.Colour.green()
					)

					embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
					embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")

					await self.client.say(embed=embed)
					users[ctx.message.author.id]["ctf1"] = 1
					users[ctx.message.author.id]["money"] += 1000
					users[ctx.message.author.id]["ctfs"] += 1

					with open("users.json", "w") as f:
						users = json.dump(users, f)
				else:
					embed = discord.Embed(
						title = "Faliure",
						description = "You hit enter but the lock still does not budge. Try again!",
						colour = discord.Colour.red()
					)

					embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
					embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")

					await self.client.say(embed=embed)
			else:
				embed = discord.Embed(
					title = "Already Completed",
					description = "This lock is already open. You leave it be.",
					colour = discord.Colour.red()
				)

				embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
				embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")

				await self.client.say(embed=embed)


		elif ctfid == 2:
			input_sum = await self.check_key2(attempt)
			if users[ctx.message.author.id]["ctf2"] == 0:
				if input_sum == 750:
					embed = discord.Embed(
						title = "0x02 - Complicated KeyGen Solved",
						description = "The lock stays still but fortunatly, it pops open. You sigh in relief. You are awarded $1500.",
						colour = discord.Colour.green()
					)

					embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
					embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")

					await self.client.say(embed=embed)
					users[ctx.message.author.id]["ctf2"] = 1
					users[ctx.message.author.id]["money"] += 1500
					users[ctx.message.author.id]["ctfs"] += 1
					with open("users.json", "w") as f:
						users = json.dump(users, f)
				else:
					embed = discord.Embed(
						title = "Faliure",
						description = "You hit enter but the lock still does not budge. Try again!",
						colour = discord.Colour.red()
					)

					embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
					embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")

					await self.client.say(embed=embed)
			else:
				embed = discord.Embed(
					title = "Already Completed",
					description = "This lock is already open. You leave it be.",
					colour = discord.Colour.red() 
				)
				embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
				embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")

				await self.client.say(embed=embed)
		else:
			embed = discord.Embed(
				title = "Unrecognized CTFID",
				description = "That CTFID isn't recognized!",
				colour = discord.Colour.red()
			)

			embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")

			await self.client.say(embed=embed)


#Setup the cog.

def setup(client):
	client.add_cog(Solve(client))
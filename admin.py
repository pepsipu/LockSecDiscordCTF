import discord
from discord.ext import commands
import json

class Admin:
	def __init__(self, client):
		self.client = client

#Prints a list of IDs.

	@commands.command(pass_context=True)
	async def userlist(self, ctx):
		with open("users.json", "r") as f:
			users = json.load(f)
		if ctx.message.author.id == "475525381609357313":
			userids = ""
			for ids in users:
				userids += " [{}]".format(ids)
			embed = discord.Embed(
				title = "Admin Interface - {}".format(ctx.message.author),
				description = "Userlist - {}".format(userids),
				colour = discord.Colour.orange()
			)

			embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
			await self.client.say(embed=embed)
		else:
			embed = discord.Embed(
				title = "Admin Interface - Faliure",
				description = "You aren't authorized!",
				colour = discord.Colour.orange()
			)

			embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
			await self.client.say(embed=embed)

	@commands.command(pass_context=True)
	async def userinfo(self, ctx, targid):
		with open("users.json", "r") as f:
			users = json.load(f)
		if users[targid]["ctf1"] == 0:
			ctf1bool = "This user has not completed 0x01."
		else:
			ctf1bool = "This user has completed 0x01."
		if users[targid]["ctf2"] == 0:
			ctf2bool = "This user has not completed 0x02."
		else:
			ctf2bool = "This user has completed 0x02."
		embed = discord.Embed(
			title = "User Interface - {}".format(ctx.message.author),
			description = "Getting information on {}.".format(targid),
			colour = discord.Colour.purple()
		)
		embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
		embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
		embed.add_field(name="Money", value="${}".format(users[targid]["money"]), inline=True)
		embed.add_field(name="CTFs Completed", value="{}".format(users[targid]["ctfs"]), inline=True)
		embed.add_field(name="CTF1", value="{}".format(ctf1bool), inline=True)
		embed.add_field(name="CTF2", value="{}".format(ctf2bool), inline=True)
		await self.client.say(embed=embed)

	@commands.command(pass_context=True)
	async def edituser(self, ctx, targid, attribute, value):
		with open("users.json", "r") as f:
			users = json.load(f)
		if ctx.message.author.id == "475525381609357313":
			if attribute == "ctfs":
				users[targid]["ctfs"] = value
			elif attribute == "ctf1":
				users[targid]["ctf1"] = value
			elif attribute == "money":
				users[targid]["money"] = value
			elif attribute == "ctf2":
				users[targid]["ctf2"] = value
			else:
				await self.client.say("That attribute doesn't exist!")
			embed = discord.Embed(
				title = "Admin Interface - {}".format(ctx.message.author),
				description = "{}'s {} has been set to {}.".format(targid, attribute, value),
				colour = discord.Colour.orange()
			)
			embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
			await self.client.say(embed=embed)
			with open("users.json", "w") as f:
				users = json.dump(users, f)
		else:
			embed = discord.Embed(
				title = "Admin Interface - Faliure",
				description = "You aren't authorized!",
				colour = discord.Colour.orange()
			)

			embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
			await self.client.say(embed=embed)

	@commands.command(pass_context=True)
	async def reset(self, ctx):
		if ctx.message.author.id == "475525381609357313":
			with open("users.json", "r") as f:
				users = json.load(f)
				users = {}
			with open("users.json", "w") as f:
				users = json.dump(users, f)
			embed = discord.Embed(
				title = "Admin Interface -  {}".format(ctx.message.author),
				description = "Database reset!",
				colour = discord.Colour.orange()
			)

			embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
			await self.client.say(embed=embed)

		else:
			embed = discord.Embed(
				title = "Admin Interface - Faliure",
				description = "You aren't authorized!",
				colour = discord.Colour.orange()
			)

			embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
			await self.client.say(embed=embed)



def setup(client):
	client.add_cog(Admin(client))
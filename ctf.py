import discord
from discord.ext import commands
import json

class CTF:
	def __init__(self, client):
		self.client = client

#Provides downloads to the different CTFs.

	@commands.command(pass_context=True)
	async def binary(self, ctx, ctfid):
		ctfid = int(ctfid)
		if ctfid == 1:
			embed = discord.Embed(
				title = "Binary Download",
				description = "Download the binary for 0x01 here. - http://pepsipu.com/locksec/",
				colour = discord.Colour.blue()
			)
			embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
			await self.client.say(embed=embed)
		elif ctfid == 2:
			embed = discord.Embed(
				title = "Binary Download",
				description = "Download the binary for 0x02 here. - http://pepsipu.com/locksec/",
				colour = discord.Colour.blue()
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

#Creates the command 'assembly' which shows pictures of the dissasembled CTF.

	@commands.command(pass_context=True)
	async def assembly(self, ctx, ctfid):
		ctfid = int(ctfid)
		if ctfid == 1:
			embed = discord.Embed(
				title = "Assembly Chart",
				description = "These images contain the main function dissassembly of the LockSec program for CTF 0x01.",
				colour = discord.Colour.blue()
			)
			embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
			await self.client.say(embed=embed)
			await self.client.say("```https://i.gyazo.com/3e02e0c684638d6fa49ba356c3501b20.png```")
			await self.client.say("```https://i.gyazo.com/6c273d600bed7c7408de097173759f87.png```")
			await self.client.say("```https://i.gyazo.com/b9ef1ea8f393ec909fa629e829ef733b.png```")
		elif ctfid == 2:
			embed = discord.Embed(
				title = "Assembly Chart",
				description = "hese images contain the main function dissassembly of the LockSec program for CTF 0x02.",
				colour = discord.Colour.blue()
			)
			embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
			embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
			await self.client.say(embed=embed)
			await self.client.say("```https://i.gyazo.com/2ccb3e38edd5411b05438fc9af2be675.png```")
			await self.client.say("```https://i.gyazo.com/c8e0d67be33b6beb1091be4e3c1244b2.png```")
			await self.client.say("```https://i.gyazo.com/30aff0fcd3fd810ae377b706d10500ba.png```")
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
	client.add_cog(CTF(client))
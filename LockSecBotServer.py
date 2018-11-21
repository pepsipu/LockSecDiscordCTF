import discord
from discord.ext import commands
import asyncio
import json

token = "NTE0MjYwNjU1NTg3NDU5MDc0.DtUCaw.MiRNQEm5QDflZ3FarlbNlVMXT5U"

extensions = ["ctf", "solve", "admin"]

client = commands.Bot(command_prefix = "./ctf ")
client.remove_command("help")

async def create_data(users, user):
	if not user.id in users:
		users[user.id] = {}
		users[user.id]["money"] = 0
		users[user.id]["ctfs"] = 0
		users[user.id]["ctf1"] = 0
		users[user.id]["ctf2"] = 0
		embed = discord.Embed(
			title = "Registered",
			description = "You have been registered. Good luck!",
			colour = discord.Colour.green()
		)
		embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
		embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")

		await client.say(embed=embed)
	else:
		embed = discord.Embed(
			title = "Already Registered",
			description = "You are already registered!",
			colour = discord.Colour.red()
		)

		embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
		embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")

		await client.say(embed=embed)


async def give_money(users, user, amount):
	users[user.id]["money"] += amount

async def ctf_add(users, user):
	users[user.id]["ctfs"] += 1

async def ctf1_done(users, user):
	users[user.id]["ctf1"] += 1

async def ctf2_done(users, user):
	users[user.id]["ctf2"] += 1

@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name="Run ./ctf help for help."))
	print("LockSec Server starting...\n")
	print("By Sammy Hajhamid / pepsipu#3655\n")
	print("pepsipu.com\n")

@client.event
async def on_member_join(member):
	with open("users.json", "r") as f:
		users = json.load(f)
	await create_data(users, member)
	with open("users.json", "w") as f:
		users = json.dump(users, f)

@client.event
async def on_message(message):
	author = message.author
	content = message.content
	channel = message.channel
	await client.process_commands(message)

@client.command(pass_context=True)
async def register(ctx):
	with open("users.json", "r") as f:
		users = json.load(f)
	await create_data(users, ctx.message.author)
	with open("users.json", "w") as f:
		users = json.dump(users, f)
	



@client.command()
async def list():
	embed = discord.Embed(
		title = "Current CTFs",
		description = "These are the current CTFs available. You will need to run the command 'assembly <ctfid>' to analyze the data.",
		colour = discord.Colour.blue()
	)

	embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
	embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
	embed.add_field(name="0x01 - KeyGen - CTFID=1", value="LockSec has come out with a licensing program, and Udobe is using it for PictureShop. It functions by taking the license key supplied by the customer, and splitting it into the individual characters. These individual characters are then coverted into their hex value, which are added up into a sum. If the supplied key matches the predetermined sum, you are authorized. Your goal is to produce a key that will get you that juicy 'Access Granted'.", inline=True)
	embed.add_field(name="0x02 - Complicated KeyGen - CTFID=2", value="After the embarrasing hack by you, LockSec has created a more complicated algorithm, a far cry from 0x01. It also takes the supplied key and breaks it down into it's hex value, but you need to see the assembly to see what it does with those numbers.", inline=True)
	await client.say(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
	embed = discord.Embed(
		title = "The LockSec Interactive Application",
		description = "The LSIA is a hacking CTF with multiple different challenges. The story revolves around a company called LockSec who develops physical and virtual locks that you, a ethical hacker, must hack. You are offered money for each lock broken, similar to bug bounties.",
		colour = discord.Colour.blue()
	)
	embed.set_footer(text="The LSIA is made by pepsipu#3655 / Check out pepsipu.com.")
	embed.set_author(name="LockSec Interactive Application", icon_url="https://cdn.discordapp.com/attachments/498720959650594830/514357970293882880/ctf.jpg")
	embed.add_field(name="Commands", value="Commands that you can execute, prefixed by ./ctf. For example, './ctf help' displays this message.", inline=False)
	embed.add_field(name="list", value="Lists all available CTFs.", inline=True)
	embed.add_field(name="solve <ctfid> <ctfanswer>", value="Solve a CTF for points.", inline=True)
	embed.add_field(name="userinfo <userid>", value="Shows the amount made from bug bounties and completed CTFs.", inline=True)
	embed.add_field(name="assembly <ctfid>", value="Get the assembly code of the program.", inline=True)
	embed.add_field(name="binary <ctfid>", value="Links a download to the CTF binary.", inline=True)
	embed.add_field(name="register", value="Creates a profile for you to play CTF.", inline=True)
	embed.add_field(name="Admin Commands", value="Commands that can only be executed by registered IDs.", inline=False)
	embed.add_field(name="userlist", value="Lists all the users in the database.", inline=True)
	embed.add_field(name="edituser <userid> <attribute> <value>", value="Edit a user's information.", inline=True)
	embed.add_field(name="reset", value="Resets the database. Dangerous command.", inline=True)


	await client.say(embed=embed)

if __name__ == "__main__":
	for extension in extensions:
		try:
			client.load_extension(extension)
		except Exception as problem:
			print("Cannot load {}. [{}]".format(extension, problem))

	client.run(token)

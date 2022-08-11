import os
os.system("cls && title Checking.... && color b")
active = False
print("Welcome! Checking...")
if os.path.exists('insert_token.txt') == False:
  print("Insert the token to the file INSERT_TOKEN.txt\nAnd restart the programm")
  open('insert_token.txt', 'w')
##### IMPORTS #####
import random
import asyncio
import discord
import json
import threading
import requests
from discord.ext import commands
######## SETUPING #######
client = commands.Bot(command_prefix = ";", self_bot = False)
guild  = client.get_guild(id)
###### STARTUP ######
@client.event
async def on_ready():
  os.system("cls && color 6")
  print(f"""
                      ________                         ___________         __             
                     /  _____/ _____     _____    ____ \_   _____/_____   |  | __  ____   
                    /   \  ___ \__  \   /     \ _/ __ \ |    __)  \__  \  |  |/ /_/ __ \  
                    \    \_\  \ / __ \_|  Y Y  \\  ___/ |     \    / __ \_|    < \  ___/  
                     \______  /(____  /|__|_|  / \___  >\___  /   (____  /|__|_ \ \___  > 
                            \/      \/       \/      \/     \/         \/      \/     \/  
                                          Logged at {client.user.name}                

                                          Valid games:
                     1) GTA V               6) NFS                11) Dota 2
                     2) Terraria            7) GTA: SA            12) Spotify
                     3) Minecraft           8) Hytale             13) Slime Rancher
                     4) OSU!                9) ROBLOX             14) Mafia II 
                     5) GameFake            10) CS: GO            
                                          
                                          Enter number to choice!                         
                                                                   
                                                                      """)
  while True:
   choice = input("[.] Choice: ")
   if choice == "1":
          game = "Grand Theft Auto V"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to GTA: V")
   if choice == "2":
          game = "Terraria"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to Terraria")
   if choice == "3":
          game = "Minecraft"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to Minecraft")
   if choice == "4":
          game = "Osu!"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to OSU!")
   if choice == "5":
          game = "github.com/knwportale/gamefake"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to GameFake")
   if choice == "6":
          game = "Need For Speed: Most Wanted"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to NFS: MW")
   if choice == "7":
          game = "Grand Theft Auto: San Andreas"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to GTA: SA")
   if choice == "8":
          game = "Hytale"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to Hytale [BUG]")
   if choice == "9":
          game = "ROBLOX"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to ROBLOX")
   if choice == "10":
          game = "Counter Strike: Global Offensive"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to CSGO")
   if choice == "11":
          game = "Dota 2"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to Dota 2")
   if choice == "12":
          game = "Grand Theft Auto V"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=game))
          print(" [!] Game changed to GTA: V")
   if choice == "13":
          game = "Slime Rancher"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to SR")
   if choice == "14":
          game = "Mafia II"
          await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=game))
          print(" [!] Game changed to Mafia II")
                                                
try:
  client.run(open('insert_token.txt', 'r').readline(), bot = True)
except:
 os.system("cls && color c && title Error!")
 print("Token not valid. Please check the file INSERT_TOKEN.txt\nIf token valid, write to the our server\ndsc.gg/areself")
 while True:
  a = 0
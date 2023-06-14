import discord
from discord import option
from discord import Embed
from discord.ext import commands
import config

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)

class DiscordBot():
    def __init__(self):
        self.register_commands()
        self.run()
        
    def register_commands(self):
        @bot.slash_command(name="chat", description="Use chatgpt plugins", guild_ids=[config.guild_id])
        #on chat command send message to process_message method
        async def on_chat(ctx, message: str):
            #can send message from here to the list of functions 
            
            await self.process_message(ctx, message)

        
    
    def process_message(self, ctx, message):
        print("chat slash command was executed")
        pass
    
    

    
    def run(self):
        bot.run(config.bot_token)
        
if __name__ == "__main__":
    DiscordBot()
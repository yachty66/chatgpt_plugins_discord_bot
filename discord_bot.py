import discord
from discord import option
from discord import Embed
from discord.ext import commands
import config
import json
import openai 

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
            await self.process_message(ctx, message)
            
    def get_functions(self):
        with open("plugins_settings.json", "r") as file:
            plugins = json.load(file)
            
        '''
        inside the plugins variable i have the follwing format:
        
                {
            "plugins": {
            "weather_example_plugin": {
                "enabled": true
            },
            "another_plugin": {
                "enabled": true
            }
            }
        }
        '''
        enabled_plugins = [plugin for plugin, settings in plugins["plugins"].items() if settings["enabled"]]
        print("enabled_plugins")
        print(enabled_plugins)
        #get all the functions and return them
        #iter over all the folder in plugins folder and extract for each folder name who appears in enabled_plugins the function which is inside functions.json
        functions = []
        for plugin in enabled_plugins:
            with open(f"plugins/{plugin}/functions.json", "r") as file:
                plugin_functions = json.load(file)
                #add json to functions
                functions.append(plugin_functions)
        return functions
                

    def process_message(self, ctx, message):
        #need to get all the functions
        functions = self.get_functions()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[{"role": "user", "content": "What's the weather like in Boston?"}],
            #need to make sure that i have certain format which is required here 
            functions=functions,
            function_call="auto",
        )
        message = response["choices"][0]["message"]
        print("message")
        print(message)

    
    def run(self):
        bot.run(config.bot_token)
        
if __name__ == "__main__":
    DiscordBot()
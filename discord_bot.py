import discord
from discord import option
from discord import Embed
from discord.ext import commands
import config
import json
import openai 
import importlib.util

intents = discord.Intents.all()
bot = discord.Bot(intents=intents)
openai.api_key = config.openai_key

class DiscordBot():
    def __init__(self):
        self.register_commands()
        self.plugins = []
        self.run()
        
    def register_commands(self):
        @bot.slash_command(name="chat", description="Use chatgpt plugins", guild_ids=[config.guild_id])
        #on chat command send message to process_message method
        async def on_chat(ctx, message: str):
            await self.process_message(ctx, message)
            
    def get_functions(self):
        with open("plugins_settings.json", "r") as file:
            plugins = json.load(file)
        enabled_plugins = [plugin for plugin, settings in plugins["plugins"].items() if settings["enabled"]]
        functions = []
        for plugin in enabled_plugins:
            self.plugins.append(plugin)
            with open(f"plugins/{plugin}/functions.json", "r") as file:
                plugin_functions = json.load(file)
                functions.append(plugin_functions)
        #todo remove code duplication
        combined_functions = []
        for func_list in functions:
            combined_functions.extend(func_list)
        functions = combined_functions
        return functions

    async def process_message(self, ctx, message):
        functions = self.get_functions()        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo-0613",
            messages=[{"role": "user", "content": "What's the weather like in Boston?"}],
            functions=functions,
            function_call="auto",
        )
        message = response["choices"][0]["message"]
        
        if message.get("function_call"):
            print("inside")
            function_name = message["function_call"]["name"]
            #iter over each file and check where name appears, if name appeared then get name of parent folder
            for plugin in self.plugins:
                with open(f"plugins/{plugin}/functions.json", "r") as file:
                    plugin_functions = json.load(file)
                    for function in plugin_functions:
                        if function["name"] == function_name:
                            plugin_folder = plugin                
            plugin_file = plugin_folder + ".py"
            plugin_path = f"plugins/{plugin_folder}/{plugin_folder}.py"
            spec = importlib.util.spec_from_file_location(f"plugins.{plugin_folder}.{plugin_folder}", plugin_path)
            plugin_module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(plugin_module)
            #tries to get the class here. can make naming convention for class name
            #hello_my_name_is_jeff is always going to be the class name = plugin_folder
            #pluging folder has always the format like hello_my_name --> needs to be converted to HelloMyName
            plugin_folder_parts = plugin_folder.split('_')
            plugin_folder = ''.join([part.capitalize() for part in plugin_folder_parts])
            
            plugin_class = getattr(plugin_module, plugin_folder)(message, function_name)
            print("function result:")
            print(plugin_class)
                
                
    def run(self):
        bot.run(config.bot_token)
        
if __name__ == "__main__":
    DiscordBot()
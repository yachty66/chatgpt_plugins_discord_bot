# ChatgptPluginsDiscordBot


ChatgptPluginsDiscordBot is a Discord bot that uses OpenAI's [function calling API](https://platform.openai.com/docs/guides/gpt/function-calling). It is designed to be easily extensible with custom plugins, allowing you to add new ones.

## Features

- Uses  OpenAI's function calling API
- Chatgpt plugins in discord 
- Easily add you own plugins 

![Giphy](https://media.giphy.com/media/kj2k4sqiyGMcWiES9W/giphy.gif)

## Installation

1. Clone the repository with git clone https://github.com/yachty66/chatgpt_plugins_discord_bot.git
2. Install the required dependencies with pip install -r requirements.txt
3. Create discord bot in [discord developer portal](https://discord.com/developers/applications). Enable all "Privileged Gateway Intents" and than under OAuth2 choose "bot" as checkbox and then "Administrator". copy the url in your browser and add the bot to your server.
4. Still in discord developer portal go to "Bot" and "reset token" if you dont have your token.
3. Create a config.py file in your root and add the following information:
guild_id = 1112547069798920353
bot_token = "MTExODUzOTYzNzQyMjU3NTg0Nw.GhWEGa.slrXsCj8l8ev9NPnsW6Tbs_6c_kkr4iTDsaj_g"
openai_key = "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"

guild id is the first number in the url of an respective server, for bot_token paste the token and your open ai key.

4. Run the bot using python discord_bot.py


## Usage

Go to the certain server and use the /chat command followed by your message to chat. 

## Creating Your Own Plugins

To create your own plugin, follow these steps:

1. Create a new folder inside the plugins directory with the format your_plugin_name. For example, weather_example_plugin.

2. Inside the new folder, create two files: functions.json and your_plugin_name_plugin.py. For example, weather_example_plugin.py.

3. In the functions.json file, define the functions that your plugin will provide. Checkout the [OpenAI cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb) for all available formats

4. In the your_plugin_name_plugin.py file, create a class with the same name as your plugin folder, but in CamelCase format. For example, WeatherExamplePlugin. This class should have an __init__ method, a method for each function defined in functions.json, and any additional helper methods as needed.

5. In the plugins_settings.json file, add your plugin to the plugins object and set its enabled property to true. Lets say you created a plugin called "another plugin" than the file would need to look like:

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

6. Restart the bot to load your new plugin.

## Contributing

I accept pull requests so that this repository can grow with an diversity of plugins like the ChatGPT from OpenAI.
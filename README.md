# ChatgptPluginsDiscordBot

ChatgptPluginsDiscordBot is a Discord bot that uses OpenAI's [function calling API](https://platform.openai.com/docs/guides/gpt/function-calling). It is designed to be easily extensible with custom plugins, allowing you to add new ones.

## Features

- Uses OpenAI's function calling API
- Chatgpt plugins in discord
- Easily add your own plugins

![Giphy](https://media.giphy.com/media/kj2k4sqiyGMcWiES9W/giphy.gif)

## Installation

1. Clone the repository with `git clone https://github.com/yachty66/chatgpt_plugins_discord_bot.git`
2. Install the required dependencies with `pip install -r requirements.txt`
3. Create a Discord bot in the [Discord Developer Portal](https://discord.com/developers/applications). Enable all "Privileged Gateway Intents" and then under OAuth2 choose "bot" as the checkbox and then "Administrator". Copy the URL in your browser and add the bot to your server.
4. Still in the Discord Developer Portal, go to "Bot" and "reset token" if you don't have your token.
5. Create a `config.py` file in your root directory and add the following information:

```python
guild_id = some_number
bot_token = "your_token"
openai_key = "your_key"
```

The guild ID is the first number in the URL of the respective server. For `bot_token`, paste the token and your OpenAI key.

6. Run the bot using `python discord_bot.py`

## Usage

Go to the specific server and use the `/chat` command followed by your message to chat.

## Creating Your Own Plugins

To create your own plugin, follow these steps:

1. Create a new folder inside the `plugins` directory with the format `your_plugin_name`. For example, `weather_example_plugin`.
2. Inside the new folder, create two files: `functions.json` and `your_plugin_name_plugin.py`. For example, `weather_example_plugin.py`.
3. In the `functions.json` file, define the functions that your plugin will provide. Check out the [OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_call_functions_with_chat_models.ipynb) for all available formats.
4. In the `your_plugin_name_plugin.py` file, create a class with the same name as your plugin folder, but in CamelCase format. For example, `WeatherExamplePlugin`. This class should have an `__init__` method, a method for each function defined in `functions.json`, and any additional helper methods as needed.
5. In the `plugins_settings.json` file, add your plugin to the `plugins` object and set its `enabled` property to `true`. Let's say you created a plugin called "another_plugin", then the file would need to look like:

```json
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
```

6. Restart the bot to load your new plugin.

## Contributing

I accept pull requests so that this repository can grow with a diversity of plugins like the ChatGPT from OpenAI.
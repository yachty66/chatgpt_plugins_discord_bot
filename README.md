# ChatgptPluginsDiscordBot


ChatgptPluginsDiscordBot is a Discord bot that uses OpenAI's [function calling API](https://platform.openai.com/docs/guides/gpt/function-calling). It is designed to be easily extensible with custom plugins, allowing you to add new ones.

## Features

<iframe src="https://giphy.com/embed/kj2k4sqiyGMcWiES9W" width="480" height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/kj2k4sqiyGMcWiES9W">via GIPHY</a></p>

- Discord bot who
- Easily extensible with custom plugins
- Utilizes OpenAI's GPT-3.5-turbo for natural language processing

## Installation

1. Clone the repository
2. Install the required dependencies
3. Set up your OpenAI API key and Discord bot token in the config.py file
4. Run the bot using python discord_bot.py

## Usage

To get the current weather information, use the following command:
?

Replace [location] with the desired city and state, e.g., "San Francisco, CA".

## Creating Your Own Plugins

To create your own plugin, follow these steps:

1. Create a new folder inside the plugins directory with the format your_plugin_name_plugin. For example, weather_example_plugin.

2. Inside the new folder, create two files: functions.json and your_plugin_name_plugin.py. For example, weather_example_plugin.py.

3. In the functions.json file, define the functions that your plugin will provide. The format should be as follows:
]

4. In the your_plugin_name_plugin.py file, create a class with the same name as your plugin folder, but in CamelCase format. For example, WeatherExamplePlugin. This class should have an __init__ method, a method for each function defined in functions.json, and any additional helper methods as needed.

5. In the plugins_settings.json file, add your plugin to the plugins object and set its enabled property to true. For example:
}

6. Restart the bot to load your new plugin.

## Naming Conventions

- Plugin folder names should be in snake_case format and end with _plugin. For example, weather_example_plugin.
- Function names in functions.json should be in snake_case format. For example, get_current_weather.
- Class names in the plugin's Python file should be in CamelCase format. For example, WeatherExamplePlugin.

## Contributing

We welcome contributions to improve WeatherBot. If you have any suggestions or bug reports, please create an issue or submit a pull request.

## License

WeatherBot is released under the [MIT License](LICENSE). 
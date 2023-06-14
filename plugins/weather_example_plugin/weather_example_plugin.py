import openai
import json

#can define weather 
class WeatherExamplePlugin():
    def __init__(self, message, function_name):
        self.message = message
        self.function_name = function_name
    
    def get_current_weather(self, location, unit="fahrenheit"):
        """Get the current weather in a given location"""
        weather_info = {
            "location": location,
            "temperature": "72",
            "unit": unit,
            "forecast": ["sunny", "windy"],
        }
        return json.dumps(weather_info)
    
    def run_conversation(self):
        function_response = self.get_current_weather(
            location=self.message.get("location"),
            unit=self.message.get("unit"),
        )
        
        second_response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0613",
        messages=[
            {"role": "user", "content": "What is the weather like in boston?"},
            self.message,
            {
                "role": "function",
                "name": self.function_name,
                "content": function_response,
            },
        ],
        )
        return second_response
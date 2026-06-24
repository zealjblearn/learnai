import gradio as gr
from ollama import chat
import requests
# import inspect

# print(gr.__version__)
# print(gr.__file__)

# print(inspect.signature(gr.ChatInterface))

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get current weather information for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "Name of the city"
                    }
                },
                "required": ["city"]
            }
        }
    }
]


def get_weather(city):
    try:

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        response.raise_for_status()

        data = response.json()

        current = data["current_condition"][0]

        return f"""
City: {city}

Temperature: {current['temp_C']}°C

Humidity: {current['humidity']}%

Condition: {current['weatherDesc'][0]['value']}

Wind Speed: {current['windspeedKmph']} km/h
"""

    except Exception as e:
        return f"Error getting weather: {str(e)}"


def execute_tool(tool_name, arguments):

    if tool_name == "get_weather":

        city = arguments.get("city", "").strip()

        if not city:
            return "Please provide a city name."

        print(f"Getting weather for: {city}")

        return get_weather(city)

    return "Unknown tool"


def generate_response(message, history):

    messages = [
        {
            "role": "system",
            "content": """
You are a helpful AI assistant.

IMPORTANT:
- Use get_weather tool whenever user asks about:
  * weather
  * temperature
  * humidity
  * climate
  * forecast

- For all other questions answer normally.
"""
        }
    ]

    # Add chat history
    for msg in history:

        content = msg.get("content", "")

        if isinstance(content, list):

            text_parts = []

            for item in content:

                if (
                    isinstance(item, dict)
                    and item.get("type") == "text"
                ):
                    text_parts.append(
                        item.get("text", "")
                    )

            content = " ".join(text_parts)

        messages.append(
            {
                "role": msg["role"],
                "content": str(content)
            }
        )

    # Current user message
    if isinstance(message, dict):
        message = message.get("text", "")

    messages.append(
        {
            "role": "user",
            "content": str(message)
        }
    )

    print("\n========== REQUEST ==========")
    print(messages)

    try:

        response = chat(
            model="llama3.2",
            messages=messages,
            tools=TOOLS
        )

        tool_calls = response["message"].get(
            "tool_calls",
            []
        )

        # No tool required
        if not tool_calls:

            content = response["message"]["content"]

            yield content

            return

        # Add assistant tool-call message
        messages.append(
            {
                "role": "assistant",
                "content": response["message"].get(
                    "content",
                    ""
                )
            }
        )

        # Execute tools
        for tool in tool_calls:

            tool_name = tool["function"]["name"]

            arguments = tool["function"].get(
                "arguments",
                {}
            )

            print(
                f"\nExecuting Tool: {tool_name}"
            )
            print(arguments)

            result = execute_tool(
                tool_name,
                arguments
            )

            print("\nTool Result:")
            print(result)

            messages.append(
                {
                    "role": "tool",
                    "content": result
                }
            )

        # Final model response
        stream = chat(
            model="llama3.2",
            messages=messages,
            stream=True
        )

        full_response = ""

        for chunk in stream:

            content = chunk["message"]["content"]

            full_response += content

            yield full_response

    except Exception as ex:

        yield f"Error: {str(ex)}"


demo = gr.ChatInterface(
    fn=generate_response,
    title="🌤 Bharathi ChatBot"
)

demo.launch()
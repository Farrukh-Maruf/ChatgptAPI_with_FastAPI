import openai
import os
from openai import OpenAI
client = OpenAI(api_key=">>>")
#OpenAI.api_key = os.getenv('>>>')

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Hello!"}
#   ]
# )

# print(completion.choices[0].message.content)

#openai.api_key = ">>>"  # Add your OpenAI API key here

def generate_description(input):
    messages = [
        {"role": "user",
         "content": """As a Product Description Generator, Generate multi paragraph rich text product description with emojis from the information provided to you' \n"""}
    ]

    messages.append({"role": "user", "content": f"{input}"})
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    reply = completion.choices[0].message.content
    return reply

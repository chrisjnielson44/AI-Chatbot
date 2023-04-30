import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Define the function to generate the response
def generate_response(prompt):
    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    max_tokens=os.getenv("YOUR_DESIRED_MAX_TOKEN_AMOUNT"),
    temperature=os.getenv("YOUR_DESIRED_TEMP"),
    messages = response.choices[0].text.strip()
    )
    return response

# Define the file to store the conversation
conversation_file = "conversation.txt"

# Create the file if it doesn't exist
if not os.path.exists(conversation_file):
    with open(conversation_file, "w") as f:
        f.write("")

# Open the file and read the last line
while True:
    user_input = input("You: ")
    prompt = f"You say: {user_input}\nAI says:"
    response = generate_response(prompt)
    print("AI:", response)

    with open(conversation_file, "a") as f:
        f.write(user_input + "\n")
        f.write(response + "\n")

import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("YOUR_OPENAI_API_KEY")

#  Define the function to generate the response from the AI
def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=int(os.getenv("YOUR_DESIRED_MAX_TOKEN_AMOUNT")),
        n=int(os.getenv("NUMBER_OF_COMPLETIONS")),
        stop=None,
        temperature=float(os.getenv("YOUR_DESIRED_TEMP")),
    )

    message = response.choices[0].text.strip()
    return message

# Create a file to store the conversation
conversation_file = "conversation.txt"

# Create the file if it doesn't exist
if not os.path.exists(conversation_file):
    with open(conversation_file, "w") as f:
        f.write("")

# Start the conversation
print("AI: Hello, I am an AI chatbot. I am very smart. Ask me anything! If you want to stop talking to me, just type 'exit'.")
while True:
    user_input = input("You: ")
    # Exit when the user says "exit"
    if user_input.lower() == "exit":
        break
    prompt = f"You say: {user_input}\nAI says:"
    response = generate_response(prompt)
    print("AI:", response)

    with open(conversation_file, "a") as f:
        f.write(user_input + "\n")
        f.write(response + "\n")

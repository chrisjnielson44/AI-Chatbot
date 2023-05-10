from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("YOUR_OPENAI_API_KEY")

# Define the function to generate the response from the AI
def generate_response(prompt, conversation_history):
    prompt_with_history = f"{conversation_history}\n{prompt}"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_with_history,
        max_tokens=int(os.getenv("YOUR_DESIRED_MAX_TOKEN_AMOUNT")),
        n=int(os.getenv("NUMBER_OF_COMPLETIONS")),
        stop=None,
        temperature=float(os.getenv("YOUR_DESIRED_TEMP")),
    )
    message = response.choices[0].text.strip()
    return message


app = Flask(__name__)

# Create a file to store the conversation
conversation_file = "conversation.txt"

# Create the file if it doesn't exist
dir_path = os.path.dirname(os.path.abspath(__file__))
conversation_file = os.path.join(dir_path, "conversation.txt")
if not os.path.exists(conversation_file):
    with open(conversation_file, "w") as f:
        f.write("")

# Define the home page
@app.route("/", methods=["GET", "POST"])
def home():
    # Start the conversation
    if request.method == "GET":
        return render_template("home.html")
    elif request.method == "POST":
        conversation_history = request.form.get("conversation_history")
        user_input = request.form.get("user_input")

        # Handle the exit button
        action = request.form.get("action")
        if action == "exit":
            with open(conversation_file, "w") as f:
                f.write("")
            return render_template("home.html")

        # Check if user pressed "cmd + Enter" or "windows key + Enter"
        if request.form.get("submit_hotkey"):
            prompt = f"You say: {user_input}\nAI says:"
            response = generate_response(prompt, conversation_history)
            conversation_history += f"\nUser: {user_input}\nAI: {response}"
            with open(conversation_file, "a") as f:
                f.write(user_input + "\n")
                f.write(response + "\n")
            return render_template("home.html", response=response, conversation_history=conversation_history)

        return render_template("home.html", conversation_history=conversation_history, user_input=user_input)


if __name__ == '__main__':
    app.run(debug=True)

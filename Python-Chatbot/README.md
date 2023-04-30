## Installation (for Python-Chatbot)
To use the python chatbot, first, clone the repository onto your local machine:
```bash
git clone https://github.com/chrisjnielson44/AI-Chatbot
```
Next, install the required dependencies by running the following command:
```bash
pip install openai python-dotenv
```
Finally, create a .env file in the root directory of the project and add your OpenAI API key (Copy .env.example):
```bash
YOUR_OPENAI_API_KEY=YOUR_API_KEY
YOUR_DESIRED_MAX_TOKEN_AMOUNT=YOUR_DESIRED_MAX_TOKEN_AMOUNT
YOUR_DESIRED_TEMP=YOUR_DESIRED_TEMP
NUMBER_OF_COMPLETIONS=NUMBER_OF_COMPLETIONS
```
## Usage (for Python-Chatbot)

To start the chatbot, run the chatbot.py file:
```bash
python chatbot.py
```
The chatbot will start running and you can begin chatting with it by typing in the terminal.

The chatbot will remember previous conversations and learn from them, allowing for more personalized and natural interactions. It can be used for a wide variety of applications, such as customer support, personal assistants, and more.
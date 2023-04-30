# Open A.I. Chatbot
This is a chatbot developed using Python and OpenAI's GPT-3.5 architecture. The chatbot is designed to remember conversations with the user and learn from them, allowing for more personalized and natural interactions.

## Installation
To use the chatbot, first, clone the repository onto your local machine:
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
## Usage

To start the chatbot, run the main.py file:
```bash
python chatbot.py
```
The chatbot will start running and you can begin chatting with it by typing in the terminal.

The chatbot will remember previous conversations and learn from them, allowing for more personalized and natural interactions. It can be used for a wide variety of applications, such as customer support, personal assistants, and more.

## Contributing

If you would like to contribute to the project, please follow these steps:

1. Fork the repository
2. Create a new branch (git checkout -b feature/your_feature)
3. Make your changes
4. Commit your changes (git commit -am 'Added some feature')
5. Push to the branch (git push origin feature/your_feature)
6. Create a new Pull Request

## Acknowledgments
Thanks to OpenAI for providing the GPT-3.5 architecture and enabling the development of this chatbot.
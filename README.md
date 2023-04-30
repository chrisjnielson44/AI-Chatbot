# Open A.I. Chatbot
This is a chatbot developed using Python and OpenAI's GPT-3.5 architecture. The chatbot is designed to remember conversations with the user and learn from them, allowing for more personalized and natural interactions.

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
## Installation (for Web-AIChatbot)
To use the python flask/web version, first, clone the repository onto your local machine:
```bash
git clone https://github.com/chrisjnielson44/AI-Chatbot
```
Next, instainstall the required dependencies by running the following command:
```bash
pip install openai python-dotenv flask
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

## Usage (for WebAI-Chatbot)
To run the flask server on your localhost, run the flaskchatbot.py
```bash
python3 flaskchatbot.py
```
When running the flask server in debug-mode you will recieve this output:
```bash 
 * Serving Flask app 'flaskchatbot'
 * Debug mode: on
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on (YOUR LOCAL HOST:5000)
Press CTRL+C to quit
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: DEBUG_PIN
 ```
Now you should be able to see the chatbot on your localhost:5000.
## ngrok Server
If you would like to see the flask server outside of your local host, one easy method is using ***ngrok***.\
To start an ngrok server, you can sign up for a free account on their website https://ngrok.com \
Then you can download ngrok to your specifc os. (Using linux as example) \
\
You can unzip ngrok by:
```bash
unzip /path/to/ngrok.zip
```
Then you can connect your account by adding your given api key with:
```bash
ngrok config add-authtoken 'YOUR_NGROK_API_KEY'
```
Finally you can start your ngrok server with the command:
```bash
ngrok http 5000
```
This will connect the flask server running on localhost:5000 to your ngrok server. \
ngrok will provide you a link that forwards your local host. Here you can access the chatbot outside of your localhost.

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
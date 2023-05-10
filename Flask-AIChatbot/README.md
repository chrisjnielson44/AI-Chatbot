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

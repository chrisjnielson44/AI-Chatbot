import React, { useState } from "react";
import axios from "axios";

function App() {
  const [conversationHistory, setConversationHistory] = useState("");
  const [userInput, setUserInput] = useState("");
  const [response, setResponse] = useState("");

  const handleUserInput = (e) => {
    setUserInput(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (userInput.trim() === "") return;

    const prompt = `You say: ${userInput}\nAI says:`;
    const promptWithHistory = `${conversationHistory}\n${prompt}`;

    try {
      const response = await axios.post(
        "https://api.openai.com/v1/engines/text-davinci-003/completions",
        {
          prompt: promptWithHistory,
          max_tokens: parseInt(process.env.REACT_APP_DESIRED_MAX_TOKEN_AMOUNT),
          n: parseInt(process.env.REACT_APP_NUMBER_OF_COMPLETIONS),
          stop: null,
          temperature: parseFloat(process.env.REACT_APP_DESIRED_TEMP),
        },
        {
          headers: {
            Authorization: `Bearer ${process.env.REACT_APP_OPENAI_API_KEY}`,
            "Content-Type": "application/json",
          },
        }
      );

      const message = response.data.choices[0].text.trim();
      const newConversationHistory = `${conversationHistory}\nUser: ${userInput}\nAI: ${message}`;

      setResponse(message);
      setConversationHistory(newConversationHistory);
      setUserInput("");
    } catch (error) {
      console.error(error);
    }
  };

  const handleExit = () => {
    setConversationHistory("");
    setUserInput("");
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <textarea
          value={conversationHistory}
          onChange={(e) => setConversationHistory(e.target.value)}
          readOnly
        />

        <input
          type="text"
          value={userInput}
          onChange={handleUserInput}
        />

        <button type="submit">Send</button>
        <button type="button" onClick={handleExit}>Exit</button>
      </form>

      <div>
        <strong>AI Response:</strong>
        <p>{response}</p>
      </div>
    </div>
  );
}

export default App;

import React, { useState } from 'react';
import { Container, Form, Button } from 'react-bootstrap';
import axios from 'axios';

function Chatbot() {
  const [message, setMessage] = useState('');
  const [chat, setChat] = useState([]);

  const sendMessage = async () => {
    // send a POST request to the chatbot API with the user's message
    const response = await axios.post('http://localhost:8000/handle_user_query/', { message });

    // update the chat state with the chatbot's response
    setChat([...chat, { message, isUser: true }]);
    setChat([...chat, { message: response.data.message, isUser: false }]);

    // clear the message input field
    setMessage('');
  }

  return (
    <Container>
      <div className="chat-container">
        <div className="chat-header">
          <h1>Travel Chatbot</h1>
          <img src="/assets/TravelChatbot.png" alt="Chatbot Icon" className="chatbot-icon" />
        </div>
        <div className="messages">
          {chat.map((chatMessage, index) => (
            <div key={index} className={`message ${chatMessage.isUser ? 'user' : 'chatbot'}`}>
              {chatMessage.message}
            </div>
          ))}
        </div>
        <Form onSubmit={(e) => { e.preventDefault(); sendMessage(); }}>
          <Form.Group className="input-container">
            <Form.Control type="text" placeholder="Type your message here" value={message} onChange={(e) => setMessage(e.target.value)} />
            <Button variant="primary" type="submit">
              Send
            </Button>
          </Form.Group>
        </Form>
      </div>
    </Container>
  );
}

export default Chatbot;

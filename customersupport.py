
import streamlit as st
from textblob import TextBlob
import random

# Simple Knowledge Base
knowledge_base = {
    "hello": "Hi there! How can I assist you today?",
    "hi": "Hello! How can I help you?",
    "how are you": "I am a bot, so I don't have feelings, but I'm ready to help you!",
    "what is deriv": "Deriv is an online trading platform offering various financial instruments like CFDs, options, and multipliers.",
    "trading": "Deriv offers CFD trading, options, and multipliers. You can learn more on their official website.",
    "account": "For account-related issues, please visit the 'Help' section on Deriv's website or contact their official support.",
    "thank you": "You're welcome! Is there anything else I can help you with?",
    "bye": "Goodbye! Have a great day!",
    "support": "You can find more support options on the official Deriv website, including FAQs and live chat."
}

def get_chatbot_response(user_input):
    user_input_lower = user_input.lower()

    # Check knowledge base for direct answers
    for key, value in knowledge_base.items():
        if key in user_input_lower:
            return value

    # Sentiment analysis
    analysis = TextBlob(user_input)
    sentiment = analysis.sentiment.polarity

    if sentiment > 0.2: # Positive sentiment
        responses = [
            "That sounds positive! How can I help further?",
            "Great to hear! What else can I do for you?"
        ]
    elif sentiment < -0.2: # Negative sentiment
        responses = [
            "I understand you might be feeling frustrated. Please tell me more so I can assist you better.",
            "I'm sorry to hear that. Can you elaborate on the issue?"
        ]
    else: # Neutral sentiment or not found in KB
        responses = [
            "I'm not sure I understand. Could you please rephrase?",
            "Can you provide more details about your query?",
            "I'm still learning. For complex issues, please refer to Deriv's official support channels."
        ]
    return random.choice(responses)

st.title("Deriv Customer Support Chatbot")
st.write("Hello! I'm here to assist you with your Deriv-related questions.")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# React to user input
if prompt := st.chat_input("Ask me anything about Deriv..."):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_chatbot_response(prompt)
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat history
    st.session_state.messages.append({"role": "assistant", "content": response})


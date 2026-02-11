# Deriv Customer Support Chatbot

A Streamlit-based customer support chatbot tailored for Deriv, featuring a knowledge base lookup system and sentiment-aware responses using TextBlob NLP.

## Features

- **Knowledge Base System**: 18 predefined Q&A pairs covering Deriv platform topics including trading, AI/ML, NLP, MLOps, vector search, generative AI, and transformers
- **Sentiment Analysis**: Uses TextBlob to analyze user sentiment and provide contextually appropriate responses (positive, negative, or neutral)
- **Chat Interface**: Real-time conversational UI using Streamlit's native chat components with persistent session history
- **Keyword Matching**: Substring-based lookup against the knowledge base for direct answers
- **Fallback Responses**: Randomized, sentiment-aware fallback responses when no knowledge base match is found

## How It Works

1. User types a message in the chat input
2. The system checks the knowledge base for keyword matches (substring matching)
3. If no match is found, TextBlob performs sentiment analysis on the input
4. Based on sentiment polarity:
   - **Positive (>0.2)**: Encouraging, helpful responses
   - **Negative (<-0.2)**: Empathetic, supportive responses
   - **Neutral**: Generic help prompts directing to official support
5. Both user messages and bot responses are stored in session state for conversation continuity

## Topics Covered

- Deriv platform overview and goals
- AI and ML at Deriv
- CFD trading, options, and multipliers
- NLP, MLOps, and vector search technologies
- Generative AI and transformer models
- Account support and general assistance

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```bash
streamlit run customersupport.py
```

The application will open in your browser at `http://localhost:8501`.

## Dependencies

- **streamlit** - Web application framework with chat UI components
- **textblob** - Natural language processing for sentiment analysis

## Project Structure

```
.
├── customersupport.py    # Main Streamlit chatbot application
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## License

MIT License

# Console Chat with LLM

A simple console-based chatbot that uses OpenRouter API to interact with the Google Gemini model.

## Requirements

- Python 3.8 or higher
- OpenRouter API key

## Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
- On Windows:
```bash
.\venv\Scripts\activate
```
- On Unix or MacOS:
```bash
source venv/bin/activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Make sure your virtual environment is activated
2. Run the chatbot:
```bash
python src/chatbot.py
```
3. Type your messages and press Enter to chat
4. Type 'exit' to quit the application

## Features

- Simple console-based interface
- Uses Google's Gemini model through OpenRouter API
- Error handling for API requests
- Easy to extend and modify

## Note

The API key is currently hardcoded in the source code. In a production environment, it should be stored in an environment variable or a secure configuration file. 
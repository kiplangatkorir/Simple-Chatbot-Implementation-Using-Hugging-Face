# Chatbot App

A simple chatbot application built with Flask and Hugging Face's `transformers` library.

## Features

- Web interface for interacting with the chatbot.
- Context management to maintain conversation history.
- Basic user authentication (can be extended).
- Deployment-ready with Flask and Gunicorn.

## Requirements

- Python 3.6+
- Flask
- transformers
- gunicorn (for deployment)

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/chatbot-app.git
    cd chatbot-app
    ```

2. Install the dependencies:

    ```sh
    pip install -r requirements.txt
    ```

3. Run the application:

    ```sh
    python run.py
    ```

4. Open your browser and navigate to `http://127.0.0.1:5000/`.

## Deployment

To deploy the application, you can use platforms like Heroku or AWS. Make sure to install Gunicorn and create a `Procfile`:


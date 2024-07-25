# Voice Assistant

A simple and fun voice assistant built using Flask and various Python libraries for speech recognition, text-to-speech, and more. This assistant can play songs, tell jokes, provide the current time, and search Wikipedia.

## Features

- **Voice Commands**: Control the assistant with your voice.
- **Play Songs**: Play any song on YouTube by giving a voice command.
- **Tell Jokes**: Get a random joke.
- **Tell Time**: Know the current time.
- **Search Wikipedia**: Get a brief summary from Wikipedia.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework.
- **SpeechRecognition**: Library for performing speech recognition.
- **Pyttsx3**: Text-to-speech conversion library.
- **PyWhatKit**: Library for YouTube automation.
- **Wikipedia-API**: Python wrapper for Wikipedia.
- **PyJokes**: Python library for programming and general jokes.

## Installation

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/pooyanazad/voice-assistant.git
    cd voice-assistant
    ```

2. **Create and Activate a Virtual Environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Running the Application

1. **Start the Flask App**:
    ```sh
    python app.py
    ```

2. **Open your browser** and go to `http://127.0.0.1:5000`.

## Usage

- Click the **"Start Listening"** button to activate the assistant.
- Give voice commands such as:
  - "Play Despacito"
  - "Tell me a joke"
  - "What time is it?"
  - "Search Python programming"
- Click the **"Stop"** button to stop the assistant.

## Project Structure

```plaintext
voice-assistant/
├── static/
│   ├── css/
│   │   └── styles.css
│   └── js/
│       └── scripts.js
├── templates/
│   └── index.html
├── app.py
└── README.md

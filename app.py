from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import threading

app = Flask(__name__)

recognizer = sr.Recognizer()
tts_engine = pyttsx3.init()

voices = tts_engine.getProperty('voices')
tts_engine.setProperty('voice', voices[1].id)

tts_lock = threading.Lock()

def speak(text):
    with tts_lock:
        tts_engine.say(text)
        tts_engine.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            command = recognizer.recognize_google(audio)
            command = command.lower()
            return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
        return ""
    except sr.RequestError:
        speak("Sorry, my speech service is down.")
        return ""

def tell_joke():
    return pyjokes.get_joke()

def play_song(song):
    pywhatkit.playonyt(song)

def tell_time():
    return datetime.datetime.now().strftime('%I:%M %p')

def search_wikipedia(topic):
    return wikipedia.summary(topic, sentences=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    command = data.get('command')

    response = ""
    if 'listen' in command:
        command = listen()
        if not command:
            response = "I didn't catch that. Please try again."
        elif 'play' in command:
            song = command.replace('play', '')
            threading.Thread(target=play_song, args=(song,)).start()
            response = f"Playing {song} on YouTube"
            threading.Thread(target=speak, args=(response,)).start()
        elif 'time' in command:
            response = tell_time()
            threading.Thread(target=speak, args=(response,)).start()
        elif 'joke' in command:
            response = tell_joke()
            threading.Thread(target=speak, args=(response,)).start()
        elif 'search' in command:
            topic = command.replace('search', '')
            response = search_wikipedia(topic)
            threading.Thread(target=speak, args=(response,)).start()
        elif 'stop' in command:
            response = "Goodbye!"
            threading.Thread(target=speak, args=(response,)).start()
        else:
            response = "I didn't get that. Can you please repeat?"
            threading.Thread(target=speak, args=(response,)).start()
    elif 'stop' in command:
        response = "Goodbye!"
        threading.Thread(target=speak, args=(response,)).start()
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)




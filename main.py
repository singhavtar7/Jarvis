import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def WishMe():
    hour = datetime.datetime.now().hour
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir")    
    else:
        speak("Good Evening Sir")

    speak("How Can I Help You?")


def jokes():
    joke = pyjokes.get_joke(language='en', category='all')
    return joke


def TakeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User Said: {query}")

    except Exception as e:    
        print("Can You Say That Again?")
        return "None"
    return query

if __name__=='__main__':
    WishMe()
    while True:
        query = TakeCommand().lower()

        if 'hello jarvis' in query or 'hello jarvis how are you' in query or 'hello' in query:
            speak("Hello Sir, How are you?")

        elif 'i am fine' in query or 'fine' in query:
            speak("Great, how can I help you?")  

        elif 'open youtube' in query:
            speak("OK!")
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            speak("OK!")
            webbrowser.open("https://www.google.com")

        elif 'open facebook' in query:
            speak("OK!")
            webbrowser.open("https://www.facebook.com")

        elif 'open groww' in query:
            speak("OK!")
            webbrowser.open("https://groww.in")

        elif 'tell me a joke' in query:
            joke = jokes()
            speak(joke)

        elif 'good bye' in query or 'bye' in query:
            speak('Have a nice day ahead!')

        
        else:
            speak("Please say that again")

import speech_recognition as sr # lets write full documentaion of this whole project in last of this file
import os
import webbrowser
import openai
import datetime
import random
import pyttsx3
import requests
import json

openai.api_key = "" # use your openai api key here
open_weather_api_key = "" # use your openweathermap api key here

chatStr = ""
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Shivam sir: {query}\n Jarvis: "
    response = openai.Completion.create(
        model="text-davinci-003", # this is the model id of openai api means which model we are using to chat with user
        prompt=chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    speak(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

def get_weather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?q=" + delhi + "&appid=" +"you api key without ("")" + "&units=metric"
    response = requests.get(url)
    data = response.json()
    if data["cod"] == "404":
        return "City not found"
    else:
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        return f"The weather in {city} is {weather_desc}. Temperature: {temperature}°C, Humidity: {humidity}%, Wind Speed: {wind_speed} m/s"

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    speak("Hello shivam sir this is jarvis your artificial intelligence assistant how may i help you sir ?")
    while True:
        print("Listening...")
        query = takeCommand()

        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                speak(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

        if "open music" in query:
            musicPath = r"C:\MUsic"
            os.system(f"start {musicPath}")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir, the time is {hour} o'clock {min} minutes")

        elif "open facetime".lower() in query.lower():
            os.system("start ms-call:")

        elif "open pass".lower() in query.lower():
            # Add code for opening Passky app
            pass

        elif "Using artificial intelligence".lower() in query.lower():
            # Add code for AI response using OpenAI
            ai(prompt=query)

        elif "Jarvis Quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        elif "what is the weather in" in query.lower():
            city = query.split("in", 1)[1].strip()
            weather_info = get_weather(city)
            speak(weather_info)

        else:
            print("Chatting...")
            response = chat(query)
            print(response)


# Documentation of this project


# 1. speech_recognition module is used to recognize the speech of user
# 2. os module is used to open any file or folder or any application
# 3. webbrowser module is used to open any website
# 4. openai module is used to use openai api to use artificial intelligence
# 5. datetime module is used to get the current time
# 6. random module is used to generate random numbers which is used in this project to generate random responses like "I am fine" or "I am good"
# 7. pyttsx3 module is used to convert text to speech and speak it
# 8. requests module is used to make http requests to get weather information from openweathermap api
# 9. json module is used to parse json data
# 10. chatStr is a string variable which is used to store the chat history of user and jarvis
# 11. engine is a pyttsx3 engine object which is used to convert text to speech and speak it engine = pyttsx3.init()
# 12. speak() function is used to convert text to speech and speak it
# 13. chat() function is used to chat with user using openai api
# 14. takeCommand() function is used to take command from user using microphone
# 15. get_weather() function is used to get weather information of any city using openweathermap api
# 16. main() function is the main function of this project which is used to run this project
# 17. sites is a list of lists which contains the name of websites and their urls
# 18. musicPath is a string variable which contains the path of music folder
# 19. hour is a string variable which contains the current hour
# 20. min is a string variable which contains the current minute
# 21. city is a string variable which contains the name of city
# 22. weather_info is a string variable which contains the weather information of city
# 23. response is a string variable which contains the response of jarvis
# 24. query is a string variable which contains the command of user
# 25. r is a speech_recognition recognizer object which is used to recognize the speech of user
# 26. audio is a speech_recognition audio object which is used to store the audio of user
# 27. url is a string variable which contains the url of openweathermap api
# 28. response is a requests response object which is used to store the response of openweathermap api
# 29. data is a dictionary which contains the data of response
# 30. weather_desc is a string variable which contains the weather description of city
# 31. temperature is a string variable which contains the temperature of city
# 32. humidity is a string variable which contains the humidity of city

# 1. The main() function is the main function of this project which is used to run this project
# 2. engine.runAndWait() is used to run the pyttsx3 engine and wait for it to complete
# 3. engine.setProperty() is used to set the property of pyttsx3 engine means the voice of pyttsx3 engine will be rate 150 words per minute
# 4. engine.say() is used to convert text to speech and speak it
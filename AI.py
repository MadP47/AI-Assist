import os
import subprocess
import wolframalpha
import pyttsx3
import json
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyjokes
import smtplib
import ctypes
import time
import requests
import shutil
from ecapture import ecapture as ec
from urllib.request import urlopen


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()


def wishme ():
    
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Goodmorning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    ainame = ("Del 1 point o")
    speak("I am your Assistant")
    speak(ainame)


def takecommand():                         
    
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)

    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query


def username():
    
    speak("What should I call you sir")
    uname = takecommand()
    speak("Welcome Mister")
    speak(uname)
    
    columns = shutil.get_terminal_size().columns

    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")


def sendEmail(to, content):
    
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()

    server.login('your email id', 'your email password')
    server.sendmail('your email id', to, content)
    server.close()


if __name__ == '__main__':
    
    clear = lambda: os.system('cls')

    clear()
    wishme()
    username()

    while(True):

        query = takecommand().lower()

        if 'wikipedia' in query:

            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 5)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:

            speak("Okay Sir opening YouTube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:

            speak("Okay Sir opening Google\n")
            webbrowser.open("google.com")

        elif 'open whatsapp web' in query:

            speak("Sure opening Web Whatsapp\n")
            webbrowser.open("web.whatsapp.com")

        elif 'open stackoverflow' in query:
            
            speak("Okay sir opening Stack Over Flow in the browser\n")
            webbrowser.open("stackoverflow.com")

        elif 'open github' in query:

            speak("okay boss opening github\n")
            webbrowser.open("github.com")

        elif 'open chrome' in query:

            codepath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Google Chrome.lnk"
            os.startfile(codepath)

        elif "play music" in query or "play songs" in query:

            speak("Okay playing Music now")
            music_dir = r"C:\Users\malha_2tkyqys\Music"
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))

        elif "open vlc player" in query:

            vlcpath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\VideoLAN\VLC media player.lnk"
            os.startfile(vlcpath)

        elif "open py charm" in query:

            pypath = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\JetBrains\PyCharm Community Edition 2021.1.1.lnk"
            os.startfile(pypath)

        elif "open python" in query:

            path = r"C:\Users\malha_2tkyqys\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Python 3.10\IDLE (Python 3.10 64-bit).lnk"
            os.startfile(path)

        elif "open git bash" in query:

            bashpath = r"C:\Users\Public\Desktop\Git Bash.lnk"
            os.startfile(bashpath)

        elif "open steam" in query:

            spath = r"C:\Users\Public\Desktop\Steam.lnk"
            os.startfile(spath)

        elif "what is the time" in query or "tell me the time" in query:
            
            strTime = datetime.datetime.now().strftime("% H:% M:% S")   
            speak(f"Sir, the time is {strTime}")

        elif 'send a mail' in query:
            
            try:
                speak("What should I write in the Email?")
                content = takecommand()
                speak("to whome should i send")
                to = input()   
                sendEmail(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif 'how are you' in query:
            
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            
            query = query.replace("change my name to", "")
            ainame = query
 
        elif "change name" in query:

            speak("What would you like to call me, Sir ")
            ainame = takecommand()
            speak("Thanks for naming me")

        elif "what's your name" in query or "What is your name" in query:
            
            speak("My friends call me")
            speak(ainame)
            print("My friends call me", ainame)

        elif "who made you" in query or "who created you" in query:
            
            speak("I have been created by a superior being.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif "calculate" in query:
             
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)
 
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)

        
        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))

        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()


        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takecommand())
            time.sleep(a)
            print(a)
 
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")


        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6))

        elif "tell me the weather" in query:
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takecommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["code"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")

        elif 'exit' in query:
            speak("Thanks call me when you need me again")
            exit()
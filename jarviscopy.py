import audioop
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():    
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning sir!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon sir!")   

    else:
        speak('Good Evening sir!') 

    speak("I am jarvis. Please tell me how may I help you sir") 

def takeCommand():
    #It take microphone input from the user and returns string output     
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("Listening...")
        #  r.pause_threshold = 1
         audio = r.listen(source)

    try:
         print("Recognizing...")
         query = r.recognize_google(audio, language='en-US').lower()
         print(f"User said: {query}\n")


    except Exception as e:
        # print(e)    
        speak('Say that again please...') 
        print("Say that again please...")
        
        return"None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('cmoulick888@gmail.com',"D:\Python\password.txt")
    server.sendmail('cmoulick888@gmail.com', 'to content')
    server.close()


if __name__=="__main__":
    # speak("Chandan is a good boy")
    wishMe()
    while True:
    #  if 1:    
        query = takeCommand().lower()


    #Logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak('opening youtube...')
            webbrowser.open("youtube.com")

        elif 'google' in query:
            speak('opening google...')
            webbrowser.open("google.com")    

        elif 'open flipkart' in query:
            speak('opening flipkart...')
            webbrowser.open("https://www.flipkart.com/")

        elif 'open portfolio' in query:
            speak('opening portfolio...')
            webbrowser.open("https://chandan888.vercel.app/")


        elif 'play music' in query:
            music_dir = ""
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M")
            speak(f"Sir,the time is{strTime}")
            
        elif 'open facebook' in query:
            speak('opening facebook...')
            webbrowser.open("facebook.com")

        elif 'open instagram' in query:
            speak('opening instagram...')
            webbrowser.open("instagram.com")   

        elif 'open linkedin' in query:
            speak('opening linkedin...')
            webbrowser.open("linkedin.com") 

        elif 'send a email' in query:
             
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "cmoulick888@gmail.com"
                sendEmail=(to, content)
                speak("Email has been sent!")
            except Exception as e:   
                print(e) 
                speak("Sorry sir, I am not able to send this email.")
       
        elif "goodbye jarvis" in query:
            engine.say("see you again sir!")
            engine.runAndWait()
            exit()            



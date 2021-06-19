import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib
import pywhatkit
import pyautogui
import time
import googlesearch


webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:\Program Files\Google\Chrome\Application\chrome.exe"))


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice',voices[0].id)







def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak(" i am Friday sir, please tell me how may i help you")

def takecommand():
    #it takes microphone input from the use and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold=200
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f" User Said: {query}\n" )

    except Exception as e: 
        #print(e)

        print("say that again please...")
        speak("please,say that again")
        return "None"
    return query
def send_email(to, content):
    server = smtplib.SMTP('smtp.gamil.com',587)
    server.ehlo()
    server.starttls()
    server.login('xyz@gmail.com','xyz@9696938273')
    server.sendmail('xyz@gmail.com', to,content)
    server.close()




if __name__ == "__main__":
    wishme()
    while True:
    #if 1:
        query=takecommand().lower()
        #Logic For executing tasks based on query

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")
        
        elif 'open google' in query:
            webbrowser.get('chrome').open("google.com")
        
        elif 'open hackerrank' in query:
            webbrowser.get('chrome').open("hackerrank.com")

        elif 'open github' in query:
            webbrowser.get('chrome').open("github.com")

        elif 'open whatsapp' in query:
            webbrowser.get('chrome').open("https://web.whatsapp.com/")
        
        elif 'open classroom' in query:
            webbrowser.get('chrome').open("https://classroom.google.com/u/1/c/MjU1MTI4NDExNDU0")
        
        elif 'open erp' in query:
            webbrowser.get('chrome').open("https://evarsity.srmist.edu.in/srmsip/")
        
        elif 'play music' in query:
            music_dir='D:\\music'
            songs=os.listdir(music_dir)
            print(songs)
            random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[random.randint(1,len(songs))]))
        elif ' the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strtime}")
        
       

        elif 'open vs code' in query:
            codepath = "C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            speak("opening Visual Studio Code!")
            os.startfile(codepath)
        
        elif "close vs code" in query:
            speak("Closing Visual Studio Code!")
            os.system("taskkill /f /im Code.exe")
        
        elif 'open telegram' in query:
            codepath = "C:\\Users\\HP\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            speak("opening Telegram!")
            os.startfile(codepath)
        
        elif "close telegram" in query:
            speak("Closing Telegram!")
            os.system("taskkill /f /im Telegram.exe")
        
        elif 'open vlc' in query:
            codepath = "C:\\Program Files (x86)\\VideoLAN\\VLC\\vlc.exe"
            speak("opening VLc player!")
            os.startfile(codepath)
        
        elif "close vlc" in query:
            speak("Closing VLC player!")
            os.system("taskkill /f /im vlc.exe")

        elif 'open ms word' in query:
            codepath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            speak("opening Ms Word!")
            os.startfile(codepath)
        
        elif "close ms word" in query:
            speak("Closing Ms word!")
            os.system("taskkill /f /im WINWORD.exe")

        elif 'send email' in query:
            try:
                speak('what should i say?')
                content = takecommand()
                to = "xyz@gmail.com"
                send_email(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak("sorry sir, can not send email")


        elif 'play songs on youtube' in query:
            try:
                speak('which song you want to play?')
                content = takecommand()
                pywhatkit.playonyt(content)
                speak("playing on youtube")
        

            except Exception as e:
                print(e)
                speak("sorry sir, can not play this song")

        elif 'search on google' in query:
            print("what do you want to search")
            speak("what do you want to search")
            
            
            new=2
            taburl="https://www.google.com/?q="
            content=takecommand()
            print(content)
            webbrowser.open(taburl+content,new=new)
            
            time.sleep(2)
            pyautogui.press("enter")

            


        elif 'quit' in query:
            exit()




        
        

        
        
        
            
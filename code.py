import pyttsx3    #pip install pyttsx3
import speech_recognition as sr   #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning!")
    elif hour>= 12 and hour<18:
        speak("good afternoon!")
    else:
        speak("good evening")
    speak("Hello sir in am jarvis . how can i help you")
    
def takeCommand():
    ''' it take microphone input from user and returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1  # this is used to increase the pause time of speaking
        audio = r.listen(source)
        
    try:
        print('recognizing....')
        query = r.recognize_google(audio, language='en.in') # en.in = english india
        print(f"USER said: {query}\n")
    except Exception as e:
      # print(e)
        
        print("say that again please....")
        return "none"
    return query


''' before doing thismyou have to sign in your google account 
    2. then search for "less secure app in gmail" and see the instruction mention there'''

def sentEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)  # 587 = port number
    server.ehlo()
    server.starttls()
    server.login("senderemail@gmail.com","your-password")   #senderemail = email from which you are going to send email
    server.sendmail("recieveremail@gmail.com",to,content)   #recieveremail = email to which you want to send
    server.close()
    
    
if __name__ == "__main__":
    speak('hello there')
    wishMe()
    while True:   #if one time we want to run it then { if 1:}
       query =  takeCommand().lower() #lower is used to convert query in lower case
#logic for executing task based on query 
       if 'wikipedia' in query:             
        speak('Searching wikipedia......')
        query = query.replace("wikipedia","") #yaha pa agar wikipedia hoga toh wo blank sa replace ho jayega
        results = wikipedia.summary(query, sentences=2) #2 sentences return karega wikipedia sa
        speak("according to wikipedia")
        print(results)
        speak(results)
        
       elif 'open youtube' in query:
         webbrowser.open("youtube.com")
        
       elif 'open google' in query:
         webbrowser.open("google.com") 
       elif 'open wikipedia' in query:
         webbrowser.open("wikipedia.com") 
       elif 'open gmail' in query:
         webbrowser.open("gmail.com")
       elif 'open stackoverflow' in query:
         webbrowser.open("stackoverflow.com")
       elif 'play music' in query:
         music_dir ="E:\\music"
         songs = os.listdir(music_dir)
         os.startfile(os.path.join(music_dir,songs[0])) #try playing music using for loop as a task
       elif "time" in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"Sir,the time is{strTime}")
       elif "jupyter notebook" in query:
        codepath = "C:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Jupyter Notebook"
        os.startfile(codepath)
       elif "spyder" in query:
        codepath = "C:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Spyder"
        os.startfile(codepath) 
       elif "anaconda prompt" in query:
        codepath = "C:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Prompt"
        os.startfile(codepath) 
       elif "anaconda navigator" in query:
        codepath = "C:\\Users\\USER\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator"
        os.startfile(codepath) 
       
       
    # We can also send email to a person from our jarvis
        
       elif "send email" in query:
         try:
                speak("what should I say?")
                content = takeCommand()
                to ="emailid@gmail.com"
                sendEmail(to,content)
                speak("email sent")
         except Exception as e:
            print(e)
            speak("I am not able to send email")
            
        
        
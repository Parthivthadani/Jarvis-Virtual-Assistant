import pyttsx3
import speech_recognition as sr
import datetime as dt
import os
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import time
import sys
import pygame
import pyjokes
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui as pi
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#type of voice male or female
engine.setProperty('voices',voices[0].id)

#print and speak jarvis
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(audio)

#users voice capture and print it
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("recognition")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}")
    except Exception as e:
        print("sorry i can't hear your voice please say that again")
        return "none"
    return query
        


#wish me function 
def wish():
    hour=int(dt.datetime.now().hour)
    
    if hour>=0 and hour<=12:
        speak("good morning sir")
    elif hour>12 and hour<=18:
        speak("good afternoon sir")
    else:
        speak("good evening sir")
    speak("I am jarvis your personal asistance, how can i help you sir")
    
     
  #main logic
if __name__=="__main__":
    wish()
    
    while True:
        #speak("how may i help you sir")
        #offline files
        
        query=takecommand().lower()
    
        files=[["notepad","C:\\Windows\\System32\\notepad.exe"],["word","C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"],["powerpoint","C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"]]
        
        for file in files:
            if f"open {file[0]}" in query:
                speak(f"opening {file[0]}")
                os.startfile(file[1])
                
        #online sites
        sites=[["youtube","www.youtube.com"],["Facebook","www.facebook.com"],["instagram","www.instagram.com"],["whatsapp","www.whatsapp.com"]]
        
        for site in sites:
            if f"open {site[0]}" in query:
                speak(f"opening {site[0]}")
                webbrowser.open(site[1])        
            
            
    #closing files
        close_files=[["notepad","taskkill /f /im notepad.exe"],["word","taskkill /f /im word.exe"],["powerpoint","taskkill /f /im powerpoint.exe"]]
        for close_file in close_files:
            if f"close {close_file[0]}" in query:
                speak(f"closing {close_file[0]}")
                os.system(close_file[1])
                
    
        if "open google" in query:
            speak("sir,what should i search on google")
            search=takecommand().lower()
            webbrowser.open(search)
        
        elif "go to sleep" in query:
            speak("okk sir,have a good day")
            sys.exit()
        
        elif "the time" in query:
            strftime =dt.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is{strftime}")
        
        elif "open vlc" in query:
            speak("open vlc")
            os.startfile("D:\\parthiv\\VLC\\vlc.exe")
        elif "play music" in query:
            music_dir="C:\\Users\\sanch\\Music"
            songs=os.listdir(music_dir)
            for song in songs:
                if song.endswith(".mp3"):
                   # rd=random.choice(songs)
                    os.startfile(os.path.join(music_dir,random.choice(songs)))
            
        #task on opened plateform logic
        elif "song on youtube" in query:
            speak("sir,what song will you listen")
            song_name=takecommand().lower()
            kit.playonyt(song_name)
        
        elif "search on youtube" in query:
            query=query.replace("search on youtube"," ")
            webbrowser.open(f"www.youtube.com/results?search_query={query}")
        
        #close browsers
        close_browsers=[["microsoft edge","taskkill /f /im msedge.exe"],["chrome","taskkill /f /im chrome.exe"],["fire fox","taskkill /f /im firefox.exe"]]
        
        for close_browser in close_browsers:
            if f"close {close_browser[0]}" in query:
                speak(f"closing {close_browser[0]}")
                os.system(close_browser[1])
                
        
        
        if "search notepad" in query:
            pi.press('win')
            time.sleep(1)
            pi.typewrite('notepad',0.2)
            pi.press('enter')
            time.sleep(2)
        
        if "typing" in query:
            speak("what should i type sir")
            cm=takecommand().lower()
            pi.typewrite(cm,0.2)
            
        elif "camera" in query:
            pi.press('win')
            time.sleep(1)
            pi.typewrite('camera',0.2)
            pi.press('enter')
            time.sleep(2)
        
        elif "picture" in query:
            pi.press('enter') 
        
        elif "volume down" in query:
            for i in range(0,11):
                pi.press('volumedown')
                
        elif "volume up" in query:
            for i in range(0,11):
                pi.press('volumeup')
                
        
        elif "blank" in query:
            '''
            pi.moveTo()
            pi.click(x=257,y=229,clicks=1,button='left')       
            '''
            pi.press('enter')
        
        #control chrome
        if "open chrome" in query:
            chrome ="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chrome)
            time.sleep(1)
            pi.click(x=884, y=474,clicks=2,button='left')
        elif "new tab" in query:
            pi.hotkey('ctrl','t')
            
        
        elif "Incognito" in query:
            pi.hotkey('ctrl','shift','n')
        
        elif "next tab" in query:
            pi.hotkey('ctrl','tab')
        
        elif "previous tab" in query:
            pi.hotkey('ctrl','shift','tab')
        
        elif "home" in query:
            pi.hotkey('alt','home')
        
        elif "close tab" in query:
            pi.hotkey('ctrl','w')
        
        elif "downloads" in query:
            pi.hotkey('ctrl','j')
        
        elif "history" in query:
            pi.hotkey('ctrl','h')
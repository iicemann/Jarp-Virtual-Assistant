from gtts import gTTS #google text to speech
import speech_recognition as sr #support for various speech recognition engines/APIs
import os #to interact with os
import subprocess #open processes
import re 
import webbrowser #to access browser
import smtplib
import requests 
import json
from time import ctime
from datetime import datetime #to get system time
import time
import playsound #to play audio files
import random #generate random file names
import wolframalpha #to ask questions and report analysis and generation
from geopy.geocoders import Nominatim #to geo-locate addresses
#from weather import Weather

def talkToMe(audio):
    "speaks audio passed as argument."

    jarp_speak(audio)
    for line in audio.splitlines():
        os.system("say " + audio)

        
    #  use the system's inbuilt say command instead of mpg123
    #  text_to_speech = gTTS(text=audio, lang='en')
    #  text_to_speech.save('audio.mp3')
    #  os.system('mpg123 audio.mp3')


 
def myCommand(ask = False):
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        if ask:
            jarp_speak(ask)
        #print('What can I do for you today, sir?')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        jarp_speak('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        jarp_speak('Didn\'t get you there sir.')
        command = myCommand();

    #if assistant command is not found
    except sr.RequestError:
        jarp_speak('Sorry sir, my speech service is down.')

    return command


def jarp_speak(audio_string):
    tts = gTTS(text = audio_string, lang = 'en')
    r = random.randint(1, 10000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    location = "D:/Abhishek/AI Assistants"
    path = os.path.join(location, audio_file)
    os.remove(path)


def assistant(command):
    "if statements for executing commands"

    if 'hey jarp' in command or 'hi jarp' in command:
        jarp_speak('Here to serve you sir.') 

    elif 'who created you' in command or 'who made you' in command:
        jarp_speak('A very smart set of people.')

    elif 'what\'s up' in command or 'what you up to' in command or 'whats up' in command:
        jarp_speak('Nothing much, sir. Just waiting to assist you.')

    elif 'what are you' in command or 'tell me about yourself' in command:
        jarp_speak('Allow me to introduce myself. I\'m Jarp. A virtual artificial intelligence. \nAnd I am here to assist you with a variety of tasks as best as I can, twenty four hours a day, seven days a week. \n\nImporting all preferences from home interface. Systems are now fully operational.')
    
    elif 'what does jarp stand for' in command:
        jarp_speak('It stands for Just Another Replaced Person.')

    elif 'you up' in command or 'jarp you there' in command:
        jarp_speak('For you sir, always.')

    elif 'thanks' in command:
        jarp_speak('Anything for you sir.')
        
    elif 'that will be all' in command or 'exit' in command:
        jarp_speak('Can\'t wait to assist you sir.')
        exit()

    elif 'switchoff PC' in command or 'shutdown PC' in command:
        shutdown = myCommand('Do you want to shutdown the PC sir?')
        if shutdown == 'no':
            exit()
        else:
            jarp_speak('Shuting down this PC in approximately five seconds sir.')
            os.system('shutdown /s /t 1')

    elif 'what\'s the time' in command or 'what time is it' in command:
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        jarp_speak(time)

    elif 'what\'s the date' in command or 'what date is it' in command or 'what\'s today\'s date' in command:
        now = datetime.now()
        date = now.strftime("%m/%d/%Y")
        jarp_speak(date)

    elif 'what day is it' in command:
        #now = datetime.now()
        #day = now.strftime()
        tday = datetime.date.today()
        daytoday = tday.ctime()
        jarp_speak(daytoday)

    elif 'i love you' in command:
        jarp_speak('I love you 3000')

    elif 'don\'t let me down' in command:
        jarp_speak('I would never sir.')

    elif 'search' in command:
        search = myCommand('What do you want me to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        jarp_speak('Here is what I found for ' + search)

    elif 'location' in command:
        location = myCommand('What location do you need, sir?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        jarp_speak('Here is the location: ' + location)

    elif 'find me this address' in command or 'find me an address' in command:
        find_address = myCommand('Please state the address sir.')
        geolocator = Nominatim(user_agent = "Veronica")
        location = geolocator.geocode(find_address)
        jarp_speak('Here\'s the address sir: ' + location.address)
        jarp_speak('The latitude is: ' + location.latitude + ' and longitude is: ' + location.longitude)

    elif 'open google' in command:
        reg_ex = re.search('open google (.*)', command)
        url = 'https://www.google.com/'
        if reg_ex:
            google = reg_ex.group(1)
            url = url + 'r/' + google
        webbrowser.open(url)
        jarp_speak('Here you go, sir.')

    elif 'open youtube' in command:
        reg_ex = re.search('open youtube (.*)', command)
        url = 'https://www.youtube.com/'
        if reg_ex:
            youtube = reg_ex.group(1)
            url = url + 'r/' + youtube
        webbrowser.open(url)
        jarp_speak('Here you go, sir.')

    elif 'open website' in command:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            jarp_speak('Here you go, sir.')
        else:
            pass

    elif 'question' in command:
        question = myCommand('What question do you have for me sir?')
        jarp_speak(question)
        app_id = "AX5Y26-KXAGRT3QP5"
        client = wolframalpha.Client(app_id)
        res = client.query(question)
        if res['@success'] == 'false':
            jarp_speak('Not resloved')
        else:
            pod0 = res['pod'][0]['subpod']['plaintext']
            jarp_speak(pod0)
            # pod[1] may contains the answer
            pod1 = res['pod'][1]
            # checking if pod1 has primary=true or title=result|definition
            if (('definition' in pod1['@title'].lower()) or ('result' in  pod1['@title'].lower()) or (pod1.get('@primary','false') == 'true')):
                # extracting result from pod1
                result = pod1['subpod']['plaintext']
                jarp_speak(result)

    elif 'joke' in command:
        res = requests.get(
                'https://icanhazdadjoke.com/',
                headers={"Accept":"application/json"}
                )
        if res.status_code == requests.codes.ok:
            jarp_speak(str(res.json()['joke']))
        else:
            jarp_speak('Oops! I ran out of jokes')

    elif 'open calculator' in command:
        subprocess.Popen('C:\\Windows\\System32\\calc.exe')

    elif 'open notepad' in command:
        subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

    elif 'open wordpad' in command:
        subprocess.Popen('C:\\Windows\\System32\\write.exe')

    #elif 'current weather in' in command:
    #   reg_ex = re.search('current weather in (.*)', command)
    #    if reg_ex:
    #        city = reg_ex.group(1)
    #        weather = Weather()
    #        location = weather.lookup_by_location(city)
    #        condition = location.condition()
    #        jarp_speak('The Current weather in %s is %s The tempeture is %.1f degree' % (city, condition.text(), (int(condition.temp())-32)/1.8))

    #elif 'weather forecast in' in command:
    #    reg_ex = re.search('weather forecast in (.*)', command)
    #    if reg_ex:
    #        city = reg_ex.group(1)
    #        weather = Weather()
    #        location = weather.lookup_by_location(city)
    #        forecasts = location.forecast()
    #        for i in range(0,3):
    #            jarp_speak('On %s will it %s. The maximum temperture will be %.1f degree.'
    #                     'The lowest temperature will be %.1f degrees.' % (forecasts[i].date(), forecasts[i].text(), (int(forecasts[i].high())-32)/1.8, (int(forecasts[i].low())-32)/1.8))

    elif 'current weather' in command:
            api_key='30f82e5c879f2ac7af9fc8919e3e041a'
            base_url='https://api.openweathermap.org/data/2.5/weather?'
            jarp_speak('What\'s the city name?')
            city_name=myCommand()
            complete_url=base_url+"appid="+api_key+"&q="+city_name
            response = requests.get(complete_url)
            x=response.json()
            if x["cod"]!="404":
                y=x["main"]
                current_temperature = y["temp"] - 273.15
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                jarp_speak("Temperature in " + city_name +" in degree celsius is " +
                      str(current_temperature) +
                      "\nhumidity in percentage is " +
                      str(current_humidiy) +
                      "\ndescription  " +
                      str(weather_description))
            else:
                jarp_speak('City Not Found.')

    elif 'news' in command:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            jarp_speak('Here are some headlines from the Times of India sir.')

    elif 'email' in command:
        jarp_speak('Who is the recipient?')
        recipient = myCommand()

        if 'brian' in recipient:
            jarp_speak('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('brian hunt', 'brian@protonmail.com', content)

            #end mail connection
            mail.close()

            jarp_speak('Email sent.')

        else:
            jarp_speak('I don\'t know what you mean!')


jarp_speak('Alive and ready for you sir.')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())

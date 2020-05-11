
import json
import pyttsx3

############## This function is to convert text to speech ################

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

################# This helps in pulling out the information from web server ##############

import requests

#these are the classification of which type of news you want to Hear
url = ('http://newsapi.org/v2/top-headlines?'
       'country=in&'  
       'q=corona&'
       'apiKey=dd8da7ce0b4d4721a6d54026a0c4b47c')
response = requests.get(url)

############ response is in json format ###################
############ response.json is in dictionary ############

#### Here we print top 5 headlines of India and in query there is time #####
for i in range(5):
    print(response.json()['articles'][i]['title'])
    ############ response.json is in dictionary ############
    speak(response.json()['articles'][i]['title'])

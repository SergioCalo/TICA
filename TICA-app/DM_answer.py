from TTS import TTS
from streamlit_bokeh_events import streamlit_bokeh_events as ASR
import streamlit as st
import pandas as pd
import spacy
nlp = spacy.load("en_core_web_sm")

def action(intent, user_input, voice, name):
    answer = "I'm sorry, I didn't understand you"
    subaction = False
    keywords = ['museum', 'bar', 'restaurant', 'opera', 'theatre', 'music', 'event']
    database = pd.read_csv('/home/sergio/Documents/MIIS/NLI/TICA-app/models/Database.csv')

 
    if intent == "GREETING ":
        
        if name:
                answer = f'Hi again {name}!'
        else:               
                answer = "Hi! What's your name?"
                subaction = 'Greeting'

                            
    if intent == "GOODBYE ":
        answer = "Bye! See you soon!"
        
    if intent == "THANKS ":
        answer = "You are welcome!"
        
    if intent == "RECOMMENDATION ":
        print(database['Labels'])
        answer = 'Need more info'
        
    if intent == "ADD_INFO Positive":
        item = detect_item(user_input, keywords)
        answer = f'Oh, I know a couple of good {item}s'
        
    if intent == "ADD_INFO Negative":
        item = detect_item(user_input, keywords)
        answer = f'Okey, No {item}s today'
        
    return answer, subaction

def sub_greeting(name, voice):
    
    answer = f"Hi {name}, I'm Hermes, how can I help you?"
    subaction = False
    return answer, name, subaction


def detect_item(inpt, keywords):
    item = None
    doc = nlp(inpt)
    for token in doc:
        if token.lemma_ in keywords:
            item = token.lemma_        
    return item

    


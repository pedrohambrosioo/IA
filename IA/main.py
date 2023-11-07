import speech_recognition as sr 
import time
rec = sr.Recognizer()
import pyttsx3



#print(sr.Microphone().list_microphone_names()) MOSTRA OS MICROFONES

#VOZES DO SISTEMA 
# Inicialize o mecanismo de conversão de texto em fala
engine = pyttsx3.init()

# Liste as vozes disponíveis no sistema
voices = engine.getProperty('voices')

for voice in voices:
    print(f"Nome: {voice.name}")
    print(f"ID: {voice.id}")
    print(f"Línguas: {voice.languages}")
    print(f"Gênero: {voice.gender}")
    print(f"Taxa de fala: {voice.rate}\n")
 



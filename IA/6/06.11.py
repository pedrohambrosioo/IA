import speech_recognition as sr
import pyttsx3


def dialogo():#funcao de retorno de voz 
    engine = pyttsx3.init()            
    frase = "Estou terminando de ser configurada para te ajudar... até breve"            
    engine.say(frase)   
    engine.runAndWait()

recognizer = sr.Recognizer()
palavra_chave = "python"


with sr.Microphone(0) as source:
    print("Fale a palavra-chave para ativar o comando...")
    while True:
        audio = recognizer.listen(source)       
        try:
            recognized_text = recognizer.recognize_google(audio)#passa o audio para text

            if palavra_chave in recognized_text.lower():#execut se a fala tiver certa 
                print("Palavra-chave detectada. Ativando comando...")
                dialogo()
                pass

            else:#pula
                pass
       
        except sr.UnknownValueError:
            pass 
        except sr.RequestError as e:
            print(f"Erro na requisição para o Google API: {e}")
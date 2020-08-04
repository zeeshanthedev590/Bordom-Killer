import pyttsx3
import webbrowser
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def Main():
    speak('Are You Bored')
    a = input('Are You Bored :')
    if a=='yes':
        speak('Whats The Height Of Your Bordom 1 to 5')
        b=input('Whats The Height Of Your Bordom 1 to 5 : ')
        if b=='1':
            speak('''knok knok .  who is there .   Zeeshan .  Zeeshan Who . Zeeshan The Most Best Web Developer''')
        if b=='2':
         speak('Okay So You Can Do Some Python Programming ')

        if b=='3':
          speak('You Can Do Some Web Development ')

        if b=='4':
         speak('Make A Python Bot')

        if b=='5':
            speak('Okay Listen This Song ')
            webbrowser.open('https://www.youtube.com/watch?v=bwmSjveL3Lc')   



    else:
        speak('''Okay That's Great''')
        exit()    




if __name__ == "__main__":  
    Main()
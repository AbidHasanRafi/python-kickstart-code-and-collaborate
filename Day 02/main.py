import pyttsx3
import cowsay

text = "Thank you for joining our day 2"

engine = pyttsx3.init()

engine.say(text)

engine.runAndWait()

cowsay.cow("see you soon")
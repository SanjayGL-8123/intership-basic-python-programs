import pyttsx3

engine = pyttsx3.init()

text = input("enter some text: ")

engine.say(text)
engine.runAndWait()

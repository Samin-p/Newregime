import random
import pyttsx3#first you have write in the terminal(pip install pyttsx3)
from num2words import num2words as n#first you have write in the terminal(pip install num2words)
import webbrowser as o
poi=pyttsx3.init()
poi.setProperty("rate",150)
def s(x):
    poi.say(x)
    poi.runAndWait()
rt="https:\\www.chess.com"
p=random.randint(3000,3019)
lo=-1
s(f"Guess it between {n(3001)} and {n(3020)}")
while lo!=p:
    k=int(input("Guess the secret code"))
    if k>p:
        print("Lesser than the number")
        s("Lesser than the number")
    elif k<p:
        print("Higher than the number")
        s("Higher than the number")
    else:
        o.open(rt)
        s("Successfully opened")



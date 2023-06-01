import pyttsx3 as pd

# Initialize the text-to-speech engine
engine = pd.init()

# Function to convert text to speech
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

print("Welcome to Robospeaker created by Amith ")
# Read text from the terminal
while(True):
     text = input("Enter the text to convert to speech and if you would like to discontinue press type No/no: ")
     if text=="No" or text=="no":
        engine.say("Thank you for testing me out")
        engine.runAndWait()
        print("Thank you")
        break
# Convert text to speech
     text_to_speech(text)
  


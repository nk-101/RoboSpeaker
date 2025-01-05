'''
import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Nidhi")
    x=input("Enter what you want me to say:")
    command=f"say {x}"
    os.system(command)
'''
import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by Nidhi")
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    while True:

        x = input("Enter what you want me to say: ")
        if x=="q":
            engine.say("bye bye friend")
            engine.runAndWait()
            break

    # Initialize the text-to-speech engine
        engine.say(x)
        engine.runAndWait()

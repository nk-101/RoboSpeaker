import win32com.client   # Imports the Windows Speech API (SAPI) COM library

if __name__ == "__main__":
    print("Welcome to RoboSpeaker 1.1 Created by Nidhi")

    # Create a SAPI voice object (this is what actually speaks)
    speaker = win32com.client.Dispatch("SAPI.SpVoice")

    while True:
        # Take input from user
        x = input("Enter what you want me to say (q to quit): ").strip()

        # If user wants to quit
        if x.lower() == "q":
            speaker.Speak("bye bye friend")   # Speak goodbye
            break                              # End program

        # If user types something (not empty)
        if x:
            speaker.Speak(x)                  # Speak the typed text
        else:
            print("Empty input — try again.") # Inform user if they typed nothing

# RoboSpeaker 1.1
RoboSpeaker 1.1 is a simple text-to-speech Python program that uses the Windows Speech API (SAPI) to speak user-entered text aloud. It provides a quick and interactive way to convert typed text into speech.

# Features:
Speaks user input using Windows’ built-in voice
Works offline
Accepts both English and Hindi text (but Hindi voice is not native)
Runs continuously until the user exits
Says a goodbye message before closing

# Requirements:
Windows OS
Python 3.x
pywin32 library (install with: pip install pywin32)

# How to Use:
Run the script
Type any sentence you want it to speak
Type q to quit
RoboSpeaker says “bye bye friend” and exits

# Example:
Input: Hello world!
Output: Speaks “Hello world!”

Input: q
Output: Speaks “bye bye friend” and quits

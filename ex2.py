import speech_recognition as sr
recognizer=sr.Recognizer()
Audio_file='audio.wav'

try:
    with sr.AudioFile(Audio_file) as source:
        print(f"processing audio:{Audio_file}")
        audio=recognizer.record(source)

    text=recognizer.recognize_google(audio)
    print(f"text:{text}")
except sr.UnknownValueError:
    print("sorry i could not understand the audio")
except sr.RequestError as e:
        print(f"could not find the request in google translator:{e}")

import os
import speech_recognition as sr

def recognize_speech():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print("Please say something")

        audio = r.listen(source)

        print("Recognizing Now .... ")

        try:
            recognized_text = r.recognize_google(audio)
            print("You have said:\n" + recognized_text)
            print("Audio Recorded Successfully\n")

            return audio, recognized_text

        except Exception as e:
            print("Error: " + str(e))
            return None, None

def save_audio(audio, file_path):
    with open(file_path, "wb") as f:
        f.write(audio.get_wav_data())

def save_text(text, file_path):
    with open(file_path, "w") as f:
        f.write(text)

def main():
    audio, recognized_text = recognize_speech()

    if audio and recognized_text:
        save_audio_option = input("Do you want to save the audio file? (y/n): ").lower()
        save_text_option = input("Do you want to save the text file? (y/n): ").lower()

        if save_audio_option == 'y':
            audio_file_path = os.path.join(os.path.expanduser("~"), "Downloads", "recorded.wav")
            save_audio(audio, audio_file_path)
            print(f"Audio file saved to: {audio_file_path}")

        if save_text_option == 'y':
            text_file_path = os.path.join(os.path.expanduser("~"), "Downloads", "recognized_text.txt")
            save_text(recognized_text, text_file_path)
            print(f"Text file saved to: {text_file_path}")

if __name__ == "__main__":
    main()
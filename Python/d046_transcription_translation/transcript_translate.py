import sys

sys.path.append("/Users/lokeshkrishnappa/Desktop/python-projects/100-Days-Of-Code/Python/d018_recording_audio")
sys.path.append("/Users/lokeshkrishnappa/Desktop/python-projects/100-Days-Of-Code/Python/d042_translation")

import audio_recorder
import translation
import datetime

def make_transcript(filename):
    audio_recorder.record(filename)
    results = audio_recorder.transcribe(filename)

    return '\n'.join([
        result.alternatives[0].transcript
        for result in results
    ])

def main():
    a = input("Enter a name for your audio file, date will be added: ")
    filename = f"{a}-{datetime.datetime.today().strftime('%Y-%m-%d')}.wav"

    transcript = make_transcript(filename=filename)
    print(transcript)
    print()

    translation.translate_phrase("english", "spanish", transcript)

if __name__ == '__main__':
    main()
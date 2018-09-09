import sys

sys.path.append(
    '/Users/lokeshkrishnappa/Desktop/python-projects/100-Days-Of-Code/Python/d018_recording_audio')
sys.path.append(
    '/Users/lokeshkrishnappa/Desktop/python-projects/100-Days-Of-Code/Python/d042_translation')
sys.path.append(
    '/Users/lokeshkrishnappa/Desktop/python-projects/100-Days-Of-Code/Python/d046_transcription_translation')

import audio_recorder
import translation
import transcript_translate

import datetime

from google.cloud import texttospeech


def create_audio(text):
    client = texttospeech.TextToSpeechClient()
    input_text = texttospeech.types.SynthesisInput(text=text)

    voice = texttospeech.types.VoiceSelectionParams(
        language_code='es_ES',
        ssml_gender=texttospeech.enums.SsmlVoiceGender.MALE
    )

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.LINEAR16
    )

    response = client.synthesize_speech(input_text, voice, audio_config)

    return response.audio_content


def main():
    a = input(
        'Enter a name for your audio files, today\'s date will be added at the end: ')
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    filename = f'{a}-{today}.wav'
    translate_filename = f'{a}-translated-{today}.wav'

    transcript = transcript_translate.make_transcript(filename=filename)
    print(transcript)
    print()

    text = translation.translate_phrase('english', transcript, target='spanish')
    audio_content = create_audio(text)

    with open(translate_filename, 'wb') as f:
        f.write(audio_content)


if __name__ == '__main__':
    main()

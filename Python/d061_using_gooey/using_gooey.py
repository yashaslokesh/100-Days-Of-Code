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
import argparse
from gooey import Gooey

from google.cloud import texttospeech



def create_audio(text, client, language_code : str, gender : str):
    
    input_text = texttospeech.types.SynthesisInput(text=text)

    voice = texttospeech.types.VoiceSelectionParams(
        language_code=language_code,
        ssml_gender=texttospeech.enums.SsmlVoiceGender[gender])

    audio_config = texttospeech.types.AudioConfig(
        audio_encoding=texttospeech.enums.AudioEncoding.MP3
    )

    response = client.synthesize_speech(input_text, voice, audio_config)

    return response.audio_content

def parse_arguments(client):
    parser = argparse.ArgumentParser(description='Use this program to speak in one language '
                                     'and hear output in another!')
                                     
    parser.add_argument('--list_sources', )
    parser.add_argument('--source_lang')
    args = parser.parse_args()

def main():
    a = input(
        'Enter a name for your audio files, today\'s date will be added at the end: ')
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    filename = f'{a}-{today}.wav'
    translate_filename = f'{a}-translated-{today}.mp3'

    transcript = transcript_translate.make_transcript(filename=filename)
    print(transcript)
    print()

    client = texttospeech.TextToSpeechClient()

    voice_list = client.list_voices()
    languages = set((tuple(voice.language_codes), voice.ssml_gender) for voice in voice_list.voices)

    genders = ['SSML_VOICE_GENDER_UNSPECIFIED', 'MALE', 'FEMALE', 'NEUTRAL']
    options = '\n'.join(f'Language: {l[0]}, Gender: {genders[l[1]]}' for l in languages)

    t = input('Enter a language code and gender (male or female) for the voice translation, with the language first\n'
              'and the gender second, separated by a comma you can chose from\n'
              'Format: language code, gender (male or female)\n'
              f'{print(options)}')

    target_code, gender = tuple(word.strip() for word in t.split(','))

    print(f'Choices: {target_code} and {gender}')
    text = translation.translate_phrase('english', transcript, target_code=target_code[0:2])
    audio_content = create_audio(text, client, language_code=target_code, gender=gender)

    with open(translate_filename, 'wb') as f:
        f.write(audio_content)


if __name__ == '__main__':
    main()

from google.cloud import translate

def translate_phrase(source, target, phrase):
    client = translate.Client()

    source_language = [
        entry['language'] for entry in client.get_languages() 
        if entry['name'].lower() == source.strip().lower()
    ]

    target_language = [
        entry['language'] for entry in client.get_languages() 
        if entry['name'].lower() == target.strip().lower()
    ]
    print()

    if source.strip():
        result = client.translate(phrase, source_language=source_language[0], 
                 target_language=target_language[0])
        print(f'{source} was used as the source language.\n'
              f'Translating "{phrase}" to {target}:\n\n{result["translatedText"]}')
    else:
        result = client.translate(phrase, target_language=target_language[0])

        print(f'The language {result["detectedSourceLanguage"]} was detected.\n'
              f'Translating "{phrase}" to {target}:\n\n{result["translatedText"]}')
    
    print()

def main():
    source = input("Enter the language your phrase is in, or leave blank to infer language: ")
    target = input("Enter target language for translation: ")
    phrase = input("Enter the phrase you would like translated: ")
    translate_phrase(source, target, phrase)

if __name__ == '__main__':
    main()
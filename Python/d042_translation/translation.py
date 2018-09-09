from google.cloud import translate

def translate_phrase(source, phrase, target=None, target_code=None):
    client = translate.Client()

    source_language = next(entry['language'] 
                           for entry in client.get_languages() 
                           if entry['name'].lower() == source.strip().lower())

    if target_code == None:
        target_language = next(entry['language'] 
                               for entry in client.get_languages() 
                               if entry['name'].lower() == target.strip().lower())
    else:
        target_language = target_code
    print()

    to_lang = target if target != None else target_code

    if source.strip():
        result = client.translate(phrase, source_language=source_language, 
                 target_language=target_language)
        print(f'{source} was used as the source language.\n'
              f'Translating "{phrase}" to {to_lang}:\n\n{result["translatedText"]}')
    else:
        result = client.translate(phrase, target_language=target_language)

        print(f'The language {result["detectedSourceLanguage"]} was detected.\n'
              f'Translating "{phrase}" to {to_lang}:\n\n{result["translatedText"]}')
    
    print()

    return result['translatedText']

def main():
    source = input("Enter the language your phrase is in, or leave blank to infer language: ")
    target = input("Enter target language for translation: ")
    phrase = input("Enter the phrase you would like translated: ")
    translate_phrase(source, phrase, target=target)

if __name__ == '__main__':
    main()
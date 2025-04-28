# translator.py

from deep_translator import GoogleTranslator

def translate_text(text, target_lang='en'):
    translator = GoogleTranslator(source='auto', target=target_lang)

    max_chunk_size = 4000  # Set safe chunk size
    chunks = [text[i:i+max_chunk_size] for i in range(0, len(text), max_chunk_size)]

    translated_text = ""
    for chunk in chunks:
        translated_chunk = translator.translate(chunk)
        translated_text += translated_chunk + " "

    return translated_text
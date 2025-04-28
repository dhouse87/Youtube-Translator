import os
from audio_downloader import download_audio
from audio_transcriber import transcribe_audio
from translator import translate_text
from yt_dlp import YoutubeDL
from tqdm import tqdm

INPUT_FOLDER = 'input'
OUTPUT_FOLDER = 'output'

# Special translation handling for low-resource or difficult languages
special_translation_languages = {
    "armenian",
    "amharic",
    "georgian",
    "azerbaijani",
    "mongolian",
    "burmese",
    "myanmar",
    "lao",
    "khmer",
    "nepali",
    "sinhala",
    "pashto",
    "kurdish",
    "yoruba",
    "hausa",
    "somali",
    "tigrinya",
    "tajik",
    "farsi",
    "persian",
    "dari",
    "uzbek",
    "kazakh",
    "kyrgyz",
    "turkmen"
}

# ✅ NEW: Language name to ISO code mapping
language_map = {
    "armenian": "hy",
    "amharic": "am",
    "georgian": "ka",
    "azerbaijani": "az",
    "mongolian": "mn",
    "burmese": "my",
    "myanmar": "my",
    "lao": "lo",
    "khmer": "km",
    "nepali": "ne",
    "sinhala": "si",
    "pashto": "ps",
    "kurdish": "ckb",   # Central Kurdish (Sorani)
    "yoruba": "yo",
    "hausa": "ha",
    "somali": "so",
    "tigrinya": "ti",
    "tajik": "tg",
    "farsi": "fa",
    "persian": "fa",
    "dari": "fa",
    "uzbek": "uz",
    "kazakh": "kk",
    "kyrgyz": "ky",
    "turkmen": "tk",
    "russian": "ru",
    "ukrainian": "uk",
    "chinese": "zh",
    "japanese": "ja",
    "korean": "ko",
    "spanish": "es",
    "french": "fr",
    "german": "de",
    "portuguese": "pt",
    "italian": "it",
    "hindi": "hi",
    "bengali": "bn",
    "turkish": "tr",
    "vietnamese": "vi",
    "thai": "th",
    "swahili": "sw",
    "greek": "el",
    "dutch": "nl",
    "polish": "pl",
    "romanian": "ro",
    "serbian": "sr",
    "croatian": "hr",
    "hebrew": "he",
    "indonesian": "id",
    "malay": "ms",
    "urdu": "ur"
}

def ensure_folders():
    os.makedirs(INPUT_FOLDER, exist_ok=True)
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def read_links():
    links_path = os.path.join(INPUT_FOLDER, 'links.txt')
    if not os.path.exists(links_path):
        print(f"No links.txt found in {INPUT_FOLDER}!")
        return []
    
    links = []
    with open(links_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith('#'):
                continue

            if "|" in line:
                url_part, language_part = map(str.strip, line.split("|"))
                language_part = language_part.lower()
                iso_code = language_map.get(language_part)  # ✅ Map full name to ISO code
                links.append((url_part, iso_code))
            else:
                links.append((line, None))
    return links

def save_text_to_file(filename, text):
    output_path = os.path.join(OUTPUT_FOLDER, filename)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

def get_video_title(youtube_url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        title = info.get('title', None)
        return title

def clean_filename(name):
    """Remove or replace bad characters for safe filenames."""
    bad_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in bad_chars:
        name = name.replace(char, '_')
    return name

def main():
    ensure_folders()

    links = read_links()
    if not links:
        print("No links to process.")
        return

    for idx, (url, language_code) in enumerate(tqdm(links, desc="Processing Videos")):
        print(f"\nProcessing ({idx + 1}/{len(links)}): {url}")

        try:
            # Get video title
            title = get_video_title(url)
            if not title:
                title = f"video_{idx + 1}"
            clean_title = clean_filename(title)

            audio_filename = clean_title

            # Step 1: Download Audio
            audio_file_path = download_audio(url, output_path=audio_filename)

            # Step 2: Transcribe Audio
            if language_code:
                print(f"--> Forcing transcription language: {language_code}")
                transcription, detected_language = transcribe_audio(audio_file_path, language=language_code)
            else:
                print(f"--> Auto-detecting language")
                transcription, detected_language = transcribe_audio(audio_file_path)

            save_text_to_file(f'{clean_title}_transcript.txt', transcription)

            # Step 3: Translate Text
            if language_code and language_code.lower() in special_translation_languages:
                print(f"--> Special handling for {language_code}: pushing raw transcription directly to Google Translate.")
            else:
                print(f"--> Normal translation flow.")

            translation = translate_text(transcription)
            save_text_to_file(f'{clean_title}_translation.txt', translation)

            print(f"Finished processing '{clean_title}'. Files saved to 'output/' folder.")

            # Optional: Clean up downloaded audio
            if os.path.exists(audio_file_path):
                os.remove(audio_file_path)
                print(f"Deleted temporary file: {audio_file_path}")

        except Exception as e:
            print(f"Error processing {url}: {e}")

if __name__ == "__main__":
    main()

# audio_downloader.py

from yt_dlp import YoutubeDL
import os

def download_audio(youtube_url, output_path='audio'):
    filename_without_ext = os.path.splitext(output_path)[0]

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': filename_without_ext + '.%(ext)s',  # let yt-dlp handle extension
        'ffmpeg_location': r'C:\ffmpeg\bin\ffmpeg.exe',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',   # ONLY this is needed!
            'preferredquality': '192'
        }],
        'noplaylist': True,
        'quiet': False,
        'postprocessor_args': [
            '-ar', '16000'
        ],
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(youtube_url, download=True)

    final_audio_path = filename_without_ext + '.mp3'
    print(f"Audio downloaded and saved as: {final_audio_path}")
    return final_audio_path

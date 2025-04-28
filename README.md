# YouTube Translator 🎥🌍

This project automatically downloads YouTube videos, extracts audio, transcribes the speech into text, and translates it into English.

It uses cutting-edge models like **Faster-Whisper** for ultra-fast transcription and **Google Translate (Deep-Translator)** for multilingual translation.

---

## 🚀 Features

- **Download YouTube videos** and extract audio.
- **Transcribe audio** into text using `faster-whisper`.
- **Translate** the transcription into English automatically.
- **Auto-detect languages** if none specified.
- **Special handling for low-resource languages** (like Armenian, Amharic, Uzbek, etc.).
- **Batch process multiple YouTube links** with a simple `links.txt`.
- **Progress bar** visualization with `tqdm`.
- **Automatic folder creation** (`input/`, `output/`).

---

## 🛠 Installation

1. **Clone this repository:**

   ```bash
   git clone https://github.com/dhouse87/Youtube-Translator.git
   cd Youtube-Translator
   ```

2. **Install required libraries:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Make sure `ffmpeg` is installed and added to your PATH**  
   - [Download ffmpeg here](https://ffmpeg.org/download.html)
   - Confirm installation:

   ```bash
   ffmpeg -version
   ```

---

## 📂 Folder Structure

```plaintext
youtube_translator/
├── main.py
├── audio_transcriber.py
├── audio_downloader.py
├── translator.py
├── run_translator.bat
├── input/
│   └── links.txt         # Place your YouTube links here
├── output/
│   ├── [Video]_transcript.txt
│   └── [Video]_translation.txt
├── requirements.txt
└── README.md
```

---

## ✍️ Usage Instructions

1. **Prepare your `input/links.txt`**

   Add YouTube links you want to process, one per line:

   ```
   https://www.youtube.com/watch?v=xxxxxxx
   ```

   ✅ Optionally, **force a language** for more accurate transcription:

   ```
   https://www.youtube.com/watch?v=xxxxxxx | Armenian
   https://www.youtube.com/watch?v=yyyyyyy | Spanish
   ```

2. **Run the project:**

   You can use the batch file:

   ```bash
   run_translator.bat
   ```

   or manually:

   ```bash
   python main.py
   ```

3. **Check your outputs:**

   - Transcripts are saved in `/output`
   - English translations are saved in `/output`

---

## 🌍 Supported Languages

- Auto-detects 100+ languages.
- **Special bypass** for low-resource languages:
  - Armenian, Amharic, Georgian, Farsi, Dari, Uzbek, Kazakh, Somali, Tigrinya, etc.
- These low-resource languages are sent **directly to Google Translate** for best results.

---

## 🧠 How It Works (Internally)

1. **Downloads audio** using `yt-dlp`.
2. **Transcribes** audio using `faster-whisper` model (`small` version for faster speed).
3. **Handles special cases:**
   - If forced language (e.g., Armenian) → Transcribe using forced language
   - If auto-detected language is special → Special direct handling
4. **Translates text** into English using `deep-translator` (Google Translate backend).
5. **Saves transcript + translation** to output folder.

---

## 📝 Requirements

- Python 3.8+
- Libraries:
  - `yt-dlp`
  - `faster-whisper`
  - `deep-translator`
  - `ffmpeg-python`
  - `tqdm`

Install them using:

```bash
pip install -r requirements.txt
```

---

## ⚙️ Notes

- You must have `ffmpeg` installed and properly set in your system PATH.
- Whisper model used: `small` for speed (can upgrade to `medium` or `large` manually).
- Google Translate has soft limits (~4000 characters per API call).
- Faster-Whisper requires CPU (works faster with GPU if available).

---

## 📢 Future Improvements (Optional Ideas)

- Streamlit web app front-end.
- Subtitle (.srt) file generation.
- Upload translated transcripts directly to YouTube.
- Handle extremely large videos by auto-splitting audio.
- Docker container for easy deployment.

---

## 📸 Screenshots (Optional)

> (You can add screenshots later showing the app running, terminal output, or sample outputs!)

---

## 🙏 Credits

- [Faster-Whisper](https://github.com/guillaumekln/faster-whisper)
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [Deep-Translator](https://github.com/nidhaloff/deep-translator)
- [FFmpeg](https://ffmpeg.org/)

---

# 🎯 Built by David Hovsepian
**Making multilingual AI easier for everyone.** 🚀

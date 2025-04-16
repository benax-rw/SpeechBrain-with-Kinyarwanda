# 🧠 SpeechBrain-with-Kinyarwanda

A lightweight Kinyarwanda automatic speech recognition (ASR) project built with [SpeechBrain](https://speechbrain.readthedocs.io/).  
This repo contains code for converting audio, transcribing speech, and experimenting with pretrained models for Kinyarwanda.

---

## 📥 Clone the Project

```bash
git clone https://github.com/benax-rw/SpeechBrain-with-Kinyarwanda.git
cd SpeechBrain-with-Kinyarwanda
```

---

## 🧪 Set Up the Environment

You can (optionally) use a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

---

## 📦 Install Dependencies

```bash
pip install -r requirements.txt  # if available
```

Or manually:

```bash
pip install speechbrain torchaudio
```

---

## 🎤 Run a Transcription

The model will **automatically download on first run**.

```bash
python transcribe_kinyarwanda.py rw-103.wav
```

---

## 🛠 Tools Included

- `convert_m4a_to_mp3.py` – convert `.m4a` files to `.mp3`
- `convert_m4a_to_wav.py` – convert `.m4a` to `.wav` for ASR
- `transcribe_kinyarwanda.py` – runs inference using pretrained model
- Sample files: `rw-103.wav`, `rw-104.wav`, etc.

---

## 🙌 Acknowledgements

- Built with ❤️ using [SpeechBrain](https://github.com/speechbrain/speechbrain)
- Kinyarwanda models from [Hugging Face](https://huggingface.co/models?language=rw)

---

## 📚 License

MIT – free for educational use and research.

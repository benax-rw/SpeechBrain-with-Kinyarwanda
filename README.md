# SpeechBrain-with-Kinyarwanda
# Clone the project
git clone https://github.com/benax-rw/SpeechBrain-with-Kinyarwanda.git
cd SpeechBrain-with-Kinyarwanda

# Create virtual environment (optional but clean)
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt  # if you include this

# Run the script (model will auto-download)
python transcribe_kinyarwanda.py rw-103.wav

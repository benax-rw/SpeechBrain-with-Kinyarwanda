from speechbrain.inference.ASR import EncoderASR
import os


# === Step 1: Load the pre-trained model for Kinyarwanda ===
asr_model = EncoderASR.from_hparams(
    source="speechbrain/asr-wav2vec2-commonvoice-14-rw",
    savedir="pretrained_models/asr-wav2vec2-commonvoice-14-rw"
)

# === Step 2: Choose your audio file ===
audio_file = "rw-104.wav"

# === Step 3: Transcribe it ===
transcription = asr_model.transcribe_file(audio_file)
print("Transcription:", transcription)

# === Step 4: Save as <audio_filename>.txt ===
output_file = os.path.splitext(audio_file)[0] + ".txt"
with open(output_file, "w", encoding="utf-8") as f:
    f.write(transcription)

print(f"✅ Transcription saved to {output_file}")

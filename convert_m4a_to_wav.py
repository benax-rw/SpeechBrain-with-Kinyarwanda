from pydub import AudioSegment

# Load your M4A file
input_file = "rw-104.m4a"
output_file = "rw-104.wav"

# Convert to MP3
audio = AudioSegment.from_file(input_file, format="m4a")
audio.export(output_file, format="wav")

print("✅ Converted successfully:", output_file)

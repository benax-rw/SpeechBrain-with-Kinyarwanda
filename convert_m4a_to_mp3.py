from pydub import AudioSegment

# Load your M4A file
input_file = "rw-103.m4a"
output_file = "rw-103.mp3"

# Convert to MP3
audio = AudioSegment.from_file(input_file, format="m4a")
audio.export(output_file, format="mp3")

print("✅ Converted successfully:", output_file)

import whisper
import time
from jiwer import wer

# Load Whisper model
model = whisper.load_model("base")

# Ground truth text
ground_truth = "hello my name is aanchal, how are you?"

# Start timer
start = time.time()

# Transcribe audio
result = model.transcribe("audio/sample1.wav")

# End timer
end = time.time()

# Calculate latency
latency = (end - start) * 1000

# Predicted text
prediction = result["text"]

# Calculate WER
error = wer(ground_truth, prediction)

# Final output
output = {
    "model": "whisper",
    "transcript": prediction,
    "wer": round(error, 3),
    "latency_ms": round(latency, 2)
}

print(output)
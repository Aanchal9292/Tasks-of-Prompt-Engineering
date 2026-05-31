import whisper
import time
import json
import wave
from jiwer import wer
from vosk import Model, KaldiRecognizer

# ==========================
# CONFIG
# ==========================

AUDIO_FILE = "audio/sample1.wav"
GROUND_TRUTH = "hello my name is aanchal, how are you?"

# ==========================
# WHISPER
# ==========================

print("Loading Whisper...")
whisper_model = whisper.load_model("base")

start = time.time()
whisper_result = whisper_model.transcribe(AUDIO_FILE)
whisper_latency = (time.time() - start) * 1000

whisper_text = whisper_result["text"]
whisper_wer = wer(GROUND_TRUTH, whisper_text)

# ==========================
# VOSK
# ==========================

print("Loading Vosk...")
vosk_model = Model("vosk-model-small-en-us-0.15")

wf = wave.open(AUDIO_FILE, "rb")
recognizer = KaldiRecognizer(vosk_model, wf.getframerate())

start = time.time()

while True:
    data = wf.readframes(4000)

    if len(data) == 0:
        break

    recognizer.AcceptWaveform(data)

vosk_result = json.loads(recognizer.FinalResult())

vosk_latency = (time.time() - start) * 1000

vosk_text = vosk_result.get("text", "")
vosk_wer = wer(GROUND_TRUTH, vosk_text)

# ==========================
# RESULTS
# ==========================

print("\n===== BENCHMARK RESULTS =====\n")

print({
    "model": "whisper",
    "transcript": whisper_text,
    "wer": round(whisper_wer, 3),
    "latency_ms": round(whisper_latency, 2)
})

print()

print({
    "model": "vosk",
    "transcript": vosk_text,
    "wer": round(vosk_wer, 3),
    "latency_ms": round(vosk_latency, 2)
})
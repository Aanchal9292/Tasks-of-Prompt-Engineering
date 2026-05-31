# Speech-to-Text Benchmarking Report

## Objective

Benchmark multiple Speech-to-Text engines based on:

* Accuracy
* Word Error Rate (WER)
* Latency

## Models Tested

1. Whisper Base
2. Vosk Small EN-US

## Results

| Model   | Transcript                              | WER  | Latency (ms) |
| Whisper | Hello, my name is Anshun, how are you?  | 0.25 | 6056.71      |
| Vosk    | one more snow than whole old            | 1.00 | 2716.16      |


## Analysis

Whisper produced a highly accurate transcript with only one incorrect word ("Aanchal" recognized as "Anshun").

Vosk failed to correctly recognize the spoken sentence and generated an unrelated transcription.

Although Vosk had lower latency, its transcription quality was significantly worse.

## Recommendation

Based on the benchmarking results, Whisper is the recommended Speech-to-Text model.

Reasons:
- Lower Word Error Rate (0.25)
- Better transcription quality
- More robust to pronunciation variations

Although Vosk achieved lower latency, its transcription accuracy was significantly lower (WER = 1.00).

Therefore, Whisper is the preferred choice when transcription accuracy is the primary requirement.
Vosk may be considered for lightweight or real-time applications where speed is more important than accuracy.
from faster_whisper import WhisperModel

segments, info = WhisperModel("medium", device="cpu").transcribe(input("arrastre aqui su mp3").strip('"'), language="es")
open("res.txt", "w", encoding="utf-8").write(" ".join(seg.text for seg in segments))
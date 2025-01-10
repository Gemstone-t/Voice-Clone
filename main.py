from TTS.api import TTS

def main():
    audio_path = "reference.wav"
    model_name = "tts_models/en/ljspeech/tacotron2-DDC"
    tts = TTS(model_name)
    script = "This is test voice cloning"
    tts.tts_with_vc_to_file(text=script, speaker_wav=audio_path, file_path="output.wav")

if __name__ == "__main__":
    main()
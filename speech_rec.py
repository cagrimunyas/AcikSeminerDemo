import azure.cognitiveservices.speech as speechsdk


speech_key, service_region = "",""
speech_config = speechsdk.SpeechConfig(subscription=speech_key,region=service_region,speech_recognition_language="tr-TR")

audio_filename="test1.wav"
audio_input = speechsdk.audio.AudioConfig(filename=audio_filename)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,audio_config=audio_input)


print("\n\nSes tanimlaniyor...")
result = speech_recognizer.recognize_once()

# STT Sonuc
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Ses tanimlandi: {}".format(result.text))
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("Ses tanimlanamadi: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Ses tanima iptal edildi: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Hata detaylari: {}".format(cancellation_details.error_details))
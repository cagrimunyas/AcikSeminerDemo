import azure.cognitiveservices.speech as speechsdk
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials

speech_key, service_region = "",""
speech_config = speechsdk.SpeechConfig(subscription=speech_key,region=service_region,speech_recognition_language="tr-TR")

audio_filename="test2.wav"
audio_input = speechsdk.audio.AudioConfig(filename=audio_filename)

speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config,audio_config=audio_input)

#LUIS konfigurasyon
LUIS_RUNTIME_KEY=""
LUIS_RUNTIME_ENDPOINT=""
LUIS_APP_ID=""
LUIS_APP_SLOT_NAME=""
clientRuntime = LUISRuntimeClient(LUIS_RUNTIME_ENDPOINT,CognitiveServicesCredentials(LUIS_RUNTIME_KEY))
def predict(query_text):
    request = {"query":query_text}
    response = clientRuntime.prediction.get_slot_prediction(app_id=LUIS_APP_ID,slot_name=LUIS_APP_SLOT_NAME,prediction_request=request)

    print("Amac: {}".format(response.prediction.top_intent))
    print("Ozellikler: {}".format(response.prediction.entities))

print("\n\nSes tanimlaniyor...")
result = speech_recognizer.recognize_once()

# STT Sonuc
if result.reason == speechsdk.ResultReason.RecognizedSpeech:
    print("Ses tanimlandi: {}\n".format(result.text))
    print("Luis'e gonderiliyor..\n")
    predict(result.text)
elif result.reason == speechsdk.ResultReason.NoMatch:
    print("Ses tanimlanamadi: {}".format(result.no_match_details))
elif result.reason == speechsdk.ResultReason.Canceled:
    cancellation_details = result.cancellation_details
    print("Ses tanima iptal edildi: {}".format(cancellation_details.reason))
    if cancellation_details.reason == speechsdk.CancellationReason.Error:
        print("Hata detaylari: {}".format(cancellation_details.error_details))
from azure.cognitiveservices.language.luis.runtime import LUISRuntimeClient
from msrest.authentication import CognitiveServicesCredentials


#LUIS konfigurasyon
LUIS_RUNTIME_KEY=""
LUIS_RUNTIME_ENDPOINT=""
LUIS_APP_ID=""
LUIS_APP_SLOT_NAME=""
clientRuntime = LUISRuntimeClient(LUIS_RUNTIME_ENDPOINT,CognitiveServicesCredentials(LUIS_RUNTIME_KEY))


def predict(query_text):
    print("\nLuis'e gonderiliyor..\n")
    request = {"query":query_text}
    response = clientRuntime.prediction.get_slot_prediction(app_id=LUIS_APP_ID,slot_name=LUIS_APP_SLOT_NAME,prediction_request=request)

    print("Amac: {}".format(response.prediction.top_intent))
    print("Ozellikler: {}".format(response.prediction.entities))


phrase="Elimizde hiç siyah tshirt var mı?"
predict(phrase)




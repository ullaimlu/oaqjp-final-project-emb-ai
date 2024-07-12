import requests
import json
def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
        
    if response.status_code == 400 or response.status_code == 500:
        return None

    emotions={
        "anger" : formatted_response['emotionPredictions'][0]['emotion']['anger'],
        "disgust" : formatted_response['emotionPredictions'][0]['emotion']['disgust'],
        "fear" : formatted_response['emotionPredictions'][0]['emotion']['fear'],
        "joy" : formatted_response['emotionPredictions'][0]['emotion']['joy'],
        "sadness" : formatted_response['emotionPredictions'][0]['emotion']['sadness']     
    }

    def get_key(val):
        for key, value in emotions.items():
            if val == value:
                return key


    final_response = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": get_key(max(emotions.values()))
    }


    return final_response



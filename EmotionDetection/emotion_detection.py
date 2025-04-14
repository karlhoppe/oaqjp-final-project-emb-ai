import requests
import json

def emotion_detector(text_to_analyze):
    url= 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers= {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj ={ "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json= myobj, headers=headers)
    mydict=json.loads(response.text)

    if response.status_code == 200:

        emotion_values = []
        for prediction in mydict['emotionPredictions']:
            emotion_values.append(prediction['emotion'])
            for mention in prediction.get('emotionMentions', []):  # Handle cases where 'emotionMentions' might be missing
                emotion_values.append(mention['emotion'])

        theemotions = (emotion_values[0])
        dominant_emotion= "None"
        max_score = .0001
        highest_score_label = max(theemotions, key=theemotions.get)

        theemotions['dominant_emotion'] = highest_score_label
        formated_response=theemotions

    elif response.status_code==400:
        baddict={'anger': 'none', 'disgust': 'none', 'fear': 'none', 'joy': 'none', 'sadness': 'none', 'dominant_emotion': 'none'}
        formated_response=baddict
        
    return formated_response
    
    
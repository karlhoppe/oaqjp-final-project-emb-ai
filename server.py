"""Module: Emotion Detection
Author: Karl Hoppe
Date: April 13, 2025
Version: 1.0
"""


from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app=Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_analyzer():
    """a function to analyze emotion
    arg is a phrase
    """
    text_to_analyze = request.args.get('textToAnalyze')

    response=emotion_detector(text_to_analyze)

    dominant_emotion=response['dominant_emotion']
    anger=response['anger']
    disgust=response['disgust']
    fear=response['fear']
    joy=response['joy']
    sadness=response['sadness']

    if dominant_emotion == 'none':
        myresponse= "Invalid text!  Please try again!"
    else:
        myresponse1=f"For the given statement, the system response is 'anger': {anger}, "
        myresponse2=f"'disgust': {disgust},'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
        myresponse3=f"The dominant emotion is {dominant_emotion}."
        myresponse = myresponse1+myresponse2+myresponse3

    return myresponse

@app.route("/")
def render_index_page():
    """a function to show index page
    I like this here
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

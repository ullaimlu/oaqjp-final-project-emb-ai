from flask import Flask, render_template, request
from emotiondetection.emotion_detection import emotion_detector

app= Flask("emotionDetector")

@app.route("/emotionDetector")
def emotion_detect():
    text_to_analyze= request.args.get('textToAnalyze')
    response= emotion_detector(text_to_analyze)
    anger= response["anger"]
    disgust= response["disgust"]
    fear= response["fear"]
    joy= response["joy"]
    disgust= response["sadness"]
    dominant_emotion= response["dominant_emotion"]

    return f"For the given statement, the system response is: \n ANGER : {anger}  \n DISGUST : {disgust} \n FEAR : {fear} \n JOY : {joy} \n SADNESS : {sadness}. The DOMINANT EMOTION is {dominant_emotion}"
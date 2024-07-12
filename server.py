''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from emotiondetection.emotion_detection import emotion_detector

app= Flask("emotionDetector")

@app.route("/emotionDetector")
def emotion_detect():
    '''
    Retrieves emotions score and dominant emotion of a text
    '''
    text_to_analyze= request.args.get('textToAnalyze')
    response= emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"

    anger= response["anger"]
    disgust= response["disgust"]
    fear= response["fear"]
    joy= response["joy"]
    sadness= response["sadness"]
    dominant_emotion= response["dominant_emotion"]

    return f"For the given statement, the system response is: <br><br> ANGER : {anger}  <br> DISGUST : {disgust} <br> FEAR : {fear} <br> JOY : {joy} <br> SADNESS : {sadness}.<br> The DOMINANT EMOTION is {dominant_emotion}"

@app.route("/")
def render_index_page():
    '''
    Render page
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port= 5000)

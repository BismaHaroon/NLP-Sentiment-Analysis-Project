"""Flask App for deploying sentiment analysis model """
from flask import Flask, request, jsonify, render_template
import joblib

app = Flask(__name__)

model = joblib.load('models/best_sentiment_analysis_model.pkl')
vectorizer = joblib.load('models/best_tfidf_vectorizer.pkl')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict_sentiment():
    data = request.get_json()
    review_text = data['review']
    text_vector = vectorizer.transform([review_text])

    sentiment = model.predict(text_vector)[0]
    sentiment_mapping = {1: 'Positive', 0: 'Neutral', -1: 'Negative'}
    sentiment_label = sentiment_mapping[sentiment]

    return jsonify({'sentiment': sentiment_label})

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
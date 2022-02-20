#!/usr/bin/env python
# coding: utf-8
from flask import Flask, request, jsonify
import nltk
nltk.download('vader_lexicon')

app = Flask(__name__)

def topic_model(text):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    from nltk import tokenize
    from rake_nltk import Rake
    
    lines_list = tokenize.sent_tokenize(text)
    scores_list = []
    positive_sentences = ""
    negative_sentences = ""
    
    for sentence in lines_list:
        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(sentence)
        scores_list.append(ss['compound'])
        if ss['compound'] > 0:
            positive_sentences += sentence
        else:
            negative_sentences += sentence
    
    overall_score = sum(scores_list) / len(scores_list)
    
    rake_nltk_pos = Rake()
    rake_nltk_pos.extract_keywords_from_text(positive_sentences)
    keyword_pos = rake_nltk_pos.get_ranked_phrases()
    
    rake_nltk_neg = Rake()
    rake_nltk_neg.extract_keywords_from_text(negative_sentences)
    keyword_neg = rake_nltk_neg.get_ranked_phrases()
    
    return (overall_score, keyword_pos, keyword_neg)

# Create a route for sentiment analysis, which accepts text as a POST parameter
@app.route('/sentiment', methods=['POST'])
def sentiment():
    text = request.json['text']
    overall_score, keyword_pos, keyword_neg = topic_model(text)
    return jsonify({'overall_score': overall_score, 'keyword_pos': keyword_pos, 'keyword_neg': keyword_neg})
    
# topics = topic_model("today was good so far. I've had a good night sleep and am ready to learn new material. Unfortuantelly I wetted my bed last night so my roommate doesn't want to talk to me anymore :(")

@app.after_request
def after_request(response):
    # enable CORS
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    return response

# start the flask app
if __name__ == '__main__':
    app.run(debug=True)

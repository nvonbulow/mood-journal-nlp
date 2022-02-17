#!/usr/bin/env python
# coding: utf-8

# In[12]:


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
    
    rake_nltk_pos = Rake()
    rake_nltk_neg.exact_keywords_from_text(negative_sentences)
    keyword_neg = rake_nltk_neg.get_ranked_phrases()
    
    return (overall_score, keyword_pos, keyword_neg)
    


# In[13]:


topic_model("today was good so far. I've had a good night sleep and am ready to learn new material. Unfortuantelly I wetted my bed last night so my roommate doesn't want to talk to me anymore :(")


# In[ ]:





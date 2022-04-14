import numpy as np
import nltk
import string
import random
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
#nltk.download('punkt')
#nltk.download('wordnet')

GREET_INPUTS = ("hello", "hi")
GREET_RESPONSE = ("hello", "hi")

f = open('/home/jerinpaul/Documents/ME/Sem 2/ML/chatbot.txt', 'r', errors = 'ignore')
raw_doc = f.read()
raw_doc = raw_doc.lower()
sent_tokens = nltk.sent_tokenize(raw_doc)
word_tokens = nltk.word_tokenize(raw_doc)

lemmer = nltk.stem.WordNetLemmatizer()

def LemTokens(tokens):
    result = []
    for token in tokens:
        result.append(lemmer.lemmatize(token))
    return result

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

def greet(sentence):
    for word in sentence:
        if word.lower() in GREET_INPUTS:
            return random.choice(GREET_RESPONSE)

def response(user_response):
    bot_response = ""
    TfidVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words = 'english')
    tfidf = TfidVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    index = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if req_tfidf == 0:
        bot_response += "I am sorry! I don't understand you!"
        return bot_response
    else:
        bot_response += sent_tokens[index]
        return bot_response

def start():
    global word_tokens
    global sent_tokens
    flag = True
    print("Hello, this is your assistant!")
    while flag:
        user_response = input()
        user_response = user_response.lower()
        if user_response == "quit":
            flag = False
        else:
            sent_tokens.append(user_response)
            word_tokens += nltk.word_tokenize(user_response)
            final_words = list(set(word_tokens))
            print("BOT: ", end = "")
            print(response(user_response))
            sent_tokens.remove(user_response)
    print("Quiting!")

start()

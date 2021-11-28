###### Import ######
import numpy as np
import pandas as pd
import nltk
import re
from bs4 import BeautifulSoup
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pickle
from joblib import load
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

###### Fonctions ######
# Fonction qui pré_traite le texte de la même façon que pour les données servant à l'entrainement
def preprocessing_text (text):
  # Suppression des lignes de code
  text = re.sub('<code>?(.*?)</code>', " ", text, flags=re.DOTALL)

  # Transformation du texte format html avec BeautifulSoup
  text = BeautifulSoup(text, features="lxml").get_text()

  # Transformation des données en minuscules
  text = text.lower()

  # Transformation des abréviations
  text = re.sub(r"what's", "what is ", text)
  text = re.sub(r"\'s", " ", text)
  text = re.sub(r"\'ve", " have ", text)
  text = re.sub(r"can't", "can not ", text)
  text = re.sub(r"n't", " not ", text)
  text = re.sub(r"i'm", "i am ", text)
  text = re.sub(r"\'re", " are ", text)
  text = re.sub(r"\'d", " would ", text)
  text = re.sub(r"\'ll", " will ", text)
  text = re.sub(r"\'scuse", " excuse ", text)
  text = re.sub(r"\'\n", " ", text)
  text = re.sub(r"\'\xa0", " ", text)
  text = re.sub('\s+', ' ', text)
  text = text.strip(' ')

  # Utilisation des expressions regulières pour enlever les chaines de caractères contenant des chiffres ou de la ponctuation
  text = re.sub(r"[^a-zA-Z\-\#\+\-\.]", " ", text)

  # Suppression des espaces dubliqués
  text = " ".join(text.split())
  
  # Tokenization
  text = nltk.word_tokenize(text)

  # lemmatisation
  wnl = WordNetLemmatizer()
  text = [wnl.lemmatize(word) for word in text]

  # Elimination des stop words et de la ponctuation restante
  stops = set(stopwords.words("english"))
  stops.add('-')
  stops.add('.')
  text = [w for w in text if not w in stops]

  # Format final des données
  text = ''.join(str(text).split(','))
  text = text.replace("'","")
  text = text[1:-1]
  text = [text]

  return text


###### Import models ######
# Import tfidfvectorizer model
tfidf_model = load('tfidfvectorizer_body.pkl')

# Import machine learning model
ml_model = load('svc_tfi.pkl')

###### Tags List ######
word_list = load('word_list.txt')
word_list = word_list[1:-1].replace("'", '')
word_list = word_list.replace(" ", '')
y_list = []
for word in word_list.split(','):
  y_list.append(word)

###### Inference ######
def predict_tags(question):
    # Preprocessing text 
    text_preprocessed = preprocessing_text(question)
    text_tfi = tfidf_model.transform(text_preprocessed)

    # Text inference 
    pred_result = ml_model.predict(text_tfi)
    pred_result = pred_result.toarray()
    tags = []
    for i in range(len(pred_result)):
        for j in range(len(pred_result[i])):
            if pred_result[i][j] == 1:
                tags.append(y_list[j])
    return tags

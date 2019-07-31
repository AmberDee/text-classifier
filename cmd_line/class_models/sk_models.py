from sklearn.externals import joblib
from .predictors import clean_text, tokenizer_spacy

def transform_text(text):
    text =  [' '.join(tokenizer_spacy(clean_text(text)))]
    vectorizer = joblib.load(open(r'class_models/vectorizer.sav', 'rb'))
    return vectorizer.transform(text)

def classify(model, text):
    return model.predict(transform_text(text))[0]

def logistic_classify(text):
    return classify(joblib.load(open(r'class_models/logistic_classifier_model.sav', 'rb')), text)

def xgboost_classify(text):
    return classify(joblib.load(open(r'class_models/xgboost_classifier_model.pk', 'rb')), text)
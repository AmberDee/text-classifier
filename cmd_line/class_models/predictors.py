import spacy
from spacy.lang.en import English
import re
from sklearn.base import TransformerMixin
import sklearn
import string
from spacy.lang.en.stop_words import STOP_WORDS

nlp = English()
spacy_stopwords = STOP_WORDS
punct = string.punctuation

#not_letter = re.compile('([^a-zA-Z]| )')
numbers = re.compile(r'(\d|\.)+')
percentamt = re.compile(r'(\d|\.)+%')
dates = re.compile(r'([1-2](0|9)[0-9][0-9]-[0-1][0-9]-[0-3][0-9]|[0-1][0-9]-[0-3][0-9]-[1-2](0|9)[0-9][0-9]|(Ja|Fe|Ma|Ap|Ju|Au|Se|Oc|No|De)\w+ (\d+), \d\d\d\d|[0-1][0-9]\/[0-3][0-9]\/([1-2](0|9)[0-9][0-9]|[0-9][0-9]))')
dollars = re.compile(r'(\$\d+)')

# Basic function to clean the text
def clean_text(text):
    # Removing spaces and converting text into lowercase
    try:
        text = unidecode.unidecode(text)
    except:
        pass    
    return numbers.sub('numberamt', percentamt.sub('percentamt', dollars.sub('dollaramt', dates.sub('dateamt', text).replace(',', '').replace('-', '')))).strip().lower()

def tokenizer_spacy(headline):
        #filtered_tokenized.append(df_union.at[i, 'headline'])
        #filtered_tokenized.append(row)

    # Creating our token object, which is used to create documents with linguistic annotations.
    mytokens = nlp(str(headline))
    
    #lemmatization improved model
    
    mytokens = [ [word.lemma_.lower().strip(), word.pos_, word.dep_, word.ent_type_] if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]

    #mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in mytokens ]
    
    # Removing stop wordsspacy_stopwords
    return [ str(word).lower().strip() for word in mytokens if str(word).lower().strip() not in spacy_stopwords and str(word).lower().strip() not in punct ]

    # return preprocessed list of tokens

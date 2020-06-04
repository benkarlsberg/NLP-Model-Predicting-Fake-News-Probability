import re
import string
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet, stopwords
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

sw = stopwords.words('english') # english stopwords list
pt = string.punctuation # punct list

def stopwords_list():
    sw = set(stopwords.words('english'))
    new_stopwords = []
    for word in sw:
        new_stopwords.append(preprocessor(word))
        # remove specified words
    remove_list = ['reuters']
    return new_stopwords + remove_list

def preprocessor(doc):
    # lower case
    doc = doc.lower()
    # html tags
    doc = re.sub('<.*?>', '', doc)
    # punctuations
    doc = re.sub('[~*.^!?\'_,&#;)(]*', '', doc)
    # numbers
    doc = re.sub(r'\w*\d\w*', '', doc).strip()
    # lemmatize
    wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}
    pos_tagged_text = pos_tag(doc.split())
    lemmatizer = WordNetLemmatizer()
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])
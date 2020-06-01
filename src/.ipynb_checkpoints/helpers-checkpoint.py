import re
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet, stopwords

def stopwords_list():
    sw = set(stopwords.words('english'))
    new_stopwords = []
    for word in sw:
        new_stopwords.append(preprocessor(word))
    return new_stopwords

def preprocessor(doc):
    # lower case
    doc = doc.lower()
    # html tags
    doc = re.sub('<.*?>', '', doc)
    # punctuations
    doc = re.sub('[~*.^!?\'_]*', '', doc)
    # numbers
    doc = re.sub(r'\w*\d\w*', '', doc).strip()
    # lemmatize
    wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}
    pos_tagged_text = pos_tag(doc.split())
    lemmatizer = WordNetLemmatizer()
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])


def lemmatize_words(text):
    wordnet_map = {"N": wordnet.NOUN, "V": wordnet.VERB, "J": wordnet.ADJ, "R": wordnet.ADV}
    pos_tagged_text = pos_tag(text.split())
    lemmatizer = WordNetLemmatizer()
    return " ".join([lemmatizer.lemmatize(word, wordnet_map.get(pos[0], wordnet.NOUN)) for word, pos in pos_tagged_text])

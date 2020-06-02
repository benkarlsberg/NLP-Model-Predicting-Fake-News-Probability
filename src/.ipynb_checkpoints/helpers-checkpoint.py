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

# Tokenizer with bigrams and trigrams
def doc_to_tokens(doc):
    doc = doc.lower() #lowercase
    doc = unicodedata.normalize('NFKD', doc).encode('ASCII', 'ignore').decode('utf8') # remove icons or non-ascii text
    doc = re.sub(r'[~*.^]*', '', doc) # remove odd puncts
    doc = word_tokenize(doc) # tokenize word
    doc = [token for token in doc if token not in sw and token not in pt] #removes stop words and puncts
    doc = [stemmer.stem(token) for token in doc] # stem word (chop end)
    bg = list(map(lambda tup: '-'.join(tup), ngrams(doc, 2))) # adds bigrams of word
    tg = list(map(lambda tup: '-'.join(tup), ngrams(doc, 3))) # adds trigrams of word
    return doc + bg + tg

def bag_of_words(docs):
    vocabulary = set()
    for doc in docs:
        for token in doc_to_tokens(doc):
            vocabulary.add(token)
    vocabulary_lookup = {word: i for i, word in enumerate(vocabulary)}
    matrix = np.zeros((len(docs), len(vocabulary)))
    for doc_id, doc in enumerate(docs):
        for token in doc_to_tokens(doc):
            word_id = vocabulary_lookup[token]
            matrix[doc_id][word_id] += 1
    columns = sorted(vocabulary_lookup, key=lambda key: vocabulary_lookup[key])
    df = pd.DataFrame(matrix.astype('int'), columns=columns)
    return df
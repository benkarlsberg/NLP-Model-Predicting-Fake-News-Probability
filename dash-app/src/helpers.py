import re
import string
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet, stopwords
from nltk.util import ngrams
from nltk.tokenize import word_tokenize
import pandas as pd
import matplotlib.pyplot as plt

sw = stopwords.words('english') # english stopwords list
pt = string.punctuation # punct list

def stopwords_list():
    sw = set(stopwords.words('english'))
    new_stopwords = []
    for word in sw:
        new_stopwords.append(preprocessor(word))
        # remove specified words
    remove_list = ['reuters']
    return new_stopwords

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

def calculate_threshold_values(prob, y):
    '''
    Build dataframe of the various confusion-matrix ratios by threshold
    from a list of predicted probabilities and actual y values
    '''
    df = pd.DataFrame({'prob': prob, 'y': y})
    df.sort_values('prob', inplace=True) # kind of the biggest deal here in terms of making this ROC curve possible
    
    actual_p = df.y.sum()
    actual_n = df.shape[0] - df.y.sum()

    df['tn'] = (df.y == 0).cumsum()
    df['fn'] = df.y.cumsum()
    df['fp'] = actual_n - df.tn
    df['tp'] = actual_p - df.fn

    df['fpr'] = df.fp/(df.fp + df.tn)
    df['tpr'] = df.tp/(df.tp + df.fn)
    df['precision'] = df.tp/(df.tp + df.fp)
    df = df.reset_index(drop=True)
    return df

def plot_roc(ax, df, model_name):
    ax.plot([1]+list(df.fpr), [1]+list(df.tpr), label=model_name)
    ax.set_xlabel('False Positive Rate', fontsize = 15)
    ax.set_ylabel('True Positive Rate', fontsize = 15)
    ax.set_title('Model Comparison ROC Curve', fontsize = 20)
#     ax.legend()
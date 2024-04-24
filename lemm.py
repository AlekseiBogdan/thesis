import pandas as pd
from tqdm import tqdm
from pymystem3.mystem import Mystem

tqdm.pandas()

df = pd.read_csv('messages.csv')
df.dropna(axis=0, inplace=True)

stemmer = Mystem()

def preprocess(text):
    text = text.replace('\n', '')
    return text

def lemmatize(text):
    analyzed = stemmer.analyze(text)
    return analyzed

df['Messages'] = df['Messages'].progress_apply(preprocess)
df['lemmas'] = df['Messages'].progress_apply(lemmatize)
df.to_csv('lemmatized_messages.csv', index=False, encoding='utf-8-sig')
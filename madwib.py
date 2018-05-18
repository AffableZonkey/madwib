#!/usr/env/python3

import nltk
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')
import os
import random

textbody = []
paragraph = []

adjdict = {'JJ': 'adjective', 'JJR': 'comparison', 'JJS': 'superlative' }
verbdict ={'VB': 'verb - present tense', 'VBD': 'verb - past tense', 'VBG': 'verb - present particple "ing"'}
noundict = {'NN': 'common noun', 'NNP': 'Proper Noun - Singular', 'NNPS': 'Plural Proper Noun', 'NNS': 'plural common noun'}


with open('/home/jebel/Documents/mlbor.txt', 'r') as mdwib:
    for line in mdwib:
        if len(line) != 0:
            linetext = nltk.word_tokenize(line)
            tagd_linetxt = nltk.pos_tag(linetext)
            paragraph.append(tagd_linetxt)
            print(paragraph[-1])
        else:
            textbody.append(paragraph)
            paragraph = []
            print(len(textbody))
    mdwib.close()

'''for pchunk in textbody:
    for sentlist in pchunk:
        for item in sentlist.items():
            print(item)
'''

def random_word_tuple(tagged_sentence):
    sentence_length = len(tagged_sentence)
    tagged_word = (tagged_sentence[random.randint(0,sentence_length)])
    return tagged_word



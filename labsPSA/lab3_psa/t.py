import json
import nltk
import regex as re
from textblob import TextBlob
from nltk.tag import pos_tag

tweets = []


def read_file():
    with open('./tweets.json', 'r', encoding='utf-8') as file:
        json_list = json.loads(file.read())
        for tweet in json_list:
            tweets.append(tweet)


def words():
    words = {}
    for tweet in tweets:
        text_words: list = nltk.word_tokenize(tweet['text'])
        for word in text_words:
            if word in words:
                words[word] += 1
            elif word not in words and word.isalpha():
                words[word] = 1
    return words


def nouns():
    nouns = {}
    for tweet in tweets:
        text_nouns = TextBlob(tweet['text'])
        for noun in text_nouns.noun_phrases:
            re.sub('[^A-Za-z0-9]+', '', noun)
            if noun in nouns:
                nouns[noun] += 1
            else:
                nouns[noun] = 1
    return nouns


def proper_nouns():
    proper_nouns = {}
    for tweet in tweets:
        tagged_sent = pos_tag(tweet['text'].split())
        proper_nouns_text = [word for word, pos in tagged_sent if pos == 'NNP']
        for noun in proper_nouns_text:
            if noun in proper_nouns:
                proper_nouns[noun] += 1
            else:
                proper_nouns[noun] = 1
    return proper_nouns


read_file()
words = words()
print('words: ')
sort_dictionary = dict(sorted(words.items(), key=lambda item: item[1], reverse=True))
first10pairs = {k: sort_dictionary[k] for k in list(sort_dictionary)[:10]}
for key in first10pairs:
    print(key, ' ', first10pairs[key])
print('nouns: ')
nouns = nouns()
sorted_nouns = dict(sorted(nouns.items(), key=lambda item: item[1], reverse=True))
first10pairs = {k: sorted_nouns[k] for k in list(sorted_nouns)[:10]}
for key in first10pairs:
    print(key, ' ', first10pairs[key])
print('proper nouns: ')
proper_nouns = proper_nouns()
sorted_proper = dict(sorted(proper_nouns.items(), key=lambda item: item[1], reverse=True))
first10pairs = {k: sorted_proper[k] for k in list(sorted_proper)[:10]}
for key in first10pairs:
    print(key, ' ', first10pairs[key])

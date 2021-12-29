import json
import nltk
import regex as re
from textblob import TextBlob
from nltk.tag import pos_tag

Tweets = {
    'id',
    'text',
    'created_at',
    'likes',
    'retweets',
    'rating'
}

tweets: Tweets = []


def get_data():
    with open('./tweets.json', 'r', encoding='utf-8') as file:
        json_list = json.loads(file.read())
        for tweet in json_list:
            tweet['rating'] = 0
            tweets.append(tweet)


def removekey(d, key):
    r = dict(d)
    del r[key]
    return r


def get_words() -> dict:
    result: dict = {}
    for tweet in tweets:
        words: list = nltk.word_tokenize(tweet['text'])
        for word in words:
            if word.lower() in result:
                result[word.lower()]['count'] += 1
                result[word.lower()]['retweets'] += tweet['retweets']
                result[word.lower()]['likes'] += tweet['likes']
            else:
                result[word.lower()] = {
                    'count': 1,
                    'retweets': tweet['retweets'],
                    'likes': tweet['likes']
                }

    for key in result:
        if not key.isalpha():
            result = removekey(result, key)
    return result


def get_nouns() -> dict:
    result: dict = {}
    for tweet in tweets:
        nouns = TextBlob(tweet['text'])
        for noun in nouns.noun_phrases:
            re.sub('[^A-Za-z0-9]+', '', noun)
            if noun in result:
                result[noun] += 1
            else:
                result[noun] = 1

    return result


def get_proper() -> dict:
    result: dict = {}
    for tweet in tweets:
        tagged_sent = pos_tag(tweet['text'].split())
        proper_nouns = [word for word, pos in tagged_sent if pos == 'NNP']
        for noun in proper_nouns:
            if noun in result:
                result[noun] += 1
            else:
                result[noun] = 1

    return result


def popularity() -> None:
    data = get_words()
    for word in data:
        data[word]['rating'] = data[word]['count'] * (1.4 + data[word]['retweets']) * (1.2 + data[word]['likes'])
    sorted_data = dict(sorted(data.items(), key=lambda x: x[1]['rating'], reverse=True))
    first2pairs = {k: sorted_data[k] for k in list(sorted_data)[:10]}
    for key in first2pairs:
        print(key, ' ', first2pairs[key])


def suggestion() -> None:
    words = get_words()
    sort_dictionary = dict(sorted(words.items(), key=lambda item: item[1]['count'], reverse=True))

    string: str = input()

    print(f'suggestions for {string}: ')
    count: int = 0
    for key in sort_dictionary:
        if count == 3:
            break
        if string in key:
            print(key, '(', sort_dictionary[key]['count'], ')')
            count += 1


def suggestion_occurences() -> None:
    string: str = input()
    result: dict = {}
    for tweet in tweets:
        words: list = nltk.word_tokenize(tweet['text'])
        if string in words:
            idx: int = 1 + words.index(string)
            if idx < len(words) and words[idx] in result:
                result[words[idx]]['count'] += 1
            else:
                result[words[idx]] = {
                    'count': 1,
                }
    sort_dictionary = dict(sorted(result.items(), key=lambda item: item[1]['count'], reverse=True))
    first3pairs = {k: sort_dictionary[k] for k in list(sort_dictionary)[:3]}
    print(f'suggestions for {string}')
    for key in first3pairs:
        print(key, '(', first3pairs[key]['count'], ')')


if __name__ == "__main__":
    get_data()
    words = get_words()
    # sort_dictionary = dict(sorted(words.items(), key=lambda item: item[1]['count'], reverse=True))
    # first2pairs = {k: sort_dictionary[k] for k in list(sort_dictionary)[:10]}
    # for key in first2pairs:
    #     print(key, ' ', first2pairs[key])
    # nouns = get_nouns()
    # sorted_nouns = dict(sorted(nouns.items(), key=lambda item: item[1], reverse=True))
    # first2pairs = {k: sorted_nouns[k] for k in list(sorted_nouns)[:10]}
    # for key in first2pairs:
    #     print(key, ' ', first2pairs[key])
    # proper_nouns = get_proper()
    # sorted_proper = dict(sorted(proper_nouns.items(), key=lambda item: item[1], reverse=True))
    # first2pairs = {k: sorted_proper[k] for k in list(sorted_proper)[:10]}
    # for key in first2pairs:
    #     print(key, ' ', first2pairs[key])
    # popularity()
    # suggestion()
    # suggestion_occurences()

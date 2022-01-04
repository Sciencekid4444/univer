import itertools
import json
import operator
from nltk.tokenize import word_tokenize
import regex as re


def get_data() -> dict:
    tweets: list = []
    with open('./tweets.txt') as f:
        for l in f:
            tweets.append(json.loads(l))

    updated_tweets: list = []
    for tweet in tweets:
        if 'created_at' in tweet:
            updated_tweets.append(tweet)
    return updated_tweets


def get_hashtags(db: list) -> dict:
    tags: dict = {}
    for entity in db:
        words: list = entity['text'].split()
        for word in words:
            if re.match(r"#[a-zA-Z]*", word):
                if word in tags:
                    tags[word] += 1
                else:
                    tags[word] = 1
    return tags


def sort(db: dict) -> list:
    return sorted(db.items(), key=lambda x: x[1], reverse=True)


def get_emotionalRating() -> dict:
    emotional_dict: dict = {}
    with open('AFINN-111.txt', 'r') as file:
        for line in file:
            values: list = line.split('\t')
            val: str = ''
            for x in values[1:len(values)]:
                val += x
            val = val.replace('\n', '')
            emotional_dict[values[0]] = int(val)
    return emotional_dict


def tokenize(db: dict, emo_rating: dict) -> dict:
    tweets_rating: list = []
    for entity in db:
        words = (word_tokenize(entity['text']))
        rating: int = 0
        tweet = {
            'id': entity['id'],
            'text': entity['text'],
            'rating': int
        }
        for word in words:
            if word in emo_rating:
                rating += emo_rating[word]
        tweet['rating'] = rating
        tweets_rating.append(tweet)
    return tweets_rating


def top(db: list):
    db.sort(key=operator.itemgetter('rating'), reverse=True)
    return db[:10]


def bottom(db: list):
    db.sort(key=operator.itemgetter('rating'))
    return db[:10]


if __name__ == '__main__':
    mock_db: dict = get_data()
    tags: dict = get_hashtags(mock_db)
    tags = sort(tags)
    top5: list = itertools.islice(tags, 5)
    for tweet in top5:
        print(tweet)


    emo_dict: dict = {}
    emo_dict = get_emotionalRating()
    tweets_rating: list = tokenize(mock_db, emo_dict)
    print('Most positive:')
    for tweet in top(tweets_rating):
        print(tweet)

    print('Most negative:')
    for tweet in bottom(tweets_rating):
        print(tweet)


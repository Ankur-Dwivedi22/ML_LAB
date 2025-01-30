from textblob import TextBlob


def label_sentiment(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity < 0:
        return 'negative'
    else:
        return 'neutral'


def label_articles(articles):
    return [label_sentiment(article) for article in articles]

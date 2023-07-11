tweets = api.search(q='python', count=100)

from textblob import TextBlob

for tweet in tweets:
    analysis = TextBlob(tweet.text)
    polarity = analysis.sentiment.polarity
    subjectivity = analysis.sentiment.subjectivity
    print(tweet.text, polarity, subjectivity)

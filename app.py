from textblob import TextBlob

print("Sentiment Analysis Tool")

text = input("Enter a sentence: ")

analysis = TextBlob(text)

if analysis.sentiment.polarity > 0:
    print("Positive Sentiment")
elif analysis.sentiment.polarity < 0:
    print("Negative Sentiment")
else:
    print("Neutral Sentiment")
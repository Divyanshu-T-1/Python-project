from textblob import TextBlob
import re

def analyze_tweet(tweet):
    # Create TextBlob
    blob = TextBlob(tweet)

    # Sentiment
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"

    # Hashtags and Mentions
    hashtags = re.findall(r"#\w+", tweet)
    mentions = re.findall(r"@\w+", tweet)

    # Word & Character Count
    words = tweet.split()
    word_count = len(words)
    char_count = len(tweet)

    # Print results
    print("\n--- Tweet Analysis ---")
    print("Sentiment:", sentiment)
    print("Word Count:", word_count)
    print("Character Count:", char_count)
    print("Hashtags:", hashtags)
    print("Mentions:", mentions)

    from textblob import TextBlob
import re

def analyze_tweet(tweet):
    # Create TextBlob
    blob = TextBlob(tweet)

    # Sentiment
    polarity = blob.sentiment.polarity
    if polarity > 0:
        sentiment = "Positive 😊"
    elif polarity < 0:
        sentiment = "Negative 😠"
    else:
        sentiment = "Neutral 😐"

    # Hashtags and Mentions
    hashtags = re.findall(r"#\w+", tweet)
    mentions = re.findall(r"@\w+", tweet)

    # Word & Character Count
    words = tweet.split()
    word_count = len(words)
    char_count = len(tweet)

    # Print results
    print("\n--- Tweet Analysis ---")
    print("Sentiment:", sentiment)
    print("Word Count:", word_count)
    print("Character Count:", char_count)
    print("Hashtags:", hashtags)
    print("Mentions:", mentions)

# Example usage
tweet = input("Enter a tweet: ")
analyze_tweet(tweet)



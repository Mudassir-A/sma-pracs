import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud # type: ignore

# Sample social media data
data = [
    "I love this product 😊",
    "Worst service ever 😡",
    "It is okay",
    "Amazing experience 😊",
    "Very disappointing service",
    "I am happy with the quality",
    "Not satisfied at all",
    "Nothing special about it",
    "Average performance"
]

# Create DataFrame
df = pd.DataFrame(data, columns=["Text"])

# Initialize Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(text)
    compound = score['compound']
    
    if compound >= 0.05:
        return "Positive"
    elif compound <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment"] = df["Text"].apply(get_sentiment)

# Print Results
print("\nSentiment Analysis Result (Positive / Negative / Neutral):\n")
print(df)

# Plot Sentiment Count
plt.figure(figsize=(6, 4))
sns.countplot(x="Sentiment", data=df, order=["Positive", "Neutral", "Negative"])
plt.title("Sentiment Analysis Result")
plt.xlabel("Sentiment")
plt.ylabel("Count")


# Generate Word Cloud
all_words = " ".join(df["Text"])
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_words)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.title("Word Cloud")
plt.show()
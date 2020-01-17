# Twitter Sentiment Analyser
# Basic script to analyse and graph how a Twitter account's "sentiment"
# varies over the months of a year. Version1.
import GetOldTweets3 as got
from textblob import TextBlob
import matplotlib.pylab as plt

# get tweets
no_of_tweets = 100
target_account = "Seikowsky"
tweetCriteria = got.manager.TweetCriteria().setUsername(target_account).setMaxTweets(no_of_tweets)
tweets = got.manager.TweetManager.getTweets(tweetCriteria)


# tweet and total sentiment counters for all months
tweet_counts = {}
sent_sums = {}

for month_index in range(1,13):
	tweet_counts[month_index] = 0
	sent_sums[month_index] = 0


# go through tweets and adjust tweet and sentiment counter for each
for tweet in tweets:
	tweet_month = tweet.date.month
	tweet_sent = TextBlob(tweet.text).sentiment.polarity

	tweet_counts[tweet_month] = tweet_counts[tweet_month] + 1
	sent_sums[tweet_month] = sent_sums[tweet_month] + tweet_sent


# compute average sentiments for all months
avg_sents = []
for month_index in range(1,13):
	if tweet_counts[month_index] != 0:
		avg_sent = sent_sums[month_index] / tweet_counts[month_index]
		avg_sents.append(avg_sent)
	else:
		avg_sents.append(0)


# plot results
plt.plot(avg_sents)
plt.title(target_account)
plt.show()
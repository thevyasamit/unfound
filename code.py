import tweepy
import nltk
from textblob import TextBlob
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import sys

consumer_key='--Enter Key here----'
consumer_secret='--Enter Key here----'

access_token='--Enter Key here----'
access_token_secret='--Enter Key here----'


auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api=tweepy.API(auth)
#orig_stdout = sys.stdout
f = open('out', 'w')
#sys.stdout = f


#public_tweets=api.search(q='Mercedes', since='2018-11-21',since_id='3')#,until='2018-11-24')
public_tweets=api.search(q='Technology',since='2018-12-06',until='2018-12-09',count='50')
#public_tweets=api.search('sad')


for tweet in public_tweets:
	f.write("\n__________________________________________\n")
	for us in tweepy.Cursor(api.mentions_timeline).items():
		print status._json['text']
	#print(tweet.text)
	
	f.write(tweet.text.encode("utf-8"))
	f.write("\n")
	#print(tweet.created_at)
	date=str(tweet.created_at)
	f.write(date)
	f.write(" \n\n")

	#-------Code to get other events-------------

	# f.write("--------Other Events--------")
	# tokenized_word=word_tokenize(tweet.text)
	# tokenized_sent=tokenized_word
	# stop_words=set(stopwords.words("english"))
	# filtered_sent=[]
	# for w in tokenized_sent:
 #    		if w not in stop_words:
 #        		filtered_sent.append(w)
 #        f.write("\n")
 #    	f.write("Filterd Sentence:")
 #    	f.write(filtered_sent[0])
 #    	f.write("\n")
 #    	txt=tweet.text
 #    	blob = TextBlob(txt)
 #    	f.seek(0)
 #    	f.write(str([word for (word, pos) in nltk.pos_tag(nltk.word_tokenize(txt)) if pos[0] == 'N']))

    	#print(blob.noun_phrases)

 	#--------end of code to get other event-----------


	#print("   ")
	#print(tweet.until)
	analysis=TextBlob(tweet.text)
	#print(analysis.sentiment)

#sys.stdout = orig_stdout
f.close()

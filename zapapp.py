import tweepy
import random
from flask import Flask, request, make_response, render_template

'''
	sprengmi 2017-04-10
	This is an app used in conjuction with a Zapier twitter trigger
	and Zapier Webhooks to find a mention and auto reply to that tweet.
	Using for my Zapier application!

	https://zapier.com/app/editor/20861058/overview
'''

app = Flask(__name__)

def my_api(tokens):
	auth = tweepy.OAuthHandler(tokens['consumer_key'], tokens['consumer_secret'])
	auth.set_access_token(tokens['access_token'], tokens['access_token_secret'])
	return tweepy.API(auth)

def main(user, tweetid):
	# https://dev.twitter.com/oauth/overview/application-owner-access-tokens
	tokens = { 
	"consumer_key"        : "5jjZS44faQDoBy0NaSM9OWpRp",
	"consumer_secret"     : "VxPnwGm4c6DvFcqiTFBzmK7KkCuwfRmBCatJh8pU4O8rljozCU",
	"access_token"        : "852401434717036544-DdvbvYbgsnRLihhkhNqJNHahjTRBVEV",
	"access_token_secret" : "MMIqLwNwuqMTRsnjVgW3byXte3BGTgo5JE55cM8CwtKST" 
	}
	
	i=random.randint(0,999)
	api = my_api(tokens)
	tweet =  ( 
		"Hello " +  "@" + user +"! Here is my Zapier app!"  + "\n" + 
		"Resume: goo.gl/g5mcFj" + "\n" +
		"GitHub: github.com/sprengmi *" 		+ str(i)
		)
	#status = api.update_status(status=tweet, tweetid=tweetid) 
	status = api.update_status(status=tweet, in_reply_to_status_id = tweetid) 
	print tweet
	
	return make_response("Tweet run", 200,)
													
@app.route("/post", methods=["GET","POST"])
def listneing():
	user = request.form.get('user',None)
	tweetid = request.form.get('tweetid',None)
	print user
	
	return main(user, tweetid)
	
	return make_response("Nothing found", 404, {"X-No-Retry": 1})

@app.route("/", methods=["GET", "POST"])
def hello():
	print "hello world"
	return make_response("hello world", 200,)		
  
if __name__ == "__main__":
	#main()
	app.run(debug=True)

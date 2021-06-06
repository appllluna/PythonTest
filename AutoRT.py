#tweepyで自分のツイートの取得

import tweepy

CONSUMER_KEY = "foLSwiCYGWLbWGan7rWUnCxoW"
CONSUMER_SECRET = "nG50TclRmutJYyh58jFVZpM6O0uP9nJMOeajF17eW2ggTDkkrv"
ACCESS_TOKEN = "623827564-wvDUNOCAH87LfLQoKrJKScaVo2PMXZNf5qbBb8t4"
ACCESS_SECRET = "H50MURjwpfG9usSJh9nMySW0adiVWOqPFZMteQgGOHLPU"

#APIインスタンスを作成
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth)

myinfo = api.me()

tweets = tweepy.Cursor(api.user_timeline, id = myinfo.id).items(100)

for tweet in tweets:
    if not "RT @" in tweet.text[0:4]:
        if "ちんちん" in tweet.text:#Retweetしたいハッシュタグの設定
            tweet_id = tweet.id
            screen_id = tweet.user.screen_name
            
            print("↓---RTするツイートの情報---↓")
            print(tweet.text)
            print ("Twitter.com/{}/status/{}".format(screen_id,tweet_id))
            print("↑---RTするツイートの情報---↑")
                
            try:
                api.unretweet(tweet_id)
            except Exception as e:
                print(e)
                print("無視してよいエラーコード")
            try:
                api.retweet(tweet_id)
                print("RTしたよ")
            except Exception as e:
                print("RT失敗しました")
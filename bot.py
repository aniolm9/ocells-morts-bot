import tweepy
import settings

def createApi():
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(settings.CONSUMER_KEY, settings.CONSUMER_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth)

    return api

def newTweet(api, text, imgFile):
    f = open(imgFile, 'rb')
    picture = api.media_upload(filename=imgFile, file=f)
    api.update_status(media_ids=[picture.media_id_string], status=text)
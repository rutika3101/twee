import tweepy
API_key='JBEOUB3VObc80iOFFAI9ZBOKH'
API_secret_key = 'KsV5PWPaSyRHa096rJCTtGYo1wLJ3CwLlklzeAxWR3n0Ypv5pc'
Access_token ='1338808861130596352-FG5J9788KkWevnurGRTdKXU4BrUPMP'
Access_token_secret = 'sXBugxv7WaIWoo3YeGDiS0xJlK44cy56crhTa6zekuS2o'

class MaxListener(tweepy.StreamListener):
    def on_data(self, raw_data):
        self.process_data(raw_data)
        return True

    def process_data(self, raw_data):
        print(raw_data)

    def on_error(self, status_code):
        if status_code == 420:
            return False


class MaxStream(tweepy.StreamListener):
    def __init__(self,auth,listener):
        self.stream = tweepy.Stream(auth=auth, listener=listener)

    def start(self, keyword_list):
        self.stream.filter(track=keyword_list)


if __name__ == "__main__":
    listener = MaxListener()
    auth = tweepy.OAuthHandler(API_key,API_secret_key)
    auth.set_access_token(Access_token,Access_token_secret)

    stream= MaxStream(auth , listener)
    stream.start(['django'])
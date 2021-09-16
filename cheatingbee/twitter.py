import datetime
import io
import os
import tweepy
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont


class Twitter:

    def __init__(self):
        load_dotenv()
        api_key = os.environ.get('TWITTER_API')
        api_key_secret = os.environ.get('TWITTER_API_SECRET')
        access_token = os.environ.get('TWITTER_ACCESS')
        access_token_secret = os.environ.get('TWITTER_ACCESS_SECRET')
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def post_tweet(self, solver_answers, pangrams, nyt_answers):
        pangrams.sort()
        nyt_answers.sort()
        text = ("Pangram(s):\n"
                + self.__make_rows(pangrams)
                + '\n\nAnswers:\n'
                + self.__make_rows(nyt_answers))
        pic = self.__create_pic(text)
        media = self.api.media_upload(
                filename=str(datetime.date.today()),
                file=pic,
                possibly_sensitive=True)
        if len(solver_answers)/len(nyt_answers) == 1:
            tweet = "Cheating Bee got all {} answers of todays #SpellingBee!🐝🎓"
            tweet = tweet + "\n\nNeed help with todays puzzle? Click the image below!"
            tweet = tweet.format(len(nyt_answers))
        else:
            tweet = "Cheating Bee got {}/{} answers of todays #SpellingBee!🐝"
            tweet = tweet + "\n\nNeed help with todays puzzle? Click the image below!"
            tweet = tweet.format(len(solver_answers), len(nyt_answers))
        self.api.update_status(status=tweet, media_ids=[media.media_id])

    def __make_rows(self, word_list):
        text = ''
        for i in range(0, len(word_list), 5):
            if i + 5 < len(word_list):
                text = text + ', '.join(word_list[i:i+5]) + ',\n'
            else:
                text = text + ', '.join(word_list[i:len(word_list)])
        return text

    def __create_pic(self, text):
        font_size = 20
        # number of lines plus 3 for padding
        height = (text.count('\n') + 3) * font_size
        # longest line in string length times font size at a ratio of .65
        width = int(
            max([len(x) for x in text.splitlines()]) * font_size * 0.65)
        pic = Image.new("RGB", (width, height), (255, 255, 255))
        font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", font_size)
        drawing = ImageDraw.Draw(pic)
        drawing.multiline_text((10, 10), text, font=font, fill=(0, 0, 0))
        b = io.BytesIO()
        pic.save(b, 'png')
        b.seek(0)
        return b

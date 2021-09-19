import datetime
import io
import os
import tweepy
from dotenv import load_dotenv
from PIL import Image, ImageDraw, ImageFont


class Twitter:
    """
    A class used to manage the connection with the Twitter API

    ...

    Methods
    -------
    post_tweet(solver_answers, nyt_answers, pangrams)
        Creates the tweet text and posts a picture with todays answers
    """

    def __init__(self):
        load_dotenv()
        api_key = os.environ.get('TWITTER_API')
        api_key_secret = os.environ.get('TWITTER_API_SECRET')
        access_token = os.environ.get('TWITTER_ACCESS')
        access_token_secret = os.environ.get('TWITTER_ACCESS_SECRET')
        auth = tweepy.OAuthHandler(api_key, api_key_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def post_tweet(self, solver_answers, nyt_answers, pangrams):
        """Composes the tweet text and posts a picture with todays answers
        marked as NSFW to avoid spoilers

        Parameters
        ----------
        solver_answers: list, required
            The answers returned by the solver
        nyt_answers: list, required
            The answers of todays New York Times Spelling Bee
        pangrams: list, required
            The pangrams in the answers of todays New York Times Spelling Bee
        """
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
        """Formats a list of words into a string with rows five words long

        Parameters
        ----------
        word_list: list, required
            A list of words

        Returns
        -------
        str
            The word list composed to a string with rows of five words
        """
        text = ''
        for i in range(0, len(word_list), 5):
            if i + 5 < len(word_list):
                text = text + ', '.join(word_list[i:i+5]) + ',\n'
            else:
                text = text + ', '.join(word_list[i:len(word_list)])
        return text

    def __create_pic(self, text):
        """Formats a list of words into a string with rows five words long

        Parameters
        ----------
        word_list: list, required
            A list of words to be formatted to a string

        Returns
        -------
        str
            The word list composed to a string with rows of five words
        """
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

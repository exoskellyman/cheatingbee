# &#128029; Cheating Bee &#128029;

Cheating Bee is a [Twitter bot](https://twitter.com/CheatingBee) designed to cheat at the New York Times Spelling Bee

## INSTALLATION

In order to run the project you must:

1. [Install python 3.7](https://github.com/pyenv/pyenv)
2. [Install pipenv](https://pipenv.pypa.io/en/latest/)
3. [Install Google Chrome](https://www.google.com/chrome/)
4. [Install Chrome driver](https://chromedriver.chromium.org/downloads)
5. [Get a Twitter developer account](https://developer.twitter.com/en)
6. Store Twitter API and account tokens in environment variables

Clone this repository navigate to the directory and run:

    $ pipenv install
    $ pipenv shell

When you want to run the bot, from the pipenv shell use:

    $ python cheatingbee

To run tests you must install developer dependencies and run:

    $ pipenv install -d
    $ python -m pytest

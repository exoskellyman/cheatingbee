from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import json


class NewYorkTimes:
    """
    A class for scraping the New York Times Spelling Bee page information

    ...

    Attributes
    ----------
    required_letters: set
        A set of the letters required in the Spelling Bee answers
    optional_letters: set
        A set of the letters optional in the Spelling Bee answers
    todays_answers: set
        The answers of todays New York Times Spelling Bee
    todays_pangrams: set
        The pangrams in the answers of todays New York Times Spelling Bee
    """
    URL = "https://www.nytimes.com/puzzles/spelling-bee"
    PLAY_BUTTON_CLASS = "pz-moment__button.primary"

    def __init__(self):
        opts = Options()
        # opts.add_argument("--user-data-dir=~/.config/google-chrome")
        opts.add_argument("start-maximized")
        opts.set_headless()
        browser = Chrome(chrome_options=opts)
        browser.get(self.URL)

        try:
            play_button = WebDriverWait(browser, 10).until(
                expected_conditions.element_to_be_clickable(
                    (By.CLASS_NAME, self.PLAY_BUTTON_CLASS)
                )
            )
            # Play button might not be in view, have to move to it to click it
            ActionChains(browser).move_to_element(play_button).perform()
            play_button.click()
            self.__load_game_data(browser.page_source)
        finally:
            browser.close()

    def __load_game_data(self, source):
        """Uses BeautifulSoup to parse the New York Times Spelling Bee page
        and load the game data into instance variables

        Parameters
        ----------
        source: driver.page_source, required
            The New York Times Spelling Bee page source code to be parsed
        """
        soup = BeautifulSoup(source, "html.parser")
        # .string returns the text but doesn't return a string so we have to
        # cast it
        game_string = str(
            soup.find(id="js-hook-game-wrapper").find("script").string)
        # We don't need the variable assignment
        game_string = game_string[game_string.find('{'):]
        game_data = json.loads(game_string)
        self.required_letters = set(game_data['today']['centerLetter'])
        self.optional_letters = set(game_data['today']['outerLetters'])
        self.todays_pangrams = set(game_data['today']['pangrams'])
        self.todays_answers = set(game_data['today']['answers'])

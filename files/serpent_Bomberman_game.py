from serpent.game import Game

from .api.api import BombermanAPI

from serpent.utilities import Singleton

from serpent.game_launchers.web_browser_game_launcher import WebBrowser


class SerpentBombermanGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "web_browser"

        # Game URL: https://www.speelspelletjes.nl/spel/playing-with-fire-2
        kwargs["window_name"] = "Playing With Fire 2 - Speel Playing With Fire 2 op Speel Spelletjes - Google Chrome"
        
        kwargs["url"] = "URL"
        kwargs["browser"] = WebBrowser.DEFAULT

        super().__init__(**kwargs)

        self.api_class = BombermanAPI
        self.api_instance = None

    @property
    def screen_regions(self):

        regions = {
            "SCREEN1_PLAY_BUTTON": (615, 392, 647, 537)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets

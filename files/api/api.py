from serpent.game_api import GameAPI


class BombermanAPI(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)

    def my_api_function(self):
        pass

    class Menu:

        @classmethod
        def click_play_button(cls):
            BombermanAPI.instance.input_controller.click_screen_region(
                screen_region="SPLASH_SCREEN_PLAY_BUTTON"
            )

        @classmethod
        def click_1_player_button(cls):
            BombermanAPI.instance.input_controller.click_screen_region(
                screen_region="PLAYER_MENU_1_PLAYER_BUTTON"
            )

        @classmethod
        def click_1_opponent_button(cls):
            BombermanAPI.instance.input_controller.click_screen_region(
                screen_region="OPPONENT_MENU_1_OPPONENT_BUTTON"
            )

        @classmethod
        def click_level_1_button(cls):
            BombermanAPI.instance.input_controller.click_screen_region(
                screen_region="LEVEL_MENU_LEVEL_1_BUTTON"
            )
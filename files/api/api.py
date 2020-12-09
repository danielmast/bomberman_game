from serpent.game_api import GameAPI


class BombermanAPI(GameAPI):

    def __init__(self, game=None):
        super().__init__(game=game)

    def my_api_function(self):
        pass

    class Menu:

        @classmethod
        def click_play_button(cls):
            print('Click play button')
            BombermanAPI.instance.input_controller.click_screen_region(
                screen_region="SPLASH_SCREEN_PLAY_BUTTON"
            )

        @classmethod
        def click_1_player_button(cls):
            print('Click 1 player button')
            BombermanAPI.instance.input_controller.click_screen_region(
                screen_region="PLAYER_MENU_1_PLAYER_BUTTON"
            )

        @classmethod
        def click_1_opponent_button(cls):
            print('Click 1 opponent button')
            BombermanAPI.instance.input_controller.click_screen_region(
                screen_region="OPPONENT_MENU_1_OPPONENT_BUTTON"
            )

        @classmethod
        def click_level_1_button(cls):
            print('Click level 1 button')
            BombermanAPI.instance.input_controller.click_screen_region(
                screen_region="LEVEL_MENU_LEVEL_1_BUTTON"
            )

        @classmethod
        def click_play_now_button(cls):
            print('Click play now button')
            BombermanAPI.instance.input_controller.click_screen_region(
                screen_region="END_OF_ROUND_PLAY_NOW_BUTTON"
            )

        @classmethod
        def click_play_again_button(cls):
            print('Click play again button')
            BombermanAPI.instance.input_controller.click_screen_region(
                screen_region="END_OF_GAME_PLAY_AGAIN_BUTTON"
            )
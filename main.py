import arcade

from WordBlasters.main import WordBlasters
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Learning Arcade Main Menu"
class MainMenu(arcade.Window):
    """
    def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = InstructionsView()
    window.show_view(game_view)
    arcade.run()
    """
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        game_view = WordBlasters().run()


def main():
    window = MainMenu()
    
    # window.show_view(game_view)
    arcade.run()
main()


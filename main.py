import arcade
import threading

from WordBlasters.wbmain import WordBlasters
from Hangman.hangman import Hangman_game

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
        # game_view = 
        

    def on_key_press(self, symbol, modifier):
        print(symbol)

def main():
    print("What game do you want to run? ")
    print("1. Word Blasters")
    print("2. Hangman")
    print("3. Oasis")
    window = MainMenu()
    wb = threading.Thread(target = WordBlasters().run)
    wb.start()

    hm = threading.Thread(target = Hangman_game().run)
    hm.start()

    # window.show_view(game_view)
    arcade.run()
main()


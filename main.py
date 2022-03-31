from concurrent.futures import thread
from webbrowser import BackgroundBrowser
import arcade
import arcade.gui
import threading

from True_Desert_main.True_Oasis import *
from WordBlasters.wbmain import WordBlasters
from Hangman.hangman import Hangman_game

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700
SCREEN_TITLE = "Learning Arcade Main Menu"

class MainMenu(arcade.View):
    """
    def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game_view = InstructionsView()
    window.show_view(game_view)
    arcade.run()
    """
    def __init__(self):
        super().__init__()
        self.background = arcade.load_texture("arcadescreen.jpg")
        self.background_sound = arcade.load_sound("Learning-Arcade\music2.mp4")
        arcade.play_sound(self.background_sound)

        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.v_box = arcade.gui.UIBoxLayout()
        
        math_button = arcade.gui.UIFlatButton(text="Oasis", width=200)
        self.v_box.add(math_button.with_space_around(bottom=20))

        word_button = arcade.gui.UIFlatButton(text="WordBlasters", width=200)
        self.v_box.add(word_button.with_space_around(bottom=20))

        hangman_button = arcade.gui.UIFlatButton(text="Hangman", width=200)
        self.v_box.add(hangman_button.with_space_around(bottom=20))

        word_button.on_click = self.run_word_blasters
        hangman_button.on_click = self.run_hangman
        math_button.on_click = self.run_true_Desert
        # game_view = 
        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x = "center_x",
                anchor_y = "center_y",
                child = self.v_box)
        )
    
            
    @staticmethod
    def run_word_blasters(event):
        wb = threading.Thread(target = WordBlasters().run)
        wb.start()
    @staticmethod
    def run_hangman(event):
        hm = threading.Thread(target = Hangman_game().run)
        hm.start()
            
        
        
    
    def run_true_Desert(self, event):
        game_view = InstructionsView()
        game_view.on_show()
        self.window.show_view(game_view)
        
        
    def on_key_press(self, symbol, modifier):
        print(symbol)

    def on_draw(self):
        self.clear()
        arcade.draw_lrwh_rectangle_textured(0, 0,
        SCREEN_WIDTH, SCREEN_HEIGHT,
        self.background)
        self.manager.draw()

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT,SCREEN_TITLE)
    menu_view = MainMenu()
    window.show_view(menu_view)
    arcade.run()
main()



# class ArcadeDemo(arcade.Window):
#     def __init__(self):
#         super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        
#     @staticmethod
#     def run():
#         window = ArcadeDemo()
#         arcade.run()

# class RaylibDemo():
#     @staticmethod
#     def run():
#         wb = threading.Thread(target = WordBlasters().run)
#         wb.start()

# def main():
#     t1 = threading.Thread(target = ArcadeDemo.run)
#     RaylibDemo.run()
#     t1.start()

# main()
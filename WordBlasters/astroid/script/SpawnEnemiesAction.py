from WordBlasters.genie.script.action import UpdateAction
from WordBlasters.astroid.cast.astroid import Astroid

import random
import time


LARGE_SIZE = (40, 55)

LARGE = 1
MEDIUM = 2
SMALL = 3

class SpawnEnemiesAction(UpdateAction):
    def __init__(self, priority, window_size, levels_dict, level):
        super().__init__(priority)
        self._timer_started = False
        self._last_spawn = 0 # seconds
        self._window_size = window_size
        self._enemy_spawn = False
        self.letter_string = ""
        self.levels_dict = levels_dict
        self.level = level

        self.round = 0
        self.letter_list = []
        self.letter_cue = []


        pos_1 = LARGE_SIZE[0] * 3
        pos_2 = self._window_size[1] / 3
        pos_3 = self._window_size[1] / 2
        pos_4 = (self._window_size[1] / 3) * 2
        pos_5 = self._window_size[1]
        start_pos_y_options = [pos_1, pos_2, pos_3, pos_4, pos_5]
        
        start_pos_x = self._window_size[0] - LARGE_SIZE[0]

        for word in self.levels_dict[self.level]:
            start_pos_y = random.choice(start_pos_y_options)
            for letter in word:
                self.letter_list.append([letter, start_pos_x, start_pos_y])

    def _create_enemy(self, x: int, y:int, letter: str = ""):
        """
            This is a helper function that creates an astroid based on
            the input "type" and the initial position
        """
        
        # possible_vel is a list of possible velocities that the emeny can have
        # possible_vel = [-3, -2, -1, 1, 2, 3]
        
        
        # letter = random.randint(1,26)

        if letter == "A": # A
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/A.png"
            self.letter_string = "A"
        elif letter == "B": # B
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/B.png"
            self.letter_string = "B"
        elif letter == "C": # C
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/C.png"
            self.letter_string = "C"
        elif letter == "D": # D
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/D.png"
            self.letter_string = "D"
        elif letter == "E": # E
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/E.png"
            self.letter_string = "E"
        elif letter == "F": # F
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/F.png"
            self.letter_string = "F"
        elif letter == "G": # G
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/G.png"
            self.letter_string = "G"
        elif letter == "H": # H
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/H.png"
            self.letter_string = "H"
        elif letter == "I": # I
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/I.png"
            self.letter_string = "I"
        elif letter == "J": # J
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/J.png"
            self.letter_string = "J"
        elif letter == "K": # K
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/K.png"
            self.letter_string = "K"
        elif letter == "L": # L
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/L.png"
            self.letter_string = "L"
        elif letter == "M": # M
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/M.png"
            self.letter_string = "M"
        elif letter == "N": # N
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/N.png"
            self.letter_string = "N"
        elif letter == "O": # O
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/O.png"
            self.letter_string = "O"
        elif letter == "P": # P
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/P.png"
            self.letter_string = "P"
        elif letter == "Q": # Q
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/Q.png"
            self.letter_string = "Q"
        elif letter == "R": # R
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/R.png"
            self.letter_string = "R"
        elif letter == "S": # S
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/S.png"
            self.letter_string = "S"
        elif letter == "T": # T
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/T.png"
            self.letter_string = "T"
        elif letter == "U": # U
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/U.png"
            self.letter_string = "U"
        elif letter == "V": # V
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/V.png"
            self.letter_string = "V"
        elif letter == "W": # W
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/W.png"
            self.letter_string = "W"
        elif letter == "X": # X
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/X.png"
            self.letter_string = "X"
        elif letter == "Y": # Y
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/Y.png"
            self.letter_string = "Y"
        elif letter == "Z": # Z
            enemy = "WordBlasters/astroid/assets/Asteroid_letters/Z.png"
            self.letter_string = "Z"

        self.letter_cue.append([self.letter_string, y])

        # randomly picks a velicity. this makes the direction when spawned in random
        # vel_x = -3
        # vel_y = 1 if y < (self._window_size[1] / 2) else -1
        if y == LARGE_SIZE[0] * 3:
            vel_y = 1.3
            vel_x = -3
        elif y == self._window_size[1]: # Done
            vel_y = -1.7
            vel_x = -3
        elif y == (self._window_size[1] / 2): # Done
            vel_y = 0
            vel_x = -3
        elif y == self._window_size[1] / 3: # Done
            vel_y = .6
            vel_x = -3
        elif y == (self._window_size[1] / 3) * 2: # Done
            vel_y = -.6
            vel_x = -3

        return Astroid(enemy,
                        health_bar_y_offset=LARGE_SIZE[1]/2+5,
                        health_bar_height=5,
                        width = LARGE_SIZE[0],
                        height = LARGE_SIZE[1],
                        x = x, y = y,
                        vx = vel_x, vy = vel_y,
                        rotation_vel=0,
                        points=1, max_hp=1, show_text_health=True)

    def get_letter_list(self):
        return self.letter_list

    def get_letter_cue(self):
        return self.letter_cue

    def cue_delete_top(self):
        self.letter_cue.pop(0)
    
    def execute(self, actors, actions, clock, callback):
        """
            - Check to see if it's time to spawn another astroid
            - Randomly pick Small, Medium, or Large
            - Pick and initial position for the astroid
            - Create the astroid by calling self._create_astroid_by_type
            - Add the astroid to the cast
            - Record the most recent spawn
        """
        if not self._timer_started:
            self._timer_started = True
            self._last_spawn = time.time()

        # get level
            # TODO:
        
                # seconds

        if self.level == 1:
            spawn_interval = 1.5
        elif self.level == 2:
            spawn_interval = 1.3
        elif self.level == 3:
            spawn_interval = 1.1
        elif self.level == 4:
            spawn_interval = .9
        elif self.level == 5:
            spawn_interval = .7
        else:
            spawn_interval = 1.5 
        if time.time() - self._last_spawn >= spawn_interval:
            # Pick a random type of astroid: Small, Medium, Large
            # astroid_type = random.randint(1,3)

            # lower_y_bound = int(self._window_size[1] / 8)
            # upper_y_bound = int(self._window_size[1] - lower_y_bound)
            

            
                # for letter in word:
                #     self.letter_list.append[letter, start_pos_x, start_pos_y]
                    # astroid = self._create_enemy(start_pos_x, start_pos_y, letter)
                    
                # actors.add_actor("astroids", astroid)
                # astroid.set_letter(self.letter_string)
                # astroid.set_start_y(start_pos_y)
                # astroid.set_has_missle(False)
 
            letter_info = self.letter_list[self.round]
            
            astroid = self._create_enemy(letter_info[1], letter_info[2], letter_info[0])
            
            actors.add_actor("astroids", astroid)
            astroid.set_letter(self.letter_string)
            astroid.set_start_y(letter_info[2])
            astroid.set_has_missle(False)
            self.round += 1
            # set last_spawn to current frame
            self._last_spawn = time.time()
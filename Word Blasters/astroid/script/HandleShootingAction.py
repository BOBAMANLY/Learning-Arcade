import time
import math

from genie.script.action import InputAction
from genie.services import keys

# from genie.services.raylib_services.constants.keys.py

from astroid.cast.bullet import Bullet

# BULLET_VX = 0
# BULLET_VY = -10
ATTACK_INTERVAL = 0   # seconds
LARGE_SIZE = (40, 55)

class HandleShootingAction(InputAction):
    def __init__(self, priority, keyboard_service, audio_service, spawn_enemies_action):
        super().__init__(priority)
        # self._ship = None
        # self._ship_2 = None
        # self._ship_3 = None
        self._ship_4 = None
        self._last_bullet_spawn = time.time()  # seconds
        # self._last_bullet_dict = {'''"ship": self._last_bullet_spawn, "ship_2": self._last_bullet_spawn, "ship_3": self._last_bullet_spawn, '''"ship_4": self._last_bullet_spawn}
        self._last_bullet_dict = {"ship_4": self._last_bullet_spawn}
        self._keyboard_service = keyboard_service
        self._audio_service = audio_service
        self._window_size = (1000, 1000)


        self.spawn_enemies_action = spawn_enemies_action
        self.round = 0
    
    def _spawn_bullet(self, clock, actors, bullet_vx, bullet_vy, ship, rotation, name):
        """
            Only spawn a bullet if:
                - The time from the last time bullet spawn until now is >= ATTACK_INTERVAL
                - The ship is still alive (not None)
        """
        time_since_last_shot = time.time() - self._last_bullet_dict[name]     # Measured in seconds
        if ship != None and time_since_last_shot >= ATTACK_INTERVAL:
            # Bullet's starting position should be right on top of the ship
            bullet_x = ship.get_x()
            bullet_y = ship.get_y() - (ship.get_height() / 2)

            if len(actors.get_actors("astroids")) != 0:
                min_x = 10000
                for actor in actors.get_actors("astroids"):
                    if actor.get_x() < min_x:
                        min_x = actor.get_x()
                        closest_astroid = actor

                closest_astroid_start_y = closest_astroid.get_start_y()

            if closest_astroid_start_y == self._window_size[1]:
                bullet_x += 40
                bullet_y += 40
            elif closest_astroid_start_y == LARGE_SIZE[0] * 3:
                bullet_x += 40
                bullet_y += 15
            elif closest_astroid_start_y == (self._window_size[1] / 3) * 2:
                bullet_x += 50
                bullet_y += 30
            elif closest_astroid_start_y == self._window_size[1] / 3:
                bullet_x += 50
                bullet_y += 15
            elif closest_astroid_start_y == self._window_size[1] / 2:
                bullet_x += 50
                bullet_y += 20
           
            
            # Spawn bullet
            bullet = Bullet("astroid/assets/bullet.png", 20, 30, x = bullet_x, y = bullet_y, vx = bullet_vx, vy = bullet_vy)
            # if name == "ship":
            #     actors.add_actor("bullets_1", bullet)
            # if name == "ship_2":
            #     actors.add_actor("bullets_2", bullet)
            # if name == "ship_3":
            #     actors.add_actor("bullets_3", bullet)
            if name == "ship_4":
                actors.add_actor("bullets_4", bullet)

            # Rotate the bullet to which player shot
            bullet.set_rotation(rotation)

            # Play the shooting sound :)
            self._audio_service.play_sound("astroid/assets/sound/bullet_shot.wav", 0.1)

            # Record the time this bullet spawns
            self._last_bullet_spawn = time.time()
            self._last_bullet_dict[name] = self._last_bullet_spawn

    def execute(self, actors, actions, clock, callback):
        """
            Handle the shooting when the user presses SPACE
        """

        self._ship_4 = actors.get_first_actor("ship_4")

        if len(actors.get_actors("astroids")) != 0:
            letter_cue = self.spawn_enemies_action.get_letter_cue()
            if len(letter_cue) != 0:
                asteroid_letter = letter_cue[0][0]
                closest_astroid_start_y = letter_cue[0][1]
                # min_x = 10000
                # for actor in actors.get_actors("astroids"):
                #     if actor.get_x() < min_x and actor.get_has_missle() == False:
                #         min_x = actor.get_x()
                #         closest_astroid = actor

                #         closest_astroid_start_y = closest_astroid.get_start_y()
                #         asteroid_letter = closest_astroid.get_letter()
            
                # for astroid in actors.get_actors("astroids"):
                    
                #     if astroid.get_x() < min_x:
                        
                #         min_x = astroid.get_x()
                #         target_asteroid = astroid
                #         asteroid_targeted = True
                #         asteroid_letter = target_asteroid.get_letter()

                letters = {"A" : 44,
                            "B" : 45,
                            "C" : 46,
                            "D" : 47,
                            "E" : 48,
                            "F" : 49,
                            "G" : 50,
                            "H" : 51,
                            "I" : 52,
                            "J" : 53,
                            "K" : 54,
                            "L" : 55,
                            "M" : 56,
                            "N" : 57,
                            "O" : 58,
                            "P" : 59,
                            "Q" : 60,
                            "R" : 61,
                            "S" : 62,
                            "T" : 63,
                            "U" : 64,
                            "V" : 65,
                            "W" : 66,
                            "X" : 67,
                            "Y" : 68,
                            "Z" : 69,
                            "BACKSLASH" : 39}

                letter_number = letters[asteroid_letter]
                
                if (self._keyboard_service.is_key_down(letter_number) and self._ship_4 != None):
                    self.round += 1
                    # pos_1 = LARGE_SIZE[0] * 3
                    # pos_2 = self._window_size[1] / 3
                    # pos_3 = self._window_size[1] / 2
                    # pos_4 = (self._window_size[1] / 3) * 2
                    # pos_5 = self._window_size[1]

                    # if y == LARGE_SIZE[0] * 3:
                    #     vel_y = 1.3
                    #     vel_x = -3
                    # elif y == self._window_size[1]: # Done
                    #     vel_y = -1.7
                    #     vel_x = -3
                    # elif y == (self._window_size[1] / 2): # Done
                    #     vel_y = 0
                    #     vel_x = -3
                    # elif y == self._window_size[1] / 3: # Done
                    #     vel_y = .6
                    #     vel_x = -3
                    # elif y == (self._window_size[1] / 3) * 2: # Done
                    #     vel_y = -.6
                    #     vel_x = -3

                    if closest_astroid_start_y == self._window_size[1] / 2:
                        self._spawn_bullet(clock, actors, 10, 0, self._ship_4, self._ship_4.get_rotation(), "ship_4") # Done
                        # closest_astroid.set_has_missle(True)
                        self.spawn_enemies_action.cue_delete_top()
                        
                    elif closest_astroid_start_y == self._window_size[1] / 3:
                        self._spawn_bullet(clock, actors, 10, -2, self._ship_4, self._ship_4.get_rotation(), "ship_4") # Done
                        # closest_astroid.set_has_missle(True)
                        self.spawn_enemies_action.cue_delete_top()
                        
                    elif closest_astroid_start_y == (self._window_size[1] / 3) * 2:
                        self._spawn_bullet(clock, actors, 10, 2.2, self._ship_4, self._ship_4.get_rotation(), "ship_4") # Done
                        # closest_astroid.set_has_missle(True)
                        self.spawn_enemies_action.cue_delete_top()
                        
                    elif closest_astroid_start_y == LARGE_SIZE[0] * 3:
                        self._spawn_bullet(clock, actors, 10, -4.7, self._ship_4, self._ship_4.get_rotation(), "ship_4") # Done
                        # closest_astroid.set_has_missle(True)
                        self.spawn_enemies_action.cue_delete_top()
                        
                    elif closest_astroid_start_y == self._window_size[1]:
                        self._spawn_bullet(clock, actors, 10, 5.7, self._ship_4, self._ship_4.get_rotation(), "ship_4") # Done
                        # closest_astroid.set_has_missle(True)
                        self.spawn_enemies_action.cue_delete_top()
                    

                elif (self._keyboard_service.is_key_down(letters["BACKSLASH"]) and self._ship_4 != None):
                    if closest_astroid_start_y == self._window_size[1] / 2:
                        self._spawn_bullet(clock, actors, 10, 0, self._ship_4, self._ship_4.get_rotation(), "ship_4") # Done
                        # closest_astroid.set_has_missle(True)
                        self.spawn_enemies_action.cue_delete_top()
                        
                    elif closest_astroid_start_y == self._window_size[1] / 3:
                        self._spawn_bullet(clock, actors, 10, -2, self._ship_4, self._ship_4.get_rotation(), "ship_4") # Done
                        # closest_astroid.set_has_missle(True)
                        self.spawn_enemies_action.cue_delete_top()
                        
                    elif closest_astroid_start_y == (self._window_size[1] / 3) * 2:
                        self._spawn_bullet(clock, actors, 10, 2.2, self._ship_4, self._ship_4.get_rotation(), "ship_4") # Done
                        # closest_astroid.set_has_missle(True)
                        self.spawn_enemies_action.cue_delete_top()
                        
                    elif closest_astroid_start_y == LARGE_SIZE[0] * 3:
                        self._spawn_bullet(clock, actors, 10, -4.7, self._ship_4, self._ship_4.get_rotation(), "ship_4") # Done
                        # closest_astroid.set_has_missle(True)
                        self.spawn_enemies_action.cue_delete_top()
                        
                    elif closest_astroid_start_y == self._window_size[1]:
                        self._spawn_bullet(clock, actors, 10, 5.7, self._ship_4, self._ship_4.get_rotation(), "ship_4") # Done
                        # closest_astroid.set_has_missle(True)
                        self.spawn_enemies_action.cue_delete_top()

        # if (self._keyboard_service.is_key_down(keys.KP4) or self._keyboard_service.is_key_down(keys.KP6)) and self._ship_4 != None:
        #     self._spawn_bullet(clock, actors, 10, 0, self._ship_4, self._ship_4.get_rotation(), "ship_4")
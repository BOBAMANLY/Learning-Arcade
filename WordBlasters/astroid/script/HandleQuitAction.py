from WordBlasters.genie.script.action import InputAction
from raylibpy import *
class HandleQuitAction(InputAction):
    def __init__(self, priority):
        super().__init__(priority)
        # self._keyboard_service = keyboard_service
        self._ship = None
    
    def execute(self, actors, actions, clock, callback):
        """
            This action handles the quit action
        """
        # If the user clicked the "X" symbol, end the game
        if window_should_close():
            callback.on_stop()
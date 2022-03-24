from raylibpy import *
from WordBlasters.genie.services.constants.mouse import *

"""
    This map maps the Genie consant id of each mouse button to its partner in the Raylib framework.
    Some of the constants defined above are not found in this map because Raylib does not support
    such mouse buttons.
"""
mouse_map = {
    LEFT : MOUSE_LEFT_BUTTON, 
    MIDDLE : MOUSE_MIDDLE_BUTTON,    # index for Middle mouse
    RIGHT : MOUSE_RIGHT_BUTTON,     # index for Right mouse

    # If mouse has more than 3 buttons:
    # EXTRA1 : MOUSE_EXTRA_BUTTON,
    
    # SIDE : MOUSE_BUTTON_SIDE,
    # FORWARD : MOUSE_BUTTON_FORWARD,
    # BACK : MOUSE_BUTTON_BACK
}
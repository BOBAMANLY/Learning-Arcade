from WordBlasters.genie.script.action import UpdateAction

LARGE_SIZE = (40, 55)

class MoveActorsAction(UpdateAction):
    def __init__(self, priority, physics_service):
        super().__init__(priority=priority)
        self._physics_service = physics_service
        self._window_size = (1000, 1000)

    def execute(self, actors, actions, clock, callback):
        """
            This action:
                - Moves all the actors according to its velocity (including the ship)
                - Rotates all the actors based on its rotational velocity
        """
        self._ship_4 = actors.get_first_actor("ship_4")

        # Get the closest astroid direction
        if len(actors.get_actors("astroids")) != 0:
            min_x = 10000
            for actor in actors.get_actors("astroids"):
                if actor.get_x() < min_x:
                    min_x = actor.get_x()
                    closest_astroid = actor

            closest_astroid_start_y = closest_astroid.get_start_y()

            # pos_1 = LARGE_SIZE[0] * 3
            # pos_2 = self._window_size[1] / 3
            # pos_3 = self._window_size[1] / 2
            # pos_4 = (self._window_size[1] / 3) * 2
            # pos_5 = self._window_size[1]

            if closest_astroid_start_y == self._window_size[1] / 2 :
                self._ship_4.set_rotation(270)
            elif closest_astroid_start_y == (self._window_size[1] / 3) * 2:
                self._ship_4.set_rotation(280)
            elif closest_astroid_start_y == LARGE_SIZE[0] * 3:
                self._ship_4.set_rotation(250)
            elif closest_astroid_start_y == self._window_size[1] / 3:
                self._ship_4.set_rotation(261)
            elif closest_astroid_start_y == self._window_size[1]:
                self._ship_4.set_rotation(300)
            

        self._physics_service.move_actors(actors.get_all_actors())
        self._physics_service.rotate_actors(actors.get_all_actors())

    
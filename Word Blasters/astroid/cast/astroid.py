from astroid.cast.HasLifeActor import HasLifeActor

class Astroid(HasLifeActor):
    def __init__(self, path: str,
                health_bar_y_offset: int,
                health_bar_height: int = 5,

                width: int = 0, 
                height: int = 0, 
                
                x: float = 0, 
                y: float = 0, 
                
                vx: float = 0, 
                vy: float = 0, 
                
                rotation: float = 0, 
                rotation_vel: float = 0,
                
                points: int = 0,
                max_hp: int = 0,
                show_text_health : bool = False,
                letter: str = "",
                has_missle: bool = False,
                start_pos_y: float = 0,):

        super().__init__(path,
                        health_bar_y_offset=health_bar_y_offset,
                        health_bar_height=health_bar_height,
                        
                        width=width, 
                        height=height, 
                        
                        x=x, 
                        y=y, 
                        
                        vx=vx, 
                        vy=vy, 
                        
                        rotation=rotation, 
                        rotation_vel=rotation_vel,
                        max_hp=max_hp,
                        show_text_health=show_text_health)

        self._points = points
        self.letter= letter
        self._start_pos_y = start_pos_y
        self.has_missle = has_missle

    def set_points(self, points):
        self._points = points
    
    def get_point(self):
        return self._points

    def set_letter(self, letter):
        self.letter = letter

    def get_letter(self):
        return self.letter

    def set_start_y(self, start_pos_y):
        self._start_pos_y = start_pos_y

    def get_start_y(self):
        return self._start_pos_y

    def set_has_missle(self, has_missle):
        self.has_missle = has_missle

    def get_has_missle(self):
        return self.has_missle

    



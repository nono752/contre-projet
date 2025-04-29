import arcade

class IFrame:
    duration: float
    is_active: bool

    def __init__(self, duration: float):
        self.duration = duration
        self.is_active = False
    
    def start(self) -> None:
        self.is_active = True
        arcade.schedule_once(lambda dt: setattr(self, "is_active", False), self.duration)
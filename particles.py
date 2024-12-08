from Particle import Particle
from Colors import *


class Electron(Particle) :
    def __init__(self, x, y):
        self.color = BLUE
        self.colors = [BLUE, WHITE]
        self.radius = 3
        self.electric_charge = -1
        self.mass = 1
        super().__init__(x, y)

class Proton(Particle) :
    def __init__(self, x, y):
        self.color = RED
        self.colors = [RED, ORANGE]
        self.radius = 6
        self.electric_charge = +1
        self.mass = 10
        super().__init__(x, y)

class Neutron(Particle) :
    def __init__(self, x, y):
        self.color = DARK_GRAY
        self.colors = [DARK_GRAY, LIGHT_GRAY]
        self.radius = 5
        self.electric_charge = 0
        self.mass = 8
        super().__init__(x, y)
        
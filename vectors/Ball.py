class Ball:
    def __init__(self, pos = (0.,0.), vel =(0.,0.), radius=5):
        self.pos = pos
        self.vel = vel
        self.radius = radius
    def __repr__(self):
        return f'{self.pos, self.vel}'

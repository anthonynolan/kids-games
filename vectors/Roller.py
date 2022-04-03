class Roller:
    def __init__(self, screen_dims):
        self.screen_dims = screen_dims

    def check_bounds(self):
        for dim in [0, 1]:
            if self.pos[dim] > self.screen_dims[dim] - self.radius:
                self.pos[dim] = 0 + self.radius

            if self.pos[dim] < 0 + self.radius:
                self.pos[dim] = self.screen_dims[dim] - self.radius

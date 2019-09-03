import pygame
import poisson_disc_sampling.pd_sampling as pd_samp
from visualize import SampleDrawing


class PoissonDist(SampleDrawing):

    def __init__(self, width, height, n, radius, max_sample=30):
        super().__init__(width, height)
        self.n = n
        self.radius = radius
        self.max_sample = max_sample
        self.points = pd_samp.generate_math(n=self.n, radius=radius, width=width,
                                            height=height, k=self.max_sample)
        self.half_rad = int(self.radius/2)

        pygame.display.set_caption("Poisson Disc Sampling")

    def visualize(self):
        """
        Draws the points to the window.
        :return: None
        """
        for pt in self.points:
            pt = (int(pt[0]), int(pt[1]))
            pygame.draw.circle(self.win, (255, 255, 255), pt, max(1, int(self.half_rad/100)), 0)
        pygame.display.update()


if __name__ == "__main__":
    import math
    dist = PoissonDist(width=800, height=600, n=10000, radius=5*math.sqrt(2))
    dist.draw()

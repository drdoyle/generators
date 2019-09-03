import pygame
import poisson_disc_sampling.pd_sampling as pd_samp
from visualize import SampleDrawing


class PoissonDist(SampleDrawing):

    def __init__(self, width, height):
        super().__init__(width, height)

        self.n = "Sample not yet generated."
        self.radius = "Sample not yet generated."
        self.half_rad = "Sample not yet generated."
        self.max_sample = "Sample not yet generated."
        self.points = "Sample not yet generated."

    def generate(self, n, radius, max_sample=30):
        self.n = n
        self.radius = radius
        self.half_rad = int(self.radius / 2)
        self.max_sample = max_sample
        self.points = pd_samp.generate_poisson_sampling(num_points=self.n, radius=self.radius, width=self.width,
                                                        height=self.height, max_sample=self.max_sample)


    def visualize(self):
        """
        Draws the points to the window.
        :return: None
        """

        pygame.display.set_caption("Poisson Disc Sampling")
        for pt in self.points:
            pt = (int(pt[0]), int(pt[1]))
            pygame.draw.circle(self.win, (255, 255, 255), pt, max(1, int(self.half_rad/100)), 0)
        pygame.display.update()


if __name__ == "__main__":
    import math
    dist = PoissonDist(width=800, height=600)
    dist.generate(n=10000, radius=5*math.sqrt(2))
    dist.draw()

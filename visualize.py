import pygame


class SampleDrawing:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.win = None

    def draw(self):
        running = True
        self.win = pygame.display.set_mode((self.width, self.height))

        bg_color = (0, 0, 0)
        self.win.fill(bg_color)
        self.visualize()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()

    def visualize(self):
        pass

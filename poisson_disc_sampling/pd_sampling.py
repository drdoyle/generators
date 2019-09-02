
try:
    import pygame
except ImportError:
    # Don't have the visualization stuff, so we can just run the creation but not visuals
    raise ImportWarning("Could not load package: pygame, so no visualization options available.")
else:
    from .visualize import draw_PD

class
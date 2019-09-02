import math
import random

# try:
#     import pygame
# except ImportError:
#     # Don't have the visualization stuff, so we can just run the creation but not visuals
#     raise ImportWarning("Could not load package: pygame, so no visualization options available.")
# else:
#     from visualize import draw_pd

try:
    import numpy as np
except ImportError:
    # Don't have numpy, so we can't use numpy arrays
    NP_LOAD = False
    raise ImportWarning("Could not load package: numpy, using base data structures.")
else:
    NP_LOAD = True


def generate_poisson_sampling(num_points, radius, width, height,
                              max_sample=30):
    if NP_LOAD:  # if we can do this with numpy, use the generate_np function
        points = generate_np(num_points, radius, width, height, max_sample)
    else:
        points = generate_math(num_points, radius, width, height, max_sample)
    return points


def generate_math(N, radius, width, height, k=30):
    side_length = radius / math.sqrt(2)
    n_w = int(math.ceil(width / side_length))
    n_h = int(math.ceil(height / side_length))
    points = []
    generators = []
    grid = []
    for i in range(n_w): # grid[x][y]
        grid.append([-1] * n_h)

    twopi = math.pi * 2 # sticking this here because we reference it a lot but don't want to multiply by 2 a bunch

    # step 1: create a first point
    new_pt = (random.random()*width, random.random()*height)
    points.append(new_pt)
    generators.append(new_pt)
    i = int(new_pt[0] // n_w)
    j = int(new_pt[1] // n_h)
    grid[i][j] = 0
    num_pt = 0

    # step 2 through 2N-1: try to make new points
    while num_pt < N:
        center = random.choice(generators)
        attempts_remaining = k
        while attempts_remaining > 0:
            # generate a random point in the annulus around the center, and compute its cell indices
            d = (random.random() + 1) * radius
            theta = random.random() * twopi
            new_pt = (center[0] + d * math.cos(theta), center[1] + d * math.sin(theta))
            # check to see if the pt is inside the area
            if not 0 <= new_pt[0] < width and 0 <= new_pt[1] < height:
                # if its outside, immediately fail the point
                attempts_remaining -= 1
            else:
                # find the cell the point is in and the indices for nearby cells
                pt_cell = (int(new_pt[0] // n_w), int(new_pt[1] // n_w))
                left = max(0, pt_cell[0] - 2)
                right = min(n_w, pt_cell[0] + 2)
                up = max(0, pt_cell[1] - 2)
                down = min(n_h, pt_cell[1] + 2)

                # iterate through nearby cells which are filled and check if any of them are too close
                filled_cells = [grid[i][j] for i in range(left, right) for j in range(up, down) if grid[i][j] > -1]
                success = True
                for cell in filled_cells:
                    pt = points[cell]  # grab the point coordinates from the list of points
                    if (pt[0] - new_pt[0])**2 + (pt[1] - new_pt[1])**2 < radius*radius:  # check square distance
                        success = False
                if success:  # pt is far from every pt in the nearby cells
                    grid[pt_cell[0]][pt_cell[1]] = num_pt
                    num_pt += 1
                    points.append(new_pt)
                    generators.append(new_pt)
                    break  # successful pt, don't continue generating the rest of the k-many pts
                else:
                    attempts_remaining -= 1  # we failed to create a point that was far enough, so we burn one attempt

        if attempts_remaining == 0:   # if we used all k-many attempts and failed every one
            generators.remove(center)  # remove the center if we tried and failed to place a point k times in a row

    return points


def generate_np(N, r, width, height, k=30):
    points =[]
    return points
import pygame
import numpy as np
import math
import utils

class Ship:
    def __init__(self, x, y, surface):
        # Position of the tip of the ship
        self.pos = np.array([x, y])
        # Rotation angle of the ship relative to the tip of the ship
        self.angle = 0.0
        # Additional properties goes here:

        # Leave the rest of these properties
        self.surface = surface
        self.radius = 20
        self.color = (0, 0, 0)
        self.collided = False

    # Update properties of the ship
    def update(self, mouse_pos, asteroids, game_status):
        # Action required!

        distance = np.array([mouse_pos[0] - self.pos[0], mouse_pos[1] - self.pos[1]]) # The distance between the two x and two y coords
        dxy = math.hypot(distance[0], distance[1]) # The straight line made using the distance variable

        # Allows the speed to be dynamic, based on the distance from the cursor
        speed = 0.05 * dxy

        # Set position of ship based on given parameters
        # The if condition stops the ship jittering when reaching the mouse's position
        direction = np.array([(speed) * math.sin(self.angle), 
                                (speed) * math.cos(self.angle)])
        
        if dxy > 0:           
            self.pos += direction


        # Determines the angle needed to move the ship to the cursor for the next update() loop
        self.angle = np.arctan2(distance[0], distance[1])

        # Leave the rest of the code
        # Check for collision
        if game_status == "started":
            self.collision(asteroids, game_status)

    # Draw the ship onto the canvas
    def draw(self):
        p1 = np.array(utils.rotate((0, 0), self.angle)) + self.pos
        p2 = np.array(utils.rotate((40, 20), self.angle)) + self.pos
        p3 = np.array(utils.rotate((30, 0), self.angle)) + self.pos
        p4 = np.array(utils.rotate((40, -20), self.angle)) + self.pos

        pygame.draw.polygon(
            self.surface,
            self.color,
            [p1, p2, p3, p4]
        )

    # Detect whether ship has collided with an asteroid
    def collision(self, asteroids, game_status):
        for asteroid in asteroids:
            if np.linalg.norm(asteroid.pos - self.pos) < (asteroid.radius + self.radius):
                self.color = (255, 0, 0)
                self.collided = True
                break





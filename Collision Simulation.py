import pygame

pygame.init()

WIDTH = 1000
HEIGHT = 600

PARTICLE_X = 200
PARTICLE_y = 250
NUCLEUS_x = 500
NUCLEUS_y = 195
VEL = 1
PARTICLE_MASS = 5
NUCLEUS_MASS = 300

PARTICLE_VELOCITY = 40
NUCLEUS_VELOCITY = 0

RED = pygame.Color(255, 0, 0)

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collsion Visulization")

# Particle shape############
PARTICLE_RADIUS = 10
PARTICLE_SIZE_VALUE = PARTICLE_RADIUS * 2
PARTICLE_SIZE = (PARTICLE_SIZE_VALUE, PARTICLE_SIZE_VALUE)

particle = pygame.Surface(PARTICLE_SIZE)
pygame.draw.circle(particle, RED, (PARTICLE_RADIUS, PARTICLE_RADIUS), PARTICLE_RADIUS,0)
##############################


# NUCLEUS shape##############
NUCLEUS_RADIUS = 65
NUCLEUS_SIZE_VALUE = NUCLEUS_RADIUS * 2
NUCLEUS_SIZE = (NUCLEUS_SIZE_VALUE, NUCLEUS_SIZE_VALUE)

nucleus = pygame.Surface(NUCLEUS_SIZE)
pygame.draw.circle(nucleus, RED, (NUCLEUS_RADIUS, NUCLEUS_RADIUS), NUCLEUS_RADIUS,0)
##############################

collsion = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()

    if (PARTICLE_X < NUCLEUS_x -PARTICLE_RADIUS*2) and not collsion:
    	PARTICLE_X += VEL	
    else:
        collsion = True
        NUCLEUS_VELOCITY_UPDATED = ((2*PARTICLE_MASS)/(PARTICLE_MASS+NUCLEUS_MASS)) * PARTICLE_VELOCITY
        PARTICLE_VELOCITY_UPDATED = ((PARTICLE_MASS-NUCLEUS_MASS)/(PARTICLE_MASS+NUCLEUS_MASS)) * PARTICLE_VELOCITY
        if PARTICLE_X < WIDTH - PARTICLE_RADIUS*2 and PARTICLE_X > 0:
        	PARTICLE_X += (VEL*PARTICLE_VELOCITY_UPDATED) / PARTICLE_VELOCITY
        if NUCLEUS_x < WIDTH - NUCLEUS_RADIUS*2  :	
            NUCLEUS_x += (VEL*NUCLEUS_VELOCITY_UPDATED) / PARTICLE_VELOCITY
        # if PARTICLE_X < 0 and NUCLEUS_x > WIDTH - NUCLEUS_RADIUS*2:
        #     collsion = False
        #     PARTICLE_X = 200
        #     NUCLEUS_x = 500
    SCREEN.fill((0, 0, 0))
    SCREEN.blit(particle, (PARTICLE_X, PARTICLE_y))
    SCREEN.blit(nucleus, (NUCLEUS_x, NUCLEUS_y))
    pygame.display.update()

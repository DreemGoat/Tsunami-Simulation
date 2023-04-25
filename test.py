import pygame 
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 1200, 1000
FPS = 60

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 2000

def create_ball(space, pos):
    ball_mass, ball_radius = 1, 60
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.8
    ball_shape.friction = 0.5
    space.add(ball_body, ball_shape)

segment_shape = pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20)
segment_wall = pymunk.Segment(space.static_body, (0, WIDTH), (WIDTH, HEIGHT), 0)
segment_shape.elasticity = 0.8
segment_wall.elasticity = 0.8
space.add(segment_wall)
space.add(segment_shape)

while True:
    surface.fill(pygame.Color('black'))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        if i.type == pygame.MOUSEBUTTONDOWN:
            if i.button == 1:
                create_ball(space, i.pos)

    space.step(1/FPS)
    space.debug_draw(draw_options)

    pygame.display.flip()
    clock.tick(FPS)
import pygame 
import pymunk.pygame_util
pymunk.pygame_util.positive_y_is_up = False

RES = WIDTH, HEIGHT = 1500, 1000
FPS = 120

pygame.init()
surface = pygame.display.set_mode(RES)
clock = pygame.time.Clock()
draw_options = pymunk.pygame_util.DrawOptions(surface)

space = pymunk.Space()
space.gravity = 0, 2000

def create_ball(space, pos):
    # mass n radius settings
    ball_mass, ball_radius = 18.5, 3
    # inertia
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    # phy
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 1
    ball_shape.friction = 0.5
    space.add(ball_body, ball_shape)

def create_ball1(space, pos):
    # mass n radius settings
    ball_mass, ball_radius = 10**30, 20
    # inertia
    ball_moment = pymunk.moment_for_circle(ball_mass, 0, ball_radius)
    ball_body = pymunk.Body(ball_mass, ball_moment)
    ball_body.position = pos
    # phy
    ball_shape = pymunk.Circle(ball_body, ball_radius)
    ball_shape.elasticity = 0.8
    ball_shape.friction = 0.5
    space.add(ball_body, ball_shape)

# segment_shape = pymunk.Segment(space.static_body, (0, HEIGHT), (WIDTH, HEIGHT), 20)
# segment_shape.elasticity = 0.8
# space.add(segment_shape)

# Define the size of the walls and the position of the corners
wall_thickness = 10
wall_segments = [
    ((0, 0), (WIDTH, 0)),  # top wall
    ((WIDTH, 0), (WIDTH, HEIGHT)),  # right wall
    ((0, HEIGHT), (WIDTH, HEIGHT)),  # bottom wall
    ((-20, HEIGHT), (-20, 0)),  # left wall
    ((0,HEIGHT), (900, 800)), #the incline
    ((900, 800),(WIDTH, 800)) #the beach

]

# Create the walls as static Pymunk bodies
for segment in wall_segments:
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, segment[0], segment[1], wall_thickness)
    space.add(body, shape)

while True:
    surface.fill(pygame.Color('black'))

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 3:
             if i.button == 3:
                create_ball1(space, i.pos)
        elif i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                left_mouse_button_down = True
        elif i.type == pygame.MOUSEBUTTONUP and i.button == 1:
                left_mouse_button_down = False

    # Get the current state of the mouse buttons
    mouse_buttons = pygame.mouse.get_pressed()

    # Check if the left mouse button is being held down
    if mouse_buttons[0] and left_mouse_button_down:
        create_ball(space, i.pos)

    space.step(1/FPS)
    space.debug_draw(draw_options)

    pygame.display.flip()
    clock.tick(FPS)

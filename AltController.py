import pygame

# Initialize
pygame.init()
pygame.joystick.init()

while True:

    pygame.event.get()

    joystick_count = pygame.joystick.get_count()

    # get joystick readings
    for i in range(joystick_count):
        joystick = pygame.joystick.Joystick(i)
        joystick.init()
        xAxisLeft = joystick.get_axis( 0 )
        print xAxisLeft

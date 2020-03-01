"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""
 
import pygame
 
# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)


def draw_circle(x, y, radius, name):
	global screen
	pygame.draw.ellipse(screen, BLUE, [x-radius, y-radius, 2*radius, 2*radius], 0)
	
	textsurface = MY_FONT.render(name, False, GREEN)
	screen.blit(textsurface,(x-int(radius/2)-10,y-15))

# Setup
pygame.init()

MY_FONT = pygame.font.SysFont('Comic Sans MS', 20)
 
# Set the width and height of the screen [width,height]
size = [1200, 700]
screen = pygame.display.set_mode(size)

#Set the game title
pygame.display.set_caption("Ball Bounce")

# Used to manage how fast the screen updates
clock = pygame.time.Clock() 

# Hide the mouse cursor
pygame.mouse.set_visible(0)
 


xspeed = 0
yspeed = 0 	

x = 300
y = 300

done = False


while not done:
	# ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			done = True
				
###########################################################################################
#-----------------------------------------FROM HERE---------------------------------------#
###########################################################################################
	
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT: # When the left key is pressed
				xspeed = -3
			elif event.key == pygame.K_RIGHT: # When the right key is pressed
				xspeed = 3
			elif event.key == pygame.K_DOWN: # When the down key is pressed
				yspeed = 3
			elif event.key == pygame.K_UP: # When the up key is pressed
				yspeed = -3

		
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT: # When the left key is released
				xspeed = 0
			elif event.key == pygame.K_RIGHT: # When the right key is released
				xspeed = 0
			elif event.key == pygame.K_DOWN: # When the down key is released
				yspeed = 0
			elif event.key == pygame.K_UP: # When the up key is released
				yspeed = 0
 
	x = x + xspeed
	y = y + yspeed
 
	screen.fill(WHITE)
	
	draw_circle(x, y, radius=40, name="Cheese")

###########################################################################################
#------------------------------------------TO HERE----------------------------------------#
###########################################################################################

	pygame.display.flip()
	clock.tick(60)
	
pygame.quit()
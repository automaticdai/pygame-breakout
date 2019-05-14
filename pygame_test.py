import pygame

pygame.init()
screen = pygame.display.set_mode((600, 600))

pos_x = 300
pos_y = 500

clock = pygame.time.Clock()

while True:
	for event in pygame.event.get():
		print(event)
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pos_x = pos_x - 20

			if event.key == pygame.K_RIGHT:
				pos_x = pos_x + 20
			
	
	screen.fill((0,0,0))
	pygame.draw.rect(screen, (200, 0, 0), (pos_x, pos_y, 50, 50))
	pygame.display.update()
	clock.tick(60)

	if event.type == pygame.QUIT:
		break
		pygame.quit()

import pygame, random

WIDTH, HEIGHT = 800, 600

WHITE = (255,255,255)
BLACK = (0,0,0)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind")
clock = pygame.time.Clock()

colores = []
colores2 = []
colores_escogidos = []
value = []
game = []

lista_pos_coloresx = [125,170,215,260]
lista_pos_coloresy = [42,78,115,155,195,235,275,315,355,395,435,475,515,550] # 14 elementos
lista_pos_valuex = [311,326]
lista_pos_valuey = [32,42,68,79,105,116,143,155,185,198,225,238,265,278,305,318,345,358,385,398,425,438,465,478,505,518,540,550]

int = 0

def value_colors(a):
	for i in range(4):
		if colores_escogidos[i] == colores[i]:
			val = Value(lista_pos_valuex[i%2], lista_pos_valuey[(4*a+i)//2],0)
			all_sprites.add(val)
			value.append(val)
			colores[i] = "valued"
			colores_escogidos[i] = "pass"
		elif colores_escogidos[i] != colores[i]:
			if colores_escogidos[i] not in colores:
				colores_escogidos[i] = "pass"
	if len(value) == 4:
		if value[0].image == value[1].image == value[2].image == value[3].image == value_images[0]:
			
			tapa.kill()
			screen.blit(background,(0,0))
			all_sprites.update()
			all_sprites.draw(screen)
			pygame.display.flip()
			pause = True
			while pause:
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
					if event.type == pygame.KEYUP:
						pause = False

	for color in colores_escogidos:
		if color == "pass":
			pass
		else: 
			if color in colores:
				val = Value(lista_pos_valuex[(4 -len(value))%2], lista_pos_valuey[2*a + (0 if len(value) < 2 else 1)],1)
				all_sprites.add(val)
				value.append("white")
				colores.remove(color)
			
def draw_text(surface, text, size, x, y):
	font = pygame.font.SysFont("serif", size)
	text_surface = font.render(text, True, (255, 255, 255))
	text_rect = text_surface.get_rect()
	text_rect.midtop = (x, y)
	surface.blit(text_surface, text_rect)

class Tapa(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = pygame.transform.scale(pygame.image.load("img/tapa.png").convert(),(200,30))
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = 191
		self.rect.bottom = 550

	def update(self):
		pass

class Color(pygame.sprite.Sprite):
	def __init__(self, x, y, int):
		super().__init__()
		self.int = int
		if self.int == 0:
			self.image = ficha_images[0]
		elif self.int == 1:
			self.image = ficha_images[1]
		elif self.int == 2:
			self.image = ficha_images[2]
		elif self.int == 3:
			self.image = ficha_images[3]
		elif self.int == 4:
			self.image = ficha_images[4]
		elif self.int == 5:
			self.image = ficha_images[5]
		elif self.int == 6:
			self.image = ficha_images[6]
		else:
			self.image = ficha_images[7]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom = y
		self.on = True

	def update(self):
		self.image.set_colorkey(WHITE)
		if self.on:
			if self.int == 0:
				self.image = ficha_images[0]
			elif self.int == 1:
				self.image = ficha_images[1]
			elif self.int == 2:
				self.image = ficha_images[2]
			elif self.int == 3:
				self.image = ficha_images[3]
			elif self.int == 4:
				self.image = ficha_images[4]
			elif self.int == 5:
				self.image = ficha_images[5]
			elif self.int == 6:
				self.image = ficha_images[6]
			else:
				self.image = ficha_images[7]


class Value(pygame.sprite.Sprite):
	def __init__(self, x, y, int):
		super().__init__()
		self.int = int
		if self.int == 0:
			self.image = value_images[0]
		else:
			self.image = value_images[1]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()
		self.rect.centerx = x
		self.rect.bottom = y


ficha_images = []
ficha_list = ["img/blue.png", "img/red.png", "img/green.png", "img/orange.png", "img/white.png", "img/purple.png", "img/black.png", "img/yellow.png"]
for img in ficha_list:
	ficha_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(25,25)))

value_images = []
value_list = ["img/red2.png", "img/white2.png"]
for img in value_list:
	value_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(15,15)))

def show_go_screen():
	#screen.fill(BLACK)
	draw_text(screen, "Mastermind", 50, WIDTH -220, HEIGHT // 4)
	draw_text(screen, "Adivina la contraseña", 27, WIDTH - 220, HEIGHT // 2)
	draw_text(screen, "Press key to begin", 17, WIDTH - 220, HEIGHT * 3//4)
	pygame.display.flip()
	waiting = True
	while waiting:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			if event.type == pygame.KEYUP:
				waiting = False

# Cargar fondo.
background = pygame.image.load("img/fond.png").convert()

all_sprites = pygame.sprite.Group()

running = True
game_over = True
counter = True

while running:
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

	if game_over:
		all_sprites.empty()
		counter = True
		game_over = False
		show_go_screen()
		colores = []
		colores2 = []
		colores_escogidos = []
		value = []
		game = []
		int = 0
		
		for i in range(4):
			color = Color(lista_pos_coloresx[i], lista_pos_coloresy[-1], random.choice([0,1,2,3,4,5,6,7]))
			colores.append(color.image)
			colores2.append(color.image)
			all_sprites.add(color)
		tapa = Tapa()
		all_sprites.add(tapa)
		game.append(tapa)
		screen.fill((0,0,0))
		screen.blit(background,(0,0))
		all_sprites.update()
		all_sprites.draw(screen)
		pygame.display.flip()

	if counter:

		for i in range(13):
			if counter:
				if i == 12:
					counter = False
				for j in range(4):

					color = Color(lista_pos_coloresx[j], lista_pos_coloresy[(j+4*i)//4], random.choice([0,1,2,3,4,5,6,7]))
					#colores_escogidos.append(color.image)
					all_sprites.add(color)
					while color.on:
						screen.blit(background,(0,0))
						all_sprites.update()
						all_sprites.draw(screen)
						pygame.display.flip()
						for event in pygame.event.get():
							if event.type == pygame.QUIT:
								running = False
								pygame.quit()
							if event.type == pygame.KEYDOWN:
								if event.key == pygame.K_SPACE:
									color.on = False
									colores_escogidos.append(color.image)
									
								elif event.key == pygame.K_UP:
									if color.int > 7:
										color.int = 0 
									else:
										color.int += 1
								elif event.key == pygame.K_DOWN:
									if color.int == 0:
										color.int = 7
									else:
										color.int -= 1
				
				value_colors(int)
				int += 1
				if len(game) == 0:
					counter = False
					game_over = True
				screen.blit(background,(0,0))
				all_sprites.update()
				all_sprites.draw(screen)
				pygame.display.flip()
				colores_escogidos = []
				colores = []
				value = []
				for i in range(4):
					colores.append(colores2[i]) 

	else:
		tapa.kill()
		waiting = True
		while waiting:
			clock.tick(60)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
				if event.type == pygame.KEYUP:
					waiting = False
					game_over = True
		

	clock.tick(60)

	screen.blit(background,(0,0))
	all_sprites.update()
	all_sprites.draw(screen)
	pygame.display.flip()

pygame.quit()
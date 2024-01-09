import pygame,sys, random
from pygame.locals import *

WIDTH = 800
HEIGHT = 600

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mastermind")
clock = pygame.time.Clock()


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
	def __init__(self):
		super().__init__()
		self.image = random.choice(ficha_images)
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()

class Color1(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 42
		
	def update(self):
		pass

class Color2(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 42
		
	def update(self):
		pass

class Color3(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 42
		
	def update(self):
		pass

class Color4(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 42
		
	def update(self):
		pass

class Color1a(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 78
		
	def update(self):
		pass

class Color2a(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 78
		
	def update(self):
		pass

class Color3a(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 78
		
	def update(self):
		pass

class Color4a(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 78
		
	def update(self):
		pass

class Color1b(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 115
		
	def update(self):
		pass

class Color2b(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 115
		
	def update(self):
		pass

class Color3b(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 115
		
	def update(self):
		pass

class Color4b(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 115
		
	def update(self):
		pass

class Color1c(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 155
		
	def update(self):
		pass

class Color2c(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 155
		
	def update(self):
		pass

class Color3c(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 155
		
	def update(self):
		pass

class Color4c(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 155
		
	def update(self):
		pass

class Color1d(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 195
		
	def update(self):
		pass

class Color2d(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 195
		
	def update(self):
		pass

class Color3d(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 195
		
	def update(self):
		pass

class Color4d(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 195
		
	def update(self):
		pass

class Color1e(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 235
		
	def update(self):
		pass

class Color2e(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 235
		
	def update(self):
		pass

class Color3e(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 235
		
	def update(self):
		pass

class Color4e(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 235
		
	def update(self):
		pass

class Color1f(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 275
		
	def update(self):
		pass

class Color2f(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 275
		
	def update(self):
		pass

class Color3f(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 275
		
	def update(self):
		pass

class Color4f(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 275
		
	def update(self):
		pass

class Color1g(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 315
		
	def update(self):
		pass

class Color2g(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 315
		
	def update(self):
		pass

class Color3g(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 315
		
	def update(self):
		pass

class Color4g(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 315
		
	def update(self):
		pass

class Color1h(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 355
		
	def update(self):
		pass

class Color2h(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 355
		
	def update(self):
		pass

class Color3h(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 355
		
	def update(self):
		pass

class Color4h(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 355
		
	def update(self):
		pass

class Color1i(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 395
		
	def update(self):
		pass

class Color2i(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 395
		
	def update(self):
		pass

class Color3i(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 395
		
	def update(self):
		pass

class Color4i(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 395
		
	def update(self):
		pass

class Color1j(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 435
		
	def update(self):
		pass

class Color2j(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 435
		
	def update(self):
		pass

class Color3j(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 435
		
	def update(self):
		pass

class Color4j(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 435
		
	def update(self):
		pass

class Color1k(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 475
		
	def update(self):
		pass

class Color2k(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 475
		
	def update(self):
		pass

class Color3k(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 475
		
	def update(self):
		pass

class Color4k(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 475
		
	def update(self):
		pass

class Color1l(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 515
		
	def update(self):
		pass

class Color2l(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 515
		
	def update(self):
		pass

class Color3l(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 515
		
	def update(self):
		pass

class Color4l(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 515
		
	def update(self):
		pass

class Color1m(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 125
		self.rect.bottom = 550
		
	def update(self):
		pass

class Color2m(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 170
		self.rect.bottom = 550
		
	def update(self):
		pass

class Color3m(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 215
		self.rect.bottom = 550
		
	def update(self):
		pass

class Color4m(Color):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 260
		self.rect.bottom = 550
		
def update(self):
		pass

class Valuer(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = value_images[0]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()

class Value1r(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 32
		
	def update(self):
		pass

class Value2r(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 32
		
	def update(self):
		pass

class Value3r(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 42
		
	def update(self):
		pass

class Value4r(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 42
		
	def update(self):
		pass

class Value1ra(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 68
		
	def update(self):
		pass

class Value2ra(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 68
		
	def update(self):
		pass

class Value3ra(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 79
		
	def update(self):
		pass

class Value4ra(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 79
		
	def update(self):
		pass

class Value1rb(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 105
		
	def update(self):
		pass

class Value2rb(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 105
		
	def update(self):
		pass

class Value3rb(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 116
		
	def update(self):
		pass

class Value4rb(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 116
		
	def update(self):
		pass

class Value1rc(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 143
		
	def update(self):
		pass

class Value2rc(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 143
		
	def update(self):
		pass

class Value3rc(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 155
		
	def update(self):
		pass

class Value4rc(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 155
		
	def update(self):
		pass

class Value1rd(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 185
		
	def update(self):
		pass

class Value2rd(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 185
		
	def update(self):
		pass

class Value3rd(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 198
		
	def update(self):
		pass

class Value4rd(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 198
		
	def update(self):
		pass

class Value1re(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 225
		
	def update(self):
		pass

class Value2re(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 225
		
	def update(self):
		pass

class Value3re(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 238
		
	def update(self):
		pass

class Value4re(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 238
		
	def update(self):
		pass

class Value1rf(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 265
		
	def update(self):
		pass

class Value2rf(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 265
		
	def update(self):
		pass

class Value3rf(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 278
		
	def update(self):
		pass

class Value4rf(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 278
		
	def update(self):
		pass

class Value1rg(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 305
		
	def update(self):
		pass

class Value2rg(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 305
		
	def update(self):
		pass

class Value3rg(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 318
		
	def update(self):
		pass

class Value4rg(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 318
		
	def update(self):
		pass

class Value1rh(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 345
		
	def update(self):
		pass

class Value2rh(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 345
		
	def update(self):
		pass

class Value3rh(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 358
		
	def update(self):
		pass

class Value4rh(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 358
		
	def update(self):
		pass

class Value1ri(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 385
		
	def update(self):
		pass

class Value2ri(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 385
		
	def update(self):
		pass

class Value3ri(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 398
		
	def update(self):
		pass

class Value4ri(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 398
		
	def update(self):
		pass

class Value1rj(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 425
		
	def update(self):
		pass

class Value2rj(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 425
		
	def update(self):
		pass

class Value3rj(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 438
		
	def update(self):
		pass

class Value4rj(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 438
		
	def update(self):
		pass

class Value1rk(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 465
		
	def update(self):
		pass

class Value2rk(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 465
		
	def update(self):
		pass

class Value3rk(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 478
		
	def update(self):
		pass

class Value4rk(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 478
		
	def update(self):
		pass

class Value1rl(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 505
		
	def update(self):
		pass

class Value2rl(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 505
		
	def update(self):
		pass

class Value3rl(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 518
		
	def update(self):
		pass

class Value4rl(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 518
		
	def update(self):
		pass

class Value1rm(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 540
		
	def update(self):
		pass

class Value2rm(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 540
		
	def update(self):
		pass

class Value3rm(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 550
		
	def update(self):
		pass

class Value4rm(Valuer):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 550
		
	def update(self):
		pass

class Valuew(pygame.sprite.Sprite):
	def __init__(self):
		super().__init__()
		self.image = value_images[1]
		self.image.set_colorkey(WHITE)
		self.rect = self.image.get_rect()

class Value1w(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 32
		
	def update(self):
		pass

class Value2w(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 32
		
	def update(self):
		pass

class Value3w(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 42
		
	def update(self):
		pass

class Value4w(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 42
		
	def update(self):
		pass

class Value1wa(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 68
		
	def update(self):
		pass

class Value2wa(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 68
		
	def update(self):
		pass

class Value3wa(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 79
		
	def update(self):
		pass

class Value4wa(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 79
		
	def update(self):
		pass

class Value1wb(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 105
		
	def update(self):
		pass

class Value2wb(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 105
		
	def update(self):
		pass

class Value3wb(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 116
		
	def update(self):
		pass

class Value4wb(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 116
		
	def update(self):
		pass

class Value1wc(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 143
		
	def update(self):
		pass

class Value2wc(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 143
		
	def update(self):
		pass

class Value3wc(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 155
		
	def update(self):
		pass

class Value4wc(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 155
		
	def update(self):
		pass

class Value1wd(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 185
		
	def update(self):
		pass

class Value2wd(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 185
		
	def update(self):
		pass

class Value3wd(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 198
		
	def update(self):
		pass

class Value4wd(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 198
		
	def update(self):
		pass

class Value1we(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 225
		
	def update(self):
		pass

class Value2we(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 225
		
	def update(self):
		pass

class Value3we(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 238
		
	def update(self):
		pass

class Value4we(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 238
		
	def update(self):
		pass

class Value1wf(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 265
		
	def update(self):
		pass

class Value2wf(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 265
		
	def update(self):
		pass

class Value3wf(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 278
		
	def update(self):
		pass

class Value4wf(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 278
		
	def update(self):
		pass

class Value1wg(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 305
		
	def update(self):
		pass

class Value2wg(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 305
		
	def update(self):
		pass

class Value3wg(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 318
		
	def update(self):
		pass

class Value4wg(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 318
		
	def update(self):
		pass

class Value1wh(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 345
		
	def update(self):
		pass

class Value2wh(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 345
		
	def update(self):
		pass

class Value3wh(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 358
		
	def update(self):
		pass

class Value4wh(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 358
		
	def update(self):
		pass

class Value1wi(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 385
		
	def update(self):
		pass

class Value2wi(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 385
		
	def update(self):
		pass

class Value3wi(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 398
		
	def update(self):
		pass

class Value4wi(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 398
		
	def update(self):
		pass

class Value1wj(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 425
		
	def update(self):
		pass

class Value2wj(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 425
		
	def update(self):
		pass

class Value3wj(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 438
		
	def update(self):
		pass

class Value4wj(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 438
		
	def update(self):
		pass

class Value1wk(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 465
		
	def update(self):
		pass

class Value2wk(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 465
		
	def update(self):
		pass

class Value3wk(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 478
		
	def update(self):
		pass

class Value4wk(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 478
		
	def update(self):
		pass

class Value1wl(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 505
		
	def update(self):
		pass

class Value2wl(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 505
		
	def update(self):
		pass

class Value3wl(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 518
		
	def update(self):
		pass

class Value4wl(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 518
		
	def update(self):
		pass

class Value1wm(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 540
		
	def update(self):
		pass

class Value2wm(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 540
		
	def update(self):
		pass

class Value3wm(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 310
		self.rect.bottom = 550
		
	def update(self):
		pass

class Value4wm(Valuew):
	def __init__(self):
		super().__init__()
		self.rect.centerx = 325
		self.rect.bottom = 550
		
	def update(self):
		pass

def test_this(user,master,n):
	for i, user_color in enumerate(user):
		if user_color in master:
			if user_color == master[i]:
				valuenr = Valuenr()
			else:
				valuenw = Valuenw()

ficha_images = []
ficha_list = ["img/blue.png", "img/red.png", "img/green.png", "img/orange.png", "img/white.png", "img/purple.png", "img/black.png", "img/yellow.png"]
for img in ficha_list:
	ficha_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(25,25)))

value_images = []
value_list = ["img/red2.png", "img/white2.png"]
for img in value_list:
	value_images.append(pygame.transform.scale(pygame.image.load(img).convert(),(15,15)))

img1 = ficha_images[0]#blue
img2 = ficha_images[1]#red
img3 = ficha_images[2]#green
img4 = ficha_images[3]#orange
img5 = ficha_images[4]#white
img6 = ficha_images[5]#purple
img7 = ficha_images[6]#black
img8 = ficha_images[7]#yellow

def show_go_screen():
	screen.fill(BLACK)
	draw_text(screen, "Mastermind", 65, WIDTH // 2, HEIGHT / 4)
	draw_text(screen, "Adivina la contraseña", 27, WIDTH // 2, HEIGHT // 2)
	draw_text(screen, "Press key to begin", 17, WIDTH // 2, HEIGHT * 3/4)
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

# Cargar sonidos

all_sprites = pygame.sprite.Group()

# Game Loop
master = []
running = True
game_over = True
switch1 = False
switch2 = False
switch3 = False
switch4 = False
switch5 = False
switch6 = False
switch7 = False
switch8 = False
switch9 = False
switch10 = False
switch11 = False
switch12 = False
switch13 = False
switch14 = False
switch15 = False
switch16 = False
switch17 = False 
switch18 = False
switch19 = False
switch20 = False
switch21 = False
switch22 = False
switch23 = False
switch24 = False
switch25 = False
switch26 = False
switch27 = False
switch28 = False
switch29 = False
switch30 = False
switch31 = False
switch32 = False
switch33 = False
switch34 = False
switch35 = False
switch36 = False
switch37 = False
switch38 = False
switch39 = False
switch40 = False
switch41 = False
switch42 = False
switch43 = False
switch44 = False
switch45 = False
switch46 = False
switch47 = False
switch48 = False
switch49 = False
switch50 = False
switch51 = False
switch52 = False
switch53 = False
switch54 = False
switch55 = False
switch56 = False
switch57 = False
switch58 = False
switch59 = False
switch60 = False
switch61 = False
switch62 = False
switch63 = False
switch64 = False
switch65 = False
switch66 = False
switch67 = False
switch68 = False
switch69 = False
switch70 = False
switch71 = False
switch72 = False
switch73 = False
switch74 = False
switch75 = False
switch76 = False
switch77 = False
switch78 = False
switch79 = False
switch80 = False
switch81 = False
switch82 = False
switch83 = False
switch84 = False
switch85 = False
switch86 = False
switch87 = False
switch88 = False
switch89 = False
switch90 = False
switch91 = False
switch92 = False
switch93 = False
switch94 = False
switch95 = False
switch96 = False
switch97 = False
switch98 = False
switch99 = False
switch100 = False
switch101 = False
switch102 = False
switch103 = False
switch104 = False
switch105 = False
switch106 = False
switch107 = False
switch108 = False
switch109 = False
switch110 = False
switch111 = False
switch112 = False
switch113 = False
switch114 = False
switch115 = False
switch116 = False
switch117 = False
switch118 = False
switch119 = False
switch120 = False
switch121 = False
switch122 = False
switch123 = False
switch124 = False
switch125 = False
switch126 = False
switch127 = False
switch128 = False
switch129 = False
switch130 = False
switch131 = False
switch132 = False
switch133 = False
switch134 = False
switch135 = False
switch136 = False
switch137 = False
switch138 = False
switch139 = False
switch140 = False
switch141 = False
switch142 = False
switch143 = False
switch144 = False
switch145 = False
switch146 = False
switch147 = False
switch148 = False
switch149 = False
switch150 = False
switch151 = False
switch152 = False
switch153 = False
switch154 = False
switch155 = False
switch156 = False
switch157 = False
switch158 = False
switch159 = False
switch160 = False
switch161 = False
switch162 = False
switch163 = False
switch164 = False
switch165 = False
switch166 = False
switch167 = False
switch168 = False
switch169 = False
switch170 = False
switch171 = False
switch172 = False
switch173 = False
switch174 = False
switch175 = False
switch176 = False
switch177 = False
switch178 = False
switch179 = False
switch180 = False
switch181 = False
switch182 = False
switch183 = False
switch184 = False
switch185 = False
switch186 = False
switch187 = False
switch188 = False
switch189 = False
switch190 = False
switch191 = False
switch192 = False
switch193 = False
switch194 = False
switch195 = False
switch196 = False
switch197 = False
switch198 = False
switch199 = False
switch200 = False
switch201 = False
switch202 = False
switch203 = False
switch204 = False
switch205 = False
switch206 = False
switch207 = False
switch208 = False
switch209 = False
switch210 = False
switch211 = False
switch212 = False
switch213 = False
switch214 = False
switch215 = False
switch216 = False
switch217 = False
switch218 = False
switch219 = False
switch220 = False
switch221 = False
switch222 = False
switch223 = False
switch224 = False
switch225 = False
switch226 = False
switch227 = False
switch228 = False
switch229 = False
switch230 = False
switch231 = False
switch232 = False
switch233 = False
switch234 = False
switch235 = False
switch236 = False
switch237 = False
switch238 = False
switch239 = False
switch240 = False
switch241 = False
switch242 = False
switch243 = False
switch244 = False
switch245 = False
switch246 = False
switch247 = False
switch248 = False
switch249 = False
switch250 = False
switch251 = False
switch252 = False
switch253 = False
switch254 = False
switch255 = False
switch256 = False
switch257 = False
switch258 = False
switch259 = False
switch260 = False
switch261 = False
switch262 = False
switch263 = False
switch264 = False
switch265 = False
switch266 = False
switch267 = False
switch268 = False
switch269 = False
switch270 = False
switch271 = False
switch272 = False
switch273 = False
switch274 = False
switch275 = False
switch276 = False
switch277 = False
switch278 = False
switch279 = False
switch280 = False
switch281 = False
switch282 = False
switch283 = False
switch284 = False
switch285 = False
switch286 = False
switch287 = False
switch288 = False
switch289 = False
switch290 = False
switch291 = False
switch292 = False
switch293 = False
switch294 = False
switch295 = False
switch296 = False
switch297 = False
switch298 = False
switch299 = False
switch300 = False
switch301 = False
switch302 = False
switch303 = False
switch304 = False
switch305 = False
switch306 = False
switch307 = False
switch308 = False
switch309 = False
switch310 = False
switch311 = False
switch312 = False
switch313 = False
switch314 = False
switch315 = False
switch316 = False
switch317 = False
switch318 = False
switch319 = False
switch320 = False
switch321 = False
switch322 = False
switch323 = False
switch324 = False
switch325 = False
switch326 = False
switch327 = False
switch328 = False
switch329 = False
switch330 = False
switch331 = False
switch332 = False
switch333 = False
switch334 = False
switch335 = False
switch336 = False
switch337 = False
switch338 = False
switch339 = False
switch340 = False
switch341 = False
switch342 = False
switch343 = False
switch344 = False
switch345 = False
switch346 = False
switch347 = False
switch348 = False
switch349 = False
switch350 = False
switch351 = False
switch352 = False
switch353 = False
switch354 = False
switch355 = False
switch356 = False
switch357 = False
switch358 = False
switch359 = False
switch360 = False
switch361 = False
switch362 = False
switch363 = False
switch364 = False
switch365 = False
switch366 = False
switch367 = False
switch368 = False
switch369 = False
switch370 = False
switch371 = False
switch372 = False
switch373 = False
switch374 = False
switch375 = False
switch376 = False
switch377 = False
switch378 = False
switch379 = False
switch380 = False
switch381 = False
switch382 = False
switch383 = False
switch384 = False
switch385 = False
switch386 = False
switch387 = False
switch388 = False
switch389 = False
switch390 = False
switch391 = False
switch392 = False
switch393 = False
switch394 = False
switch395 = False
switch396 = False
switch397 = False
switch398 = False
switch399 = False
switch400 = False
switch401 = False
switch402 = False
switch403 = False
switch404 = False
switch405 = False
switch406 = False
switch407 = False
switch408 = False
switch409 = False
switch410 = False
switch411 = False
switch412 = False
switch413 = False
switch414 = False
switch415 = False
switch416 = False
switch417 = False
switch418 = False
switch419 = False
switch420 = False
switch421 = False
switch422 = False
switch423 = False
switch424 = False
switch425 = False
switch426 = False
switch427 = False
switch428 = False
switch429 = False
switch430 = False
switch431 = False
switch432 = False
switch433 = False
switch434 = False
switch435 = False
switch436 = False
switch437 = False
switch438 = False
switch439 = False
switch440 = False
switch441 = False
switch442 = False
switch443 = False
switch444 = False
switch445 = False
switch446 = False
switch447 = False
switch448 = False
switch449 = False
switch450 = False
switch451 = False
switch452 = False
switch453 = False
switch454 = False
switch455 = False
switch456 = False
switch457 = False
switch458 = False
switch459 = False
switch460 = False
switch461 = False
switch462 = False
switch463 = False
switch464 = False
switch465 = False
switch466 = False
switch467 = False
switch468 = False
switch469 = False
switch470 = False
switch471 = False
switch472 = False
switch473 = False
switch474 = False
switch475 = False
switch476 = False
switch477 = False
switch478 = False
switch479 = False
switch480 = False
switch481 = False


while running:
	# Keep loop running at the right speed
	clock.tick(60)
	# Process input (events)
	for event in pygame.event.get():
		# check for closing window
		if event.type == pygame.QUIT:
			running = False
		
		#elif event.type == pygame.KEYDOWN:
			#if event.key == pygame.K_SPACE:
				#pass

		if switch481:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4l.image = img1
					color4l.image.set_colorkey(WHITE)
					switch481 = False
					switch473 = True
				elif event.key == pygame.K_SPACE:
					if color1l.image == color1m.image and color2l.image == color2m.image and color3l.image == color3m.image and color4l.image == color4m.image:
						value1rl = Value1rl()
						value2rl = Value2rl()
						value3rl = Value3rl()
						value4rl = Value4rl()
						all_sprites.add(value1rl, value2rl, value3rl, value4rl)
					
					elif color1l.image != color1m.image and color2l.image != color2m.image and color3l.image != color3m.image and color4l.image != color4m.image:
						pass
					switch481 = False
					tapa.kill()
					#switch38 = True

		if switch480:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4l.image = img8
					color4l.image.set_colorkey(WHITE)
					switch480 = False
					switch481 = True
				elif event.key == pygame.K_SPACE:
					if color1l.image == color1m.image and color2l.image == color2m.image and color3l.image == color3m.image and color4l.image == color4m.image:
						value1rl = Value1rl()
						value2rl = Value2rl()
						value3rl = Value3rl()
						value4rl = Value4rl()
						all_sprites.add(value1rl, value2rl, value3rl, value4rl)
					
					elif color1l.image != color1m.image and color2l.image != color2m.image and color3l.image != color3m.image and color4l.image != color4m.image:
						pass
					switch480 = False
					tapa.kill()
					#switch38 = True
		
		if switch479:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4l.image = img7
					color4l.image.set_colorkey(WHITE)
					switch479 = False
					switch480 = True
				elif event.key == pygame.K_SPACE:
					if color1l.image == color1m.image and color2l.image == color2m.image and color3l.image == color3m.image and color4l.image == color4m.image:
						value1rl = Value1rl()
						value2rl = Value2rl()
						value3rl = Value3rl()
						value4rl = Value4rl()
						all_sprites.add(value1rl, value2rl, value3rl, value4rl)
					
					elif color1l.image != color1m.image and color2l.image != color2m.image and color3l.image != color3m.image and color4l.image != color4m.image:
						pass
					
					switch479 = False
					tapa.kill()
					#switch38 = True
		
		if switch478:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4l.image = img6
					color4l.image.set_colorkey(WHITE)
					switch478 = False
					switch479 = True
				elif event.key == pygame.K_SPACE:
					if color1l.image == color1m.image and color2l.image == color2m.image and color3l.image == color3m.image and color4l.image == color4m.image:
						value1rl = Value1rl()
						value2rl = Value2rl()
						value3rl = Value3rl()
						value4rl = Value4rl()
						all_sprites.add(value1rl, value2rl, value3rl, value4rl)
					
					elif color1l.image != color1m.image and color2l.image != color2m.image and color3l.image != color3m.image and color4l.image != color4m.image:
						pass
					switch478 = False
					tapa.kill()
					#switch38 = True
		
		if switch477:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4l.image = img5
					color4l.image.set_colorkey(WHITE)
					switch477 = False
					switch478 = True
				elif event.key == pygame.K_SPACE:
					if color1l.image == color1m.image and color2l.image == color2m.image and color3l.image == color3m.image and color4l.image == color4m.image:
						value1rl = Value1rl()
						value2rl = Value2rl()
						value3rl = Value3rl()
						value4rl = Value4rl()
						all_sprites.add(value1rl, value2rl, value3rl, value4rl)
					
					elif color1l.image != color1m.image and color2l.image != color2m.image and color3l.image != color3m.image and color4l.image != color4m.image:
						pass
					switch477 = False
					tapa.kill()
					#switch38 = True
		
		if switch476:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4l.image = img4
					color4l.image.set_colorkey(WHITE)
					switch476 = False
					switch477 = True
				elif event.key == pygame.K_SPACE:
					if color1l.image == color1m.image and color2l.image == color2m.image and color3l.image == color3m.image and color4l.image == color4m.image:
						value1rl = Value1rl()
						value2rl = Value2rl()
						value3rl = Value3rl()
						value4rl = Value4rl()
						all_sprites.add(value1rl, value2rl, value3rl, value4rl)
					
					elif color1l.image != color1m.image and color2l.image != color2m.image and color3l.image != color3m.image and color4l.image != color4m.image:
						pass
					switch476 = False
					tapa.kill()
					#switch38 = True
		
		if switch475:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4l.image = img3
					color4l.image.set_colorkey(WHITE)
					switch475 = False
					switch476 = True
				elif event.key == pygame.K_SPACE:
					if color1l.image == color1m.image and color2l.image == color2m.image and color3l.image == color3m.image and color4l.image == color4m.image:
						value1rl = Value1rl()
						value2rl = Value2rl()
						value3rl = Value3rl()
						value4rl = Value4rl()
						all_sprites.add(value1rl, value2rl, value3rl, value4rl)
					
					elif color1l.image != color1m.image and color2l.image != color2m.image and color3l.image != color3m.image and color4l.image != color4m.image:
						pass
					switch475 = False
					tapa.kill()
					#switch38 = True
		
		if switch474:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4l.image = img2
					color4l.image.set_colorkey(WHITE)
					switch474 = False
					switch475 = True
				elif event.key == pygame.K_SPACE:
					if color1l.image == color1m.image and color2l.image == color2m.image and color3l.image == color3m.image and color4l.image == color4m.image:
						value1rl = Value1rl()
						value2rl = Value2rl()
						value3rl = Value3rl()
						value4rl = Value4rl()
						all_sprites.add(value1rl, value2rl, value3rl, value4rl)
					
					elif color1l.image != color1m.image and color2l.image != color2m.image and color3l.image != color3m.image and color4l.image != color4m.image:
						pass
					switch474 = False
					tapa.kill()
					#switch38 = True
		
		if switch473:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4l.image = img1
					color4l.image.set_colorkey(WHITE)
					switch473 = False
					switch474 = True
				elif event.key == pygame.K_SPACE:
					if color1l.image == color1m.image and color2l.image == color2m.image and color3l.image == color3m.image and color4l.image == color4m.image:
						value1rl = Value1rl()
						value2rl = Value2rl()
						value3rl = Value3rl()
						value4rl = Value4rl()
						all_sprites.add(value1rl, value2rl, value3rl, value4rl)
					
					elif color1l.image != color1m.image and color2l.image != color2m.image and color3l.image != color3m.image and color4l.image != color4m.image:
						pass
					switch473 = False
					tapa.kill()
					#switch38 = True

		if switch472:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3l.image = img1
					color3l.image.set_colorkey(WHITE)
					switch472 = False
					switch464 = True
				elif event.key == pygame.K_SPACE:
					color4l = Color4l()
					all_sprites.add(color4l)
					switch472 = False
					switch473 = True		
		
		if switch471:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3l.image = img8
					color3l.image.set_colorkey(WHITE)
					switch471 = False
					switch472 = True
				elif event.key == pygame.K_SPACE:
					color4l = Color4l()
					all_sprites.add(color4l)
					switch471 = False
					switch473 = True
		
		if switch470:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3l.image = img7
					color3l.image.set_colorkey(WHITE)
					switch470 = False
					switch471 = True
				elif event.key == pygame.K_SPACE:
					color4l = Color4l()
					all_sprites.add(color4l)
					switch470 = False
					switch473 = True
		
		if switch469:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3l.image = img6
					color3l.image.set_colorkey(WHITE)
					switch469 = False
					switch470 = True
				elif event.key == pygame.K_SPACE:
					color4l = Color4l()
					all_sprites.add(color4l)
					switch469 = False
					switch473 = True
		
		if switch468:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3l.image = img5
					color3l.image.set_colorkey(WHITE)
					switch468 = False
					switch469 = True
				elif event.key == pygame.K_SPACE:
					color4l = Color4l()
					all_sprites.add(color4l)
					switch468 = False
					switch473 = True
		
		if switch467:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3l.image = img4
					color3l.image.set_colorkey(WHITE)
					switch467 = False
					switch468 = True
				elif event.key == pygame.K_SPACE:
					color4l = Color4l()
					all_sprites.add(color4l)
					switch467 = False
					switch473 = True
		
		if switch466:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3l.image = img3
					color3l.image.set_colorkey(WHITE)
					switch466 = False
					switch467 = True
				elif event.key == pygame.K_SPACE:
					color4l = Color4l()
					all_sprites.add(color4l)
					switch466 = False
					switch473 = True
		
		if switch465:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3l.image = img2
					color3l.image.set_colorkey(WHITE)
					switch465 = False
					switch466 = True
				elif event.key == pygame.K_SPACE:
					color4l = Color4l()
					all_sprites.add(color4l)
					switch465 = False
					switch473 = True


		if switch464:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3l.image = img1
					color3l.image.set_colorkey(WHITE)
					switch464 = False
					switch465 = True
				elif event.key == pygame.K_SPACE:
					color4l = Color4l()
					all_sprites.add(color4l)
					switch464 = False
					switch473 = True

		if switch463:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2l.image = img1
					color2l.image.set_colorkey(WHITE)
					switch463 = False
					switch455 = True
				elif event.key == pygame.K_SPACE:
					color3l = Color3l()
					all_sprites.add(color3l)
					switch463 = False
					switch464 = True

		if switch462:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2l.image = img8
					color2l.image.set_colorkey(WHITE)
					switch462 = False
					switch463 = True
				elif event.key == pygame.K_SPACE:
					color3l = Color3l()
					all_sprites.add(color3l)
					switch462 = False
					switch464 = True
		
		if switch461:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2l.image = img7
					color2l.image.set_colorkey(WHITE)
					switch461 = False
					switch462 = True
				elif event.key == pygame.K_SPACE:
					color3l = Color3l()
					all_sprites.add(color3l)
					switch461 = False
					switch464 = True
		
		if switch460:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2l.image = img6
					color2l.image.set_colorkey(WHITE)
					switch460 = False
					switch461 = True
				elif event.key == pygame.K_SPACE:
					color3l = Color3l()
					all_sprites.add(color3l)
					switch460 = False
					switch464 = True
		
		if switch459:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2l.image = img5
					color2l.image.set_colorkey(WHITE)
					switch459 = False
					switch460 = True
				elif event.key == pygame.K_SPACE:
					color3l = Color3l()
					all_sprites.add(color3l)
					switch459 = False
					switch464 = True
		
		if switch458:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2l.image = img4
					color2l.image.set_colorkey(WHITE)
					switch458 = False
					switch459 = True
				elif event.key == pygame.K_SPACE:
					color3l = Color3l()
					all_sprites.add(color3l)
					switch458 = False
					switch464 = True
		
		if switch457:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2l.image = img3
					color2l.image.set_colorkey(WHITE)
					switch457 = False
					switch458 = True
				elif event.key == pygame.K_SPACE:
					color3l = Color3l()
					all_sprites.add(color3l)
					switch457 = False
					switch464 = True
		
		if switch456:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2l.image = img2
					color2l.image.set_colorkey(WHITE)
					switch456 = False
					switch457 = True
				elif event.key == pygame.K_SPACE:
					color3l = Color3l()
					all_sprites.add(color3l)
					switch456 = False
					switch464 = True

		if switch455:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2l.image = img1
					color2l.image.set_colorkey(WHITE)
					switch455 = False
					switch456 = True
				elif event.key == pygame.K_SPACE:
					color3l = Color3l()
					all_sprites.add(color3l)
					switch455 = False
					switch464 = True

		if switch454:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1l.image = img1
					color1l.image.set_colorkey(WHITE)
					switch454 = False
					switch446 = True
				elif event.key == pygame.K_SPACE:
					color2l = Color2l()
					all_sprites.add(color2l)
					switch454 = False
					switch455 = True

		if switch453:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1l.image = img8
					color1l.image.set_colorkey(WHITE)
					switch453 = False
					switch454 = True
				elif event.key == pygame.K_SPACE:
					color2l = Color2l()
					all_sprites.add(color2l)
					switch453 = False
					switch455 = True

		if switch452:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1l.image = img7
					color1l.image.set_colorkey(WHITE)
					switch452 = False
					switch453 = True
				elif event.key == pygame.K_SPACE:
					color2l = Color2l()
					all_sprites.add(color2l)
					switch452 = False
					switch455 = True
		
		if switch451:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1l.image = img6
					color1l.image.set_colorkey(WHITE)
					switch451 = False
					switch452 = True
				elif event.key == pygame.K_SPACE:
					color2l = Color2l()
					all_sprites.add(color2l)
					switch451 = False
					switch455 = True
		
		if switch450:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1l.image = img5
					color1l.image.set_colorkey(WHITE)
					switch450 = False
					switch451 = True
				elif event.key == pygame.K_SPACE:
					color2l = Color2l()
					all_sprites.add(color2l)
					switch450 = False
					switch455 = True
		
		if switch449:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1l.image = img4
					color1l.image.set_colorkey(WHITE)
					switch449 = False
					switch450 = True
				elif event.key == pygame.K_SPACE:
					color2l = Color2l()
					all_sprites.add(color2l)
					switch449 = False
					switch455 = True
		
		if switch448:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1l.image = img3
					color1l.image.set_colorkey(WHITE)
					switch448 = False
					switch449 = True
				elif event.key == pygame.K_SPACE:
					color2l = Color2l()
					all_sprites.add(color2l)
					switch448 = False
					switch455 = True
		
		if switch447:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1l.image = img2
					color1l.image.set_colorkey(WHITE)
					switch447 = False
					switch448 = True
				elif event.key == pygame.K_SPACE:
					color2l = Color2l()
					all_sprites.add(color2l)
					switch447 = False
					switch455 = True


		if switch446:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1l.image = img1
					color1l.image.set_colorkey(WHITE)
					switch446 = False
					switch447 = True
				elif event.key == pygame.K_SPACE:
					color2l = Color2l()
					all_sprites.add(color2l)
					switch446 = False
					switch455 = True

		if switch445:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1l = Color1l()
					all_sprites.add(color1l)
					switch445 = False
					switch446 = True
	
		if switch444:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4k.image = img1
					color4k.image.set_colorkey(WHITE)
					switch444 = False
					switch436 = True
				elif event.key == pygame.K_SPACE:
					if color1k.image == color1m.image and color2k.image == color2m.image and color3k.image == color3m.image and color4k.image == color4m.image:
						value1rk = Value1rk()
						value2rk = Value2rk()
						value3rk = Value3rk()
						value4rk = Value4rk()
						all_sprites.add(value1rk, value2rk, value3rk, value4rk)
						tapa.kill()
					
					elif color1k.image != color1m.image and color2k.image != color2m.image and color3k.image != color3m.image and color4k.image != color4m.image:
						pass
					switch444 = False
					switch445 = True

		if switch443:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4k.image = img8
					color4k.image.set_colorkey(WHITE)
					switch443 = False
					switch444 = True
				elif event.key == pygame.K_SPACE:
					if color1k.image == color1m.image and color2k.image == color2m.image and color3k.image == color3m.image and color4k.image == color4m.image:
						value1rk = Value1rk()
						value2rk = Value2rk()
						value3rk = Value3rk()
						value4rk = Value4rk()
						all_sprites.add(value1rk, value2rk, value3rk, value4rk)
						tapa.kill()
					
					elif color1k.image != color1m.image and color2k.image != color2m.image and color3k.image != color3m.image and color4k.image != color4m.image:
						pass
					switch443 = False
					switch445 = True
		
		if switch442:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4k.image = img7
					color4k.image.set_colorkey(WHITE)
					switch442 = False
					switch443 = True
				elif event.key == pygame.K_SPACE:
					if color1k.image == color1m.image and color2k.image == color2m.image and color3k.image == color3m.image and color4k.image == color4m.image:
						value1rk = Value1rk()
						value2rk = Value2rk()
						value3rk = Value3rk()
						value4rk = Value4rk()
						all_sprites.add(value1rk, value2rk, value3rk, value4rk)
						tapa.kill()
					
					elif color1k.image != color1m.image and color2k.image != color2m.image and color3k.image != color3m.image and color4k.image != color4m.image:
						pass
					switch442 = False
					switch445 = True
		
		if switch441:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4k.image = img6
					color4k.image.set_colorkey(WHITE)
					switch441 = False
					switch442 = True
				elif event.key == pygame.K_SPACE:
					if color1k.image == color1m.image and color2k.image == color2m.image and color3k.image == color3m.image and color4k.image == color4m.image:
						value1rk = Value1rk()
						value2rk = Value2rk()
						value3rk = Value3rk()
						value4rk = Value4rk()
						all_sprites.add(value1rk, value2rk, value3rk, value4rk)
						tapa.kill()
					
					elif color1k.image != color1m.image and color2k.image != color2m.image and color3k.image != color3m.image and color4k.image != color4m.image:
						pass
					switch441 = False
					switch445 = True
		
		if switch440:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4k.image = img5
					color4k.image.set_colorkey(WHITE)
					switch440 = False
					switch441 = True
				elif event.key == pygame.K_SPACE:
					if color1k.image == color1m.image and color2k.image == color2m.image and color3k.image == color3m.image and color4k.image == color4m.image:
						value1rk = Value1rk()
						value2rk = Value2rk()
						value3rk = Value3rk()
						value4rk = Value4rk()
						all_sprites.add(value1rk, value2rk, value3rk, value4rk)
						tapa.kill()
					
					elif color1k.image != color1m.image and color2k.image != color2m.image and color3k.image != color3m.image and color4k.image != color4m.image:
						pass
					switch440 = False
					switch445 = True
		
		if switch439:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4k.image = img4
					color4k.image.set_colorkey(WHITE)
					switch439 = False
					switch440 = True
				elif event.key == pygame.K_SPACE:
					if color1k.image == color1m.image and color2k.image == color2m.image and color3k.image == color3m.image and color4k.image == color4m.image:
						value1rk = Value1rk()
						value2rk = Value2rk()
						value3rk = Value3rk()
						value4rk = Value4rk()
						all_sprites.add(value1rk, value2rk, value3rk, value4rk)
						tapa.kill()
					
					elif color1k.image != color1m.image and color2k.image != color2m.image and color3k.image != color3m.image and color4k.image != color4m.image:
						pass
					switch439 = False
					switch445 = True
		
		if switch438:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4k.image = img3
					color4k.image.set_colorkey(WHITE)
					switch438 = False
					switch439 = True
				elif event.key == pygame.K_SPACE:
					if color1k.image == color1m.image and color2k.image == color2m.image and color3k.image == color3m.image and color4k.image == color4m.image:
						value1rk = Value1rk()
						value2rk = Value2rk()
						value3rk = Value3rk()
						value4rk = Value4rk()
						all_sprites.add(value1rk, value2rk, value3rk, value4rk)
						tapa.kill()
					
					elif color1k.image != color1m.image and color2k.image != color2m.image and color3k.image != color3m.image and color4k.image != color4m.image:
						pass
					switch438 = False
					switch445 = True
		
		if switch437:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4k.image = img2
					color4k.image.set_colorkey(WHITE)
					switch437 = False
					switch438 = True
				elif event.key == pygame.K_SPACE:
					if color1k.image == color1m.image and color2k.image == color2m.image and color3k.image == color3m.image and color4k.image == color4m.image:
						value1rk = Value1rk()
						value2rk = Value2rk()
						value3rk = Value3rk()
						value4rk = Value4rk()
						all_sprites.add(value1rk, value2rk, value3rk, value4rk)
						tapa.kill()
					
					elif color1k.image != color1m.image and color2k.image != color2m.image and color3k.image != color3m.image and color4k.image != color4m.image:
						pass
					switch437 = False
					switch445 = True
		
		if switch436:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4k.image = img1
					color4k.image.set_colorkey(WHITE)
					switch436 = False
					switch437 = True
				elif event.key == pygame.K_SPACE:
					if color1k.image == color1m.image and color2k.image == color2m.image and color3k.image == color3m.image and color4k.image == color4m.image:
						value1rk = Value1rk()
						value2rk = Value2rk()
						value3rk = Value3rk()
						value4rk = Value4rk()
						all_sprites.add(value1rk, value2rk, value3rk, value4rk)
						tapa.kill()
					
					elif color1k.image != color1m.image and color2k.image != color2m.image and color3k.image != color3m.image and color4k.image != color4m.image:
						pass
					switch436 = False
					switch445 = True

		if switch435:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3k.image = img1
					color3k.image.set_colorkey(WHITE)
					switch435 = False
					switch427 = True
				elif event.key == pygame.K_SPACE:
					color4k = Color4k()
					all_sprites.add(color4k)
					switch435 = False
					switch436 = True		
		
		if switch434:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3k.image = img8
					color3k.image.set_colorkey(WHITE)
					switch434 = False
					switch435 = True
				elif event.key == pygame.K_SPACE:
					color4k = Color4k()
					all_sprites.add(color4k)
					switch434 = False
					switch436 = True
		
		if switch433:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3k.image = img7
					color3k.image.set_colorkey(WHITE)
					switch433 = False
					switch434 = True
				elif event.key == pygame.K_SPACE:
					color4k = Color4k()
					all_sprites.add(color4k)
					switch433 = False
					switch436 = True
		
		if switch432:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3k.image = img6
					color3k.image.set_colorkey(WHITE)
					switch432 = False
					switch433 = True
				elif event.key == pygame.K_SPACE:
					color4k = Color4k()
					all_sprites.add(color4k)
					switch432 = False
					switch436 = True
		
		if switch431:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3k.image = img5
					color3k.image.set_colorkey(WHITE)
					switch431 = False
					switch432 = True
				elif event.key == pygame.K_SPACE:
					color4k = Color4k()
					all_sprites.add(color4k)
					switch431 = False
					switch436 = True
		
		if switch430:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3k.image = img4
					color3k.image.set_colorkey(WHITE)
					switch430 = False
					switch431 = True
				elif event.key == pygame.K_SPACE:
					color4k = Color4k()
					all_sprites.add(color4k)
					switch430 = False
					switch436 = True
		
		if switch429:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3k.image = img3
					color3k.image.set_colorkey(WHITE)
					switch429 = False
					switch430 = True
				elif event.key == pygame.K_SPACE:
					color4k = Color4k()
					all_sprites.add(color4k)
					switch429 = False
					switch436 = True
		
		if switch428:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3k.image = img2
					color3k.image.set_colorkey(WHITE)
					switch428 = False
					switch429 = True
				elif event.key == pygame.K_SPACE:
					color4k = Color4k()
					all_sprites.add(color4k)
					switch428 = False
					switch436 = True


		if switch427:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3k.image = img1
					color3k.image.set_colorkey(WHITE)
					switch427 = False
					switch428 = True
				elif event.key == pygame.K_SPACE:
					color4k = Color4k()
					all_sprites.add(color4k)
					switch427 = False
					switch436 = True


		if switch426:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2k.image = img1
					color2k.image.set_colorkey(WHITE)
					switch426 = False
					switch418 = True
				elif event.key == pygame.K_SPACE:
					color3k = Color3k()
					all_sprites.add(color3k)
					switch426 = False
					switch427 = True

		if switch425:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2k.image = img8
					color2k.image.set_colorkey(WHITE)
					switch425 = False
					switch426 = True
				elif event.key == pygame.K_SPACE:
					color3k = Color3k()
					all_sprites.add(color3k)
					switch425 = False
					switch427 = True
		
		if switch424:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2k.image = img7
					color2k.image.set_colorkey(WHITE)
					switch424 = False
					switch425 = True
				elif event.key == pygame.K_SPACE:
					color3k = Color3k()
					all_sprites.add(color3k)
					switch424 = False
					switch427 = True
		
		if switch423:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2k.image = img6
					color2k.image.set_colorkey(WHITE)
					switch423 = False
					switch424 = True
				elif event.key == pygame.K_SPACE:
					color3k = Color3k()
					all_sprites.add(color3k)
					switch423 = False
					switch427 = True
		
		if switch422:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2k.image = img5
					color2k.image.set_colorkey(WHITE)
					switch422 = False
					switch423 = True
				elif event.key == pygame.K_SPACE:
					color3k = Color3k()
					all_sprites.add(color3k)
					switch422 = False
					switch427 = True
		
		if switch421:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2k.image = img4
					color2k.image.set_colorkey(WHITE)
					switch421 = False
					switch422 = True
				elif event.key == pygame.K_SPACE:
					color3k = Color3k()
					all_sprites.add(color3k)
					switch421 = False
					switch427 = True
		
		if switch420:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2k.image = img3
					color2k.image.set_colorkey(WHITE)
					switch420 = False
					switch421 = True
				elif event.key == pygame.K_SPACE:
					color3k = Color3k()
					all_sprites.add(color3k)
					switch420 = False
					switch427 = True
		
		if switch419:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2k.image = img2
					color2k.image.set_colorkey(WHITE)
					switch419 = False
					switch420 = True
				elif event.key == pygame.K_SPACE:
					color3k = Color3k()
					all_sprites.add(color3k)
					switch419 = False
					switch427 = True

		if switch418:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2k.image = img1
					color2k.image.set_colorkey(WHITE)
					switch418 = False
					switch419 = True
				elif event.key == pygame.K_SPACE:
					color3k = Color3k()
					all_sprites.add(color3k)
					switch418 = False
					switch427 = True

		if switch417:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1k.image = img1
					color1k.image.set_colorkey(WHITE)
					switch417 = False
					switch409 = True
				elif event.key == pygame.K_SPACE:
					color2k = Color2k()
					all_sprites.add(color2k)
					switch417 = False
					switch418 = True

		if switch416:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1k.image = img8
					color1k.image.set_colorkey(WHITE)
					switch416 = False
					switch417 = True
				elif event.key == pygame.K_SPACE:
					color2k = Color2k()
					all_sprites.add(color2k)
					switch416 = False
					switch418 = True

		if switch415:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1k.image = img7
					color1k.image.set_colorkey(WHITE)
					switch415 = False
					switch416 = True
				elif event.key == pygame.K_SPACE:
					color2k = Color2k()
					all_sprites.add(color2k)
					switch415 = False
					switch418 = True
		
		if switch414:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1k.image = img6
					color1k.image.set_colorkey(WHITE)
					switch414 = False
					switch415 = True
				elif event.key == pygame.K_SPACE:
					color2k = Color2k()
					all_sprites.add(color2k)
					switch414 = False
					switch418 = True
		
		if switch413:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1k.image = img5
					color1k.image.set_colorkey(WHITE)
					switch413 = False
					switch414 = True
				elif event.key == pygame.K_SPACE:
					color2k = Color2k()
					all_sprites.add(color2k)
					switch413 = False
					switch418 = True
		
		if switch412:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1k.image = img4
					color1k.image.set_colorkey(WHITE)
					switch412 = False
					switch413 = True
				elif event.key == pygame.K_SPACE:
					color2k = Color2k()
					all_sprites.add(color2k)
					switch412 = False
					switch418 = True
		
		if switch411:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1k.image = img3
					color1k.image.set_colorkey(WHITE)
					switch411 = False
					switch412 = True
				elif event.key == pygame.K_SPACE:
					color2k = Color2k()
					all_sprites.add(color2k)
					switch411 = False
					switch418 = True
		
		if switch410:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1k.image = img2
					color1k.image.set_colorkey(WHITE)
					switch410 = False
					switch411 = True
				elif event.key == pygame.K_SPACE:
					color2k = Color2k()
					all_sprites.add(color2k)
					switch410 = False
					switch418 = True


		if switch409:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1k.image = img1
					color1k.image.set_colorkey(WHITE)
					switch409 = False
					switch410 = True
				elif event.key == pygame.K_SPACE:
					color2k = Color2k()
					all_sprites.add(color2k)
					switch409 = False
					switch418 = True
		


		if switch408:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1k = Color1k()
					all_sprites.add(color1k)
					switch408 = False
					switch409 = True

		if switch407:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4j.image = img1
					color4j.image.set_colorkey(WHITE)
					switch407 = False
					switch399 = True
				elif event.key == pygame.K_SPACE:
					if color1j.image == color1m.image and color2j.image == color2m.image and color3j.image == color3m.image and color4j.image == color4m.image:
						value1rj = Value1rj()
						value2rj = Value2rj()
						value3rj = Value3rj()
						value4rj = Value4rj()
						all_sprites.add(value1rj, value2rj, value3rj, value4rj)
						tapa.kill()
					
					elif color1j.image != color1m.image and color2j.image != color2m.image and color3j.image != color3m.image and color4j.image != color4m.image:
						pass
					switch407 = False
					switch408 = True

		if switch406:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4j.image = img8
					color4j.image.set_colorkey(WHITE)
					switch406 = False
					switch407 = True
				elif event.key == pygame.K_SPACE:
					if color1j.image == color1m.image and color2j.image == color2m.image and color3j.image == color3m.image and color4j.image == color4m.image:
						value1rj = Value1rj()
						value2rj = Value2rj()
						value3rj = Value3rj()
						value4rj = Value4rj()
						all_sprites.add(value1rj, value2rj, value3rj, value4rj)
						tapa.kill()
					
					elif color1j.image != color1m.image and color2j.image != color2m.image and color3j.image != color3m.image and color4j.image != color4m.image:
						pass
					switch406 = False
					switch408 = True
		
		if switch405:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4j.image = img7
					color4j.image.set_colorkey(WHITE)
					switch405 = False
					switch406 = True
				elif event.key == pygame.K_SPACE:
					if color1j.image == color1m.image and color2j.image == color2m.image and color3j.image == color3m.image and color4j.image == color4m.image:
						value1rj = Value1rj()
						value2rj = Value2rj()
						value3rj = Value3rj()
						value4rj = Value4rj()
						all_sprites.add(value1rj, value2rj, value3rj, value4rj)
						tapa.kill()
					
					elif color1j.image != color1m.image and color2j.image != color2m.image and color3j.image != color3m.image and color4j.image != color4m.image:
						pass
					
					switch405 = False
					switch408 = True
		
		if switch404:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4j.image = img6
					color4j.image.set_colorkey(WHITE)
					switch404 = False
					switch405 = True
				elif event.key == pygame.K_SPACE:
					if color1j.image == color1m.image and color2j.image == color2m.image and color3j.image == color3m.image and color4j.image == color4m.image:
						value1rj = Value1rj()
						value2rj = Value2rj()
						value3rj = Value3rj()
						value4rj = Value4rj()
						all_sprites.add(value1rj, value2rj, value3rj, value4rj)
						tapa.kill()
					
					elif color1j.image != color1m.image and color2j.image != color2m.image and color3j.image != color3m.image and color4j.image != color4m.image:
						pass
					switch404 = False
					switch408 = True
		
		if switch403:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4j.image = img5
					color4j.image.set_colorkey(WHITE)
					switch403 = False
					switch404 = True
				elif event.key == pygame.K_SPACE:
					if color1j.image == color1m.image and color2j.image == color2m.image and color3j.image == color3m.image and color4j.image == color4m.image:
						value1rj = Value1rj()
						value2rj = Value2rj()
						value3rj = Value3rj()
						value4rj = Value4rj()
						all_sprites.add(value1rj, value2rj, value3rj, value4rj)
						tapa.kill()
					
					elif color1j.image != color1m.image and color2j.image != color2m.image and color3j.image != color3m.image and color4j.image != color4m.image:
						pass
					switch403 = False
					switch408 = True
		
		if switch402:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4j.image = img4
					color4j.image.set_colorkey(WHITE)
					switch402 = False
					switch403 = True
				elif event.key == pygame.K_SPACE:
					if color1j.image == color1m.image and color2j.image == color2m.image and color3j.image == color3m.image and color4j.image == color4m.image:
						value1rj = Value1rj()
						value2rj = Value2rj()
						value3rj = Value3rj()
						value4rj = Value4rj()
						all_sprites.add(value1rj, value2rj, value3rj, value4rj)
						tapa.kill()
					
					elif color1j.image != color1m.image and color2j.image != color2m.image and color3j.image != color3m.image and color4j.image != color4m.image:
						pass
					switch402 = False
					switch408 = True
		
		if switch401:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4j.image = img3
					color4j.image.set_colorkey(WHITE)
					switch401 = False
					switch402 = True
				elif event.key == pygame.K_SPACE:
					if color1j.image == color1m.image and color2j.image == color2m.image and color3j.image == color3m.image and color4j.image == color4m.image:
						value1rj = Value1rj()
						value2rj = Value2rj()
						value3rj = Value3rj()
						value4rj = Value4rj()
						all_sprites.add(value1rj, value2rj, value3rj, value4rj)
						tapa.kill()
					
					elif color1j.image != color1m.image and color2j.image != color2m.image and color3j.image != color3m.image and color4j.image != color4m.image:
						pass
					switch401 = False
					switch408 = True
		
		if switch400:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4j.image = img2
					color4j.image.set_colorkey(WHITE)
					switch400 = False
					switch401 = True
				elif event.key == pygame.K_SPACE:
					if color1j.image == color1m.image and color2j.image == color2m.image and color3j.image == color3m.image and color4j.image == color4m.image:
						value1rj = Value1rj()
						value2rj = Value2rj()
						value3rj = Value3rj()
						value4rj = Value4rj()
						all_sprites.add(value1rj, value2rj, value3rj, value4rj)
						tapa.kill()
					
					elif color1j.image != color1m.image and color2j.image != color2m.image and color3j.image != color3m.image and color4j.image != color4m.image:
						pass
					switch400 = False
					switch408 = True
		
		if switch399:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4j.image = img1
					color4j.image.set_colorkey(WHITE)
					switch399 = False
					switch400 = True
				elif event.key == pygame.K_SPACE:
					if color1j.image == color1m.image and color2j.image == color2m.image and color3j.image == color3m.image and color4j.image == color4m.image:
						value1rj = Value1rj()
						value2rj = Value2rj()
						value3rj = Value3rj()
						value4rj = Value4rj()
						all_sprites.add(value1rj, value2rj, value3rj, value4rj)
						tapa.kill()
					
					elif color1j.image != color1m.image and color2j.image != color2m.image and color3j.image != color3m.image and color4j.image != color4m.image:
						pass
					switch399 = False
					switch408 = True

		if switch398:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3j.image = img1
					color3j.image.set_colorkey(WHITE)
					switch398 = False
					switch390 = True
				elif event.key == pygame.K_SPACE:
					color4j = Color4j()
					all_sprites.add(color4j)
					switch398 = False
					switch399 = True		
		
		if switch397:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3j.image = img8
					color3j.image.set_colorkey(WHITE)
					switch397 = False
					switch398 = True
				elif event.key == pygame.K_SPACE:
					color4j = Color4j()
					all_sprites.add(color4j)
					switch397 = False
					switch399 = True
		
		if switch396:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3j.image = img7
					color3j.image.set_colorkey(WHITE)
					switch396 = False
					switch397 = True
				elif event.key == pygame.K_SPACE:
					color4j = Color4j()
					all_sprites.add(color4j)
					switch396 = False
					switch399 = True
		
		if switch395:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3j.image = img6
					color3j.image.set_colorkey(WHITE)
					switch395 = False
					switch396 = True
				elif event.key == pygame.K_SPACE:
					color4j = Color4j()
					all_sprites.add(color4j)
					switch395 = False
					switch399 = True
		
		if switch394:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3j.image = img5
					color3j.image.set_colorkey(WHITE)
					switch394 = False
					switch395 = True
				elif event.key == pygame.K_SPACE:
					color4j = Color4j()
					all_sprites.add(color4j)
					switch394 = False
					switch399 = True
		
		if switch393:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3j.image = img4
					color3j.image.set_colorkey(WHITE)
					switch393 = False
					switch394 = True
				elif event.key == pygame.K_SPACE:
					color4j = Color4j()
					all_sprites.add(color4j)
					switch393 = False
					switch399 = True
		
		if switch392:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3j.image = img3
					color3j.image.set_colorkey(WHITE)
					switch392 = False
					switch393 = True
				elif event.key == pygame.K_SPACE:
					color4j = Color4j()
					all_sprites.add(color4j)
					switch392 = False
					switch399 = True
		
		if switch391:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3j.image = img2
					color3j.image.set_colorkey(WHITE)
					switch391 = False
					switch392 = True
				elif event.key == pygame.K_SPACE:
					color4j = Color4j()
					all_sprites.add(color4j)
					switch391 = False
					switch399 = True


		if switch390:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3j.image = img1
					color3j.image.set_colorkey(WHITE)
					switch390 = False
					switch391 = True
				elif event.key == pygame.K_SPACE:
					color4j = Color4j()
					all_sprites.add(color4j)
					switch390 = False
					switch399 = True

		if switch389:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2j.image = img1
					color2j.image.set_colorkey(WHITE)
					switch389 = False
					switch381 = True
				elif event.key == pygame.K_SPACE:
					color3j = Color3j()
					all_sprites.add(color3j)
					switch389 = False
					switch390 = True

		if switch388:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2j.image = img8
					color2j.image.set_colorkey(WHITE)
					switch388 = False
					switch389 = True
				elif event.key == pygame.K_SPACE:
					color3j = Color3j()
					all_sprites.add(color3j)
					switch388 = False
					switch390 = True
		
		if switch387:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2j.image = img7
					color2j.image.set_colorkey(WHITE)
					switch387 = False
					switch388 = True
				elif event.key == pygame.K_SPACE:
					color3j = Color3j()
					all_sprites.add(color3j)
					switch387 = False
					switch390 = True
		
		if switch386:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2j.image = img6
					color2j.image.set_colorkey(WHITE)
					switch386 = False
					switch387 = True
				elif event.key == pygame.K_SPACE:
					color3j = Color3j()
					all_sprites.add(color3j)
					switch386 = False
					switch390 = True
		
		if switch385:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2j.image = img5
					color2j.image.set_colorkey(WHITE)
					switch385 = False
					switch386 = True
				elif event.key == pygame.K_SPACE:
					color3j = Color3j()
					all_sprites.add(color3j)
					switch385 = False
					switch390 = True
		
		if switch384:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2j.image = img4
					color2j.image.set_colorkey(WHITE)
					switch384 = False
					switch385 = True
				elif event.key == pygame.K_SPACE:
					color3j = Color3j()
					all_sprites.add(color3j)
					switch384 = False
					switch390 = True
		
		if switch383:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2j.image = img3
					color2j.image.set_colorkey(WHITE)
					switch383 = False
					switch384 = True
				elif event.key == pygame.K_SPACE:
					color3j = Color3j()
					all_sprites.add(color3j)
					switch383 = False
					switch390 = True
		
		if switch382:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2j.image = img2
					color2j.image.set_colorkey(WHITE)
					switch382 = False
					switch383 = True
				elif event.key == pygame.K_SPACE:
					color3j = Color3j()
					all_sprites.add(color3j)
					switch382 = False
					switch390 = True

		if switch381:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2j.image = img1
					color2j.image.set_colorkey(WHITE)
					switch381 = False
					switch382 = True
				elif event.key == pygame.K_SPACE:
					color3j = Color3j()
					all_sprites.add(color3j)
					switch381 = False
					switch390 = True

		if switch380:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1j.image = img1
					color1j.image.set_colorkey(WHITE)
					switch380 = False
					switch372 = True
				elif event.key == pygame.K_SPACE:
					color2j = Color2j()
					all_sprites.add(color2j)
					switch380 = False
					switch381 = True

		if switch379:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1j.image = img8
					color1j.image.set_colorkey(WHITE)
					switch379 = False
					switch380 = True
				elif event.key == pygame.K_SPACE:
					color2j = Color2j()
					all_sprites.add(color2j)
					switch379 = False
					switch381 = True

		if switch378:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1j.image = img7
					color1j.image.set_colorkey(WHITE)
					switch378 = False
					switch379 = True
				elif event.key == pygame.K_SPACE:
					color2j = Color2j()
					all_sprites.add(color2j)
					switch378 = False
					switch381 = True
		
		if switch377:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1j.image = img6
					color1j.image.set_colorkey(WHITE)
					switch377 = False
					switch378 = True
				elif event.key == pygame.K_SPACE:
					color2j = Color2j()
					all_sprites.add(color2j)
					switch377 = False
					switch381 = True
		
		if switch376:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1j.image = img5
					color1j.image.set_colorkey(WHITE)
					switch376 = False
					switch377 = True
				elif event.key == pygame.K_SPACE:
					color2j = Color2j()
					all_sprites.add(color2j)
					switch376 = False
					switch381 = True
		
		if switch375:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1j.image = img4
					color1j.image.set_colorkey(WHITE)
					switch375 = False
					switch376 = True
				elif event.key == pygame.K_SPACE:
					color2j = Color2j()
					all_sprites.add(color2j)
					switch375 = False
					switch381 = True
		
		if switch374:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1j.image = img3
					color1j.image.set_colorkey(WHITE)
					switch374 = False
					switch375 = True
				elif event.key == pygame.K_SPACE:
					color2j = Color2j()
					all_sprites.add(color2j)
					switch374 = False
					switch381 = True
		
		if switch373:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1j.image = img2
					color1j.image.set_colorkey(WHITE)
					switch373 = False
					switch374 = True
				elif event.key == pygame.K_SPACE:
					color2j = Color2j()
					all_sprites.add(color2j)
					switch373 = False
					switch381 = True


		if switch372:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1j.image = img1
					color1j.image.set_colorkey(WHITE)
					switch372 = False
					switch373 = True
				elif event.key == pygame.K_SPACE:
					color2j = Color2j()
					all_sprites.add(color2j)
					switch372 = False
					switch381 = True
		


		if switch371:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1j = Color1j()
					all_sprites.add(color1j)
					switch371 = False
					switch372 = True

		if switch370:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4i.image = img1
					color4i.image.set_colorkey(WHITE)
					switch370 = False
					switch362 = True
				elif event.key == pygame.K_SPACE:
					if color1i.image == color1m.image and color2i.image == color2m.image and color3i.image == color3m.image and color4i.image == color4m.image:
						value1ri = Value1ri()
						value2ri = Value2ri()
						value3ri = Value3ri()
						value4ri = Value4ri()
						all_sprites.add(value1ri, value2ri, value3ri, value4ri)
						tapa.kill()
					
					elif color1i.image != color1m.image and color2i.image != color2m.image and color3i.image != color3m.image and color4i.image != color4m.image:
						pass
					switch370 = False
					switch371 = True

		if switch369:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4i.image = img8
					color4i.image.set_colorkey(WHITE)
					switch369 = False
					switch370 = True
				elif event.key == pygame.K_SPACE:
					if color1i.image == color1m.image and color2i.image == color2m.image and color3i.image == color3m.image and color4i.image == color4m.image:
						value1ri = Value1ri()
						value2ri = Value2ri()
						value3ri = Value3ri()
						value4ri = Value4ri()
						all_sprites.add(value1ri, value2ri, value3ri, value4ri)
						tapa.kill()
					
					elif color1i.image != color1m.image and color2i.image != color2m.image and color3i.image != color3m.image and color4i.image != color4m.image:
						pass
					switch369 = False
					switch371 = True
		
		if switch368:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4i.image = img7
					color4i.image.set_colorkey(WHITE)
					switch368 = False
					switch369 = True
				elif event.key == pygame.K_SPACE:
					if color1i.image == color1m.image and color2i.image == color2m.image and color3i.image == color3m.image and color4i.image == color4m.image:
						value1ri = Value1ri()
						value2ri = Value2ri()
						value3ri = Value3ri()
						value4ri = Value4ri()
						all_sprites.add(value1ri, value2ri, value3ri, value4ri)
						tapa.kill()
					
					elif color1i.image != color1m.image and color2i.image != color2m.image and color3i.image != color3m.image and color4i.image != color4m.image:
						pass
					switch368 = False
					switch371 = True
		
		if switch367:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4i.image = img6
					color4i.image.set_colorkey(WHITE)
					switch367 = False
					switch368 = True
				elif event.key == pygame.K_SPACE:
					if color1i.image == color1m.image and color2i.image == color2m.image and color3i.image == color3m.image and color4i.image == color4m.image:
						value1ri = Value1ri()
						value2ri = Value2ri()
						value3ri = Value3ri()
						value4ri = Value4ri()
						all_sprites.add(value1ri, value2ri, value3ri, value4ri)
						tapa.kill()
					
					elif color1i.image != color1m.image and color2i.image != color2m.image and color3i.image != color3m.image and color4i.image != color4m.image:
						pass
					switch367 = False
					switch371 = True
		
		if switch366:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4i.image = img5
					color4i.image.set_colorkey(WHITE)
					switch366 = False
					switch367 = True
				elif event.key == pygame.K_SPACE:
					if color1i.image == color1m.image and color2i.image == color2m.image and color3i.image == color3m.image and color4i.image == color4m.image:
						value1ri = Value1ri()
						value2ri = Value2ri()
						value3ri = Value3ri()
						value4ri = Value4ri()
						all_sprites.add(value1ri, value2ri, value3ri, value4ri)
						tapa.kill()
					
					elif color1i.image != color1m.image and color2i.image != color2m.image and color3i.image != color3m.image and color4i.image != color4m.image:
						pass
					switch366 = False
					switch371 = True
		
		if switch365:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4i.image = img4
					color4i.image.set_colorkey(WHITE)
					switch365 = False
					switch366 = True
				elif event.key == pygame.K_SPACE:
					if color1i.image == color1m.image and color2i.image == color2m.image and color3i.image == color3m.image and color4i.image == color4m.image:
						value1ri = Value1ri()
						value2ri = Value2ri()
						value3ri = Value3ri()
						value4ri = Value4ri()
						all_sprites.add(value1ri, value2ri, value3ri, value4ri)
						tapa.kill()
					
					elif color1i.image != color1m.image and color2i.image != color2m.image and color3i.image != color3m.image and color4i.image != color4m.image:
						pass
					switch365 = False
					switch371 = True
		
		if switch364:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4i.image = img3
					color4i.image.set_colorkey(WHITE)
					switch364 = False
					switch365 = True
				elif event.key == pygame.K_SPACE:
					if color1i.image == color1m.image and color2i.image == color2m.image and color3i.image == color3m.image and color4i.image == color4m.image:
						value1ri = Value1ri()
						value2ri = Value2ri()
						value3ri = Value3ri()
						value4ri = Value4ri()
						all_sprites.add(value1ri, value2ri, value3ri, value4ri)
						tapa.kill()
					
					elif color1i.image != color1m.image and color2i.image != color2m.image and color3i.image != color3m.image and color4i.image != color4m.image:
						pass
					switch364 = False
					switch371 = True
		
		if switch363:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4i.image = img2
					color4i.image.set_colorkey(WHITE)
					switch363 = False
					switch364 = True
				elif event.key == pygame.K_SPACE:
					if color1i.image == color1m.image and color2i.image == color2m.image and color3i.image == color3m.image and color4i.image == color4m.image:
						value1ri = Value1ri()
						value2ri = Value2ri()
						value3ri = Value3ri()
						value4ri = Value4ri()
						all_sprites.add(value1ri, value2ri, value3ri, value4ri)
						tapa.kill()
					
					elif color1i.image != color1m.image and color2i.image != color2m.image and color3i.image != color3m.image and color4i.image != color4m.image:
						pass
					switch363 = False
					switch371 = True
		
		if switch362:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4i.image = img1
					color4i.image.set_colorkey(WHITE)
					switch362 = False
					switch363 = True
				elif event.key == pygame.K_SPACE:
					if color1i.image == color1m.image and color2i.image == color2m.image and color3i.image == color3m.image and color4i.image == color4m.image:
						value1ri = Value1ri()
						value2ri = Value2ri()
						value3ri = Value3ri()
						value4ri = Value4ri()
						all_sprites.add(value1ri, value2ri, value3ri, value4ri)
						tapa.kill()
					
					elif color1i.image != color1m.image and color2i.image != color2m.image and color3i.image != color3m.image and color4i.image != color4m.image:
						pass
					switch362 = False
					switch371 = True

		if switch361:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3i.image = img1
					color3i.image.set_colorkey(WHITE)
					switch361 = False
					switch353 = True
				elif event.key == pygame.K_SPACE:
					color4i = Color4i()
					all_sprites.add(color4i)
					switch361 = False
					switch362 = True		
		
		if switch360:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3i.image = img8
					color3i.image.set_colorkey(WHITE)
					switch360 = False
					switch361 = True
				elif event.key == pygame.K_SPACE:
					color4i = Color4i()
					all_sprites.add(color4i)
					switch360 = False
					switch362 = True
		
		if switch359:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3i.image = img7
					color3i.image.set_colorkey(WHITE)
					switch359 = False
					switch360 = True
				elif event.key == pygame.K_SPACE:
					color4i = Color4i()
					all_sprites.add(color4i)
					switch359 = False
					switch362 = True
		
		if switch358:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3i.image = img6
					color3i.image.set_colorkey(WHITE)
					switch358 = False
					switch359 = True
				elif event.key == pygame.K_SPACE:
					color4i = Color4i()
					all_sprites.add(color4i)
					switch358 = False
					switch362 = True
		
		if switch357:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3i.image = img5
					color3i.image.set_colorkey(WHITE)
					switch357 = False
					switch358 = True
				elif event.key == pygame.K_SPACE:
					color4i = Color4i()
					all_sprites.add(color4i)
					switch357 = False
					switch362 = True
		
		if switch356:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3i.image = img4
					color3i.image.set_colorkey(WHITE)
					switch356 = False
					switch357 = True
				elif event.key == pygame.K_SPACE:
					color4i = Color4i()
					all_sprites.add(color4i)
					switch356 = False
					switch362 = True
		
		if switch355:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3i.image = img3
					color3i.image.set_colorkey(WHITE)
					switch355 = False
					switch356 = True
				elif event.key == pygame.K_SPACE:
					color4i = Color4i()
					all_sprites.add(color4i)
					switch355 = False
					switch362 = True
		
		if switch354:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3i.image = img2
					color3i.image.set_colorkey(WHITE)
					switch354 = False
					switch355 = True
				elif event.key == pygame.K_SPACE:
					color4i = Color4i()
					all_sprites.add(color4i)
					switch354 = False
					switch362 = True


		if switch353:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3i.image = img1
					color3i.image.set_colorkey(WHITE)
					switch353 = False
					switch354 = True
				elif event.key == pygame.K_SPACE:
					color4i = Color4i()
					all_sprites.add(color4i)
					switch353 = False
					switch362 = True

		if switch352:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2i.image = img1
					color2i.image.set_colorkey(WHITE)
					switch352 = False
					switch344 = True
				elif event.key == pygame.K_SPACE:
					color3i = Color3i()
					all_sprites.add(color3i)
					switch352 = False
					switch353 = True

		if switch351:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2i.image = img8
					color2i.image.set_colorkey(WHITE)
					switch351 = False
					switch352 = True
				elif event.key == pygame.K_SPACE:
					color3i = Color3i()
					all_sprites.add(color3i)
					switch351 = False
					switch353 = True
		
		if switch350:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2i.image = img7
					color2i.image.set_colorkey(WHITE)
					switch350 = False
					switch351 = True
				elif event.key == pygame.K_SPACE:
					color3i = Color3i()
					all_sprites.add(color3i)
					switch350 = False
					switch353 = True
		
		if switch349:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2i.image = img6
					color2i.image.set_colorkey(WHITE)
					switch349 = False
					switch350 = True
				elif event.key == pygame.K_SPACE:
					color3i = Color3i()
					all_sprites.add(color3i)
					switch349 = False
					switch353 = True
		
		if switch348:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2i.image = img5
					color2i.image.set_colorkey(WHITE)
					switch348 = False
					switch349 = True
				elif event.key == pygame.K_SPACE:
					color3i = Color3i()
					all_sprites.add(color3i)
					switch348 = False
					switch353 = True
		
		if switch347:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2i.image = img4
					color2i.image.set_colorkey(WHITE)
					switch347 = False
					switch348 = True
				elif event.key == pygame.K_SPACE:
					color3i = Color3i()
					all_sprites.add(color3i)
					switch347 = False
					switch353 = True
		
		if switch346:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2i.image = img3
					color2i.image.set_colorkey(WHITE)
					switch346 = False
					switch347 = True
				elif event.key == pygame.K_SPACE:
					color3i = Color3i()
					all_sprites.add(color3i)
					switch346 = False
					switch353 = True
		
		if switch345:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2i.image = img2
					color2i.image.set_colorkey(WHITE)
					switch345 = False
					switch346 = True
				elif event.key == pygame.K_SPACE:
					color3i = Color3i()
					all_sprites.add(color3i)
					switch345 = False
					switch353 = True

		if switch344:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2i.image = img1
					color2i.image.set_colorkey(WHITE)
					switch344 = False
					switch345 = True
				elif event.key == pygame.K_SPACE:
					color3i = Color3i()
					all_sprites.add(color3i)
					switch344 = False
					switch353 = True

		if switch343:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1i.image = img1
					color1i.image.set_colorkey(WHITE)
					switch343 = False
					switch335 = True
				elif event.key == pygame.K_SPACE:
					color2i = Color2i()
					all_sprites.add(color2i)
					switch343 = False
					switch344 = True

		if switch342:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1i.image = img8
					color1i.image.set_colorkey(WHITE)
					switch342 = False
					switch343 = True
				elif event.key == pygame.K_SPACE:
					color2i = Color2i()
					all_sprites.add(color2i)
					switch342 = False
					switch344 = True

		if switch341:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1i.image = img7
					color1i.image.set_colorkey(WHITE)
					switch341 = False
					switch342 = True
				elif event.key == pygame.K_SPACE:
					color2i = Color2i()
					all_sprites.add(color2i)
					switch341 = False
					switch344 = True
		
		if switch340:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1i.image = img6
					color1i.image.set_colorkey(WHITE)
					switch340 = False
					switch341 = True
				elif event.key == pygame.K_SPACE:
					color2i = Color2i()
					all_sprites.add(color2i)
					switch340 = False
					switch344 = True
		
		if switch339:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1i.image = img5
					color1i.image.set_colorkey(WHITE)
					switch339 = False
					switch340 = True
				elif event.key == pygame.K_SPACE:
					color2i = Color2i()
					all_sprites.add(color2i)
					switch339 = False
					switch344 = True
		
		if switch338:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1i.image = img4
					color1i.image.set_colorkey(WHITE)
					switch338 = False
					switch339 = True
				elif event.key == pygame.K_SPACE:
					color2i = Color2i()
					all_sprites.add(color2i)
					switch338 = False
					switch344 = True
		
		if switch337:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1i.image = img3
					color1i.image.set_colorkey(WHITE)
					switch337 = False
					switch338 = True
				elif event.key == pygame.K_SPACE:
					color2i = Color2i()
					all_sprites.add(color2i)
					switch337 = False
					switch344 = True
		
		if switch336:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1i.image = img2
					color1i.image.set_colorkey(WHITE)
					switch336 = False
					switch337 = True
				elif event.key == pygame.K_SPACE:
					color2i = Color2i()
					all_sprites.add(color2i)
					switch336 = False
					switch344 = True


		if switch335:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1i.image = img1
					color1i.image.set_colorkey(WHITE)
					switch335 = False
					switch336 = True
				elif event.key == pygame.K_SPACE:
					color2i = Color2i()
					all_sprites.add(color2i)
					switch335 = False
					switch344 = True
		


		if switch334:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1i = Color1i()
					all_sprites.add(color1i)
					switch334 = False
					switch335 = True

		if switch333:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4h.image = img1
					color4h.image.set_colorkey(WHITE)
					switch333 = False
					switch325 = True
				elif event.key == pygame.K_SPACE:
					if color1h.image == color1m.image and color2h.image == color2m.image and color3h.image == color3m.image and color4h.image == color4m.image:
						value1rh = Value1rh()
						value2rh = Value2rh()
						value3rh = Value3rh()
						value4rh = Value4rh()
						all_sprites.add(value1rh, value2rh, value3rh, value4rh)
						tapa.kill()
					
					elif color1h.image != color1m.image and color2h.image != color2m.image and color3h.image != color3m.image and color4h.image != color4m.image:
						pass
					switch333 = False
					switch334 = True

		if switch332:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4h.image = img8
					color4h.image.set_colorkey(WHITE)
					switch332 = False
					switch333 = True
				elif event.key == pygame.K_SPACE:
					if color1h.image == color1m.image and color2h.image == color2m.image and color3h.image == color3m.image and color4h.image == color4m.image:
						value1rh = Value1rh()
						value2rh = Value2rh()
						value3rh = Value3rh()
						value4rh = Value4rh()
						all_sprites.add(value1rh, value2rh, value3rh, value4rh)
						tapa.kill()
					
					elif color1h.image != color1m.image and color2h.image != color2m.image and color3h.image != color3m.image and color4h.image != color4m.image:
						pass
					switch332 = False
					switch334 = True
		
		if switch331:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4h.image = img7
					color4h.image.set_colorkey(WHITE)
					switch331 = False
					switch332 = True
				elif event.key == pygame.K_SPACE:
					if color1h.image == color1m.image and color2h.image == color2m.image and color3h.image == color3m.image and color4h.image == color4m.image:
						value1rh = Value1rh()
						value2rh = Value2rh()
						value3rh = Value3rh()
						value4rh = Value4rh()
						all_sprites.add(value1rh, value2rh, value3rh, value4rh)
						tapa.kill()
					
					elif color1h.image != color1m.image and color2h.image != color2m.image and color3h.image != color3m.image and color4h.image != color4m.image:
						pass
					switch331 = False
					switch334 = True
		
		if switch330:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4h.image = img6
					color4h.image.set_colorkey(WHITE)
					switch330 = False
					switch331 = True
				elif event.key == pygame.K_SPACE:
					if color1h.image == color1m.image and color2h.image == color2m.image and color3h.image == color3m.image and color4h.image == color4m.image:
						value1rh = Value1rh()
						value2rh = Value2rh()
						value3rh = Value3rh()
						value4rh = Value4rh()
						all_sprites.add(value1rh, value2rh, value3rh, value4rh)
						tapa.kill()
					
					elif color1h.image != color1m.image and color2h.image != color2m.image and color3h.image != color3m.image and color4h.image != color4m.image:
						pass
					switch330 = False
					switch334 = True
		
		if switch329:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4h.image = img5
					color4h.image.set_colorkey(WHITE)
					switch329 = False
					switch330 = True
				elif event.key == pygame.K_SPACE:
					if color1h.image == color1m.image and color2h.image == color2m.image and color3h.image == color3m.image and color4h.image == color4m.image:
						value1rh = Value1rh()
						value2rh = Value2rh()
						value3rh = Value3rh()
						value4rh = Value4rh()
						all_sprites.add(value1rh, value2rh, value3rh, value4rh)
						tapa.kill()
					
					elif color1h.image != color1m.image and color2h.image != color2m.image and color3h.image != color3m.image and color4h.image != color4m.image:
						pass
					switch329 = False
					switch334 = True
		
		if switch328:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4h.image = img4
					color4h.image.set_colorkey(WHITE)
					switch328 = False
					switch329 = True
				elif event.key == pygame.K_SPACE:
					if color1h.image == color1m.image and color2h.image == color2m.image and color3h.image == color3m.image and color4h.image == color4m.image:
						value1rh = Value1rh()
						value2rh = Value2rh()
						value3rh = Value3rh()
						value4rh = Value4rh()
						all_sprites.add(value1rh, value2rh, value3rh, value4rh)
						tapa.kill()
					
					elif color1h.image != color1m.image and color2h.image != color2m.image and color3h.image != color3m.image and color4h.image != color4m.image:
						pass
					switch328 = False
					switch334 = True
		
		if switch327:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4h.image = img3
					color4h.image.set_colorkey(WHITE)
					switch327 = False
					switch328 = True
				elif event.key == pygame.K_SPACE:
					if color1h.image == color1m.image and color2h.image == color2m.image and color3h.image == color3m.image and color4h.image == color4m.image:
						value1rh = Value1rh()
						value2rh = Value2rh()
						value3rh = Value3rh()
						value4rh = Value4rh()
						all_sprites.add(value1rh, value2rh, value3rh, value4rh)
						tapa.kill()
					
					elif color1h.image != color1m.image and color2h.image != color2m.image and color3h.image != color3m.image and color4h.image != color4m.image:
						pass
					switch327 = False
					switch334 = True
		
		if switch326:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4h.image = img2
					color4h.image.set_colorkey(WHITE)
					switch326 = False
					switch327 = True
				elif event.key == pygame.K_SPACE:
					if color1h.image == color1m.image and color2h.image == color2m.image and color3h.image == color3m.image and color4h.image == color4m.image:
						value1rh = Value1rh()
						value2rh = Value2rh()
						value3rh = Value3rh()
						value4rh = Value4rh()
						all_sprites.add(value1rh, value2rh, value3rh, value4rh)
						tapa.kill()
					
					elif color1h.image != color1m.image and color2h.image != color2m.image and color3h.image != color3m.image and color4h.image != color4m.image:
						pass
					switch326 = False
					switch334 = True
		
		if switch325:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4h.image = img1
					color4h.image.set_colorkey(WHITE)
					switch325 = False
					switch326 = True
				elif event.key == pygame.K_SPACE:
					if color1h.image == color1m.image and color2h.image == color2m.image and color3h.image == color3m.image and color4h.image == color4m.image:
						value1rh = Value1rh()
						value2rh = Value2rh()
						value3rh = Value3rh()
						value4rh = Value4rh()
						all_sprites.add(value1rh, value2rh, value3rh, value4rh)
						tapa.kill()
					
					elif color1h.image != color1m.image and color2h.image != color2m.image and color3h.image != color3m.image and color4h.image != color4m.image:
						pass
					switch325 = False
					switch334 = True

		if switch324:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3h.image = img1
					color3h.image.set_colorkey(WHITE)
					switch324 = False
					switch316 = True
				elif event.key == pygame.K_SPACE:
					color4h = Color4h()
					all_sprites.add(color4h)
					switch324 = False
					switch325 = True		
		
		if switch323:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3h.image = img8
					color3h.image.set_colorkey(WHITE)
					switch323 = False
					switch324 = True
				elif event.key == pygame.K_SPACE:
					color4h = Color4h()
					all_sprites.add(color4h)
					switch323 = False
					switch325 = True
		
		if switch322:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3h.image = img7
					color3h.image.set_colorkey(WHITE)
					switch322 = False
					switch323 = True
				elif event.key == pygame.K_SPACE:
					color4h = Color4h()
					all_sprites.add(color4h)
					switch322 = False
					switch325 = True
		
		if switch321:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3h.image = img6
					color3h.image.set_colorkey(WHITE)
					switch321 = False
					switch322 = True
				elif event.key == pygame.K_SPACE:
					color4h = Color4h()
					all_sprites.add(color4h)
					switch321 = False
					switch325 = True
		
		if switch320:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3h.image = img5
					color3h.image.set_colorkey(WHITE)
					switch320 = False
					switch321 = True
				elif event.key == pygame.K_SPACE:
					color4h = Color4h()
					all_sprites.add(color4h)
					switch320 = False
					switch325 = True
		
		if switch319:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3h.image = img4
					color3h.image.set_colorkey(WHITE)
					switch319 = False
					switch320 = True
				elif event.key == pygame.K_SPACE:
					color4h = Color4h()
					all_sprites.add(color4h)
					switch319 = False
					switch325 = True
		
		if switch318:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3h.image = img3
					color3h.image.set_colorkey(WHITE)
					switch318 = False
					switch319 = True
				elif event.key == pygame.K_SPACE:
					color4h = Color4h()
					all_sprites.add(color4h)
					switch318 = False
					switch325 = True
		
		if switch317:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3h.image = img2
					color3h.image.set_colorkey(WHITE)
					switch317 = False
					switch318 = True
				elif event.key == pygame.K_SPACE:
					color4h = Color4h()
					all_sprites.add(color4h)
					switch317 = False
					switch325 = True


		if switch316:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3h.image = img1
					color3h.image.set_colorkey(WHITE)
					switch316 = False
					switch317 = True
				elif event.key == pygame.K_SPACE:
					color4h = Color4h()
					all_sprites.add(color4h)
					switch316 = False
					switch325 = True

		if switch315:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2h.image = img1
					color2h.image.set_colorkey(WHITE)
					switch315 = False
					switch307 = True
				elif event.key == pygame.K_SPACE:
					color3h = Color3h()
					all_sprites.add(color3h)
					switch315 = False
					switch316 = True

		if switch314:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2h.image = img8
					color2h.image.set_colorkey(WHITE)
					switch314 = False
					switch315 = True
				elif event.key == pygame.K_SPACE:
					color3h = Color3h()
					all_sprites.add(color3h)
					switch314 = False
					switch316 = True
		
		if switch313:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2h.image = img7
					color2h.image.set_colorkey(WHITE)
					switch313 = False
					switch314 = True
				elif event.key == pygame.K_SPACE:
					color3h = Color3h()
					all_sprites.add(color3h)
					switch313 = False
					switch316 = True
		
		if switch312:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2h.image = img6
					color2h.image.set_colorkey(WHITE)
					switch312 = False
					switch313 = True
				elif event.key == pygame.K_SPACE:
					color3h = Color3h()
					all_sprites.add(color3h)
					switch312 = False
					switch316 = True
		
		if switch311:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2h.image = img5
					color2h.image.set_colorkey(WHITE)
					switch311 = False
					switch312 = True
				elif event.key == pygame.K_SPACE:
					color3h = Color3h()
					all_sprites.add(color3h)
					switch311 = False
					switch316 = True
		
		if switch310:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2h.image = img4
					color2h.image.set_colorkey(WHITE)
					switch310 = False
					switch311 = True
				elif event.key == pygame.K_SPACE:
					color3h = Color3h()
					all_sprites.add(color3h)
					switch310 = False
					switch316 = True
		
		if switch309:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2h.image = img3
					color2h.image.set_colorkey(WHITE)
					switch309 = False
					switch310 = True
				elif event.key == pygame.K_SPACE:
					color3h = Color3h()
					all_sprites.add(color3h)
					switch309 = False
					switch316 = True
		
		if switch308:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2h.image = img2
					color2h.image.set_colorkey(WHITE)
					switch308 = False
					switch309 = True
				elif event.key == pygame.K_SPACE:
					color3h = Color3h()
					all_sprites.add(color3h)
					switch308 = False
					switch316 = True

		if switch307:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2h.image = img1
					color2h.image.set_colorkey(WHITE)
					switch307 = False
					switch308 = True
				elif event.key == pygame.K_SPACE:
					color3h = Color3h()
					all_sprites.add(color3h)
					switch307 = False
					switch316 = True

		if switch306:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1h.image = img1
					color1h.image.set_colorkey(WHITE)
					switch306 = False
					switch298 = True
				elif event.key == pygame.K_SPACE:
					color2h = Color2h()
					all_sprites.add(color2h)
					switch306 = False
					switch307 = True

		if switch305:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1h.image = img8
					color1h.image.set_colorkey(WHITE)
					switch305 = False
					switch306 = True
				elif event.key == pygame.K_SPACE:
					color2h = Color2h()
					all_sprites.add(color2h)
					switch305 = False
					switch307 = True

		if switch304:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1h.image = img7
					color1h.image.set_colorkey(WHITE)
					switch304 = False
					switch305 = True
				elif event.key == pygame.K_SPACE:
					color2h = Color2h()
					all_sprites.add(color2h)
					switch304 = False
					switch307 = True
		
		if switch303:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1h.image = img6
					color1h.image.set_colorkey(WHITE)
					switch303 = False
					switch304 = True
				elif event.key == pygame.K_SPACE:
					color2h = Color2h()
					all_sprites.add(color2h)
					switch303 = False
					switch307 = True
		
		if switch302:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1h.image = img5
					color1h.image.set_colorkey(WHITE)
					switch302 = False
					switch303 = True
				elif event.key == pygame.K_SPACE:
					color2h = Color2h()
					all_sprites.add(color2h)
					switch302 = False
					switch307 = True
		
		if switch301:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1h.image = img4
					color1h.image.set_colorkey(WHITE)
					switch301 = False
					switch302 = True
				elif event.key == pygame.K_SPACE:
					color2h = Color2h()
					all_sprites.add(color2h)
					switch301 = False
					switch307 = True
		
		if switch300:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1h.image = img3
					color1h.image.set_colorkey(WHITE)
					switch300 = False
					switch301 = True
				elif event.key == pygame.K_SPACE:
					color2h = Color2h()
					all_sprites.add(color2h)
					switch300 = False
					switch307 = True
		
		if switch299:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1h.image = img2
					color1h.image.set_colorkey(WHITE)
					switch299 = False
					switch300 = True
				elif event.key == pygame.K_SPACE:
					color2h = Color2h()
					all_sprites.add(color2h)
					switch299 = False
					switch307 = True


		if switch298:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1h.image = img1
					color1h.image.set_colorkey(WHITE)
					switch298 = False
					switch299 = True
				elif event.key == pygame.K_SPACE:
					color2h = Color2h()
					all_sprites.add(color2h)
					switch298 = False
					switch307 = True
		


		if switch297:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1h = Color1h()
					all_sprites.add(color1h)
					switch297 = False
					switch298 = True

		if switch296:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4g.image = img1
					color4g.image.set_colorkey(WHITE)
					switch296 = False
					switch288 = True
				elif event.key == pygame.K_SPACE:
					if color1g.image == color1m.image and color2g.image == color2m.image and color3g.image == color3m.image and color4g.image == color4m.image:
						value1rg = Value1rg()
						value2rg = Value2rg()
						value3rg = Value3rg()
						value4rg = Value4rg()
						all_sprites.add(value1rg, value2rg, value3rg, value4rg)
						tapa.kill()
					
					elif color1g.image != color1m.image and color2g.image != color2m.image and color3g.image != color3m.image and color4g.image != color4m.image:
						pass
					switch296 = False
					switch297 = True

		if switch295:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4g.image = img8
					color4g.image.set_colorkey(WHITE)
					switch295 = False
					switch296 = True
				elif event.key == pygame.K_SPACE:
					if color1g.image == color1m.image and color2g.image == color2m.image and color3g.image == color3m.image and color4g.image == color4m.image:
						value1rg = Value1rg()
						value2rg = Value2rg()
						value3rg = Value3rg()
						value4rg = Value4rg()
						all_sprites.add(value1rg, value2rg, value3rg, value4rg)
						tapa.kill()
					
					elif color1g.image != color1m.image and color2g.image != color2m.image and color3g.image != color3m.image and color4g.image != color4m.image:
						pass
					switch295 = False
					switch297 = True
		
		if switch294:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4g.image = img7
					color4g.image.set_colorkey(WHITE)
					switch294 = False
					switch295 = True
				elif event.key == pygame.K_SPACE:
					if color1g.image == color1m.image and color2g.image == color2m.image and color3g.image == color3m.image and color4g.image == color4m.image:
						value1rg = Value1rg()
						value2rg = Value2rg()
						value3rg = Value3rg()
						value4rg = Value4rg()
						all_sprites.add(value1rg, value2rg, value3rg, value4rg)
						tapa.kill()
					
					elif color1g.image != color1m.image and color2g.image != color2m.image and color3g.image != color3m.image and color4g.image != color4m.image:
						pass
					switch294 = False
					switch297 = True
		
		if switch293:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4g.image = img6
					color4g.image.set_colorkey(WHITE)
					switch293 = False
					switch294 = True
				elif event.key == pygame.K_SPACE:
					if color1g.image == color1m.image and color2g.image == color2m.image and color3g.image == color3m.image and color4g.image == color4m.image:
						value1rg = Value1rg()
						value2rg = Value2rg()
						value3rg = Value3rg()
						value4rg = Value4rg()
						all_sprites.add(value1rg, value2rg, value3rg, value4rg)
						tapa.kill()
					
					elif color1g.image != color1m.image and color2g.image != color2m.image and color3g.image != color3m.image and color4g.image != color4m.image:
						pass
					switch293 = False
					switch297 = True
		
		if switch292:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4g.image = img5
					color4g.image.set_colorkey(WHITE)
					switch292 = False
					switch293 = True
				elif event.key == pygame.K_SPACE:
					if color1g.image == color1m.image and color2g.image == color2m.image and color3g.image == color3m.image and color4g.image == color4m.image:
						value1rg = Value1rg()
						value2rg = Value2rg()
						value3rg = Value3rg()
						value4rg = Value4rg()
						all_sprites.add(value1rg, value2rg, value3rg, value4rg)
						tapa.kill()
					
					elif color1g.image != color1m.image and color2g.image != color2m.image and color3g.image != color3m.image and color4g.image != color4m.image:
						pass
					switch292 = False
					switch297 = True
		
		if switch291:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4g.image = img4
					color4g.image.set_colorkey(WHITE)
					switch291 = False
					switch292 = True
				elif event.key == pygame.K_SPACE:
					if color1g.image == color1m.image and color2g.image == color2m.image and color3g.image == color3m.image and color4g.image == color4m.image:
						value1rg = Value1rg()
						value2rg = Value2rg()
						value3rg = Value3rg()
						value4rg = Value4rg()
						all_sprites.add(value1rg, value2rg, value3rg, value4rg)
						tapa.kill()
					
					elif color1g.image != color1m.image and color2g.image != color2m.image and color3g.image != color3m.image and color4g.image != color4m.image:
						pass
					switch291 = False
					switch297 = True
		
		if switch290:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4g.image = img3
					color4g.image.set_colorkey(WHITE)
					switch290 = False
					switch291 = True
				elif event.key == pygame.K_SPACE:
					if color1g.image == color1m.image and color2g.image == color2m.image and color3g.image == color3m.image and color4g.image == color4m.image:
						value1rg = Value1rg()
						value2rg = Value2rg()
						value3rg = Value3rg()
						value4rg = Value4rg()
						all_sprites.add(value1rg, value2rg, value3rg, value4rg)
						tapa.kill()
					
					elif color1g.image != color1m.image and color2g.image != color2m.image and color3g.image != color3m.image and color4g.image != color4m.image:
						pass
					switch290 = False
					switch297 = True
		
		if switch289:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4g.image = img2
					color4g.image.set_colorkey(WHITE)
					switch289 = False
					switch290 = True
				elif event.key == pygame.K_SPACE:
					if color1g.image == color1m.image and color2g.image == color2m.image and color3g.image == color3m.image and color4g.image == color4m.image:
						value1rg = Value1rg()
						value2rg = Value2rg()
						value3rg = Value3rg()
						value4rg = Value4rg()
						all_sprites.add(value1rg, value2rg, value3rg, value4rg)
						tapa.kill()
					
					elif color1g.image != color1m.image and color2g.image != color2m.image and color3g.image != color3m.image and color4g.image != color4m.image:
						pass
					switch289 = False
					switch297 = True
		
		if switch288:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4g.image = img1
					color4g.image.set_colorkey(WHITE)
					switch288 = False
					switch289 = True
				elif event.key == pygame.K_SPACE:
					if color1g.image == color1m.image and color2g.image == color2m.image and color3g.image == color3m.image and color4g.image == color4m.image:
						value1rg = Value1rg()
						value2rg = Value2rg()
						value3rg = Value3rg()
						value4rg = Value4rg()
						all_sprites.add(value1rg, value2rg, value3rg, value4rg)
						tapa.kill()
					
					elif color1g.image != color1m.image and color2g.image != color2m.image and color3g.image != color3m.image and color4g.image != color4m.image:
						pass
					switch288 = False
					switch297 = True

		if switch287:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3g.image = img1
					color3g.image.set_colorkey(WHITE)
					switch287 = False
					switch279 = True
				elif event.key == pygame.K_SPACE:
					color4g = Color4g()
					all_sprites.add(color4g)
					switch287 = False
					switch288 = True		
		
		if switch286:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3g.image = img8
					color3g.image.set_colorkey(WHITE)
					switch286 = False
					switch287 = True
				elif event.key == pygame.K_SPACE:
					color4g = Color4g()
					all_sprites.add(color4g)
					switch286 = False
					switch288 = True
		
		if switch285:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3g.image = img7
					color3g.image.set_colorkey(WHITE)
					switch285 = False
					switch286 = True
				elif event.key == pygame.K_SPACE:
					color4g = Color4g()
					all_sprites.add(color4g)
					switch285 = False
					switch288 = True
		
		if switch284:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3g.image = img6
					color3g.image.set_colorkey(WHITE)
					switch284 = False
					switch285 = True
				elif event.key == pygame.K_SPACE:
					color4g = Color4g()
					all_sprites.add(color4g)
					switch284 = False
					switch288 = True
		
		if switch283:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3g.image = img5
					color3g.image.set_colorkey(WHITE)
					switch283 = False
					switch284 = True
				elif event.key == pygame.K_SPACE:
					color4g = Color4g()
					all_sprites.add(color4g)
					switch283 = False
					switch288 = True
		
		if switch282:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3g.image = img4
					color3g.image.set_colorkey(WHITE)
					switch282 = False
					switch283 = True
				elif event.key == pygame.K_SPACE:
					color4g = Color4g()
					all_sprites.add(color4g)
					switch282 = False
					switch288 = True
		
		if switch281:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3g.image = img3
					color3g.image.set_colorkey(WHITE)
					switch281 = False
					switch282 = True
				elif event.key == pygame.K_SPACE:
					color4g = Color4g()
					all_sprites.add(color4g)
					switch281 = False
					switch288 = True
		
		if switch280:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3g.image = img2
					color3g.image.set_colorkey(WHITE)
					switch280 = False
					switch281 = True
				elif event.key == pygame.K_SPACE:
					color4g = Color4g()
					all_sprites.add(color4g)
					switch280 = False
					switch288 = True


		if switch279:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3g.image = img1
					color3g.image.set_colorkey(WHITE)
					switch279 = False
					switch280 = True
				elif event.key == pygame.K_SPACE:
					color4g = Color4g()
					all_sprites.add(color4g)
					switch279 = False
					switch288 = True

		if switch278:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2g.image = img1
					color2g.image.set_colorkey(WHITE)
					switch278 = False
					switch270 = True
				elif event.key == pygame.K_SPACE:
					color3g = Color3g()
					all_sprites.add(color3g)
					switch278 = False
					switch279 = True

		if switch277:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2g.image = img8
					color2g.image.set_colorkey(WHITE)
					switch277 = False
					switch278 = True
				elif event.key == pygame.K_SPACE:
					color3g = Color3g()
					all_sprites.add(color3g)
					switch277 = False
					switch279 = True
		
		if switch276:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2g.image = img7
					color2g.image.set_colorkey(WHITE)
					switch276 = False
					switch277 = True
				elif event.key == pygame.K_SPACE:
					color3g = Color3g()
					all_sprites.add(color3g)
					switch276 = False
					switch279 = True
		
		if switch275:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2g.image = img6
					color2g.image.set_colorkey(WHITE)
					switch275 = False
					switch276 = True
				elif event.key == pygame.K_SPACE:
					color3g = Color3g()
					all_sprites.add(color3g)
					switch275 = False
					switch279 = True
		
		if switch274:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2g.image = img5
					color2g.image.set_colorkey(WHITE)
					switch274 = False
					switch275 = True
				elif event.key == pygame.K_SPACE:
					color3g = Color3g()
					all_sprites.add(color3g)
					switch274 = False
					switch279 = True
		
		if switch273:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2g.image = img4
					color2g.image.set_colorkey(WHITE)
					switch273 = False
					switch274 = True
				elif event.key == pygame.K_SPACE:
					color3g = Color3g()
					all_sprites.add(color3g)
					switch273 = False
					switch279 = True
		
		if switch272:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2g.image = img3
					color2g.image.set_colorkey(WHITE)
					switch272 = False
					switch273 = True
				elif event.key == pygame.K_SPACE:
					color3g = Color3g()
					all_sprites.add(color3g)
					switch272 = False
					switch279 = True
		
		if switch271:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2g.image = img2
					color2g.image.set_colorkey(WHITE)
					switch271 = False
					switch272 = True
				elif event.key == pygame.K_SPACE:
					color3g = Color3g()
					all_sprites.add(color3g)
					switch271 = False
					switch279 = True

		if switch270:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2g.image = img1
					color2g.image.set_colorkey(WHITE)
					switch270 = False
					switch271 = True
				elif event.key == pygame.K_SPACE:
					color3g = Color3g()
					all_sprites.add(color3g)
					switch270 = False
					switch279 = True

		if switch269:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1g.image = img1
					color1g.image.set_colorkey(WHITE)
					switch269 = False
					switch261 = True
				elif event.key == pygame.K_SPACE:
					color2g = Color2g()
					all_sprites.add(color2g)
					switch269 = False
					switch270 = True

		if switch268:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1g.image = img8
					color1g.image.set_colorkey(WHITE)
					switch268 = False
					switch269 = True
				elif event.key == pygame.K_SPACE:
					color2g = Color2g()
					all_sprites.add(color2g)
					switch268 = False
					switch270 = True

		if switch267:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1g.image = img7
					color1g.image.set_colorkey(WHITE)
					switch267 = False
					switch268 = True
				elif event.key == pygame.K_SPACE:
					color2g = Color2g()
					all_sprites.add(color2g)
					switch267 = False
					switch270 = True
		
		if switch266:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1g.image = img6
					color1g.image.set_colorkey(WHITE)
					switch266 = False
					switch267 = True
				elif event.key == pygame.K_SPACE:
					color2g = Color2g()
					all_sprites.add(color2g)
					switch266 = False
					switch270 = True
		
		if switch265:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1g.image = img5
					color1g.image.set_colorkey(WHITE)
					switch265 = False
					switch266 = True
				elif event.key == pygame.K_SPACE:
					color2g = Color2g()
					all_sprites.add(color2g)
					switch265 = False
					switch270 = True
		
		if switch264:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1g.image = img4
					color1g.image.set_colorkey(WHITE)
					switch264 = False
					switch265 = True
				elif event.key == pygame.K_SPACE:
					color2g = Color2g()
					all_sprites.add(color2g)
					switch264 = False
					switch270 = True
		
		if switch263:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1g.image = img3
					color1g.image.set_colorkey(WHITE)
					switch263 = False
					switch264 = True
				elif event.key == pygame.K_SPACE:
					color2g = Color2g()
					all_sprites.add(color2g)
					switch263 = False
					switch270 = True
		
		if switch262:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1g.image = img2
					color1g.image.set_colorkey(WHITE)
					switch262 = False
					switch263 = True
				elif event.key == pygame.K_SPACE:
					color2g = Color2g()
					all_sprites.add(color2g)
					switch262 = False
					switch270 = True


		if switch261:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1g.image = img1
					color1g.image.set_colorkey(WHITE)
					switch261 = False
					switch262 = True
				elif event.key == pygame.K_SPACE:
					color2g = Color2g()
					all_sprites.add(color2g)
					switch261 = False
					switch270 = True
		

		if switch260:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1g = Color1g()
					all_sprites.add(color1g)
					switch260 = False
					switch261 = True

		if switch259:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4f.image = img1
					color4f.image.set_colorkey(WHITE)
					switch259 = False
					switch251 = True
				elif event.key == pygame.K_SPACE:
					if color1f.image == color1m.image and color2f.image == color2m.image and color3f.image == color3m.image and color4f.image == color4m.image:
						value1rf = Value1rf()
						value2rf = Value2rf()
						value3rf = Value3rf()
						value4rf = Value4rf()
						all_sprites.add(value1rf, value2rf, value3rf, value4rf)
						tapa.kill()
					
					elif color1f.image != color1m.image and color2f.image != color2m.image and color3f.image != color3m.image and color4f.image != color4m.image:
						pass
					switch259 = False
					switch260 = True

		if switch258:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4f.image = img8
					color4f.image.set_colorkey(WHITE)
					switch258 = False
					switch259 = True
				elif event.key == pygame.K_SPACE:
					if color1f.image == color1m.image and color2f.image == color2m.image and color3f.image == color3m.image and color4f.image == color4m.image:
						value1rf = Value1rf()
						value2rf = Value2rf()
						value3rf = Value3rf()
						value4rf = Value4rf()
						all_sprites.add(value1rf, value2rf, value3rf, value4rf)
						tapa.kill()
					
					elif color1f.image != color1m.image and color2f.image != color2m.image and color3f.image != color3m.image and color4f.image != color4m.image:
						pass
					switch258 = False
					switch260 = True
		
		if switch257:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4f.image = img7
					color4f.image.set_colorkey(WHITE)
					switch257 = False
					switch258 = True
				elif event.key == pygame.K_SPACE:
					if color1f.image == color1m.image and color2f.image == color2m.image and color3f.image == color3m.image and color4f.image == color4m.image:
						value1rf = Value1rf()
						value2rf = Value2rf()
						value3rf = Value3rf()
						value4rf = Value4rf()
						all_sprites.add(value1rf, value2rf, value3rf, value4rf)
						tapa.kill()
					
					elif color1f.image != color1m.image and color2f.image != color2m.image and color3f.image != color3m.image and color4f.image != color4m.image:
						pass
					switch257 = False
					switch260 = True
		
		if switch256:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4f.image = img6
					color4f.image.set_colorkey(WHITE)
					switch256 = False
					switch257 = True
				elif event.key == pygame.K_SPACE:
					if color1f.image == color1m.image and color2f.image == color2m.image and color3f.image == color3m.image and color4f.image == color4m.image:
						value1rf = Value1rf()
						value2rf = Value2rf()
						value3rf = Value3rf()
						value4rf = Value4rf()
						all_sprites.add(value1rf, value2rf, value3rf, value4rf)
						tapa.kill()
					
					elif color1f.image != color1m.image and color2f.image != color2m.image and color3f.image != color3m.image and color4f.image != color4m.image:
						pass
					switch256 = False
					switch260 = True
		
		if switch255:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4f.image = img5
					color4f.image.set_colorkey(WHITE)
					switch255 = False
					switch256 = True
				elif event.key == pygame.K_SPACE:
					if color1f.image == color1m.image and color2f.image == color2m.image and color3f.image == color3m.image and color4f.image == color4m.image:
						value1rf = Value1rf()
						value2rf = Value2rf()
						value3rf = Value3rf()
						value4rf = Value4rf()
						all_sprites.add(value1rf, value2rf, value3rf, value4rf)
						tapa.kill()
					
					elif color1f.image != color1m.image and color2f.image != color2m.image and color3f.image != color3m.image and color4f.image != color4m.image:
						pass
					switch255 = False
					switch260 = True
		
		if switch254:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4f.image = img4
					color4f.image.set_colorkey(WHITE)
					switch254 = False
					switch255 = True
				elif event.key == pygame.K_SPACE:
					if color1f.image == color1m.image and color2f.image == color2m.image and color3f.image == color3m.image and color4f.image == color4m.image:
						value1rf = Value1rf()
						value2rf = Value2rf()
						value3rf = Value3rf()
						value4rf = Value4rf()
						all_sprites.add(value1rf, value2rf, value3rf, value4rf)
						tapa.kill()
					
					elif color1f.image != color1m.image and color2f.image != color2m.image and color3f.image != color3m.image and color4f.image != color4m.image:
						pass
					switch254 = False
					switch260 = True
		
		if switch253:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4f.image = img3
					color4f.image.set_colorkey(WHITE)
					switch253 = False
					switch254 = True
				elif event.key == pygame.K_SPACE:
					if color1f.image == color1m.image and color2f.image == color2m.image and color3f.image == color3m.image and color4f.image == color4m.image:
						value1rf = Value1rf()
						value2rf = Value2rf()
						value3rf = Value3rf()
						value4rf = Value4rf()
						all_sprites.add(value1rf, value2rf, value3rf, value4rf)
						tapa.kill()
					
					elif color1f.image != color1m.image and color2f.image != color2m.image and color3f.image != color3m.image and color4f.image != color4m.image:
						pass
					switch253 = False
					switch260 = True
		
		if switch252:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4f.image = img2
					color4f.image.set_colorkey(WHITE)
					switch252 = False
					switch253 = True
				elif event.key == pygame.K_SPACE:
					if color1f.image == color1m.image and color2f.image == color2m.image and color3f.image == color3m.image and color4f.image == color4m.image:
						value1rf = Value1rf()
						value2rf = Value2rf()
						value3rf = Value3rf()
						value4rf = Value4rf()
						all_sprites.add(value1rf, value2rf, value3rf, value4rf)
						tapa.kill()
					
					elif color1f.image != color1m.image and color2f.image != color2m.image and color3f.image != color3m.image and color4f.image != color4m.image:
						pass
					switch252 = False
					switch260 = True
		
		if switch251:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4f.image = img1
					color4f.image.set_colorkey(WHITE)
					switch251 = False
					switch252 = True
				elif event.key == pygame.K_SPACE:
					if color1f.image == color1m.image and color2f.image == color2m.image and color3f.image == color3m.image and color4f.image == color4m.image:
						value1rf = Value1rf()
						value2rf = Value2rf()
						value3rf = Value3rf()
						value4rf = Value4rf()
						all_sprites.add(value1rf, value2rf, value3rf, value4rf)
						tapa.kill()
					
					elif color1f.image != color1m.image and color2f.image != color2m.image and color3f.image != color3m.image and color4f.image != color4m.image:
						pass
					switch251 = False
					switch260 = True

		if switch250:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3f.image = img1
					color3f.image.set_colorkey(WHITE)
					switch250 = False
					switch242 = True
				elif event.key == pygame.K_SPACE:
					color4f = Color4f()
					all_sprites.add(color4f)
					switch250 = False
					switch251 = True		
		
		if switch249:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3f.image = img8
					color3f.image.set_colorkey(WHITE)
					switch249 = False
					switch250 = True
				elif event.key == pygame.K_SPACE:
					color4f = Color4f()
					all_sprites.add(color4f)
					switch249 = False
					switch251 = True
		
		if switch248:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3f.image = img7
					color3f.image.set_colorkey(WHITE)
					switch248 = False
					switch249 = True
				elif event.key == pygame.K_SPACE:
					color4f = Color4f()
					all_sprites.add(color4f)
					switch248 = False
					switch251 = True
		
		if switch247:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3f.image = img6
					color3f.image.set_colorkey(WHITE)
					switch247 = False
					switch248 = True
				elif event.key == pygame.K_SPACE:
					color4f = Color4f()
					all_sprites.add(color4f)
					switch247 = False
					switch251 = True
		
		if switch246:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3f.image = img5
					color3f.image.set_colorkey(WHITE)
					switch246 = False
					switch247 = True
				elif event.key == pygame.K_SPACE:
					color4f = Color4f()
					all_sprites.add(color4f)
					switch246 = False
					switch251 = True
		
		if switch245:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3f.image = img4
					color3f.image.set_colorkey(WHITE)
					switch245 = False
					switch246 = True
				elif event.key == pygame.K_SPACE:
					color4f = Color4f()
					all_sprites.add(color4f)
					switch245 = False
					switch251 = True
		
		if switch244:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3f.image = img3
					color3f.image.set_colorkey(WHITE)
					switch244 = False
					switch245 = True
				elif event.key == pygame.K_SPACE:
					color4f = Color4f()
					all_sprites.add(color4f)
					switch244 = False
					switch251 = True
		
		if switch243:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3f.image = img2
					color3f.image.set_colorkey(WHITE)
					switch243 = False
					switch244 = True
				elif event.key == pygame.K_SPACE:
					color4f = Color4f()
					all_sprites.add(color4f)
					switch243 = False
					switch251 = True


		if switch242:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3f.image = img1
					color3f.image.set_colorkey(WHITE)
					switch242 = False
					switch243 = True
				elif event.key == pygame.K_SPACE:
					color4f = Color4f()
					all_sprites.add(color4f)
					switch242 = False
					switch251 = True

		if switch241:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2f.image = img1
					color2f.image.set_colorkey(WHITE)
					switch241 = False
					switch233 = True
				elif event.key == pygame.K_SPACE:
					color3f = Color3f()
					all_sprites.add(color3f)
					switch241 = False
					switch242 = True

		if switch240:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2f.image = img8
					color2f.image.set_colorkey(WHITE)
					switch240 = False
					switch241 = True
				elif event.key == pygame.K_SPACE:
					color3f = Color3f()
					all_sprites.add(color3f)
					switch240 = False
					switch242 = True
		
		if switch239:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2f.image = img7
					color2f.image.set_colorkey(WHITE)
					switch239 = False
					switch240 = True
				elif event.key == pygame.K_SPACE:
					color3f = Color3f()
					all_sprites.add(color3f)
					switch239 = False
					switch242 = True
		
		if switch238:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2f.image = img6
					color2f.image.set_colorkey(WHITE)
					switch238 = False
					switch239 = True
				elif event.key == pygame.K_SPACE:
					color3f = Color3f()
					all_sprites.add(color3f)
					switch238 = False
					switch242 = True
		
		if switch237:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2f.image = img5
					color2f.image.set_colorkey(WHITE)
					switch237 = False
					switch238 = True
				elif event.key == pygame.K_SPACE:
					color3f = Color3f()
					all_sprites.add(color3f)
					switch237 = False
					switch242 = True
		
		if switch236:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2f.image = img4
					color2f.image.set_colorkey(WHITE)
					switch236 = False
					switch237 = True
				elif event.key == pygame.K_SPACE:
					color3f = Color3f()
					all_sprites.add(color3f)
					switch236 = False
					switch242 = True
		
		if switch235:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2f.image = img3
					color2f.image.set_colorkey(WHITE)
					switch235 = False
					switch236 = True
				elif event.key == pygame.K_SPACE:
					color3f = Color3f()
					all_sprites.add(color3f)
					switch235 = False
					switch242 = True
		
		if switch234:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2f.image = img2
					color2f.image.set_colorkey(WHITE)
					switch234 = False
					switch235 = True
				elif event.key == pygame.K_SPACE:
					color3f = Color3f()
					all_sprites.add(color3f)
					switch234 = False
					switch242 = True

		if switch233:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2f.image = img1
					color2f.image.set_colorkey(WHITE)
					switch233 = False
					switch234 = True
				elif event.key == pygame.K_SPACE:
					color3f = Color3f()
					all_sprites.add(color3f)
					switch233 = False
					switch242 = True

		if switch232:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1f.image = img1
					color1f.image.set_colorkey(WHITE)
					switch232 = False
					switch224 = True
				elif event.key == pygame.K_SPACE:
					color2f = Color2f()
					all_sprites.add(color2f)
					switch232 = False
					switch233 = True

		if switch231:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1f.image = img8
					color1f.image.set_colorkey(WHITE)
					switch231 = False
					switch232 = True
				elif event.key == pygame.K_SPACE:
					color2f = Color2f()
					all_sprites.add(color2f)
					switch231 = False
					switch233 = True

		if switch230:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1f.image = img7
					color1f.image.set_colorkey(WHITE)
					switch230 = False
					switch231 = True
				elif event.key == pygame.K_SPACE:
					color2f = Color2f()
					all_sprites.add(color2f)
					switch230 = False
					switch233 = True
		
		if switch229:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1f.image = img6
					color1f.image.set_colorkey(WHITE)
					switch229 = False
					switch230 = True
				elif event.key == pygame.K_SPACE:
					color2f = Color2f()
					all_sprites.add(color2f)
					switch229 = False
					switch233 = True
		
		if switch228:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1f.image = img5
					color1f.image.set_colorkey(WHITE)
					switch228 = False
					switch229 = True
				elif event.key == pygame.K_SPACE:
					color2f = Color2f()
					all_sprites.add(color2f)
					switch228 = False
					switch233 = True
		
		if switch227:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1f.image = img4
					color1f.image.set_colorkey(WHITE)
					switch227 = False
					switch228 = True
				elif event.key == pygame.K_SPACE:
					color2f = Color2f()
					all_sprites.add(color2f)
					switch227 = False
					switch233 = True
		
		if switch226:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1f.image = img3
					color1f.image.set_colorkey(WHITE)
					switch226 = False
					switch227 = True
				elif event.key == pygame.K_SPACE:
					color2f = Color2f()
					all_sprites.add(color2f)
					switch226 = False
					switch233 = True
		
		if switch225:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1f.image = img2
					color1f.image.set_colorkey(WHITE)
					switch225 = False
					switch226 = True
				elif event.key == pygame.K_SPACE:
					color2f = Color2f()
					all_sprites.add(color2f)
					switch225 = False
					switch233 = True


		if switch224:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1f.image = img1
					color1f.image.set_colorkey(WHITE)
					switch224 = False
					switch225 = True
				elif event.key == pygame.K_SPACE:
					color2f = Color2f()
					all_sprites.add(color2f)
					switch224 = False
					switch233 = True

		if switch223:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1f = Color1f()
					all_sprites.add(color1f)
					switch223 = False
					switch224 = True

		if switch222:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4e.image = img1
					color4e.image.set_colorkey(WHITE)
					switch222 = False
					switch214 = True
				elif event.key == pygame.K_SPACE:
					if color1e.image == color1m.image and color2e.image == color2m.image and color3e.image == color3m.image and color4e.image == color4m.image:
						value1re = Value1re()
						value2re = Value2re()
						value3re = Value3re()
						value4re = Value4re()
						all_sprites.add(value1re, value2re, value3re, value4re)
						tapa.kill()
					
					elif color1e.image != color1m.image and color2e.image != color2m.image and color3e.image != color3m.image and color4e.image != color4m.image:
						pass
					switch222 = False
					switch223 = True

		if switch221:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4e.image = img8
					color4e.image.set_colorkey(WHITE)
					switch221 = False
					switch222 = True
				elif event.key == pygame.K_SPACE:
					if color1e.image == color1m.image and color2e.image == color2m.image and color3e.image == color3m.image and color4e.image == color4m.image:
						value1re = Value1re()
						value2re = Value2re()
						value3re = Value3re()
						value4re = Value4re()
						all_sprites.add(value1re, value2re, value3re, value4re)
						tapa.kill()
					
					elif color1e.image != color1m.image and color2e.image != color2m.image and color3e.image != color3m.image and color4e.image != color4m.image:
						pass
					switch221 = False
					switch223 = True
		
		if switch220:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4e.image = img7
					color4e.image.set_colorkey(WHITE)
					switch220 = False
					switch221 = True
				elif event.key == pygame.K_SPACE:
					if color1e.image == color1m.image and color2e.image == color2m.image and color3e.image == color3m.image and color4e.image == color4m.image:
						value1re = Value1re()
						value2re = Value2re()
						value3re = Value3re()
						value4re = Value4re()
						all_sprites.add(value1re, value2re, value3re, value4re)
						tapa.kill()
					
					elif color1e.image != color1m.image and color2e.image != color2m.image and color3e.image != color3m.image and color4e.image != color4m.image:
						pass
					switch220 = False
					switch223 = True
		
		if switch219:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4e.image = img6
					color4e.image.set_colorkey(WHITE)
					switch219 = False
					switch220 = True
				elif event.key == pygame.K_SPACE:
					if color1e.image == color1m.image and color2e.image == color2m.image and color3e.image == color3m.image and color4e.image == color4m.image:
						value1re = Value1re()
						value2re = Value2re()
						value3re = Value3re()
						value4re = Value4re()
						all_sprites.add(value1re, value2re, value3re, value4re)
						tapa.kill()
					
					elif color1e.image != color1m.image and color2e.image != color2m.image and color3e.image != color3m.image and color4e.image != color4m.image:
						pass
					switch219 = False
					switch223 = True
		
		if switch218:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4e.image = img5
					color4e.image.set_colorkey(WHITE)
					switch218 = False
					switch219 = True
				elif event.key == pygame.K_SPACE:
					if color1e.image == color1m.image and color2e.image == color2m.image and color3e.image == color3m.image and color4e.image == color4m.image:
						value1re = Value1re()
						value2re = Value2re()
						value3re = Value3re()
						value4re = Value4re()
						all_sprites.add(value1re, value2re, value3re, value4re)
						tapa.kill()
					
					elif color1e.image != color1m.image and color2e.image != color2m.image and color3e.image != color3m.image and color4e.image != color4m.image:
						pass
					switch218 = False
					switch223 = True
		
		if switch217:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4e.image = img4
					color4e.image.set_colorkey(WHITE)
					switch217 = False
					switch218 = True
				elif event.key == pygame.K_SPACE:
					if color1e.image == color1m.image and color2e.image == color2m.image and color3e.image == color3m.image and color4e.image == color4m.image:
						value1re = Value1re()
						value2re = Value2re()
						value3re = Value3re()
						value4re = Value4re()
						all_sprites.add(value1re, value2re, value3re, value4re)
						tapa.kill()
					
					elif color1e.image != color1m.image and color2e.image != color2m.image and color3e.image != color3m.image and color4e.image != color4m.image:
						pass
					switch217 = False
					switch223 = True
		
		if switch216:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4e.image = img3
					color4e.image.set_colorkey(WHITE)
					switch216 = False
					switch217 = True
				elif event.key == pygame.K_SPACE:
					if color1e.image == color1m.image and color2e.image == color2m.image and color3e.image == color3m.image and color4e.image == color4m.image:
						value1re = Value1re()
						value2re = Value2re()
						value3re = Value3re()
						value4re = Value4re()
						all_sprites.add(value1re, value2re, value3re, value4re)
						tapa.kill()
					
					elif color1e.image != color1m.image and color2e.image != color2m.image and color3e.image != color3m.image and color4e.image != color4m.image:
						pass
					switch216 = False
					switch223 = True
		
		if switch215:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4e.image = img2
					color4e.image.set_colorkey(WHITE)
					switch215 = False
					switch216 = True
				elif event.key == pygame.K_SPACE:
					if color1e.image == color1m.image and color2e.image == color2m.image and color3e.image == color3m.image and color4e.image == color4m.image:
						value1re = Value1re()
						value2re = Value2re()
						value3re = Value3re()
						value4re = Value4re()
						all_sprites.add(value1re, value2re, value3re, value4re)
						tapa.kill()
					
					elif color1e.image != color1m.image and color2e.image != color2m.image and color3e.image != color3m.image and color4e.image != color4m.image:
						pass
					switch215 = False
					switch223 = True
		
		if switch214:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4e.image = img1
					color4e.image.set_colorkey(WHITE)
					switch214 = False
					switch215 = True
				elif event.key == pygame.K_SPACE:
					if color1e.image == color1m.image and color2e.image == color2m.image and color3e.image == color3m.image and color4e.image == color4m.image:
						value1re = Value1re()
						value2re = Value2re()
						value3re = Value3re()
						value4re = Value4re()
						all_sprites.add(value1re, value2re, value3re, value4re)
						tapa.kill()
					
					elif color1e.image != color1m.image and color2e.image != color2m.image and color3e.image != color3m.image and color4e.image != color4m.image:
						pass
					switch214 = False
					switch223 = True

		if switch213:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3e.image = img1
					color3e.image.set_colorkey(WHITE)
					switch213 = False
					switch205 = True
				elif event.key == pygame.K_SPACE:
					color4e = Color4e()
					all_sprites.add(color4e)
					switch213 = False
					switch214 = True		
		
		if switch212:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3e.image = img8
					color3e.image.set_colorkey(WHITE)
					switch212 = False
					switch213 = True
				elif event.key == pygame.K_SPACE:
					color4e = Color4e()
					all_sprites.add(color4e)
					switch212 = False
					switch214 = True
		
		if switch211:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3e.image = img7
					color3e.image.set_colorkey(WHITE)
					switch211 = False
					switch212 = True
				elif event.key == pygame.K_SPACE:
					color4e = Color4e()
					all_sprites.add(color4e)
					switch211 = False
					switch214 = True
		
		if switch210:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3e.image = img6
					color3e.image.set_colorkey(WHITE)
					switch210 = False
					switch211 = True
				elif event.key == pygame.K_SPACE:
					color4e = Color4e()
					all_sprites.add(color4e)
					switch210 = False
					switch214 = True
		
		if switch209:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3e.image = img5
					color3e.image.set_colorkey(WHITE)
					switch209 = False
					switch210 = True
				elif event.key == pygame.K_SPACE:
					color4e = Color4e()
					all_sprites.add(color4e)
					switch209 = False
					switch214 = True
		
		if switch208:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3e.image = img4
					color3e.image.set_colorkey(WHITE)
					switch208 = False
					switch209 = True
				elif event.key == pygame.K_SPACE:
					color4e = Color4e()
					all_sprites.add(color4e)
					switch208 = False
					switch214 = True
		
		if switch207:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3e.image = img3
					color3e.image.set_colorkey(WHITE)
					switch207 = False
					switch208 = True
				elif event.key == pygame.K_SPACE:
					color4e = Color4e()
					all_sprites.add(color4e)
					switch207 = False
					switch214 = True
		
		if switch206:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3e.image = img2
					color3e.image.set_colorkey(WHITE)
					switch206 = False
					switch207 = True
				elif event.key == pygame.K_SPACE:
					color4e = Color4e()
					all_sprites.add(color4e)
					switch206 = False
					switch214 = True


		if switch205:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3e.image = img1
					color3e.image.set_colorkey(WHITE)
					switch205 = False
					switch206 = True
				elif event.key == pygame.K_SPACE:
					color4e = Color4e()
					all_sprites.add(color4e)
					switch205 = False
					switch214 = True

		if switch204:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2e.image = img1
					color2e.image.set_colorkey(WHITE)
					switch204 = False
					switch196 = True
				elif event.key == pygame.K_SPACE:
					color3e = Color3e()
					all_sprites.add(color3e)
					switch204 = False
					switch205 = True

		if switch203:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2e.image = img8
					color2e.image.set_colorkey(WHITE)
					switch203 = False
					switch204 = True
				elif event.key == pygame.K_SPACE:
					color3e = Color3e()
					all_sprites.add(color3e)
					switch203 = False
					switch205 = True
		
		if switch202:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2e.image = img7
					color2e.image.set_colorkey(WHITE)
					switch202 = False
					switch203 = True
				elif event.key == pygame.K_SPACE:
					color3e = Color3e()
					all_sprites.add(color3e)
					switch202 = False
					switch205 = True
		
		if switch201:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2e.image = img6
					color2e.image.set_colorkey(WHITE)
					switch201 = False
					switch202 = True
				elif event.key == pygame.K_SPACE:
					color3e = Color3e()
					all_sprites.add(color3e)
					switch201 = False
					switch205 = True
		
		if switch200:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2e.image = img5
					color2e.image.set_colorkey(WHITE)
					switch200 = False
					switch201 = True
				elif event.key == pygame.K_SPACE:
					color3e = Color3e()
					all_sprites.add(color3e)
					switch200 = False
					switch205 = True
		
		if switch199:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2e.image = img4
					color2e.image.set_colorkey(WHITE)
					switch199 = False
					switch200 = True
				elif event.key == pygame.K_SPACE:
					color3e = Color3e()
					all_sprites.add(color3e)
					switch199 = False
					switch205 = True
		
		if switch198:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2e.image = img3
					color2e.image.set_colorkey(WHITE)
					switch198 = False
					switch199 = True
				elif event.key == pygame.K_SPACE:
					color3e = Color3e()
					all_sprites.add(color3e)
					switch198 = False
					switch205 = True
		
		if switch197:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2e.image = img2
					color2e.image.set_colorkey(WHITE)
					switch197 = False
					switch198 = True
				elif event.key == pygame.K_SPACE:
					color3e = Color3e()
					all_sprites.add(color3e)
					switch197 = False
					switch205 = True

		if switch196:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2e.image = img1
					color2e.image.set_colorkey(WHITE)
					switch196 = False
					switch197 = True
				elif event.key == pygame.K_SPACE:
					color3e = Color3e()
					all_sprites.add(color3e)
					switch196 = False
					switch205 = True

		if switch195:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1e.image = img1
					color1e.image.set_colorkey(WHITE)
					switch195 = False
					switch187 = True
				elif event.key == pygame.K_SPACE:
					color2e = Color2e()
					all_sprites.add(color2e)
					switch195 = False
					switch196 = True

		if switch194:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1e.image = img8
					color1e.image.set_colorkey(WHITE)
					switch194 = False
					switch195 = True
				elif event.key == pygame.K_SPACE:
					color2e = Color2e()
					all_sprites.add(color2e)
					switch194 = False
					switch196 = True

		if switch193:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1e.image = img7
					color1e.image.set_colorkey(WHITE)
					switch193 = False
					switch194 = True
				elif event.key == pygame.K_SPACE:
					color2e = Color2e()
					all_sprites.add(color2e)
					switch193 = False
					switch196 = True
		
		if switch192:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1e.image = img6
					color1e.image.set_colorkey(WHITE)
					switch192 = False
					switch193 = True
				elif event.key == pygame.K_SPACE:
					color2e = Color2e()
					all_sprites.add(color2e)
					switch192 = False
					switch196 = True
		
		if switch191:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1e.image = img5
					color1e.image.set_colorkey(WHITE)
					switch191 = False
					switch192 = True
				elif event.key == pygame.K_SPACE:
					color2e = Color2e()
					all_sprites.add(color2e)
					switch191 = False
					switch196 = True
		
		if switch190:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1e.image = img4
					color1e.image.set_colorkey(WHITE)
					switch190 = False
					switch191 = True
				elif event.key == pygame.K_SPACE:
					color2e = Color2e()
					all_sprites.add(color2e)
					switch190 = False
					switch196 = True
		
		if switch189:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1e.image = img3
					color1e.image.set_colorkey(WHITE)
					switch189 = False
					switch190 = True
				elif event.key == pygame.K_SPACE:
					color2e = Color2e()
					all_sprites.add(color2e)
					switch189 = False
					switch196 = True
		
		if switch188:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1e.image = img2
					color1e.image.set_colorkey(WHITE)
					switch188 = False
					switch189 = True
				elif event.key == pygame.K_SPACE:
					color2e = Color2e()
					all_sprites.add(color2e)
					switch188 = False
					switch196 = True


		if switch187:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1e.image = img1
					color1e.image.set_colorkey(WHITE)
					switch187 = False
					switch188 = True
				elif event.key == pygame.K_SPACE:
					color2e = Color2e()
					all_sprites.add(color2e)
					switch187 = False
					switch196 = True

		if switch186:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1e = Color1e()
					all_sprites.add(color1e)
					switch186 = False
					switch187 = True

		if switch185:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4d.image = img1
					color4d.image.set_colorkey(WHITE)
					switch185 = False
					switch177 = True
				elif event.key == pygame.K_SPACE:
					if color1d.image == color1m.image and color2d.image == color2m.image and color3d.image == color3m.image and color4d.image == color4m.image:
						value1rd = Value1rd()
						value2rd = Value2rd()
						value3rd = Value3rd()
						value4rd = Value4rd()
						all_sprites.add(value1rd, value2rd, value3rd, value4rd)
						tapa.kill()
					
					elif color1d.image != color1m.image and color2d.image != color2m.image and color3d.image != color3m.image and color4d.image != color4m.image:
						pass
					switch185 = False
					switch186 = True

		if switch184:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4d.image = img8
					color4d.image.set_colorkey(WHITE)
					switch184 = False
					switch185 = True
				elif event.key == pygame.K_SPACE:
					if color1d.image == color1m.image and color2d.image == color2m.image and color3d.image == color3m.image and color4d.image == color4m.image:
						value1rd = Value1rd()
						value2rd = Value2rd()
						value3rd = Value3rd()
						value4rd = Value4rd()
						all_sprites.add(value1rd, value2rd, value3rd, value4rd)
						tapa.kill()
					
					elif color1d.image != color1m.image and color2d.image != color2m.image and color3d.image != color3m.image and color4d.image != color4m.image:
						pass
					switch184 = False
					switch186 = True
		
		if switch183:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4d.image = img7
					color4d.image.set_colorkey(WHITE)
					switch183 = False
					switch184 = True
				elif event.key == pygame.K_SPACE:
					if color1d.image == color1m.image and color2d.image == color2m.image and color3d.image == color3m.image and color4d.image == color4m.image:
						value1rd = Value1rd()
						value2rd = Value2rd()
						value3rd = Value3rd()
						value4rd = Value4rd()
						all_sprites.add(value1rd, value2rd, value3rd, value4rd)
						tapa.kill()
					
					elif color1d.image != color1m.image and color2d.image != color2m.image and color3d.image != color3m.image and color4d.image != color4m.image:
						pass
					
					switch183 = False
					switch186 = True
		
		if switch182:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4d.image = img6
					color4d.image.set_colorkey(WHITE)
					switch182 = False
					switch183 = True
				elif event.key == pygame.K_SPACE:
					if color1d.image == color1m.image and color2d.image == color2m.image and color3d.image == color3m.image and color4d.image == color4m.image:
						value1rd = Value1rd()
						value2rd = Value2rd()
						value3rd = Value3rd()
						value4rd = Value4rd()
						all_sprites.add(value1rd, value2rd, value3rd, value4rd)
						tapa.kill()
					
					elif color1d.image != color1m.image and color2d.image != color2m.image and color3d.image != color3m.image and color4d.image != color4m.image:
						pass
					switch182 = False
					switch186 = True
		
		if switch181:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4d.image = img5
					color4d.image.set_colorkey(WHITE)
					switch181 = False
					switch182 = True
				elif event.key == pygame.K_SPACE:
					if color1d.image == color1m.image and color2d.image == color2m.image and color3d.image == color3m.image and color4d.image == color4m.image:
						value1rd = Value1rd()
						value2rd = Value2rd()
						value3rd = Value3rd()
						value4rd = Value4rd()
						all_sprites.add(value1rd, value2rd, value3rd, value4rd)
						tapa.kill()
					
					elif color1d.image != color1m.image and color2d.image != color2m.image and color3d.image != color3m.image and color4d.image != color4m.image:
						pass
					switch181 = False
					switch186 = True
		
		if switch180:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4d.image = img4
					color4d.image.set_colorkey(WHITE)
					switch180 = False
					switch181 = True
				elif event.key == pygame.K_SPACE:
					if color1d.image == color1m.image and color2d.image == color2m.image and color3d.image == color3m.image and color4d.image == color4m.image:
						value1rd = Value1rd()
						value2rd = Value2rd()
						value3rd = Value3rd()
						value4rd = Value4rd()
						all_sprites.add(value1rd, value2rd, value3rd, value4rd)
						tapa.kill()
					
					elif color1d.image != color1m.image and color2d.image != color2m.image and color3d.image != color3m.image and color4d.image != color4m.image:
						pass
					switch180 = False
					switch186 = True
		
		if switch179:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4d.image = img3
					color4d.image.set_colorkey(WHITE)
					switch179 = False
					switch180 = True
				elif event.key == pygame.K_SPACE:
					if color1d.image == color1m.image and color2d.image == color2m.image and color3d.image == color3m.image and color4d.image == color4m.image:
						value1rd = Value1rd()
						value2rd = Value2rd()
						value3rd = Value3rd()
						value4rd = Value4rd()
						all_sprites.add(value1rd, value2rd, value3rd, value4rd)
						tapa.kill()
					
					elif color1d.image != color1m.image and color2d.image != color2m.image and color3d.image != color3m.image and color4d.image != color4m.image:
						pass
					switch179 = False
					switch186 = True
		
		if switch178:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4d.image = img2
					color4d.image.set_colorkey(WHITE)
					switch178 = False
					switch179 = True
				elif event.key == pygame.K_SPACE:
					if color1d.image == color1m.image and color2d.image == color2m.image and color3d.image == color3m.image and color4d.image == color4m.image:
						value1rd = Value1rd()
						value2rd = Value2rd()
						value3rd = Value3rd()
						value4rd = Value4rd()
						all_sprites.add(value1rd, value2rd, value3rd, value4rd)
						tapa.kill()
					
					elif color1d.image != color1m.image and color2d.image != color2m.image and color3d.image != color3m.image and color4d.image != color4m.image:
						pass
					switch178 = False
					switch186 = True
		
		if switch177:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4d.image = img1
					color4d.image.set_colorkey(WHITE)
					switch177 = False
					switch178 = True
				elif event.key == pygame.K_SPACE:
					if color1d.image == color1m.image and color2d.image == color2m.image and color3d.image == color3m.image and color4d.image == color4m.image:
						value1rd = Value1rd()
						value2rd = Value2rd()
						value3rd = Value3rd()
						value4rd = Value4rd()
						all_sprites.add(value1rd, value2rd, value3rd, value4rd)
						tapa.kill()
					
					elif color1d.image != color1m.image and color2d.image != color2m.image and color3d.image != color3m.image and color4d.image != color4m.image:
						pass
					switch177 = False
					switch186 = True

		if switch176:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3d.image = img1
					color3d.image.set_colorkey(WHITE)
					switch176 = False
					switch168 = True
				elif event.key == pygame.K_SPACE:
					color4d = Color4d()
					all_sprites.add(color4d)
					switch176 = False
					switch177 = True		
		
		if switch175:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3d.image = img8
					color3d.image.set_colorkey(WHITE)
					switch175 = False
					switch176 = True
				elif event.key == pygame.K_SPACE:
					color4d = Color4d()
					all_sprites.add(color4d)
					switch175 = False
					switch177 = True
		
		if switch174:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3d.image = img7
					color3d.image.set_colorkey(WHITE)
					switch174 = False
					switch175 = True
				elif event.key == pygame.K_SPACE:
					color4d = Color4d()
					all_sprites.add(color4d)
					switch174 = False
					switch177 = True
		
		if switch173:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3d.image = img6
					color3d.image.set_colorkey(WHITE)
					switch173 = False
					switch174 = True
				elif event.key == pygame.K_SPACE:
					color4d = Color4d()
					all_sprites.add(color4d)
					switch173 = False
					switch177 = True
		
		if switch172:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3d.image = img5
					color3d.image.set_colorkey(WHITE)
					switch172 = False
					switch173 = True
				elif event.key == pygame.K_SPACE:
					color4d = Color4d()
					all_sprites.add(color4d)
					switch172 = False
					switch177 = True
		
		if switch171:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3d.image = img4
					color3d.image.set_colorkey(WHITE)
					switch171 = False
					switch172 = True
				elif event.key == pygame.K_SPACE:
					color4d = Color4d()
					all_sprites.add(color4d)
					switch171 = False
					switch177 = True
		
		if switch170:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3d.image = img3
					color3d.image.set_colorkey(WHITE)
					switch170 = False
					switch171 = True
				elif event.key == pygame.K_SPACE:
					color4d = Color4d()
					all_sprites.add(color4d)
					switch170 = False
					switch177 = True
		
		if switch169:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3d.image = img2
					color3d.image.set_colorkey(WHITE)
					switch169 = False
					switch170 = True
				elif event.key == pygame.K_SPACE:
					color4d = Color4d()
					all_sprites.add(color4d)
					switch169 = False
					switch177 = True


		if switch168:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3d.image = img1
					color3d.image.set_colorkey(WHITE)
					switch168 = False
					switch169 = True
				elif event.key == pygame.K_SPACE:
					color4d = Color4d()
					all_sprites.add(color4d)
					switch168 = False
					switch177 = True

		if switch167:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2d.image = img1
					color2d.image.set_colorkey(WHITE)
					switch167 = False
					switch159 = True
				elif event.key == pygame.K_SPACE:
					color3d = Color3d()
					all_sprites.add(color3d)
					switch167 = False
					switch168 = True

		if switch166:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2d.image = img8
					color2d.image.set_colorkey(WHITE)
					switch166 = False
					switch167 = True
				elif event.key == pygame.K_SPACE:
					color3d = Color3d()
					all_sprites.add(color3d)
					switch166 = False
					switch168 = True
		
		if switch165:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2d.image = img7
					color2d.image.set_colorkey(WHITE)
					switch165 = False
					switch166 = True
				elif event.key == pygame.K_SPACE:
					color3d = Color3d()
					all_sprites.add(color3d)
					switch165 = False
					switch168 = True
		
		if switch164:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2d.image = img6
					color2d.image.set_colorkey(WHITE)
					switch164 = False
					switch165 = True
				elif event.key == pygame.K_SPACE:
					color3d = Color3d()
					all_sprites.add(color3d)
					switch164 = False
					switch168 = True
		
		if switch163:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2d.image = img5
					color2d.image.set_colorkey(WHITE)
					switch163 = False
					switch164 = True
				elif event.key == pygame.K_SPACE:
					color3d = Color3d()
					all_sprites.add(color3d)
					switch163 = False
					switch168 = True
		
		if switch162:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2d.image = img4
					color2d.image.set_colorkey(WHITE)
					switch162 = False
					switch163 = True
				elif event.key == pygame.K_SPACE:
					color3d = Color3d()
					all_sprites.add(color3d)
					switch162 = False
					switch168 = True
		
		if switch161:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2d.image = img3
					color2d.image.set_colorkey(WHITE)
					switch161 = False
					switch162 = True
				elif event.key == pygame.K_SPACE:
					color3d = Color3d()
					all_sprites.add(color3d)
					switch161 = False
					switch168 = True
		
		if switch160:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2d.image = img2
					color2d.image.set_colorkey(WHITE)
					switch160 = False
					switch161 = True
				elif event.key == pygame.K_SPACE:
					color3d = Color3d()
					all_sprites.add(color3d)
					switch160 = False
					switch168 = True

		if switch159:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2d.image = img1
					color2d.image.set_colorkey(WHITE)
					switch159 = False
					switch160 = True
				elif event.key == pygame.K_SPACE:
					color3d = Color3d()
					all_sprites.add(color3d)
					switch159 = False
					switch168 = True

		if switch158:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1d.image = img1
					color1d.image.set_colorkey(WHITE)
					switch158 = False
					switch150 = True
				elif event.key == pygame.K_SPACE:
					color2d = Color2d()
					all_sprites.add(color2d)
					switch158 = False
					switch159 = True

		if switch157:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1d.image = img8
					color1d.image.set_colorkey(WHITE)
					switch157 = False
					switch158 = True
				elif event.key == pygame.K_SPACE:
					color2d = Color2d()
					all_sprites.add(color2d)
					switch157 = False
					switch159 = True

		if switch156:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1d.image = img7
					color1d.image.set_colorkey(WHITE)
					switch156 = False
					switch157 = True
				elif event.key == pygame.K_SPACE:
					color2d = Color2d()
					all_sprites.add(color2d)
					switch156 = False
					switch159 = True
		
		if switch155:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1d.image = img6
					color1d.image.set_colorkey(WHITE)
					switch155 = False
					switch156 = True
				elif event.key == pygame.K_SPACE:
					color2d = Color2d()
					all_sprites.add(color2d)
					switch155 = False
					switch159 = True
		
		if switch154:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1d.image = img5
					color1d.image.set_colorkey(WHITE)
					switch154 = False
					switch155 = True
				elif event.key == pygame.K_SPACE:
					color2d = Color2d()
					all_sprites.add(color2d)
					switch154 = False
					switch159 = True
		
		if switch153:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1d.image = img4
					color1d.image.set_colorkey(WHITE)
					switch153 = False
					switch154 = True
				elif event.key == pygame.K_SPACE:
					color2d = Color2d()
					all_sprites.add(color2d)
					switch153 = False
					switch159 = True
		
		if switch152:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1d.image = img3
					color1d.image.set_colorkey(WHITE)
					switch152 = False
					switch153 = True
				elif event.key == pygame.K_SPACE:
					color2d = Color2d()
					all_sprites.add(color2d)
					switch152 = False
					switch159 = True
		
		if switch151:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1d.image = img2
					color1d.image.set_colorkey(WHITE)
					switch151 = False
					switch152 = True
				elif event.key == pygame.K_SPACE:
					color2d = Color2d()
					all_sprites.add(color2d)
					switch151 = False
					switch159 = True


		if switch150:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1d.image = img1
					color1d.image.set_colorkey(WHITE)
					switch150 = False
					switch151 = True
				elif event.key == pygame.K_SPACE:
					color2d = Color2d()
					all_sprites.add(color2d)
					switch150 = False
					switch159 = True

		if switch149:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1d = Color1d()
					all_sprites.add(color1d)
					switch149 = False
					switch150 = True

		if switch148:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4c.image = img1
					color4c.image.set_colorkey(WHITE)
					switch148 = False
					switch140 = True
				elif event.key == pygame.K_SPACE:
					if color1c.image == color1m.image and color2c.image == color2m.image and color3c.image == color3m.image and color4c.image == color4m.image:
						value1rc = Value1rc()
						value2rc = Value2rc()
						value3rc = Value3rc()
						value4rc = Value4rc()
						all_sprites.add(value1rc, value2rc, value3rc, value4rc)
						tapa.kill()
					
					elif color1c.image != color1m.image and color2c.image != color2m.image and color3c.image != color3m.image and color4c.image != color4m.image:
						pass
					switch148 = False
					switch149 = True

		if switch147:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4c.image = img8
					color4c.image.set_colorkey(WHITE)
					switch147 = False
					switch148 = True
				elif event.key == pygame.K_SPACE:
					if color1c.image == color1m.image and color2c.image == color2m.image and color3c.image == color3m.image and color4c.image == color4m.image:
						value1rc = Value1rc()
						value2rc = Value2rc()
						value3rc = Value3rc()
						value4rc = Value4rc()
						all_sprites.add(value1rc, value2rc, value3rc, value4rc)
						tapa.kill()
					
					elif color1c.image != color1m.image and color2c.image != color2m.image and color3c.image != color3m.image and color4c.image != color4m.image:
						pass
					switch147 = False
					switch149 = True
		
		if switch146:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4c.image = img7
					color4c.image.set_colorkey(WHITE)
					switch146 = False
					switch147 = True
				elif event.key == pygame.K_SPACE:
					if color1c.image == color1m.image and color2c.image == color2m.image and color3c.image == color3m.image and color4c.image == color4m.image:
						value1rc = Value1rc()
						value2rc = Value2rc()
						value3rc = Value3rc()
						value4rc = Value4rc()
						all_sprites.add(value1rc, value2rc, value3rc, value4rc)
						tapa.kill()
					
					elif color1c.image != color1m.image and color2c.image != color2m.image and color3c.image != color3m.image and color4c.image != color4m.image:
						pass
					
					switch146 = False
					switch149 = True
		
		if switch145:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4c.image = img6
					color4c.image.set_colorkey(WHITE)
					switch145 = False
					switch146 = True
				elif event.key == pygame.K_SPACE:
					if color1c.image == color1m.image and color2c.image == color2m.image and color3c.image == color3m.image and color4c.image == color4m.image:
						value1rc = Value1rc()
						value2rc = Value2rc()
						value3rc = Value3rc()
						value4rc = Value4rc()
						all_sprites.add(value1rc, value2rc, value3rc, value4rc)
						tapa.kill()
					
					elif color1c.image != color1m.image and color2c.image != color2m.image and color3c.image != color3m.image and color4c.image != color4m.image:
						pass
					switch145 = False
					switch149 = True
		
		if switch144:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4c.image = img5
					color4c.image.set_colorkey(WHITE)
					switch144 = False
					switch145 = True
				elif event.key == pygame.K_SPACE:
					if color1c.image == color1m.image and color2c.image == color2m.image and color3c.image == color3m.image and color4c.image == color4m.image:
						value1rc = Value1rc()
						value2rc = Value2rc()
						value3rc = Value3rc()
						value4rc = Value4rc()
						all_sprites.add(value1rc, value2rc, value3rc, value4rc)
						tapa.kill()
					
					elif color1c.image != color1m.image and color2c.image != color2m.image and color3c.image != color3m.image and color4c.image != color4m.image:
						pass
					switch144 = False
					switch149 = True
		
		if switch143:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4c.image = img4
					color4c.image.set_colorkey(WHITE)
					switch143 = False
					switch144 = True
				elif event.key == pygame.K_SPACE:
					if color1c.image == color1m.image and color2c.image == color2m.image and color3c.image == color3m.image and color4c.image == color4m.image:
						value1rc = Value1rc()
						value2rc = Value2rc()
						value3rc = Value3rc()
						value4rc = Value4rc()
						all_sprites.add(value1rc, value2rc, value3rc, value4rc)
						tapa.kill()
					
					elif color1c.image != color1m.image and color2c.image != color2m.image and color3c.image != color3m.image and color4c.image != color4m.image:
						pass
					switch143 = False
					switch149 = True
		
		if switch142:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4c.image = img3
					color4c.image.set_colorkey(WHITE)
					switch142 = False
					switch143 = True
				elif event.key == pygame.K_SPACE:
					if color1c.image == color1m.image and color2c.image == color2m.image and color3c.image == color3m.image and color4c.image == color4m.image:
						value1rc = Value1rc()
						value2rc = Value2rc()
						value3rc = Value3rc()
						value4rc = Value4rc()
						all_sprites.add(value1rc, value2rc, value3rc, value4rc)
						tapa.kill()
					
					elif color1c.image != color1m.image and color2c.image != color2m.image and color3c.image != color3m.image and color4c.image != color4m.image:
						pass
					switch142 = False
					switch149 = True
		
		if switch141:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4c.image = img2
					color4c.image.set_colorkey(WHITE)
					switch141 = False
					switch142 = True
				elif event.key == pygame.K_SPACE:
					if color1c.image == color1m.image and color2c.image == color2m.image and color3c.image == color3m.image and color4c.image == color4m.image:
						value1rc = Value1rc()
						value2rc = Value2rc()
						value3rc = Value3rc()
						value4rc = Value4rc()
						all_sprites.add(value1rc, value2rc, value3rc, value4rc)
						tapa.kill()
					
					elif color1c.image != color1m.image and color2c.image != color2m.image and color3c.image != color3m.image and color4c.image != color4m.image:
						pass
					switch141 = False
					switch149 = True
		
		if switch140:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4c.image = img1
					color4c.image.set_colorkey(WHITE)
					switch140 = False
					switch141 = True
				elif event.key == pygame.K_SPACE:
					if color1c.image == color1m.image and color2c.image == color2m.image and color3c.image == color3m.image and color4c.image == color4m.image:
						value1rc = Value1rc()
						value2rc = Value2rc()
						value3rc = Value3rc()
						value4rc = Value4rc()
						all_sprites.add(value1rc, value2rc, value3rc, value4rc)
						tapa.kill()
					
					elif color1c.image != color1m.image and color2c.image != color2m.image and color3c.image != color3m.image and color4c.image != color4m.image:
						pass
					switch140 = False
					switch149 = True

		if switch139:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3c.image = img1
					color3c.image.set_colorkey(WHITE)
					switch139 = False
					switch131 = True
				elif event.key == pygame.K_SPACE:
					color4c = Color4c()
					all_sprites.add(color4c)
					switch139 = False
					switch140 = True		
		
		if switch138:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3c.image = img8
					color3c.image.set_colorkey(WHITE)
					switch138 = False
					switch139 = True
				elif event.key == pygame.K_SPACE:
					color4c = Color4c()
					all_sprites.add(color4c)
					switch138 = False
					switch140 = True
		
		if switch137:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3c.image = img7
					color3c.image.set_colorkey(WHITE)
					switch137 = False
					switch138 = True
				elif event.key == pygame.K_SPACE:
					color4c = Color4c()
					all_sprites.add(color4c)
					switch137 = False
					switch140 = True
		
		if switch136:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3c.image = img6
					color3c.image.set_colorkey(WHITE)
					switch136 = False
					switch137 = True
				elif event.key == pygame.K_SPACE:
					color4c = Color4c()
					all_sprites.add(color4c)
					switch136 = False
					switch140 = True
		
		if switch135:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3c.image = img5
					color3c.image.set_colorkey(WHITE)
					switch135 = False
					switch136 = True
				elif event.key == pygame.K_SPACE:
					color4c = Color4c()
					all_sprites.add(color4c)
					switch135 = False
					switch140 = True
		
		if switch134:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3c.image = img4
					color3c.image.set_colorkey(WHITE)
					switch134 = False
					switch135 = True
				elif event.key == pygame.K_SPACE:
					color4c = Color4c()
					all_sprites.add(color4c)
					switch134 = False
					switch140 = True
		
		if switch133:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3c.image = img3
					color3c.image.set_colorkey(WHITE)
					switch133 = False
					switch134 = True
				elif event.key == pygame.K_SPACE:
					color4c = Color4c()
					all_sprites.add(color4c)
					switch133 = False
					switch140 = True
		
		if switch132:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3c.image = img2
					color3c.image.set_colorkey(WHITE)
					switch132 = False
					switch133 = True
				elif event.key == pygame.K_SPACE:
					color4c = Color4c()
					all_sprites.add(color4c)
					switch132 = False
					switch140 = True


		if switch131:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3c.image = img1
					color3c.image.set_colorkey(WHITE)
					switch131 = False
					switch132 = True
				elif event.key == pygame.K_SPACE:
					color4c = Color4c()
					all_sprites.add(color4c)
					switch131 = False
					switch140 = True

		if switch130:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2c.image = img1
					color2c.image.set_colorkey(WHITE)
					switch130 = False
					switch122 = True
				elif event.key == pygame.K_SPACE:
					color3c = Color3c()
					all_sprites.add(color3c)
					switch130 = False
					switch131 = True

		if switch129:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2c.image = img8
					color2c.image.set_colorkey(WHITE)
					switch129 = False
					switch130 = True
				elif event.key == pygame.K_SPACE:
					color3c = Color3c()
					all_sprites.add(color3c)
					switch129 = False
					switch131 = True
		
		if switch128:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2c.image = img7
					color2c.image.set_colorkey(WHITE)
					switch128 = False
					switch129 = True
				elif event.key == pygame.K_SPACE:
					color3c = Color3c()
					all_sprites.add(color3c)
					switch128 = False
					switch131 = True
		
		if switch127:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2c.image = img6
					color2c.image.set_colorkey(WHITE)
					switch127 = False
					switch128 = True
				elif event.key == pygame.K_SPACE:
					color3c = Color3c()
					all_sprites.add(color3c)
					switch127 = False
					switch131 = True
		
		if switch126:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2c.image = img5
					color2c.image.set_colorkey(WHITE)
					switch126 = False
					switch127 = True
				elif event.key == pygame.K_SPACE:
					color3c = Color3c()
					all_sprites.add(color3c)
					switch126 = False
					switch131 = True
		
		if switch125:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2c.image = img4
					color2c.image.set_colorkey(WHITE)
					switch125 = False
					switch126 = True
				elif event.key == pygame.K_SPACE:
					color3c = Color3c()
					all_sprites.add(color3c)
					switch125 = False
					switch131 = True
		
		if switch124:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2c.image = img3
					color2c.image.set_colorkey(WHITE)
					switch124 = False
					switch125 = True
				elif event.key == pygame.K_SPACE:
					color3c = Color3c()
					all_sprites.add(color3c)
					switch124 = False
					switch131 = True
		
		if switch123:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2c.image = img2
					color2c.image.set_colorkey(WHITE)
					switch123 = False
					switch124 = True
				elif event.key == pygame.K_SPACE:
					color3c = Color3c()
					all_sprites.add(color3c)
					switch123 = False
					switch131 = True

		if switch122:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2c.image = img1
					color2c.image.set_colorkey(WHITE)
					switch122 = False
					switch123 = True
				elif event.key == pygame.K_SPACE:
					color3c = Color3c()
					all_sprites.add(color3c)
					switch122 = False
					switch131 = True

		if switch121:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1c.image = img1
					color1c.image.set_colorkey(WHITE)
					switch121 = False
					switch113 = True
				elif event.key == pygame.K_SPACE:
					color2c = Color2c()
					all_sprites.add(color2c)
					switch121 = False
					switch122 = True

		if switch120:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1c.image = img8
					color1c.image.set_colorkey(WHITE)
					switch120 = False
					switch121 = True
				elif event.key == pygame.K_SPACE:
					color2c = Color2c()
					all_sprites.add(color2c)
					switch120 = False
					switch122 = True

		if switch119:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1c.image = img7
					color1c.image.set_colorkey(WHITE)
					switch119 = False
					switch120 = True
				elif event.key == pygame.K_SPACE:
					color2c = Color2c()
					all_sprites.add(color2c)
					switch119 = False
					switch122 = True
		
		if switch118:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1c.image = img6
					color1c.image.set_colorkey(WHITE)
					switch118 = False
					switch119 = True
				elif event.key == pygame.K_SPACE:
					color2c = Color2c()
					all_sprites.add(color2c)
					switch118 = False
					switch122 = True
		
		if switch117:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1c.image = img5
					color1c.image.set_colorkey(WHITE)
					switch117 = False
					switch118 = True
				elif event.key == pygame.K_SPACE:
					color2c = Color2c()
					all_sprites.add(color2c)
					switch117 = False
					switch122 = True
		
		if switch116:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1c.image = img4
					color1c.image.set_colorkey(WHITE)
					switch116 = False
					switch117 = True
				elif event.key == pygame.K_SPACE:
					color2c = Color2c()
					all_sprites.add(color2c)
					switch116 = False
					switch122 = True
		
		if switch115:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1c.image = img3
					color1c.image.set_colorkey(WHITE)
					switch115 = False
					switch116 = True
				elif event.key == pygame.K_SPACE:
					color2c = Color2c()
					all_sprites.add(color2c)
					switch115 = False
					switch122 = True
		
		if switch114:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1c.image = img2
					color1c.image.set_colorkey(WHITE)
					switch114 = False
					switch115 = True
				elif event.key == pygame.K_SPACE:
					color2c = Color2c()
					all_sprites.add(color2c)
					switch114 = False
					switch122 = True


		if switch113:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1c.image = img1
					color1c.image.set_colorkey(WHITE)
					switch113 = False
					switch114 = True
				elif event.key == pygame.K_SPACE:
					color2c = Color2c()
					all_sprites.add(color2c)
					switch113 = False
					switch122 = True

		if switch112:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1c = Color1c()
					all_sprites.add(color1c)
					switch112 = False
					switch113 = True
	
		if switch111:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4b.image = img1
					color4b.image.set_colorkey(WHITE)
					switch111 = False
					switch103 = True
				elif event.key == pygame.K_SPACE:
					if color1b.image == color1m.image and color2b.image == color2m.image and color3b.image == color3m.image and color4b.image == color4m.image:
						value1rb = Value1rb()
						value2rb = Value2rb()
						value3rb = Value3rb()
						value4rb = Value4rb()
						all_sprites.add(value1rb, value2rb, value3rb, value4rb)
						tapa.kill()
					
					elif color1b.image != color1m.image and color2b.image != color2m.image and color3b.image != color3m.image and color4b.image != color4m.image:
						pass
					switch111 = False
					switch112 = True

		if switch110:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4b.image = img8
					color4b.image.set_colorkey(WHITE)
					switch110 = False
					switch111 = True
				elif event.key == pygame.K_SPACE:
					if color1b.image == color1m.image and color2b.image == color2m.image and color3b.image == color3m.image and color4b.image == color4m.image:
						value1rb = Value1rb()
						value2rb = Value2rb()
						value3rb = Value3rb()
						value4rb = Value4rb()
						all_sprites.add(value1rb, value2rb, value3rb, value4rb)
						tapa.kill()
					
					elif color1b.image != color1m.image and color2b.image != color2m.image and color3b.image != color3m.image and color4b.image != color4m.image:
						pass
					switch110 = False
					switch112 = True
		
		if switch109:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4b.image = img7
					color4b.image.set_colorkey(WHITE)
					switch109 = False
					switch110 = True
				elif event.key == pygame.K_SPACE:
					if color1b.image == color1m.image and color2b.image == color2m.image and color3b.image == color3m.image and color4b.image == color4m.image:
						value1rb = Value1rb()
						value2rb = Value2rb()
						value3rb = Value3rb()
						value4rb = Value4rb()
						all_sprites.add(value1rb, value2rb, value3rb, value4rb)
						tapa.kill()
					
					elif color1b.image != color1m.image and color2b.image != color2m.image and color3b.image != color3m.image and color4b.image != color4m.image:
						pass
					
					switch109 = False
					switch112 = True
		
		if switch108:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4b.image = img6
					color4b.image.set_colorkey(WHITE)
					switch108 = False
					switch109 = True
				elif event.key == pygame.K_SPACE:
					if color1b.image == color1m.image and color2b.image == color2m.image and color3b.image == color3m.image and color4b.image == color4m.image:
						value1rb = Value1rb()
						value2rb = Value2rb()
						value3rb = Value3rb()
						value4rb = Value4rb()
						all_sprites.add(value1rb, value2rb, value3rb, value4rb)
						tapa.kill()
					
					elif color1b.image != color1m.image and color2b.image != color2m.image and color3b.image != color3m.image and color4b.image != color4m.image:
						pass
					switch108 = False
					switch112 = True
		
		if switch107:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4b.image = img5
					color4b.image.set_colorkey(WHITE)
					switch107 = False
					switch108 = True
				elif event.key == pygame.K_SPACE:
					if color1b.image == color1m.image and color2b.image == color2m.image and color3b.image == color3m.image and color4b.image == color4m.image:
						value1rb = Value1rb()
						value2rb = Value2rb()
						value3rb = Value3rb()
						value4rb = Value4rb()
						all_sprites.add(value1rb, value2rb, value3rb, value4rb)
						tapa.kill()
					
					elif color1b.image != color1m.image and color2b.image != color2m.image and color3b.image != color3m.image and color4b.image != color4m.image:
						pass
					switch107 = False
					switch112 = True
		
		if switch106:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4b.image = img4
					color4b.image.set_colorkey(WHITE)
					switch106 = False
					switch107 = True
				elif event.key == pygame.K_SPACE:
					if color1b.image == color1m.image and color2b.image == color2m.image and color3b.image == color3m.image and color4b.image == color4m.image:
						value1rb = Value1rb()
						value2rb = Value2rb()
						value3rb = Value3rb()
						value4rb = Value4rb()
						all_sprites.add(value1rb, value2rb, value3rb, value4rb)
						tapa.kill()
					
					elif color1b.image != color1m.image and color2b.image != color2m.image and color3b.image != color3m.image and color4b.image != color4m.image:
						pass
					switch106 = False
					switch112 = True
		
		if switch105:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4b.image = img3
					color4b.image.set_colorkey(WHITE)
					switch105 = False
					switch106 = True
				elif event.key == pygame.K_SPACE:
					if color1b.image == color1m.image and color2b.image == color2m.image and color3b.image == color3m.image and color4b.image == color4m.image:
						value1rb = Value1rb()
						value2rb = Value2rb()
						value3rb = Value3rb()
						value4rb = Value4rb()
						all_sprites.add(value1rb, value2rb, value3rb, value4rb)
						tapa.kill()
					
					elif color1b.image != color1m.image and color2b.image != color2m.image and color3b.image != color3m.image and color4b.image != color4m.image:
						pass
					switch105 = False
					switch112 = True
		
		if switch104:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4b.image = img2
					color4b.image.set_colorkey(WHITE)
					switch104 = False
					switch105 = True
				elif event.key == pygame.K_SPACE:
					if color1b.image == color1m.image and color2b.image == color2m.image and color3b.image == color3m.image and color4b.image == color4m.image:
						value1rb = Value1rb()
						value2rb = Value2rb()
						value3rb = Value3rb()
						value4rb = Value4rb()
						all_sprites.add(value1rb, value2rb, value3rb, value4rb)
						tapa.kill()
					
					elif color1b.image != color1m.image and color2b.image != color2m.image and color3b.image != color3m.image and color4b.image != color4m.image:
						pass
					switch104 = False
					switch112 = True
		
		if switch103:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4b.image = img1
					color4b.image.set_colorkey(WHITE)
					switch103 = False
					switch104 = True
				elif event.key == pygame.K_SPACE:
					if color1b.image == color1m.image and color2b.image == color2m.image and color3b.image == color3m.image and color4b.image == color4m.image:
						value1rb = Value1rb()
						value2rb = Value2rb()
						value3rb = Value3rb()
						value4rb = Value4rb()
						all_sprites.add(value1rb, value2rb, value3rb, value4rb)
						tapa.kill()
					
					elif color1b.image != color1m.image and color2b.image != color2m.image and color3b.image != color3m.image and color4b.image != color4m.image:
						pass
					switch103 = False
					switch112 = True

		if switch102:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3b.image = img1
					color3b.image.set_colorkey(WHITE)
					switch102 = False
					switch94 = True
				elif event.key == pygame.K_SPACE:
					color4b = Color4b()
					all_sprites.add(color4b)
					switch102 = False
					switch103 = True		
		
		if switch101:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3b.image = img8
					color3b.image.set_colorkey(WHITE)
					switch101 = False
					switch102 = True
				elif event.key == pygame.K_SPACE:
					color4b = Color4b()
					all_sprites.add(color4b)
					switch101 = False
					switch103 = True
		
		if switch100:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3b.image = img7
					color3b.image.set_colorkey(WHITE)
					switch100 = False
					switch101 = True
				elif event.key == pygame.K_SPACE:
					color4b = Color4b()
					all_sprites.add(color4b)
					switch100 = False
					switch103 = True
		
		if switch99:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3b.image = img6
					color3b.image.set_colorkey(WHITE)
					switch99 = False
					switch100 = True
				elif event.key == pygame.K_SPACE:
					color4b = Color4b()
					all_sprites.add(color4b)
					switch99 = False
					switch103 = True
		
		if switch98:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3b.image = img5
					color3b.image.set_colorkey(WHITE)
					switch98 = False
					switch99 = True
				elif event.key == pygame.K_SPACE:
					color4b = Color4b()
					all_sprites.add(color4b)
					switch98 = False
					switch103 = True
		
		if switch97:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3b.image = img4
					color3b.image.set_colorkey(WHITE)
					switch97 = False
					switch98 = True
				elif event.key == pygame.K_SPACE:
					color4b = Color4b()
					all_sprites.add(color4b)
					switch97 = False
					switch103 = True
		
		if switch96:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3b.image = img3
					color3b.image.set_colorkey(WHITE)
					switch96 = False
					switch97 = True
				elif event.key == pygame.K_SPACE:
					color4b = Color4b()
					all_sprites.add(color4b)
					switch96 = False
					switch103 = True
		
		if switch95:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3b.image = img2
					color3b.image.set_colorkey(WHITE)
					switch95 = False
					switch96 = True
				elif event.key == pygame.K_SPACE:
					color4b = Color4b()
					all_sprites.add(color4b)
					switch95 = False
					switch103 = True


		if switch94:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3b.image = img1
					color3b.image.set_colorkey(WHITE)
					switch94 = False
					switch95 = True
				elif event.key == pygame.K_SPACE:
					color4b = Color4b()
					all_sprites.add(color4b)
					switch94 = False
					switch103 = True


		if switch93:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2b.image = img1
					color2b.image.set_colorkey(WHITE)
					switch93 = False
					switch85 = True
				elif event.key == pygame.K_SPACE:
					color3b = Color3b()
					all_sprites.add(color3b)
					switch93 = False
					switch94 = True

		if switch92:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2b.image = img8
					color2b.image.set_colorkey(WHITE)
					switch92 = False
					switch93 = True
				elif event.key == pygame.K_SPACE:
					color3b = Color3b()
					all_sprites.add(color3b)
					switch92 = False
					switch94 = True
		
		if switch91:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2b.image = img7
					color2b.image.set_colorkey(WHITE)
					switch91 = False
					switch92 = True
				elif event.key == pygame.K_SPACE:
					color3b = Color3b()
					all_sprites.add(color3b)
					switch91 = False
					switch94 = True
		
		if switch90:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2b.image = img6
					color2b.image.set_colorkey(WHITE)
					switch90 = False
					switch91 = True
				elif event.key == pygame.K_SPACE:
					color3b = Color3b()
					all_sprites.add(color3b)
					switch90 = False
					switch94 = True
		
		if switch89:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2b.image = img5
					color2b.image.set_colorkey(WHITE)
					switch89 = False
					switch90 = True
				elif event.key == pygame.K_SPACE:
					color3b = Color3b()
					all_sprites.add(color3b)
					switch89 = False
					switch94 = True
		
		if switch88:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2b.image = img4
					color2b.image.set_colorkey(WHITE)
					switch88 = False
					switch89 = True
				elif event.key == pygame.K_SPACE:
					color3b = Color3b()
					all_sprites.add(color3b)
					switch88 = False
					switch94 = True
		
		if switch87:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2b.image = img3
					color2b.image.set_colorkey(WHITE)
					switch87 = False
					switch88 = True
				elif event.key == pygame.K_SPACE:
					color3b = Color3b()
					all_sprites.add(color3b)
					switch87 = False
					switch94 = True
		
		if switch86:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2b.image = img2
					color2b.image.set_colorkey(WHITE)
					switch86 = False
					switch87 = True
				elif event.key == pygame.K_SPACE:
					color3b = Color3b()
					all_sprites.add(color3b)
					switch86 = False
					switch94 = True

		if switch85:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2b.image = img1
					color2b.image.set_colorkey(WHITE)
					switch85 = False
					switch86 = True
				elif event.key == pygame.K_SPACE:
					color3b = Color3b()
					all_sprites.add(color3b)
					switch85 = False
					switch94 = True

		if switch84:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1b.image = img1
					color1b.image.set_colorkey(WHITE)
					switch84 = False
					switch76 = True
				elif event.key == pygame.K_SPACE:
					color2b = Color2b()
					all_sprites.add(color2b)
					switch84 = False
					switch85 = True

		if switch83:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1b.image = img8
					color1b.image.set_colorkey(WHITE)
					switch83 = False
					switch84 = True
				elif event.key == pygame.K_SPACE:
					color2b = Color2b()
					all_sprites.add(color2b)
					switch83 = False
					switch85 = True

		if switch82:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1b.image = img7
					color1b.image.set_colorkey(WHITE)
					switch82 = False
					switch83 = True
				elif event.key == pygame.K_SPACE:
					color2b = Color2b()
					all_sprites.add(color2b)
					switch82 = False
					switch85 = True
		
		if switch81:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1b.image = img6
					color1b.image.set_colorkey(WHITE)
					switch81 = False
					switch82 = True
				elif event.key == pygame.K_SPACE:
					color2b = Color2b()
					all_sprites.add(color2b)
					switch81 = False
					switch85 = True
		
		if switch80:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1b.image = img5
					color1b.image.set_colorkey(WHITE)
					switch80 = False
					switch81 = True
				elif event.key == pygame.K_SPACE:
					color2b = Color2b()
					all_sprites.add(color2b)
					switch80 = False
					switch85 = True
		
		if switch79:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1b.image = img4
					color1b.image.set_colorkey(WHITE)
					switch79 = False
					switch80 = True
				elif event.key == pygame.K_SPACE:
					color2b = Color2b()
					all_sprites.add(color2b)
					switch79 = False
					switch85 = True
		
		if switch78:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1b.image = img3
					color1b.image.set_colorkey(WHITE)
					switch78 = False
					switch79 = True
				elif event.key == pygame.K_SPACE:
					color2b = Color2b()
					all_sprites.add(color2b)
					switch78 = False
					switch85 = True
		
		if switch77:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1b.image = img2
					color1b.image.set_colorkey(WHITE)
					switch77 = False
					switch78 = True
				elif event.key == pygame.K_SPACE:
					color2b = Color2b()
					all_sprites.add(color2b)
					switch77 = False
					switch85 = True


		if switch76:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1b.image = img1
					color1b.image.set_colorkey(WHITE)
					switch76 = False
					switch77 = True
				elif event.key == pygame.K_SPACE:
					color2b = Color2b()
					all_sprites.add(color2b)
					switch76 = False
					switch85 = True

		
		if switch75:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1b = Color1b()
					all_sprites.add(color1b)
					switch75 = False
					switch76 = True

		if switch74:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4a.image = img1
					color4a.image.set_colorkey(WHITE)
					switch74 = False
					switch66 = True
				elif event.key == pygame.K_SPACE:
					if color1a.image == color1m.image and color2a.image == color2m.image and color3a.image == color3m.image and color4a.image == color4m.image:
						value1ra = Value1ra()
						value2ra = Value2ra()
						value3ra = Value3ra()
						value4ra = Value4ra()
						all_sprites.add(value1ra, value2ra, value3ra, value4ra)
						tapa.kill()
					
					elif color1a.image != color1m.image and color2a.image != color2m.image and color3a.image != color3m.image and color4a.image != color4m.image:
						pass
					switch74 = False
					switch75 = True

		if switch73:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4a.image = img8
					color4a.image.set_colorkey(WHITE)
					switch73 = False
					switch74 = True
				elif event.key == pygame.K_SPACE:
					if color1a.image == color1m.image and color2a.image == color2m.image and color3a.image == color3m.image and color4a.image == color4m.image:
						value1ra = Value1ra()
						value2ra = Value2ra()
						value3ra = Value3ra()
						value4ra = Value4ra()
						all_sprites.add(value1ra, value2ra, value3ra, value4ra)
						tapa.kill()
					
					elif color1a.image != color1m.image and color2a.image != color2m.image and color3a.image != color3m.image and color4a.image != color4m.image:
						pass
					switch73 = False
					switch75 = True
		
		if switch72:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4a.image = img7
					color4a.image.set_colorkey(WHITE)
					switch72 = False
					switch73 = True
				elif event.key == pygame.K_SPACE:
					if color1a.image == color1m.image and color2a.image == color2m.image and color3a.image == color3m.image and color4a.image == color4m.image:
						value1ra = Value1ra()
						value2ra = Value2ra()
						value3ra = Value3ra()
						value4ra = Value4ra()
						all_sprites.add(value1ra, value2ra, value3ra, value4ra)
						tapa.kill()
					
					elif color1a.image != color1m.image and color2a.image != color2m.image and color3a.image != color3m.image and color4a.image != color4m.image:
						pass
					switch72 = False
					switch75 = True
		
		if switch71:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4a.image = img6
					color4a.image.set_colorkey(WHITE)
					switch71 = False
					switch72 = True
				elif event.key == pygame.K_SPACE:
					if color1a.image == color1m.image and color2a.image == color2m.image and color3a.image == color3m.image and color4a.image == color4m.image:
						value1ra = Value1ra()
						value2ra = Value2ra()
						value3ra = Value3ra()
						value4ra = Value4ra()
						all_sprites.add(value1ra, value2ra, value3ra, value4ra)
						tapa.kill()
					
					elif color1a.image != color1m.image and color2a.image != color2m.image and color3a.image != color3m.image and color4a.image != color4m.image:
						pass
					switch70 = False
					switch75 = True
		
		if switch69:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4a.image = img4
					color4a.image.set_colorkey(WHITE)
					switch69 = False
					switch70 = True
				elif event.key == pygame.K_SPACE:
					if color1a.image == color1m.image and color2a.image == color2m.image and color3a.image == color3m.image and color4a.image == color4m.image:
						value1ra = Value1ra()
						value2ra = Value2ra()
						value3ra = Value3ra()
						value4ra = Value4ra()
						all_sprites.add(value1ra, value2ra, value3ra, value4ra)
						tapa.kill()
					
					elif color1a.image != color1m.image and color2a.image != color2m.image and color3a.image != color3m.image and color4a.image != color4m.image:
						pass
					switch69 = False
					switch75 = True
		
		if switch68:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4a.image = img3
					color4a.image.set_colorkey(WHITE)
					switch68 = False
					switch69 = True
				elif event.key == pygame.K_SPACE:
					if color1a.image == color1m.image and color2a.image == color2m.image and color3a.image == color3m.image and color4a.image == color4m.image:
						value1ra = Value1ra()
						value2ra = Value2ra()
						value3ra = Value3ra()
						value4ra = Value4ra()
						all_sprites.add(value1ra, value2ra, value3ra, value4ra)
						tapa.kill()
					
					elif color1a.image != color1m.image and color2a.image != color2m.image and color3a.image != color3m.image and color4a.image != color4m.image:
						pass
					switch68 = False
					switch75 = True
		
		if switch67:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4a.image = img2
					color4a.image.set_colorkey(WHITE)
					switch67 = False
					switch68 = True
				elif event.key == pygame.K_SPACE:
					if color1a.image == color1m.image and color2a.image == color2m.image and color3a.image == color3m.image and color4a.image == color4m.image:
						value1ra = Value1ra()
						value2ra = Value2ra()
						value3ra = Value3ra()
						value4ra = Value4ra()
						all_sprites.add(value1ra, value2ra, value3ra, value4ra)
						tapa.kill()
					
					elif color1a.image != color1m.image and color2a.image != color2m.image and color3a.image != color3m.image and color4a.image != color4m.image:
						pass
					switch67 = False
					switch75 = True
		
		if switch66:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4a.image = img1
					color4a.image.set_colorkey(WHITE)
					switch66 = False
					switch67 = True
				elif event.key == pygame.K_SPACE:
					if color1a.image == color1m.image and color2a.image == color2m.image and color3a.image == color3m.image and color4a.image == color4m.image:
						value1ra = Value1ra()
						value2ra = Value2ra()
						value3ra = Value3ra()
						value4ra = Value4ra()
						all_sprites.add(value1ra, value2ra, value3ra, value4ra)
						tapa.kill()
					
					elif color1a.image != color1m.image and color2a.image != color2m.image and color3a.image != color3m.image and color4a.image != color4m.image:
						pass
					switch66 = False
					switch75 = True


		if switch65:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3a.image = img1
					color3a.image.set_colorkey(WHITE)
					switch65 = False
					switch57 = True
				elif event.key == pygame.K_SPACE:
					color4a = Color4a()
					all_sprites.add(color4a)
					switch65 = False
					switch66 = True

		if switch64:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3a.image = img8
					color3a.image.set_colorkey(WHITE)
					switch64 = False
					switch65 = True
				elif event.key == pygame.K_SPACE:
					color4a = Color4a()
					all_sprites.add(color4a)
					switch64 = False
					switch66 = True
		
		if switch63:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3a.image = img7
					color3a.image.set_colorkey(WHITE)
					switch63 = False
					switch64 = True
				elif event.key == pygame.K_SPACE:
					color4a = Color4a()
					all_sprites.add(color4a)
					switch63 = False
					switch66 = True
		
		if switch62:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3a.image = img6
					color3a.image.set_colorkey(WHITE)
					switch62 = False
					switch63 = True
				elif event.key == pygame.K_SPACE:
					color4a = Color4a()
					all_sprites.add(color4a)
					switch62 = False
					switch66 = True
		
		if switch61:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3a.image = img5
					color3a.image.set_colorkey(WHITE)
					switch61 = False
					switch62 = True
				elif event.key == pygame.K_SPACE:
					color4a = Color4a()
					all_sprites.add(color4a)
					switch61 = False
					switch66 = True
		
		if switch60:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3a.image = img4
					color3a.image.set_colorkey(WHITE)
					switch60 = False
					switch61 = True
				elif event.key == pygame.K_SPACE:
					color4a = Color4a()
					all_sprites.add(color4a)
					switch60 = False
					switch66 = True
		
		if switch59:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3a.image = img3
					color3a.image.set_colorkey(WHITE)
					switch59 = False
					switch60 = True
				elif event.key == pygame.K_SPACE:
					color4a = Color4a()
					all_sprites.add(color4a)
					switch59 = False
					switch66 = True
		
		if switch58:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3a.image = img2
					color3a.image.set_colorkey(WHITE)
					switch58 = False
					switch59 = True
				elif event.key == pygame.K_SPACE:
					color4a = Color4a()
					all_sprites.add(color4a)
					switch58 = False
					switch66 = True


		if switch57:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3a.image = img1
					color3a.image.set_colorkey(WHITE)
					switch57 = False
					switch58 = True
				elif event.key == pygame.K_SPACE:
					color4a = Color4a()
					all_sprites.add(color4a)
					switch57 = False
					switch66 = True

		if switch56:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2a.image = img1
					color2a.image.set_colorkey(WHITE)
					switch56 = False
					switch48 = True
				elif event.key == pygame.K_SPACE:
					color3a = Color3a()
					all_sprites.add(color3a)
					switch56 = False
					switch57 = True

		if switch55:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2a.image = img8
					color2a.image.set_colorkey(WHITE)
					switch55 = False
					switch56 = True
				elif event.key == pygame.K_SPACE:
					color3a = Color3a()
					all_sprites.add(color3a)
					switch55 = False
					switch57 = True
		
		if switch54:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2a.image = img7
					color2a.image.set_colorkey(WHITE)
					switch54 = False
					switch55 = True
				elif event.key == pygame.K_SPACE:
					color3a = Color3a()
					all_sprites.add(color3a)
					switch54 = False
					switch57 = True
		
		if switch53:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2a.image = img6
					color2a.image.set_colorkey(WHITE)
					switch53 = False
					switch54 = True
				elif event.key == pygame.K_SPACE:
					color3a = Color3a()
					all_sprites.add(color3a)
					switch53 = False
					switch57 = True
		
		if switch52:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2a.image = img5
					color2a.image.set_colorkey(WHITE)
					switch52 = False
					switch53 = True
				elif event.key == pygame.K_SPACE:
					color3a = Color3a()
					all_sprites.add(color3a)
					switch52 = False
					switch57 = True
		
		if switch51:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2a.image = img4
					color2a.image.set_colorkey(WHITE)
					switch51 = False
					switch52 = True
				elif event.key == pygame.K_SPACE:
					color3a = Color3a()
					all_sprites.add(color3a)
					switch51 = False
					switch57 = True
		
		if switch50:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2a.image = img3
					color2a.image.set_colorkey(WHITE)
					switch50 = False
					switch51 = True
				elif event.key == pygame.K_SPACE:
					color3a = Color3a()
					all_sprites.add(color3a)
					switch50 = False
					switch57 = True
		
		if switch49:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2a.image = img2
					color2a.image.set_colorkey(WHITE)
					switch49 = False
					switch50 = True
				elif event.key == pygame.K_SPACE:
					color3a = Color3a()
					all_sprites.add(color3a)
					switch49 = False
					switch57 = True

		if switch48:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2a.image = img1
					color2a.image.set_colorkey(WHITE)
					switch48 = False
					switch49 = True
				elif event.key == pygame.K_SPACE:
					color3a = Color3a()
					all_sprites.add(color3a)
					switch48 = False
					switch57 = True

		if switch47:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1a.image = img1
					color1a.image.set_colorkey(WHITE)
					switch47 = False
					switch39 = True
				elif event.key == pygame.K_SPACE:
					color2a = Color2a()
					all_sprites.add(color2a)
					switch47 = False
					switch48 = True

		if switch46:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1a.image = img8
					color1a.image.set_colorkey(WHITE)
					switch46 = False
					switch47 = True
				elif event.key == pygame.K_SPACE:
					color2a = Color2a()
					all_sprites.add(color2a)
					switch46 = False
					switch48 = True

		if switch45:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1a.image = img7
					color1a.image.set_colorkey(WHITE)
					switch45 = False
					switch46 = True
				elif event.key == pygame.K_SPACE:
					color2a = Color2a()
					all_sprites.add(color2a)
					switch45 = False
					switch48 = True
		
		if switch44:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1a.image = img6
					color1a.image.set_colorkey(WHITE)
					switch44 = False
					switch45 = True
				elif event.key == pygame.K_SPACE:
					color2a = Color2a()
					all_sprites.add(color2a)
					switch44 = False
					switch48 = True
		
		if switch43:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1a.image = img5
					color1a.image.set_colorkey(WHITE)
					switch43 = False
					switch44 = True
				elif event.key == pygame.K_SPACE:
					color2a = Color2a()
					all_sprites.add(color2a)
					switch43 = False
					switch48 = True
		
		if switch42:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1a.image = img4
					color1a.image.set_colorkey(WHITE)
					switch42 = False
					switch43 = True
				elif event.key == pygame.K_SPACE:
					color2a = Color2a()
					all_sprites.add(color2a)
					switch42 = False
					switch48 = True
		
		if switch41:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1a.image = img3
					color1a.image.set_colorkey(WHITE)
					switch41 = False
					switch42 = True
				elif event.key == pygame.K_SPACE:
					color2a = Color2a()
					all_sprites.add(color2a)
					switch41 = False
					switch48 = True
		
		if switch40:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1a.image = img2
					color1a.image.set_colorkey(WHITE)
					switch40 = False
					switch41 = True
				elif event.key == pygame.K_SPACE:
					color2a = Color2a()
					all_sprites.add(color2a)
					switch40 = False
					switch48 = True


		if switch39:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1a.image = img1
					color1a.image.set_colorkey(WHITE)
					switch39 = False
					switch40 = True
				elif event.key == pygame.K_SPACE:
					color2a = Color2a()
					all_sprites.add(color2a)
					switch39 = False
					switch48 = True


		if switch38:
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1a = Color1a()
					all_sprites.add(color1a)
					switch38 = False
					switch39 = True
	
		if switch37:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4.image = img1
					color4.image.set_colorkey(WHITE)
					switch37 = False
					switch29 = True
				elif event.key == pygame.K_SPACE:
					if color1.image == color1m.image and color2.image == color2m.image and color3.image == color3m.image and color4.image == color4m.image:
						value1r = Value1r()
						value2r = Value2r()
						value3r = Value3r()
						value4r = Value4r()
						all_sprites.add(value1r, value2r, value3r, value4r)
						tapa.kill()
					
					elif color1.image != color1m.image and color2.image != color2m.image and color3.image != color3m.image and color4.image != color4m.image:
						pass
					switch37 = False
					switch38 = True

		if switch36:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4.image = img8
					color4.image.set_colorkey(WHITE)
					switch36 = False
					switch37 = True
				elif event.key == pygame.K_SPACE:
					if color1.image == color1m.image and color2.image == color2m.image and color3.image == color3m.image and color4.image == color4m.image:
						value1r = Value1r()
						value2r = Value2r()
						value3r = Value3r()
						value4r = Value4r()
						all_sprites.add(value1r, value2r, value3r, value4r)
						tapa.kill()
					
					elif color1.image != color1m.image and color2.image != color2m.image and color3.image != color3m.image and color4.image != color4m.image:
						pass
					switch36 = False
					switch38 = True
		
		if switch35:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4.image = img7
					color4.image.set_colorkey(WHITE)
					switch35 = False
					switch36 = True
				elif event.key == pygame.K_SPACE:
					if color1.image == color1m.image and color2.image == color2m.image and color3.image == color3m.image and color4.image == color4m.image:
						value1r = Value1r()
						value2r = Value2r()
						value3r = Value3r()
						value4r = Value4r()
						all_sprites.add(value1r, value2r, value3r, value4r)
						tapa.kill()
					
					elif color1.image != color1m.image and color2.image != color2m.image and color3.image != color3m.image and color4.image != color4m.image:
						pass
					
					switch35 = False
					switch38 = True
		
		if switch34:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4.image = img6
					color4.image.set_colorkey(WHITE)
					switch34 = False
					switch35 = True
				elif event.key == pygame.K_SPACE:
					if color1.image == color1m.image and color2.image == color2m.image and color3.image == color3m.image and color4.image == color4m.image:
						value1r = Value1r()
						value2r = Value2r()
						value3r = Value3r()
						value4r = Value4r()
						all_sprites.add(value1r, value2r, value3r, value4r)
						tapa.kill()
					
					elif color1.image != color1m.image and color2.image != color2m.image and color3.image != color3m.image and color4.image != color4m.image:
						pass
					switch34 = False
					switch38 = True
		
		if switch33:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4.image = img5
					color4.image.set_colorkey(WHITE)
					switch33 = False
					switch34 = True
				elif event.key == pygame.K_SPACE:
					if color1.image == color1m.image and color2.image == color2m.image and color3.image == color3m.image and color4.image == color4m.image:
						value1r = Value1r()
						value2r = Value2r()
						value3r = Value3r()
						value4r = Value4r()
						all_sprites.add(value1r, value2r, value3r, value4r)
						tapa.kill()
					
					elif color1.image != color1m.image and color2.image != color2m.image and color3.image != color3m.image and color4.image != color4m.image:
						pass
					switch33 = False
					switch38 = True
		
		if switch32:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4.image = img4
					color4.image.set_colorkey(WHITE)
					switch32 = False
					switch33 = True
				elif event.key == pygame.K_SPACE:
					if color1.image == color1m.image and color2.image == color2m.image and color3.image == color3m.image and color4.image == color4m.image:
						value1r = Value1r()
						value2r = Value2r()
						value3r = Value3r()
						value4r = Value4r()
						all_sprites.add(value1r, value2r, value3r, value4r)
						tapa.kill()
					
					elif color1.image != color1m.image and color2.image != color2m.image and color3.image != color3m.image and color4.image != color4m.image:
						pass
					switch32 = False
					switch38 = True
		
		if switch31:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4.image = img3
					color4.image.set_colorkey(WHITE)
					switch31 = False
					switch32 = True
				elif event.key == pygame.K_SPACE:
					if color1.image == color1m.image and color2.image == color2m.image and color3.image == color3m.image and color4.image == color4m.image:
						value1r = Value1r()
						value2r = Value2r()
						value3r = Value3r()
						value4r = Value4r()
						all_sprites.add(value1r, value2r, value3r, value4r)
						tapa.kill()
					
					elif color1.image != color1m.image and color2.image != color2m.image and color3.image != color3m.image and color4.image != color4m.image:
						pass
					switch31 = False
					switch38 = True
		
		if switch30:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4.image = img2
					color4.image.set_colorkey(WHITE)
					switch30 = False
					switch31 = True
				elif event.key == pygame.K_SPACE:
					if color1.image == color1m.image and color2.image == color2m.image and color3.image == color3m.image and color4.image == color4m.image:
						value1r = Value1r()
						value2r = Value2r()
						value3r = Value3r()
						value4r = Value4r()
						all_sprites.add(value1r, value2r, value3r, value4r)
						tapa.kill()
					
					elif color1.image != color1m.image and color2.image != color2m.image and color3.image != color3m.image and color4.image != color4m.image:
						pass
					switch30 = False
					switch38 = True
		
		if switch29:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color4.image = img1
					color4.image.set_colorkey(WHITE)
					switch29 = False
					switch30 = True
				elif event.key == pygame.K_SPACE:
					if color1.image == color1m.image and color2.image == color2m.image and color3.image == color3m.image and color4.image == color4m.image:
						value1r = Value1r()
						value2r = Value2r()
						value3r = Value3r()
						value4r = Value4r()
						all_sprites.add(value1r, value2r, value3r, value4r)
						tapa.kill()
					
					elif color1.image != color1m.image and color2.image != color2m.image and color3.image != color3m.image and color4.image != color4m.image:
						pass
					switch29 = False
					switch38 = True

		if switch28:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3.image = img1
					color3.image.set_colorkey(WHITE)
					switch28 = False
					switch21 = True
				elif event.key == pygame.K_SPACE:
					color4 = Color4()
					all_sprites.add(color4)
					switch28 = False
					switch29 = True		
		
		if switch27:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3.image = img8
					color3.image.set_colorkey(WHITE)
					switch27 = False
					switch28 = True
				elif event.key == pygame.K_SPACE:
					color4 = Color4()
					all_sprites.add(color4)
					switch27 = False
					switch29 = True
		
		if switch26:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3.image = img7
					color3.image.set_colorkey(WHITE)
					switch26 = False
					switch27 = True
				elif event.key == pygame.K_SPACE:
					color4 = Color4()
					all_sprites.add(color4)
					switch26 = False
					switch29 = True
		
		if switch25:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3.image = img6
					color3.image.set_colorkey(WHITE)
					switch25 = False
					switch26 = True
				elif event.key == pygame.K_SPACE:
					color4 = Color4()
					all_sprites.add(color4)
					switch25 = False
					switch29 = True
		
		if switch24:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3.image = img5
					color3.image.set_colorkey(WHITE)
					switch24 = False
					switch25 = True
				elif event.key == pygame.K_SPACE:
					color4 = Color4()
					all_sprites.add(color4)
					switch24 = False
					switch29 = True
		
		if switch23:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3.image = img4
					color3.image.set_colorkey(WHITE)
					switch23 = False
					switch24 = True
				elif event.key == pygame.K_SPACE:
					color4 = Color4()
					all_sprites.add(color4)
					switch23 = False
					switch29 = True
		
		if switch22:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3.image = img3
					color3.image.set_colorkey(WHITE)
					switch22 = False
					switch23 = True
				elif event.key == pygame.K_SPACE:
					color4 = Color4()
					all_sprites.add(color4)
					switch22 = False
					switch29 = True
		
		if switch21:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3.image = img2
					color3.image.set_colorkey(WHITE)
					switch21 = False
					switch22 = True
				elif event.key == pygame.K_SPACE:
					color4 = Color4()
					all_sprites.add(color4)
					switch21 = False
					switch29 = True


		if switch20:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color3.image = img1
					color3.image.set_colorkey(WHITE)
					switch20 = False
					switch21 = True
				elif event.key == pygame.K_SPACE:
					color4 = Color4()
					all_sprites.add(color4)
					switch20 = False
					switch29 = True

		if switch19:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2.image = img1
					color2.image.set_colorkey(WHITE)
					switch19 = False
					switch11 = True
				elif event.key == pygame.K_SPACE:
					color3 = Color3()
					all_sprites.add(color3)
					switch19 = False
					switch20 = True

		if switch18:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2.image = img8
					color2.image.set_colorkey(WHITE)
					switch18 = False
					switch19 = True
				elif event.key == pygame.K_SPACE:
					color3 = Color3()
					all_sprites.add(color3)
					switch18 = False
					switch20 = True
		
		if switch17:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2.image = img7
					color2.image.set_colorkey(WHITE)
					switch17 = False
					switch18 = True
				elif event.key == pygame.K_SPACE:
					color3 = Color3()
					all_sprites.add(color3)
					switch17 = False
					switch20 = True
		
		if switch16:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2.image = img6
					color2.image.set_colorkey(WHITE)
					switch16 = False
					switch17 = True
				elif event.key == pygame.K_SPACE:
					color3 = Color3()
					all_sprites.add(color3)
					switch16 = False
					switch20 = True
		
		if switch15:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2.image = img5
					color2.image.set_colorkey(WHITE)
					switch15 = False
					switch16 = True
				elif event.key == pygame.K_SPACE:
					color3 = Color3()
					all_sprites.add(color3)
					switch15 = False
					switch20 = True
		
		if switch14:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2.image = img4
					color2.image.set_colorkey(WHITE)
					switch14 = False
					switch15 = True
				elif event.key == pygame.K_SPACE:
					color3 = Color3()
					all_sprites.add(color3)
					switch14 = False
					switch20 = True
		
		if switch13:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2.image = img3
					color2.image.set_colorkey(WHITE)
					switch13 = False
					switch14 = True
				elif event.key == pygame.K_SPACE:
					color3 = Color3()
					all_sprites.add(color3)
					switch13 = False
					switch20 = True
		
		if switch12:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2.image = img2
					color2.image.set_colorkey(WHITE)
					switch12 = False
					switch13 = True
				elif event.key == pygame.K_SPACE:
					color3 = Color3()
					all_sprites.add(color3)
					switch12 = False
					switch20 = True

		if switch11:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color2.image = img1
					color2.image.set_colorkey(WHITE)
					switch11 = False
					switch12 = True
				elif event.key == pygame.K_SPACE:
					color3 = Color3()
					all_sprites.add(color3)
					switch11 = False
					switch20 = True

		if switch10:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1.image = img1
					color1.image.set_colorkey(WHITE)
					switch10 = False
					switch2 = True
				elif event.key == pygame.K_SPACE:
					color2 = Color2()
					all_sprites.add(color2)
					switch10 = False
					switch11 = True

		if switch9:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1.image = img8
					color1.image.set_colorkey(WHITE)
					switch9 = False
					switch10 = True
				elif event.key == pygame.K_SPACE:
					color2 = Color2()
					all_sprites.add(color2)
					switch9 = False
					switch11 = True

		if switch8:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1.image = img7
					color1.image.set_colorkey(WHITE)
					switch8 = False
					switch9 = True
				elif event.key == pygame.K_SPACE:
					color2 = Color2()
					all_sprites.add(color2)
					switch8 = False
					switch11 = True
		
		if switch7:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1.image = img6
					color1.image.set_colorkey(WHITE)
					switch7 = False
					switch8 = True
				elif event.key == pygame.K_SPACE:
					color2 = Color2()
					all_sprites.add(color2)
					switch7 = False
					switch11 = True
		
		if switch6:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1.image = img5
					color1.image.set_colorkey(WHITE)
					switch6 = False
					switch7 = True
				elif event.key == pygame.K_SPACE:
					color2 = Color2()
					all_sprites.add(color2)
					switch6 = False
					switch11 = True
		
		if switch5:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1.image = img4
					color1.image.set_colorkey(WHITE)
					switch5 = False
					switch6 = True
				elif event.key == pygame.K_SPACE:
					color2 = Color2()
					all_sprites.add(color2)
					switch5 = False
					switch11 = True
		
		if switch4:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1.image = img3
					color1.image.set_colorkey(WHITE)
					switch4 = False
					switch5 = True
				elif event.key == pygame.K_SPACE:
					color2 = Color2()
					all_sprites.add(color2)
					switch4 = False
					switch11 = True
		
		if switch3:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1.image = img2
					color1.image.set_colorkey(WHITE)
					switch3 = False
					switch4 = True
				elif event.key == pygame.K_SPACE:
					color2 = Color2()
					all_sprites.add(color2)
					switch3 = False
					switch11 = True


		if switch2:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1.image = img1
					color1.image.set_colorkey(WHITE)
					switch2 = False
					switch3 = True
				elif event.key == pygame.K_SPACE:
					color2 = Color2()
					all_sprites.add(color2)
					switch2 = False
					switch11 = True
		


		if switch1:
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					color1 = Color1()
					all_sprites.add(color1)
					switch1 = False
					switch2 = True
	
	
	if game_over:
		game_over = False
		show_go_screen()
		screen.fill(BLACK)			
		color1m = Color1m()
		color2m = Color2m()
		color3m = Color3m()
		color4m = Color4m()
		tapa = Tapa()
		all_sprites.add(color1m, color2m, color3m, color4m, tapa)	
		master.add(color1m, color2m, color3m, color4m)
		
		switch1 = True
		

	# Update
	all_sprites.update()

	#Draw / Render
	screen.blit(background, [0, 0])
	all_sprites.draw(screen)

	pygame.display.flip()

pygame.quit()
#Importing Some Matrix Mathematical Magical Modules :D 
import numpy as np
import pygame
import random
from nn_stuffs import *



pygame.init()
#Getting a Pygame Window for Seeing our Predictor in Action
width = 800
height = 500
init = pygame.display.init()
screen=pygame.display.set_mode([width,height])
pygame.display.set_caption("Neural Network Based Colour Predictor")
run = True
r , g , b = 0,0,0
my_nn = Neural_Network(3,3,2)


def pre_made_func(r,g,b):
	return my_nn.predict([r/255,g/255,b/255])

which = pre_made_func(r,g,b)



while run:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	keys = pygame.key.get_pressed()
	mouse = pygame.mouse.get_pressed()
	mouse_pos =  pygame.mouse.get_pos()
	if mouse[0] == 1:
		r , g , b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
	which = pre_made_func(r,g,b)
	def train_nn(r,g,b):
		inputs = [r/255,g/255,b/255]
		target = [0,0]
		if mouse_pos[0] < width//2:
			target = [1,0]
		elif mouse_pos[0] > width//2:
			target = [0,1]
		my_nn.train([r/255,g/255,b/255],target)
	if keys[pygame.K_SPACE]:
		train_nn(r,g,b)
	

	

	pygame.draw.rect(screen,(r,g,b),(0,0 ,width,height))
	my_fonts = pygame.font.SysFont("Arial",80,1)
	black_txt = my_fonts.render("Black",1,(0,0,0))
	white_txt = my_fonts.render("White",1,(255,255,255))
	pygame.draw.line(screen,(255,70,70),[width//2,0],[width//2,height],10)
	if which == (0,0,0):
		pygame.draw.circle(screen,which,[20*2,height//2+20],20,20)
	
	else:
		pygame.draw.circle(screen,which,[int(width//1.4),height//2+20],20,20)

	screen.blit(black_txt,(20,height//2-80))
	screen.blit(white_txt,(width//1.4,height//2-80))
	
	pygame.display.update()

            	
	
	
pygame.quit()

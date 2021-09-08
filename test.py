# -*- coding:utf-8 -*-
import sys  
import pygame 
import random


class Bird(object):
	def __init__(self):
		self.birdRect = pygame.Rect(25,20,20,20)
		birdLiveImage = pygame.image.load("2.webp")
		birdLiveImage = pygame.transform.scale(birdLiveImage,(80,60))
		birdDeadImage = pygame.image.load("dead.jfif")
		birdDeadImage = pygame.transform.scale(birdDeadImage,(80,60))
		self.birdStatus = [birdLiveImage,
							birdLiveImage,
							birdDeadImage]
		self.status = 0
		self.birdX = 120
		self.birdY = 350
		self.jump = False
		self.jumpSpeed = 10
		self.gravity = 5
		self.dead = False

	def birdUpdate(self):
		if self.jump:
			self.jumpSpeed -= 1
			self.birdY -= self.jumpSpeed
		else:
			self.gravity += 0.2
			self.birdY += self.gravity
		self.birdRect[1] = self.birdY

class Pipeline(object):
	def __init__(self):
		self.wallx = 400
		pineUpImage = pygame.image.load("jg.jfif")
		pineUpImage = pygame.transform.scale(pineUpImage,(200,100))
		self.pineUp = pineUpImage
		pineDownImage = pygame.image.load("jg2.webp")
		pineDownImage = pygame.transform.scale(pineDownImage,(200,100))
		self.pineDown = pineDownImage

	def updatePipeline(self):
		self.wallx -= 5
		if self.wallx < -80:
			global score
			score += 1
			self.wallx = 400


def createMap():
	screen.fill((255, 255, 255)) 
	screen.blit(background, (0, 0))  
	pygame.display.update()  
	screen.blit(Pipeline.pineUp, (Pipeline.wallx, 100))   
	screen.blit(Pipeline.pineDown, (Pipeline.wallx, 500))  
	Pipeline.updatePipeline()  

	if Bird.dead:             
		Bird.status = 2
	elif Bird.jump:            
		Bird.status = 1
	screen.blit(Bird.birdStatus[Bird.status], (Bird.birdX, Bird.birdY))             
	Bird.birdUpdate()     

	screen.blit(font.render('Score:' + str(score), -1, (255, 255, 255)), (100, 50))  
	pygame.display.update() 

def checkDead():
	upRect = pygame.Rect(Pipeline.wallx, 100,
						Pipeline.pineUp.get_width() - 10,
						Pipeline.pineUp.get_height())

	downRect = pygame.Rect(Pipeline.wallx, 500,
							Pipeline.pineDown.get_width() - 10,
							Pipeline.pineDown.get_height())
	if upRect.colliderect(Bird.birdRect) or downRect.colliderect(Bird.birdRect):
		Bird.dead = True
	if not 0 < Bird.birdRect[1] < height:
		Bird.dead = True
		return True
	else:
		return False
		
def getResutl():
	final_text1 = "Game Over"
	final_text2 = "Your final score is:  " + str(score)
	ft1_font = pygame.font.SysFont("Arial", 70)                                      
	ft1_surf = font.render(final_text1, 1, (242, 3, 36))                             
	ft2_font = pygame.font.SysFont("Arial", 50)                                     
	ft2_surf = font.render(final_text2, 1, (253, 177, 6))                            
	screen.blit(ft1_surf, [screen.get_width() / 2 - ft1_surf.get_width() / 2, 100])  
	screen.blit(ft2_surf, [screen.get_width() / 2 - ft2_surf.get_width() / 2, 200])  
	pygame.display.flip()   



if __name__ == '__main__':
	pygame.init()                           
	pygame.font.init()                     
	font = pygame.font.SysFont("Arial", 50) 
	size = width, height = 400, 650         
	screen = pygame.display.set_mode(size)   
	clock = pygame.time.Clock()              
	Pipeline = Pipeline()                    
	Bird = Bird()                            
	score = 0
	while True:
		clock.tick(60)                  
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			if (event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN) and not Bird.dead:
				Bird.jump = True             
				Bird.gravity = 5             
				Bird.jumpSpeed = 10          

		background = pygame.image.load("D:\\ga\\bg.png")  
		if checkDead():                      
			getResutl()                      
			Bird.status = 2
		else:
			createMap()                      
	pygame.quit()


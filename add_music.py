import pygame

#explosion_sound = pygame.mixer.sound("BigExplosion.mp3")
#explosion_sound.play()
#click_sound = pygame.mixer.Sound("ButtonClick.mp3")
#engine_pickup_sound = pygame.mixer.Sound("EnginePickup.mp3")
#item_pickup_sound = pygame.mixer.Sound("ItemPickup.mp3")
#portal_sound = pygame.mixer.Sound("Portal.mp3")
#powerup_sound = pygame.mixer.Sound("powerup.mp3")
#walking_sound = pygame.mixer.Sound("Walking.mp3")

#import webbrowser
#webbrowser.open("C:/Users/HP/Documents/Virtual Machines/python2020/pyweek/BigExplosion.mp3")

from pygame import mixer 

# Starting the mixer 
mixer.init() 

# Loading the song 
mixer.music.load("C:/Users/HP/Documents/Virtual Machines/python2020/pyweek/BigExplosion.mp3") 

# Setting the volume 
mixer.music.set_volume(0.7) 

# Start playing the song 
mixer.music.play() 

print("completed")

# infinite loop 
while False: 
	
	print("Press 'p' to pause, 'r' to resume") 
	print("Press 'e' to exit the program") 
	query = input(" ") 
	
	if query == 'p': 

		# Pausing the music 
		mixer.music.pause()	 
	elif query == 'r': 

		# Resuming the music 
		mixer.music.unpause() 
	elif query == 'e': 

		# Stop the mixer 
		mixer.music.stop() 
		break

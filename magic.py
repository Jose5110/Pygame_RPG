import pygame
from settings import *
from random import randint
from os.path import join

class MagicPlayer:
	def __init__(self, animation_player):
		self.animation_player = animation_player
		self.sounds = {
		'heal': pygame.mixer.Sound(join('.','assets','audio','heal.wav')),
		'flame': pygame.mixer.Sound(join('.','assets','audio','Fire.wav')),
		}

	def heal(self, player, strength, cost, groups):
		offset = pygame.math.Vector2(0,50)
		
		# if player.energy >= cost and player.health != player.stats['health']:
		if player.energy >= cost:
			player.health += strength
			player.energy -= cost
			self.sounds['heal'].play()
			self.sounds['heal'].set_volume(0.4)
			if player.health >= player.stats['health']:
				player.health = player.stats['health']

			self.animation_player.create_particles(player.rect.center - offset,'heal',groups)
			self.animation_player.create_particles(player.rect.center,'aura',groups)

	def flame(self, player, cost, groups):
		if player.energy >= cost:
			player.energy -= cost
			self.sounds['flame'].play()
			self.sounds['flame'].set_volume(0.1)

		if player.status.split('_')[0] == 'right': direction = pygame.math.Vector2(1,0)
		elif player.status.split('_')[0] == 'left': direction = pygame.math.Vector2(-1,0)
		elif player.status.split('_')[0] == 'up': direction = pygame.math.Vector2(0,-1)
		else: direction = pygame.math.Vector2(0,1)

		for i in range(1,6):
			if direction.x:
				offset_x = (direction.x * i) * TILE_SIZE
				x = player.rect.centerx + offset_x + randint(-TILE_SIZE // 3, TILE_SIZE // 3)
				y = player.rect.centery + randint(-TILE_SIZE // 3, TILE_SIZE // 3)
				self.animation_player.create_particles((x,y), 'flame', groups)
			else:
				offset_y = (direction.y * i) * TILE_SIZE
				x = player.rect.centerx +  randint(-TILE_SIZE // 3, TILE_SIZE // 3)
				y = player.rect.centery + offset_y + randint(-TILE_SIZE // 3, TILE_SIZE // 3)
				self.animation_player.create_particles((x,y), 'flame', groups)
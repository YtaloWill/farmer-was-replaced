import Polyculture
import PumpkinStrategy
import GrassStrategy
import CactusStrategy
#import LabyrinthStrategy
import SunflowerStrategy
import Core

harvest()
# setup
clear()
change_hat(Hats.Purple_Hat)



def cactus_spawner():
	size = 5
	CactusStrategy.run(size, size)
			

def sunflower_spawner():
	size = 6
	SunflowerStrategy.run(size, size)

def pumpkin_spawner():
	size = 6
	PumpkinStrategy.run(size)

cactus_spawner()
#Core.move_to(10, 10)
#spawn_drone(sunflower_spawner)


#Core.move_to(0, 0)
#Polyculture.run(8, 8)
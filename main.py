import Polyculture
import PumpkinStrategy
import GrassStrategy
#import CactusStrategy
#import LabyrinthStrategy
import SunflowerStrategy
import Core

harvest()
# setup
clear()
change_hat(Hats.Purple_Hat)

def sunflower_spawner():
	SunflowerStrategy.run()

def pumpkin_spawner():
	size = 6
	PumpkinStrategy.run(size)


spawn_drone(sunflower_spawner)

Core.move_to(4, 0)
spawn_drone(pumpkin_spawner)

Core.move_to(11, 0)
spawn_drone(pumpkin_spawner)

Core.move_to(0, 6)
Polyculture.run(5, 5)
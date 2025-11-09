import Polyculture
import PumpkinStrategy
import GrassStrategy
#import CactusStrategy
#import LabyrinthStrategy
import SunflowerStrategy

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

for _ in range(4):
	move(East)
spawn_drone(pumpkin_spawner)

for _ in range(6):
	move(East)
spawn_drone(pumpkin_spawner)

for _ in range(6):
	move(East)
for _ in range(10):
	move(South)
Polyculture.run(16, 10)
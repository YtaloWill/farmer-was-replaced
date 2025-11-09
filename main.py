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

#while True:
#	LabyrinthStrategy.run()
#	CactusStrategy.run()
#	do_a_flip()
#	if num_items(Items.Hay) < 5000:
#		GrassStrategy.run(0, 0, get_world_size()-1, get_world_size()-1)
#	else:
#		default_polyculture()
	
	#PumpkinStrategy.run(get_world_size())
spawn_drone(SunflowerStrategy.run)
for _ in range(4):
	move(East)
Polyculture.run(12)
	
#	CactoStrategy.run()
from f0 import default_polyculture
#import PumpkinStrategy
import GrassStrategy
#import CactusStrategy
#import LabyrinthStrategy

harvest()
# setup
clear()
change_hat(Hats.Purple_Hat)
while True:
#	LabyrinthStrategy.run()
#	CactusStrategy.run()
	do_a_flip()
	if num_items(Items.Hay) < 5000:
		GrassStrategy.run(0, 0, get_world_size()-1, get_world_size()-1)
	else:
		default_polyculture()
	
	#PumpkinStrategy.run(6)
	
#	CactoStrategy.run()
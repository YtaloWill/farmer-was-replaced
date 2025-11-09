import Core
import xtate

def _plant_cactus():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Cactus)

def _sort():
	current = measure()
	north = measure(North)
	east = measure(East)
	
	if current != None and north != None and north < current:
		swap(North)
		xtate.cactus_counter = 0
	elif current != None and east != None and east < current:
		swap(East)
		xtate.cactus_counter = 0
	xtate.cactus_counter += 1
	

def run(lx, ly):
	init_position = (get_pos_x(), get_pos_y())
	while True:
		Core.move_x_by_y(_plant_cactus, lx, ly)
		for _ in range(lx):
			move(West)
		harvested = False
		while not harvested:
			xtate.cactus_counter = 0
			Core.move_x_by_y(_sort, lx, ly)
			if xtate.cactus_counter == lx * ly:
				for _ in range(ly-1):
					move(North)
				move(West)
				harvest()
				harvested = True
			Core.move_to(init_position[0], init_position[1])
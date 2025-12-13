import Core
import xtate

def _plant_cactus():
	if get_ground_type() != Grounds.Soil:
		till()
	if get_entity_type() != Entities.Cactus:
		plant(Entities.Cactus)

def _sort():
	current = measure()
	north = measure(North)
	east = measure(East)
	is_x_limit = get_pos_x() == get_world_size()-1
	is_y_limit = get_pos_y() == get_world_size()-1
	
	if not is_y_limit and current != None and north != None and north < current:
		swap(North)
		xtate.cactus_counter = 0
	elif not is_x_limit and current != None and east != None and east < current:
		swap(East)
		xtate.cactus_counter = 0
	xtate.cactus_counter += 1
	

def execute():
	_plant_cactus()
	_sort()
	if xtate.cactus_counter == get_world_size() * get_world_size():
		harvest()


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
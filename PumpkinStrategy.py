import Core

def setup(size):
	if get_ground_type() != Grounds.Soil:
		Core.move_x_by_y(Core.check_and_till, size, size)
		for i in range(size):
			move(West)
def run(size, use_fertilizer):
	while True:
		setup(size)
		for i in range(size):
			for j in range(size):
				while not can_harvest():
					plant(Entities.Pumpkin)
					if use_fertilizer:	
						use_item(Items.Fertilizer)
					elif get_water() < 0.1:
						use_item(Items.Water)
				move(North)
			for i in range(size):
				move(South)
			move(East)
		for i in range(size):
			move(West)
		harvest()


def _setup():
	Core.check_and_till()

def _plant_pumpkim():
	while not can_harvest():
		plant(Entities.Pumpkin)
		if get_water() < 0.5:
			use_item(Items.Water)
#		use_item(Items.Fertilizer)
		

def _execute(lx, ly):
	def a():
		if get_ground_type() != Grounds.Soil:
			Core.move_x_by_y(_setup, lx, ly)
		Core.move_to(get_pos_x()-lx, get_pos_y())
		Core.move_x_by_y(_plant_pumpkim, lx, ly)
	return a

def run_multithread():
	splited = get_world_size()/max_drones()
	for i in range(max_drones()-1):
		spawn_drone(_execute(splited, get_world_size()))
		for _ in range(splited):
			move(East)
	_execute(splited, get_world_size())()
	Core.move_to(0,0)
	first = measure()
	while first == None:
		first = measure()
	move(West)
	move(South)
	while True:
		if measure() == first:
			break
	harvest()
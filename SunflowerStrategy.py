import xtate
import Core

# DEPRECATED: Should be refactored to use in run method
def _is_max_petals():
	cur_petals = measure() or 0
	if cur_petals == 15:
		return True
	cur_position = (get_pos_x(), get_pos_y())
	finded_greater = False
	for coordinate in xtate.sunflower_max_petals:
		if cur_petals < xtate.sunflower_max_petals[coordinate]:
			return False
	return True

def _use_water():
	if get_water() < 0.5:
		use_item(Items.Water)

def _plant():
	plant(Entities.Sunflower)
	_use_water()
	cur_petals = measure()
	cur_position = (get_pos_x(), get_pos_y())
	xtate.sunflower_max_petals[cur_position] = cur_petals

def _replant():
	if can_harvest():
		harvest()
		_plant()

def _rebuild(init_pos, lx, ly):
	Core.move_to(init_pos[0], init_pos[1])
	Core.move_x_by_y(_build, lx, ly)
	Core.move_to(init_pos[0], init_pos[1])

def _build():
	if can_harvest():
		harvest()
	Core.check_and_till()
	_plant()

def run(lx, ly):
	init_pos = (get_pos_x(), get_pos_y())
	while True:
		min_petals = 0
		if get_ground_type() != Grounds.Soil:
			Core.move_x_by_y(_build, lx, ly)
		greater = init_pos
		for coordinate in xtate.sunflower_max_petals:
			if xtate.sunflower_max_petals[coordinate] >= xtate.sunflower_max_petals[greater]:
				greater = coordinate
			if xtate.sunflower_max_petals[coordinate] <= 9:
				min_petals += 1
		if min_petals / (lx * ly) > 0.8:
			_rebuild(init_pos, lx, ly)
		else:
			Core.move_to(greater[0], greater[1])
			_replant()
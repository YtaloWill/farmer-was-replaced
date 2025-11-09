import xtate
import Core

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
	if get_water() < 0.1:
		use_item(Items.Water)		

def _execute():
	if can_harvest() and _is_max_petals():
		harvest()
	Core.check_and_till()
	plant(Entities.Sunflower)
	_use_water()
	cur_petals = measure()
	cur_position = (get_pos_x(), get_pos_y())
	xtate.sunflower_max_petals[cur_position] = cur_petals

def run(lx, ly):
	while True:
		Core.move_x_by_y(_execute, lx, ly)
		for _ in range(lx):
			move(West)
	
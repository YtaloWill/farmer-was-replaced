import Core

def _execute():
	plants = [Entities.Bush, Entities.Grass, Entities.Carrot]
	to_plant = plants[get_pos_y() % len(plants)]
	if can_harvest():
		harvest()
		if (get_pos_x() + get_pos_y()) % 2 == 0:
			plant(Entities.Tree)
			use_item(Items.Water)
			return
		if (to_plant == Entities.Carrot and get_ground_type() != Grounds.Soil):
			till()
		plant(to_plant)

def run(lx, ly):
	current_plant = 0
	while True:
		Core.move_x_by_y(_execute, lx, ly)
		for _ in range(lx):
			move(West)
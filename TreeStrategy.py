def run(x,y):
	if (get_pos_x() + get_pos_y()) % 2 == 0:
		plant(Entities.Tree)
		use_item(Items.Water)
		move(North)

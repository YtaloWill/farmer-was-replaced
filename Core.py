def move_robot(fn, x, y, lx, ly):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_pos_x() >= x and get_pos_x() <= lx and get_pos_y() >= y and get_pos_y() <= ly:
				fn()
			move(North)
		move(East)

def move_x_by_y(fn, x, y):
	for i in range(x):
		for j in range(y):
			fn()
			move(North)
		for i in range(y):
			move(South)
		move(East)

def check_and_till():
	if get_ground_type() != Grounds.Soil:
		till()
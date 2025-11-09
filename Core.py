def move_robot(fn, x, y, lx, ly):
	for i in range(get_world_size()):
		for j in range(get_world_size()):
			if get_pos_x() >= x and get_pos_x() < lx and get_pos_y() >= y and get_pos_y() < ly:
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

def move_to(x, y):
	cur_x = get_pos_x()
	cur_y = get_pos_y()
	
	diff_x = x - cur_x
	diff_y = y - cur_y

	while diff_x != 0:
		if diff_x < 0:
			diff_x += 1
			move(West)
		if diff_x > 0:
			diff_x -= 1
			move(East)

	while diff_y != 0:
		if diff_y < 0:
			diff_y += 1
			move(South)
		if diff_y > 0:
			diff_y -= 1
			move(North)


def check_and_till():
	if get_ground_type() != Grounds.Soil:
		till()
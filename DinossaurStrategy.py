import Core


def _moving(side):
	move(side)
	return measure()

def _comeback():
	new_next = None
	new_next = new_next or _moving(East)
	if get_pos_x() != get_world_size() - 1:
		while(can_move(North)):
			new_next = _moving(North) or new_next
	while(can_move(East)):
		new_next = _moving(East)  or new_next
	while(can_move(South)):
		new_next = _moving(South)  or new_next
	while(can_move(West)):
		new_next = _moving(West)  or new_next
	while(can_move(North)):
		new_next = _moving(North)  or new_next
	return new_next

def _brute_force():
	move(East)
	while(get_pos_y() > 1) and can_move(South):
		move(South)
	move(East)
	while(can_move(North)):
		move(North)	

def _can_move():
	return can_move(North) or can_move(East) or can_move(West) or can_move(South)

def run():
	change_hat(Hats.Dinosaur_Hat)
	next_x, next_y = measure()
	counter = 0
	while counter < get_world_size() - 3:
		Core.move_to(next_x, next_y)
		if measure() != None:
			next_x, next_y = measure()
		new_next = _comeback()
		if new_next != None:
			next_x, next_y = new_next
		counter += 1
	while _can_move():
		while(get_pos_x() != get_world_size()-1 and _can_move()):
			_brute_force()
		move(South)
		while can_move(West):
			move(West)
		while can_move(North):
			move(North)
		
	change_hat(Hats.Pumpkin_Hat)
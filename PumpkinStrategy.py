import Core

def setup(size):
	Core.move_x_by_y(Core.check_and_till, size, size)
	for i in range(size):
		move(West)

def run(size):
	setup(size)
	for i in range(size):
		for j in range(size):
			while not can_harvest():
				plant(Entities.Pumpkin)
				use_item(Items.Fertilizer)
			move(North)
		for i in range(size):
			move(South)
		move(East)
	for i in range(size):
		move(West)
	harvest()
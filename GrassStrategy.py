import Core

def _execute():
	if can_harvest():
		harvest()

def run(x, y, lx, ly):
	Core.move_robot(_execute, x, y, lx, ly)
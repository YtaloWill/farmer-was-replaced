# TODO: reuse labyrinth
import Core

def _get_weird_substance_needed(laby_size):
	return laby_size * 2**(num_unlocked(Unlocks.Mazes) - 1)

def _build(laby_size):
	plant(Entities.Bush)
	substance = laby_size or get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1)
	use_item(Items.Weird_Substance, substance)

def _set_drone_positions(laby_size):
	Core.move_to(0, laby_size-1)
	spawn_drone(_execute([East, South, North, West]))
	Core.move_to(laby_size-1, laby_size-1)
	spawn_drone(_execute([East, South, North, West]))
	Core.move_to(laby_size-1, 0)
	spawn_drone(_execute([East, South, North, West]))
	Core.move_to(0, 0)

def _clamp(lowest, greatest, value):
	if value > greatest:
		return lowest
	if value < lowest:
		return greatest
	return value

def _get_position_direction(direction):
	current = [get_pos_x(), get_pos_y()]
	if direction == North:
		current[1] += 1
	if direction == South:
		current[1] -= 1
	if direction == West:
		current[0] -= 1
	if direction == East:
		current[0] += 1
	x = _clamp(0, get_world_size(), current[0])
	y = _clamp(0, get_world_size(), current[1])
	return (x, y)

def _execute(moves):
	def _search():
		while get_entity_type() != Entities.Hedge:
			continue
		
		while True:
			if get_entity_type() == Entities.Treasure or get_entity_type() != Entities.Hedge:
				harvest()
				break
	
			maze[(get_pos_x(), get_pos_y())] = True
			moved = False
			if get_entity_type() == Entities.Hedge:
				for m in moves:
					pos = (get_pos_x(), get_pos_y())
					already_pass = _get_position_direction(m) in maze and maze[_get_position_direction(m)]
					if can_move(m) and not already_pass:
						move(m)
						backtrack.append(m)
						moved = True
						break
				if not moved:
					step = backtrack.pop()
					move(backstep[step])
		return

	backstep = {North:South, South:North, West:East, East:West}
	backtrack = []
	maze = {}
	return _search

def run():
	laby_size = get_world_size()
	_set_drone_positions(laby_size)
	
	if get_entity_type() != Entities.Treasure and get_entity_type() != Entities.Hedge:
		_build(_get_weird_substance_needed(laby_size))
	_execute([West, North, South, East])()
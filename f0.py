def default_polyculture():
	plants = [Entities.Bush, Entities.Grass, Entities.Carrot, Entities.Sunflower]
	current_plant = 0
	
	def clamp(maximo, value):
		if value > maximo:
			return 0
		return value
	
	# behavior
	for line in range(get_world_size()):
		for col in range(get_world_size()):
			if can_harvest():
				harvest()
			
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				plant(Entities.Tree)
				use_item(Items.Water)
				move(North)
				continue
			if (plants[current_plant] == Entities.Carrot or plants[current_plant] == Entities.Sunflower) and get_ground_type() != Grounds.Soil:
				till()
			plant(plants[current_plant])
			current_plant = clamp(len(plants)-1, current_plant+1)
			move(North)
			
		move(East)
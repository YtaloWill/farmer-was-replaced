import Core

def _plant_companion():
	companion_plant = Entities.Carrot
	while True:
		if can_harvest():
			harvest()
			if Core.is_soil_ground_plant(companion_plant):
				if get_ground_type() != Grounds.Soil:
					till()
			else:
				if get_ground_type() != Grounds.Grassland:
					till()
			plant(companion_plant)
			if get_water() < 0.5:
				use_item(Items.Water)
			companion_plant, (x, y) = get_companion()
			Core.move_to(x, y)


def run():
	spawn_drone(_plant_companion)
	move(East)
	spawn_drone(_plant_companion)
	move(East)
	spawn_drone(_plant_companion)
	move(East)
	_plant_companion()

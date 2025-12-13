filename = "testing"
sim_unlocks = Unlocks
sim_items = {
	Items.Hay: 100000000000000000,
	Items.Wood: 100000000000000000,
	Items.Carrot: 100000000000000000,
	Items.Pumpkin: 100000000000000000,
	Items.Cactus: 100000000000000000,
	Items.Bone: 100000000000000000,
	Items.Gold: 100000000000000000,
	Items.Weird_Substance: 100000000000000000,
	Items.Water: 100000000000000000,
	Items.Fertilizer: 100000000000000000,
	Items.Power: 100000000000000000,
}
sim_globals = {"sunflower_max_petals" : {}, "cactus_counter": 0}
seed = 1
speedup = 64
run_time = simulate(filename, sim_unlocks, sim_items, sim_globals, seed, speedup)
print(run_time)
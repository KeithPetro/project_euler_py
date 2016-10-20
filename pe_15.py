#Project Euler - 15
#Keith Petro - 2016/10/20
#Problem Name: Lattice paths
#Description: How many possible routes (moving right and down only) are there
#from the top left to the bottom right of a 20*20 grid?

def get_num_lattice_paths(grid_size):
	paths = 1
	for i in range(0, grid_size): # 40 choose 20
		paths *= 2 * grid_size - i
		paths //= i + 1

	return paths

print(get_num_lattice_paths(20))
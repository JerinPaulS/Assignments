import random
import collections

board = []
N = 8
POP_SIZE = 1000
ITERATIONS = 100

def generate_population(POP_SIZE):
	DATA = []
	occupied = set()
	for pop in range(POP_SIZE):
		count = 0
		temp = []
		while count < N:
			if len(occupied) == N * N:
				break
			row = random.randint(0, 7)
			col = random.randint(0, 7)
			if (row, col) not in occupied:
				count += 1
				occupied.add((row, col))
				temp.append((row, col))
		occupied.clear()
		DATA.append(temp)
	return DATA

def display(positions):
	board = []
	for row in range(N):
		temp = []
		for col in range(N):
			if (row, col) in positions:
				temp.append("Q")
				print(" Q ", end = "")
			else:
				temp.append(" ")
				print(" . ", end = "")
		board.append(temp)
		print()

def evaluation_func(curr_pop, row, col):
	return rowScore(curr_pop, row, col) + colScore(curr_pop, row, col) + diagScore(curr_pop, row, col)

def fitness(curr_pop, row, col):
	return evaluation_func(curr_pop, row, col) - 0

def rowScore(curr_pop, row, col):
	rows = 0
	for c in range(N):
		if col == c:
			continue
		if (row, c) in curr_pop:
			rows += 1
		#print(curr_pop, rows)
	return rows

def colScore(curr_pop, row, col):
	cols = 0
	for r in range(N):
		if row == r:
			continue
		if (r, col) in curr_pop:
			cols += 1
		#print(curr_pop, cols)
	return cols

def diagScore(curr_pop, row, col):
	posDiag, posDiag1 = 0, 0
	negDiag, negDiag1 = 0, 0
	r, c = row + 1, col + 1
	while 0 <= r < N and 0 <= c < N:
		if (r, c) in curr_pop:
			posDiag += 1
		r += 1
		c += 1
	r, c = row - 1, col - 1
	while 0 <= r < N and 0 <= c < N:
		if (r, c) in curr_pop:
			negDiag += 1
		r -= 1
		c -= 1
	r, c = row - 1, col + 1
	while 0 <= r < N and 0 <= c < N:
		if (r, c) in curr_pop:
			posDiag1 += 1
		r -= 1
		c += 1
	r, c = row + 1, col - 1
	while 0 <= r < N and 0 <= c < N:
		if (r, c) in curr_pop:
			negDiag1 += 1
		r += 1
		c -= 1
	#print(curr_pop, posDiag + negDiag)
	return posDiag + negDiag + posDiag1 + negDiag1

def direction(curr_pop, row, col):
	directions = [(1, 1), (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1)]
	for d in directions:
		new_x, new_y = d[0] + row, d[1] + col
		if 0 <= new_x < N and 0 <= new_y < N:
			return (new_x, new_y)
	return (0, 0)

def select_population(population):
	population.sort(key = lambda x:x[1])
	data = population[:800]
	#print(data, len(data))
	new_data = []
	for i in range(len(data)):
		new_data.append(data[i][0])
	new_data = new_data + generate_population(200)
	#print(new_data, len(new_data))
	return new_data

def PSO():
	r1, r2 = round(random.uniform(0, 1), 4), round(random.uniform(0, 1), 4)
	w, c1, c2 = 2, 2, 2
	pbest, gbest = 10 ** 3, 10 ** 3
	new_x, new_y = 0, 0
	vx, vy = 1, 1
	DATA = generate_population(1000)
	global_result = None
	iter_count = 0
	#for i in range(ITERATIONS):
	i = 0
	while gbest > 2:
		iter_count += 1
		population = []
		print("\n\t *** ITERATION " + str(i + 1) + " ***")
		pop_result = []
		for p in DATA:
			temp = []
			total = 0
			print(len(p))
			for index, individual in enumerate(p):
				row, col = individual
				total += fitness(p, row, col)
				x, y = direction(p, row, col)
				vx = round(((w * vx) + (c1 * r1 * (pbest - x)) + (c1 * r1 * (gbest - x))), 4)
				vy = round(((w * vy) + (c1 * r1 * (pbest - y)) + (c1 * r1 * (gbest - y))), 4)
				if vx > 8 or vx < 0:
					vx = random.randint(1, 8)
				if vy > 8 or vy < 0:
					vy = random.randint(1, 8)
				vx, vy = int(vx), int(vy)
				if 0 <= row + vx < N and 0 <= col + vy < N and (row + vx, col + vy) not in p:
					new_x = row + vx
					new_y = col + vy
					p[index] = (new_x, new_y)
			if pbest > total:
				pbest = total
				pop_result = p
			temp.append(p)
			temp.append(total)
			population.append(temp)
		if gbest > pbest:
			gbest = pbest
			global_result = pop_result
		display(global_result)
		print("\t\tGBest " + str(gbest))
		DATA = select_population(population)
		i += 1
	display(global_result)
	print("\t\tGBest " + str(gbest))
	print(iter_count)
	return

PSO()
#d = generate_population(1)
#display(d[0])
#print(fitness(d[0], 3, 3))

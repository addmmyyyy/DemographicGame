from Agents import agent
from PayoffFunctions import prisonersDilemma

import random as r

defector_rarity = 0.5
sight = 1

# creates a grid where some coordinate points are not occupied at the start of the simulation
def createSparseNeighbourhood(size_x,size_y,no_of_agents):
	neighbourhood = []
	random_numbers =[]
	
	for number in range(no_of_agents):
		random_numbers.append(r.random())
		
	for y in range(size_y):
		row = []
		for x in range(size_x):
			row.append(0)
		neighbourhood.append(row)
	
	i = 0
	
	for _ in range(no_of_agents):
		agent_placed = False
		while (not agent_placed):
			x = r.randint(0,size_x-1)
			y = r.randint(0,size_y-1)
		
			if neighbourhood[y][x] == 0:
				neighbourhood[y][x] = agent(random_numbers[i],sight,defector_rarity)
				agent_placed = True
				i+=1
			
	return neighbourhood

# creates a grid where all coordinate points are occupied at the start of the simulation
def createDenseNeighbourhood(size_x,size_y):
	neighbourhood = []
	i = 0
	
	random_numbers = []
	for number in range(size_x*size_y+1):
		random_numbers.append(r.random())
	
	for y in range(size_y):
		row = []
		for x in range(size_x):
			row.append(agent(random_numbers[i],sight,defector_rarity))
			i+=1
		neighbourhood.append(row)
	return neighbourhood

def simulateTurn(size_x,size_y,neighbourhood):
	for row in range(size_y):
		for column in range(size_x):
		
			if neighbourhood[row][column] != 0:
				agent = neighbourhood[row][column]
				
				north = neighbourhood[(row+1)%size_x][column]
				west = neighbourhood[row][(column-1)%size_x]
				south = neighbourhood[(row-1)%size_y][column]
				east = neighbourhood[row][(column+1)%size_x]
				
				neighbours = []
				
				if north != 0:
					neighbours.append(north)
				if west != 0:
					neighbours.append(west)
				if south != 0:
					neighbours.append(south)
				if east != 0:
					neighbours.append(east)
				
				# if there are no neighbours to compete with, the agent moves to a neighbouring empty spot
				if (east == 0) and (west == 0) and (north == 0) and (south == 0):
					neighbourhood = agent.moveAgent(neighbourhood, column,row)
				else:

					direction_decider = r.randint(0,len(neighbours)-1)
					opponent = neighbours[direction_decider]
						
					p1,p2 = prisonersDilemma(agent.strategy,opponent.strategy)
					agent.score+=p1
					opponent.score+=p2

	neighbourhood = deathsAndBirths(neighbourhood,size_x,size_y)

	# print("-------------------------------------")
	# printNeighbourhood(neighbourhood,10,10)
	countStrategies(size_x,size_y,neighbourhood)
	return neighbourhood
	
def deathsAndBirths(neighbourhood,size_x,size_y):
	death_threshold = -10
	replicate_threshold = 10 
	
	for row in range(size_y):
		for column in range(size_x):
			occupant = neighbourhood[row][column]
			if occupant != 0:
				if occupant.score < death_threshold:
					neighbourhood[row][column] = 0
				else:
					if occupant.score > replicate_threshold:
						occupant.replicateAgent(neighbourhood,column,row)
	return neighbourhood
						

def printNeighbourhood(neighbourhood,size_x,size_y):
	for row in range(size_y):
		strategy_row = []
		for column in range(size_x):
			point = neighbourhood[column][row]
			
			if point == 0:
				strategy_row.append("X")
			else:
				if point.strategy == "cooperate":
					strategy_row.append("C")
				else:
					strategy_row.append("D")
		print(strategy_row)
		
	
def printScores(size_x,size_y,neighbourhood):

	# prints the score and strategy of each agent
	for y in range(size_y):
		for x in range(size_x):
			agent = neighbourhood[y][x]
			if agent != 0:
				print(agent.strategy, agent.score)

def countStrategies(size_x,size_y,neighbourhood):

	d=0
	c=0
	for y in range(size_y):
		for x in range(size_x):
			agent = neighbourhood[y][x]
			if agent != 0:
				if agent.strategy == "cooperate":
					c+=1
				else:
					d+=1
	print(c, d)

			
if __name__ == "__main__":

	size_x = 10
	size_y = 10
	#neighbourhood = createDenseNeighbourhood(size_x,size_y)
	neighbourhood = createSparseNeighbourhood(size_x,size_y,20)
	
	printNeighbourhood(neighbourhood,size_x,size_y)
	
	for _ in range(10000):
		neighbourhood = simulateTurn(size_x,size_y,neighbourhood)
		
	print("-------------------------------------")
	printNeighbourhood(neighbourhood,size_x,size_y)
	
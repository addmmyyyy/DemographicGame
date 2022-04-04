from Agents import agent
from PayoffFunctions import prisonersDilemma
from Visualisation import graphAgents

import random as r
import matplotlib.pyplot as plt

does_age = 0
defector_rarity = 0.5
sight = 1

size_x = 10
size_y = 10
number_of_simulations = 50
number_of_agents = 20

generations = [0]
number_of_cooperators = []
number_of_defectors = []
	
	

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
	
# runs through each agent and has it play the dilemma with a random neighbour. if there are no such neighbours, it instead moves.
def simulateTurn(size_x,size_y,neighbourhood):
	for row in range(size_y):
		for column in range(size_x):
		
			if neighbourhood[row][column] != 0:
				agent = neighbourhood[row][column]
				
				north = neighbourhood[(row+1)%size_y][column]
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
				
				agent.age+=does_age

	neighbourhood = deathsAndBirths(neighbourhood,size_x,size_y)

	# print("-------------------------------------")
	# printNeighbourhood(neighbourhood,10,10)
	generations.append(int(generations[-1])+1)
	countStrategies(size_x,size_y,neighbourhood)
	return neighbourhood
	
def deathsAndBirths(neighbourhood,size_x,size_y):
	death_threshold = -10
	replicate_threshold = 10 
	maximum_age = 5
	
	for row in range(size_y):
		for column in range(size_x):
			occupant = neighbourhood[row][column]
			if occupant != 0:
				if occupant.score < death_threshold or occupant.age > maximum_age:
					neighbourhood[row][column] = 0
				else:
					if occupant.score > replicate_threshold:
						occupant.replicateAgent(neighbourhood,column,row)
	return neighbourhood
						
# displays whether each point is empty, a cooperator, or a defector
def printNeighbourhood(neighbourhood,size_x,size_y):
	for row in range(size_y):
		strategy_row = []
		for column in range(size_x):
			point = neighbourhood[row][column]
			
			if point == 0:
				strategy_row.append("X")
			else:
				if point.strategy == "cooperate":
					strategy_row.append("C")
				else:
					strategy_row.append("D")
		print(strategy_row)
		
	

# counts how many cooperators and defectors there are
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
	number_of_cooperators.append(c)
	number_of_defectors.append(d)
	print("There are " + str(c) + " cooperators and " + str(d) + " defectors")

			
if __name__ == "__main__":
	
	"""default = input("Do you want to use default values (y/n)?    > ")
	
	if default == "n":
		size_x = int(input("How many cells are in each row? "))
		size_y = int(input("How many rows are there? "))
		does_age = int(input("Do agents age (0 = no, 1 = yes) "))
		defector_rarity = float(input("What is the probability of a starting agent being a defector? (in the range of 0 to 1) "))
		number_of_agents = int(input("How many starting agents are there? "))
		number_of_simulations = int(input("How many generations do you want to simulate?" ))"""
	#neighbourhood = createDenseNeighbourhood(size_x,size_y)
	neighbourhood = createSparseNeighbourhood(size_x,size_y,number_of_agents)
	
	#printNeighbourhood(neighbourhood,size_x,size_y)
	countStrategies(size_x,size_y,neighbourhood)
	
	for _ in range(number_of_simulations):
		neighbourhood = simulateTurn(size_x,size_y,neighbourhood)
		
	graphAgents(generations,number_of_cooperators,number_of_defectors)
	print("-------------------------------------")
	#printNeighbourhood(neighbourhood,size_x,size_y)
	
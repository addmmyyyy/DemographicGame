import random as r

class agent:
	def __init__(self,chosen_strategy,sight,defector_rarity):
	
		# score tracks the sum of the payoffs the agent has received. age tracks how many iterations of the gane the agent has played. 
		# sight is used to determine how far the agent can move. in games without mobility, it is always 0.
		self.score = 0
		self.age = 0
		self.sight = sight
		
		# defector_rarity is how common we want defectors to be, with a value of 1 creating an all-defector population, and a value of 0 creating an all-cooperator population.
		# chosen_strategy is a random value between 0 and 1,
		if chosen_strategy > defector_rarity:
			self.strategy = "cooperate"
		else:
			self.strategy = "defect"
	
	def updatePosition(self,neighbourhood,x_coord,y_coord):
		self.x = x_coord
		self.y = y_coord
		size_x = len(neighbourhood[0])
		size_y = len(neighbourhood)
		
		self.north = neighbourhood[(y_coord+1)%size_x][x_coord]
		self.west = neighbourhood[y_coord][(x_coord-1)%size_x]
		self.south = neighbourhood[(y_coord-1)%size_y][x_coord]
		self.east = neighbourhood[y_coord][(x_coord+1)%size_x]
		
		
	def moveAgent(self, neighbourhood,x_coord,y_coord):
		self.updatePosition(neighbourhood,x_coord,y_coord)
		size_x = len(neighbourhood[0])
		size_y = len(neighbourhood)
		
		empty_spots = []
		if self.north == 0:
			empty_spots.append("north")
		if self.west == 0:
			empty_spots.append("west")
		if self.south == 0:
			empty_spots.append("south")
		if self.east == 0:
			empty_spots.append("east")
		
		if len(empty_spots) > 0:
			new_location = empty_spots[r.randint(0,len(empty_spots)-1)]
		
			if new_location == "north":
				neighbourhood[(y_coord+1)%size_x][x_coord] = self
			if new_location == "west":
				neighbourhood[y_coord][(x_coord-1)%size_x] = self
			if new_location == "south":
				neighbourhood[(y_coord-1)%size_x][x_coord] = self
			if new_location == "east":
				neighbourhood[y_coord][(x_coord+1)%size_x] = self
			
			neighbourhood[y_coord][x_coord] = 0
			return(neighbourhood)
		else:
			return(neighbourhood)
	
	def replicateAgent(self, neighbourhood, x_coord, y_coord):
		self.updatePosition(neighbourhood,x_coord,y_coord)
		size_x = len(neighbourhood[0])
		size_y = len(neighbourhood)
		
		empty_spots = []
		if self.north == 0:
			empty_spots.append("north")
		if self.west == 0:
			empty_spots.append("west")
		if self.south == 0:
			empty_spots.append("south")
		if self.east == 0:
			empty_spots.append("east")
		
		if len(empty_spots) > 0:
			new_location = empty_spots[r.randint(0,len(empty_spots)-1)]
		
			if new_location == "north":
				neighbourhood[(y_coord+1)%size_x][x_coord] = self
			if new_location == "west":
				neighbourhood[y_coord][(x_coord-1)%size_x] = self
			if new_location == "south":
				neighbourhood[(y_coord-1)%size_x][x_coord] = self
			if new_location == "east":
				neighbourhood[y_coord][(x_coord+1)%size_x] = self
			
			return(neighbourhood)
		else:
			return(neighbourhood)
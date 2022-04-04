import matplotlib.pyplot as plt

def graphAgents(x_axis,y_axis1,y_axis2):
	plt.plot(x_axis, y_axis1, label = "cooperators")
	plt.plot(x_axis, y_axis2, label = "defectors")
	plt.xlabel('Generation')
	plt.ylabel('Number of agents using strategy')
	plt.title('Strategy populations over time')
	plt.legend()
	plt.show
	plt.savefig('filename.svg')
	
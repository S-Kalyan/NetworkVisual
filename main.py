from network_visualize import PlotNetwork
import numpy as np
layer_nodes = [10, 30, 10] # all layers

data = [] #multi neuron spike train data
#creating random spike train, with 100 timesteps
for nodes in layer_nodes:
    data.append(np.random.randint(0,2,[nodes,100]))
plot_network = PlotNetwork(layer_nodes,data)
plot_network.run_simulation()
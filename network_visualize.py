import matplotlib.pyplot as plt
import matplotlib.patches as pth
import numpy as np
import matplotlib.collections as collections



class Neuron(object):
    def __init__(self, x, y, radius, active):
        self.x = x
        self.y = y
        self.radius = radius

    def get_patch(self):
        circle = pth.Circle((self.x, self.y), self.radius, color='black')
        return circle


class PlotNetwork(object):

    def __init__(self, layer_nodes,data):
        self.layer_nodes = layer_nodes
        self.layers = len(layer_nodes)
        self.widest_layer = max(layer_nodes)
        self.layer_distance = 100 # distance between layers
        self.node_distance = 15 #distance between two nodes in a layer
        self.radius = 5
        self.x_pos = 0
        self.y_pos = 0
        self.patches = []
        self.data = data
        self.nsteps = data[0].shape[1] #no .of time steos

    def plot_layer(self,layer_ind):
        self.x_pos = 0.5 * (self.widest_layer - self.layer_nodes[layer_ind])*self.node_distance
        for node in range(self.layer_nodes[layer_ind]):
            neuron = Neuron(self.x_pos, self.y_pos, self.radius, active=0)
            patch = neuron.get_patch()
            self.patches.append(patch)
            self.x_pos += self.node_distance
        self.y_pos += self.layer_distance

    def plot_network(self):

        for layer_ind in range(self.layers):
            self.plot_layer(layer_ind)


    def run_simulation(self):
        self.plot_network()
        fig = plt.figure()
        ax = fig.add_subplot(111)
        for step in range(self.nsteps):
            ax.clear()
            actives = np.empty((sum(self.layer_nodes)))
            start = 0
            for layer_ind in range(self.layers):
                actives[start:start+self.layer_nodes[layer_ind]] = self.data[layer_ind][:,step]
                start += self.layer_nodes[layer_ind]
            active_indices = np.where(actives==1)[0] #nodes that are spiked
            inactive_indices = np.where(actives == 0)[0]
            for ind in active_indices:
                self.patches[ind].set_color('red')
            for ind in inactive_indices:
                self.patches[ind].set_color('black')

            patches_collection = collections.PatchCollection(self.patches, match_original=True)
            ax.add_collection(patches_collection)
            plt.draw()
            plt.axis('scaled')
            plt.axis('off')
            plt.pause(0.1)



# MSTs-with-Kruskal-s-Algorithm
This code is an implementation of Kruskal's Algorithm for finding minimum spanning trees (MSTs) in weighted graphs. A minimum spanning tree is a tree that connects all vertices of a weighted graph while minimizing the total sum of the edge weights. Kruskal's Algorithm is an efficient and widely used algorithm for finding a minimum spanning tree in a graph.
Kruskal's Algorithm is a greedy algorithm that builds a minimum spanning tree by iteratively adding the smallest weighted edge that does not create a cycle until all vertices are connected. Here is a brief overview of the algorithm:
* Sort all the edges in non-decreasing order of their weight.
* Initialize an empty tree.
* For each edge in the sorted order, add the edge to the tree if it does not create a cycle.
* Repeat step 3 until all vertices are connected or no more edges are left.
This algorithm guarantees that the minimum spanning tree is found since it starts by adding the smallest edge, and adds edges only if they do not create a cycle.

In this code, the WeightedTree class inherits from the WeightedGraph class, which represents weighted graphs using adjacency matrices. The MSTfromGraph method in WeightedTree uses Kruskal's Algorithm to create a minimum spanning tree from the given graph.

The package consists of two classes: 
### WeightedGraph 
The WeightedGraph class represents a weighted undirected graph, where the weights are non-negative integers. The class is implemented using an adjacency matrix, and provides methods for adding edges, computing the total weight of the graph, and reading/writing graphs from/to files.

    WeightedGraph objects can be used to work with weighted graphs.
    They are internally represented using modified adjacency matrices where each entry a(i,j) is either
    - 0 if there is no edge between vertices i and j
    - a positive integer representing the weight of the edge between i and j if there is such an edge
    Note that the graph is simple and therefore the adjacency matrix representation is symmetric   

### WeightedTree.
The WeightedTree class represents a weighted undirected tree, which is a special case of a weighted graph. The class is implemented as a subclass of WeightedGraph, and provides methods for computing the MST of a graph using Kruskal's algorithm, checking whether a given tree is indeed a tree, and checking whether a given tree is a spanning tree of a given graph.

		WeightedTree objects are WeightedGraphs that are trees.
    They are internally represented using modified adjacency matrices where each entry a(i,j) is either
    - 0 if there is no edge between vertices i and j
    - a positive integer representing the weight of the edge between i and j if there is such an edge
    Note that the graph is simple and therefore the adjacency matrix representation is symmetric
		
		
## Requirements
This package requires Python 3.x and the pytest library (for running the test cases).

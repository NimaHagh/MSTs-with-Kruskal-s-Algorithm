from WeightedGraph import WeightedGraph

class WeightedTree(WeightedGraph):
    """
    WeightedTree objects are WeightedGraphs that are trees.
    They are internally represented using modified adjacency matrices where each entry a(i,j) is either
    - 0 if there is no edge between vertices i and j
    - a positive integer representing the weight of the edge between i and j if there is such an edge
    Note that the graph is simple and therefore the adjacency matrix representation is symmetric
    """

###########################  DO NOT MODIFY THESE FUNCTIONS  ####################################


    def __init__(self, vertices, edges):
        self.inPath = [0]*vertices # used to check for an existing path between 2 vertices
        super().__init__(vertices, edges)

    def __init__(self, vertices):
        self.inPath = [0]*vertices # used to check for an existing path between 2 vertices
        edges = []
        for i in range(vertices):
            edges.append(list([0]*vertices))
        super().__init__(vertices, edges)

    @classmethod
    def fromFile(cls, filename):
        """
        Instantiates a WeightedGraph read from a file.  
        See the description of WeightedGraph.readGraph for the file format.
	
        Parameters:
            str filename: name of file containing the graph
	
        Returns a WeightedGraph described by the file. 
        """
        vertices, edges = WeightedGraph.readGraph(filename)
        return WeightedTree(vertices, edges)

###########################  START YOUR CODE HERE  ####################################
 

    @classmethod
    def MSTfromGraph(cls, graph):
        """
	      Creates a WeightedTree that is a MST of graph.  
	
        Parameters:
            WeightedGraph graph: graph whose MST will be computed
	
        Returns a WeightedTree MST for the graph, or None if this is not possible. 
            """
        
        sortedEdge = WeightedTree.sortEdges(graph) # Sort all edges in increasing order of their edge weights.
        initialTree = WeightedTree(graph.totalVertices()) #graph whose MST will be computed

        i = 0 
        while i < len(sortedEdge) and not initialTree.isTree(): # loop through to see if an edge can be added to the tree and is not a tree
            edge = sortedEdge[i] # trying to pick the smallest edge
            if initialTree.canAdd(edge): #Check if the new edge creates a cycle or loop in a spanning tree.
                initialTree.addEdge(edge)
            i += 1

        if initialTree.isTree(): # when it is a tree return the MSTtree 
            return initialTree
            
        return #otherwise return  none

        
 
    @classmethod
    def sortEdges(cls, graph):
        """
	      Sort the edges of the graph in order of increasing weight 
	
        Parameters:
            WeightedGraph graph: graph whose edges will be sorted
	
        Returns a sorted list of the edges of the graph.
        Each edge is a triple of format (weight, v1, v2) 
	      """
        
      
        
        
        unsortedEdges = [(graph.getEdge(vertix1, vertix2), vertix1, vertix2) #it ceates a list of soreted edges and loops through all the vertexs-
         for vertix1 in range(graph.totalVertices())   #in the graph, for each graph it it uses teh function getEdge, -
         for vertix2 in range(vertix1+1, graph.totalVertices())  #to get the weight of the edge and places it in the list accordingly - 
         if graph.getEdge(vertix1, vertix2) > 0]
        sortedEdges = sorted(unsortedEdges) #so the list is in accending order
        return (sortedEdges)

                           
            
    def canAdd(self,newedge):
        """
        Checks whether a new edge can be added to self without introducing a cycle
	
        Parameters:
            triple newedge: edge that could be added.  Its format is (weight,v1,v2)
        
        Returns True if newedge can be added to self without introducing a cycle, and False otherwise
        """
        weightNotUsed, v1, v2 = newedge
        
        if self.isPath(newedge[1], newedge[2]) or self.getEdge(newedge[1], newedge[2]) >0: # if there is a cycle return false or if the edge already exists
            return False
        
        return True

    def isPath(self,i,j):
        """
        Determines whether there is a path from i to j in self
        by trying to find such a path recursively, backtracking when necessary
	
        Parameters:
            int i,j: vertices in self which may or may not be connected
        
        Returns True if self contains a path from i to j, and False otherwise
        
        Side-Effect:
            self.inPath[] is used and modified by this method as follows (where v is a vertex):
            - self.inPath[v] = 0 when self does not include any edges ajacent to v yet
            - self.inPath[v] = 1 when self does include at least one edge adjacent to v,
                            but v is not yet part of the path  
            - self.inPath[v] = 2 when self does include at least one edge adjacent to v,
                            and v is already part of the path   
        """ 
        
         #
        if i == j: # check if there is a path from i to j 
            self.inPath=[0]*self.totalVertices() # reset the path 
            return True # and return true that there is a path 
        
    
        self.inPath[i] = 2 # when self does include at least one edge adjacent to i, and i is already part of the path 
        
        temp = 0
        while temp < self.totalVertices():
            if self.getEdge(i, temp) > 0 and self.inPath[temp] != 2:
                if self.isPath(temp, j):
                    return True
            temp=temp+ 1

    
        self.inPath[i] = 1
        
        return False # if there are no path from i to j return false

    def addEdge(self,newedge):
        """
        Adds a new edge to self
	
        Parameters:
            triple newedge: edge that will be added.  Its format is (weight,v1,v2)
        
        Returns nothing
        """
        if self.canAdd(newedge):
            weight, v1, v2 = newedge
            self.edges[v1][v2] = weight
            self.edges[v2][v1] = weight
            self.totalE = self.totalE + 1
            self.totalW= self.totalW+weight
        return

###########################  COPY YOUR LAB6 CODE FOR THESE FUNCTIONS  ####################################

    def isTree(self):
        """
        Checks whether self is tree
        
        Returns True if self is a tree, and False otherwise

        """

        if ((self.totalVertices() - 1) == self.totalEdges() ):
            if (self.isConnected()):
                return True
        return False

        
    def isSpanningtree(self,graph):
        """
        Checks whether self is a spanning tree of a graph

        Parameters:
            int graph: WeightedGraph that may have self as a spanning tree

        Assumptions:
            the vertices have the same numbering in both graphs
            
        Returns True if self is a spanning tree of graph, and False otherwise

        """

        if (not self.isTree()):
            return False
        
        if (not self.isSubgraph(graph)):
            return False
        return True

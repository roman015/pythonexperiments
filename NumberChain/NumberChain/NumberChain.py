import numpy

# Function to Initialize the graph
def CreateGraph(numSet, visited, neighbours) :
    # Sort numSet
    numSet = sorted(numSet);

    # Initialize the visited graph (0 - Not visited, Non zero - Visited)
    visited = numpy.zeros(len(numSet))

    # Setup Neighbours List
    for i in range(len(numSet)) :
        neighbours.append([]);
        for j in range(len(numSet)) :
            if (i==j) : continue;
            elif ((numSet[i] % numSet[j] == 0) or (numSet[j] % numSet[i] == 0)) :
                neighbours[i].append(numSet[j]);

def BruteForce(numSet, visited, neighbours, curr) :
    currvisited = visited[:]
    for i in range(curr, len(numSet)) :
        #TODO : Complete this
        

# SCRIPT STARTS HERE
numSet = range(1,11)
visited = numpy.zeros(len(numSet))
neighbours = [];

CreateGraph(numSet, visited, neighbours)

print("Numbers: " + str(numSet))
print("Visited: " + str(visited))
print("Neighbours : \n" + str(neighbours))
import time
import numpy

# Function to determine if given number is a prime
def IsPrime(x) :
    for i in range(2, x) :
        if ( x % i == 0 ) :
            return False
    return True

# Function to determine if two numbers can be linked
def IsLinkable(a, b) :
    return (a % b == 0) or (b % a == 0)

# Function to Initialize the graph
def CreateGraph(numSet, visited, neighbours) :
    # Sort numSet
    numSet = sorted(numSet);

    # Setup Neighbours List
    for i in range(len(numSet)) :
        neighbours.append([]);
        for j in range(len(numSet)) :
            if (i==j) : continue;
            elif ((numSet[i] % numSet[j] == 0) or (numSet[j] % numSet[i] == 0)) :
                neighbours[i].append(j);

# Brute Force Method
def BruteForce(numSet, visited, neighbours, currIdx, filterOutputSize) :
    result = visited[:]

    # Make a backup
    currvisited = visited[:]

    # Check all potential neighbours
    for i in range(len(neighbours[currIdx])) :
        # Get Index and value of potential neighbour
        neighbourIdx = neighbours[currIdx][i]
        neighbour = numSet[neighbourIdx]

        # Perform Recursion
        if (neighbour not in visited) and (IsLinkable(numSet[currIdx], neighbour)) :
            # Mark number as visited
            currvisited = visited[:]
            currvisited.append(neighbour)

            # Perform recursion
            BruteForce(numSet, currvisited, neighbours, neighbourIdx, filterOutputSize)

            # Update Result
            if len(result) < len(currvisited) :
                result = currvisited[:]

            # Print if the solution is large enough
            if len(result) >= filterOutputSize :
                filterOutputSize = len(result)
                print("Potential Chain: " + str(result))
                print("Potential Length:" + str(len(result)))

    visited.clear()
    for currVal in result :
        visited.append(currVal)

# Solve the problem for a specific size
def Solve(setSize, outputSize) :
    problemSize = []
    solutionSize = []
    excludedPrimeSize = []

    result = []
    numSet = range(1,setSize + 1)
    visited = []
    neighbours = []
    prime = []
    excludedPrimes = []

    # Fill the required data structures
    CreateGraph(numSet, visited, neighbours)
                
    # Find all the primes in the list
    for currNum in numSet :
        if IsPrime(currNum) :
            prime.append(currNum)
            if (currNum * 2 > setSize) :
                excludedPrimes.append(currNum)

    # Start the recursion
    for currStart in range(len(numSet)) :
        visited.clear()
        visited.append(numSet[currStart])
        BruteForce(numSet, visited, neighbours, currStart, outputSize)
        if outputSize < len(visited) : 
            outputSize = len(visited)
        if len(visited) > len(result) :
            result.clear()
            for currVal in visited :
                result.append(currVal)

    # Return the biggest sequence
    return  result

# SCRIPT STARTS HERE
for problemSize in range (1, 5) :
    maxSolution = 1
    solution = []
    start_time = time.clock()
    solution = Solve(problemSize, maxSolution)
    if len(solution) > maxSolution : 
        maxSolution = len(solution)
    end_time = time.clock()
    print("Problem Size : " + str(problemSize))
    print("Time Taken : " + str(end_time-start_time))
    print("-----------------------------------------")

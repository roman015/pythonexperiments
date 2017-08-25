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

# Global variable to count number of solutions found
NumberOfSolutions = 0

# Brute Force Method
def BruteForce(numSet, visited, neighbours, currIdx, filterOutputSize) :
    global NumberOfSolutions
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
                NumberOfSolutions = NumberOfSolutions + 1
                filterOutputSize = len(result)
                print("Potential Chain: " + str(result))
                print("Potential Length:" + str(len(result)))

    visited.clear()
    for currVal in result :
        visited.append(currVal)

# Solve the problem for a specific size
def Solve(setSize, outputSize) :
    global NumberOfSolutions
    problemSize = []
    solutionSize = []
    excludedPrimeSize = []

    result = []
    numSet = range(1,setSize + 1)
    visited = []
    neighbours = []
    prime = []
    excludedPrimes = []

    # Reset the Global Counter
    NumberOfSolutions = 0

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
ExpectedSizes = [1, 2, 3, 4, 4, 6, 6, 7, 8, 9, 9, 11, 11, 12, 13, 14, 14, 16, 16, 17, 18, 19, 19, 21, 21, 22, 23, 24, 24]

#inputSize  = 2
#outputSize = 2
#while inputSize < 101 :
#   inputSize = inputSize + 1

#   print("Output : \t" + str(outputSize) + "\tInput : \t" + str(inputSize))
#   outputSize = outputSize + 1

#   if ((outputSize) % 5 == 0) :
#       print("Output : \t" + str(outputSize-1) + "\tInput : \t" + str(inputSize+1))
#       outputSize = outputSize  + 1
#       print("Output : \t" + str(outputSize) + "\tInput : \t" + str(inputSize+2))
#       inputSize = inputSize + 2

    

total_start_time = time.time()
for problemSize in range (1, 10) :
    #maxSolution = 1
    solution = []
    start_time = time.time()
    solution = Solve(problemSize, ExpectedSizes[problemSize-1])
    #if len(solution) > maxSolution : 
    #    maxSolution = len(solution)
    end_time = time.time()
    print()
    print("Problem Size : " + str(problemSize))
    print("Solution Size : " + str(len(solution)))
    print("Number of Solution : " + str(NumberOfSolutions))
    print("Time Taken : " + str(end_time-start_time))
    print("-----------------------------------------")
    print()

total_end_time = time.time()
print("TOTAL TIME : " + str(total_end_time - total_start_time))
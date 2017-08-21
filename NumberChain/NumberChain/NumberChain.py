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
def BruteForce(numSet, visited, neighbours, currIdx) :
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
            BruteForce(numSet, currvisited, neighbours, neighbourIdx)

            # Update Result
            if len(result) < len(currvisited) :
                result = currvisited[:]

    visited.clear()
    for currVal in result :
        visited.append(currVal)
            

# SCRIPT STARTS HERE
problemSize = []
solutionSize = []
excludedPrimeSize = []

result = []
numSet = range(1,1)
visited = []
neighbours = []
prime = []
excludedPrimes = []

# Trying out with multiple sets
for setSize in range(1,30) :
    # Reset values
    result.clear()
    numSet = range(1,setSize+1)
    visited.clear()
    neighbours.clear()
    prime.clear()
    excludedPrimes.clear()

    # Fill the required data structures
    CreateGraph(numSet, visited, neighbours)

    # Find all the primes in the list
    for currNum in numSet :
        if IsPrime(currNum) :
            prime.append(currNum)
            if (currNum * 2 > setSize) :
                excludedPrimes.append(currNum)

    # Display input
    print("Testing with %s numbers" % len(numSet))
    #print("Numbers: " + str(numSet))
    #print("Visited: " + str(visited))
    #print("Neighbours : \n" + str(neighbours))
    #print()
    #print()
    #print("------------------");

    # Start the recursion
    for currStart in range(len(numSet)) :
        visited.clear()
        visited.append(numSet[currStart])
        BruteForce(numSet, visited, neighbours, currStart)
        # Update Result
        #if  len(visited) >= (len(numSet) - len(excludedPrimes) + 1) :
        #    print("Potential Chain: " + str(visited))
        #    print("Potential Len: " + str(len(visited)))
        if len(visited) > len(result) :
            result.clear()
            for currVal in visited :
                result.append(currVal)        

    # Display the result
    #print("------------------");
    #print()
    #print()
    #print("Biggest Chain: " + str(result))
    print("Length of Chain: " + str(len(result)))
    #print()
    #print("Sorted: " + str(sorted(result)))
    #print()

    # Display the primes and excluded primes
    #print("Primes: " + str(prime))
    #print("Excluded Primes: " + str(excludedPrimes))
    #print()
    print("There are %s Excluded Primes"%len(excludedPrimes))
    #print()
    print("------------------");

    problemSize.append(setSize)
    solutionSize.append(len(result))
    excludedPrimeSize.append(len(excludedPrimes))

# End of loop
print(str(problemSize))
print()
print(str(solutionSize))
print()
print(str(excludedPrimeSize))
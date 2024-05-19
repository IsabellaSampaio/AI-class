## Chapter 4 - Beyond Classical Search 

* In the 8-queens problem what matters is the final configuration of the queens, not the order in which they are added.

* Local search algorithms operate using a single current node, instead of multiple paths, and generally move only to neighbors of that node. In that sense, the paths followed by the search are not retrained, only the current state is maintained in the memory. 

* Local search algorithms are used for solving optimization problems, in which the objective is to find the best sate according to an objective function.

    * An objetive function in a mathematical optimization problem is a function that maps states to real values.

    * Decision variables in an optimization problem are those variables whose values can vary over the feasible set of alternatives in order to either increase or decrease the value of the objective function.

* The hill-climbing search algorithm is a loop that continually moves in the direction of increasing value, that being, uphill. It terminates when it reaches a "peak" where no neighbor has a higher value. 

    * Hill-climbing algorithms typically choose randomly among the set of best successors if there is more than one. 

    * Local maxima is a peak that is higher than each of its neighboring states but lower than the global maximum. 

* Simulated Annealing is combines a incomplete hill-climbing algorithm with a a random walk (moving to a successor chosen uniformly at random from the set of successors, being complete). 

    * The simulated-annealing solution is to start by shaking hard and then gradually reducing the intensity of the shaking.

    * Its very similar to hill-climbing, but it doesn't pick the best move, it picks the random move. 

* Genetic Algorithm is a a sample from a class of methods called evolutionaary algorithms. In this context, *objective functions* are called fitness functions. 
    
    * It maintains a population of k states called individuals and each of those is a potential solution. The algorithm creates a new population from the previous one trying to increase the fitness of the individuals. 

    * Tournament selection is a technique for selecting parents from the population. It chooses two individuals from the population, at random, and the one with highest fitness, is selected.

    * The cross-over operation creates new individuals by mixing the parents. 

    * The mutation operation transforms the individual by changing the state value. 

    ### The 8 queens - Using GA 
    
    * An *individual* is a state in which the 8 queens can be represented in the board. It can be as a sequence of 8 numbers ranging from 1 to 8. Each of the 8 numbers represents the position (row) of a queen in a column of the board 

    * The fitness function is the number of *nonattacking* pairs of queens, which has a value of 28 for a solution. GA will try to solve the problem by maximizing this fitness function. 

    * Mutation in this case is to choose a queen at random and move it to a random square in its column. 

    * In the single point crossover, we choose a queen *q* at random, then, create a child by merging the positions from 0 to this *q* queen from the first parent and the positions *q+1* to 8 from the second parent. After that, we do the opposite for the second child. 

    ### The exploration x exploitation dilemma 

    * *Crossover* and *Mutation* are exploration components and aim to not get stuck in the local maxima, while *Selection* is and exploitation operation that aims at reaching the global maximum. 

    * The best way to deal with them is to balance their use, finding a good trade-off between them. 

* The gradient of the objective function is a vector deltaf that gives the magnitude and direction of the steepest slope. 

    * With a locally correct expression for the gradient, it's possible to perform steepest-ascent hill climbing (or gradient ascent / descent). The formula is: x <- x + a*deltaf(x)* where a is a small constant (step size). 

    * Its very important to choose a optimal value for a as it can cause diverse problems. 

* The best-known category is that of a linear programming problems, in which constraints must be linear inequalities forming a convex set and the objective function is also linear. 

    * Convex functions have no local maxima (or optima) only global.  


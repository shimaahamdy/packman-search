# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    
    #dfs algorithm (iterative dfs):
    #1-Created a stack of nodes and visited array 
    #2-Insert the root in the stack and mark it visited.
    #3-loop over stack till it become empty:
             #Pop the element from the stack.
             #check if it is goal ---> return path
             #get childrens and unvisited node of current node
             #mark the children nodes and insert it in the stack.

    # 1
    s=util.Stack()  
    vis = []
    # 2
    root_node = problem.getStartState()    #startstate return x,y only not like getsuccessors 
    s.push((root_node,[]))                 #push node and path that we will take 
    # we need list to attach to stack to removed invaild pathes easily when we return
    vis.append(root_node)
     
    # 3
    while not s.isEmpty():
        current_node,path = s.pop()
        
        if problem.isGoalState(current_node):
            return path
        
        for child_node, next_dir, cost in problem.getSuccessors(current_node):
            if child_node not in vis:
                vis.append(child_node)
                s.push((child_node,path + [next_dir]))
                
              
                
    util.raiseNotDefined()
    

    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

      
    #bfs algorithm (similar to dfs but use queue to trace first insert first):
    #1-Created a queue of nodes and visited array 
    #2-Insert the root in the queue and mark it visited.
    #3-loop over queue till it become empty:
             #Pop the element from the queue.
             #check if it is goal ---> return path
             #get childrens and unvisited node of current node
             #mark the children nodes and insert it in the queue.

    #1
    q=util.Queue()
    vis = []  

    #note, i used first a set to track visited nodes like dfs but in search corner broblem
    #i use a list express state not just postion so i have to changed to a list 

    #2
    root_node = problem.getStartState()
    q.push((root_node,[]))
    vis.append(root_node)

    # 3
    while not q.isEmpty():
        current_node,path = q.pop()
        
        if problem.isGoalState(current_node):
            return path
        
        for child_node, next_dir, cost in problem.getSuccessors(current_node):
            if child_node not in vis:
                vis.append(child_node)
                q.push((child_node,path + [next_dir]))

    util.raiseNotDefined()

    

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #UFC algorithm (use a priority queue to trace low cost first):
    #1-Created a priority queue of nodes and visited array to trck parents nodes that we traced
    #2-Insert the root in the priority queue  with cost=0 and mark it visited.
    #3-loop over priority queue till it become empty:
             #Pop the element with highst prioity from the priority queue.
             #check if it wasnt visited before, mark it visited
             #check if it is goal ---> return path
             #get childrens  of current node
             #insert it in the queue with cost.
    
    #1
    pq = util.PriorityQueue()
    vis = []
    #2
    root_node = problem.getStartState()
    pq.push((root_node,[],0),0)  # the implmented priority queue take proirty as individual item so 
                                 # send cost twice one as actual cost and one used in sorting
    #3
    while not pq.isEmpty():

        current_node,path,parent_cost=pq.pop()
        if current_node not in vis:

            vis.append(current_node)
            
            if problem.isGoalState(current_node):
                return path
            
            for child_node, next_dir, cost in problem.getSuccessors(current_node):
                pq.push((child_node,path+[next_dir],parent_cost+cost),parent_cost+cost)




    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #A* algorithm (same as UCS but priority depend on both heurstic and cost functions):
    #1-Created a priority queue of nodes and visited array to trck parents nodes that we traced
    #2-Insert the root in the priority queue  with cost=0,priority=0 and mark it visited.
    #3-loop over priority queue till it become empty:
             #Pop the element with highst prioity from the priority queue.
             #check if it wasnt visited before, mark it visited
             #check if it is goal ---> return path
             #get childrens  of current node
             #insert it in the queue with cost and priority of heurstic and cost values
    
    #1
    pq = util.PriorityQueue()
    vis = []
    #2
    root_node = problem.getStartState()
    pq.push((root_node,[],0),0)  # the implmented priority queue take proirty as individual item so 
                                 # send cost twice one as actual cost and one used in sorting
    #3
    while not pq.isEmpty():

        current_node,path,parent_cost=pq.pop()
        if current_node not in vis:

            vis.append(current_node)
            
            if problem.isGoalState(current_node):
                return path
            
            for child_node, next_dir, cost in problem.getSuccessors(current_node):
                new_priority = heuristic(child_node,problem)+parent_cost+cost
                pq.push((child_node,path+[next_dir],parent_cost+cost),new_priority)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

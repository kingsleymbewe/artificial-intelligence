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
    # Use a Stack, so the search explores from the last node visited
    fringe = util.Stack()
    # Make an empty list of explored nodes
    visited = []
    # Make an empty list of actions
    actionList = []
    # Place the starting point in the stack
    fringe.push((problem.getStartState(), actionList))
    while fringe:
        node, actions = fringe.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                fringe.push((coordinate, nextActions))
    return []

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    # Use a Queue, so the search explores all nodes on one level before moving to the next level
    fringe = util.Queue()
    # Make an empty list of explored nodes
    visited = []
    # Make an empty list of actions
    actionList = []
    # Place the starting point in the queue
    fringe.push((problem.getStartState(), actionList))
    while fringe:
        node, actions = fringe.pop()
        if not node in visited:
            visited.append(node)
            if problem.isGoalState(node):
                return actions
            for successor in problem.getSuccessors(node):
                coordinate, direction, cost = successor
                nextActions = actions + [direction]
                fringe.push((coordinate, nextActions))
    return []
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
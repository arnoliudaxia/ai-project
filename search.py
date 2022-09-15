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
import search
import searchAgents


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self)->[int,int]:
        """
        return [int,int]
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        """
        util.raiseNotDefined()

    def getSuccessors(self, state)->[(int,int),str,int]:
        """
          state: Search state

        give state, return [(successor state,action, stepCost),...]
        action as 'South'
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

class Node:
    def __init__(self, state, path=None, cost=0):
        if path is None:
            path = []
        self.state = state
        self.path = path
        self.cost = cost





    # util.raiseNotDefined()

def generalGraphSearch(problem:search.SearchProblem, strategy:str,heuristic=lambda x,y:0):
    if problem.isGoalState(problem.getStartState()):
        return []
    #region choose strategy
    dataStructure={
        "dfs":util.Stack,
        "bfs":util.Queue,
        "ucs":util.PriorityQueue,
        "astar":util.PriorityQueue,
        "greedy":util.PriorityQueue,
    }
    frige=dataStructure[strategy]()
    #endregion
    #region init
    startState=problem.getStartState()
    if not isinstance(frige,util.PriorityQueue):
        frige.push(Node(startState))
    else:
        frige.push(Node(startState),0+heuristic(startState,problem))
    visited = []
    #endregion
    while not frige.isEmpty():
        leaf=frige.pop()

        if leaf.state in visited:
            continue
        visited.append(leaf.state)
        if problem.isGoalState(leaf.state):
            print("path is",leaf.path)
            print("step is ",len(leaf.path))
            return leaf.path
        for child in problem.getSuccessors(leaf.state):
            # (5, 4), 'South', 1
            if child[0] in visited:
                continue
            if strategy == 'ucs' or strategy == 'astar' or strategy == 'greedy':
                frige.push(Node(child[0], leaf.path + [child[1]], leaf.cost+child[2]),
                           (strategy == 'ucs' or strategy == 'astar')*(leaf.cost+child[2])+heuristic(child[0],problem))
            else:
                frige.push(Node(child[0],leaf.path+[child[1]]))
    return []

def depthFirstSearch(problem):
    return generalGraphSearch(problem,'dfs')

def breadthFirstSearch(problem):
    return generalGraphSearch(problem,'bfs')

def uniformCostSearch(problem):
    return generalGraphSearch(problem,'ucs')

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    return generalGraphSearch(problem,'astar',heuristic)

def greedySearch(problem, heuristic=nullHeuristic):
    return generalGraphSearch(problem,'greedy',heuristic)
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch

import copy

class Node:
    def __init__(self,value, g, h):
        self.value = value
        
        self.h = h
        self.g = g
        self.f = g+h
        
            
    def __hash__(self):
        return hash(str(self.value))
    
    def __eq__(self, node):
        return node.value == self.value


def h(curState, goalState):
    """heuristic function h(x)"""
    nb = 0
    for cur, goal in zip(curState, goalState):
        for cur_i, goal_i in zip(cur, goal):
            if cur_i != goal_i and cur_i!=" ":
                nb+=1
                
    return nb





def empty_pos(board):
    """ get the empty position """
    for i, row in enumerate(board):
        if " "in row:
            return i, row.index(" ") 
      

def generate_childs(cur_node: Node, goalState):
    """generate all the childs of a specific node"""
    i, j = empty_pos(cur_node.value)
    moves= [(i, j+1), (i, j-1), (i-1, j), (i+1, j)] #right, left, up, down

    childs = []
    for x, y in moves:
        temp = copy.deepcopy(cur_node.value)
        
        if x in range(3) and y in range(3):
            temp[x][y], temp[i][j] = temp[i][j], temp[x][y]

        else:
            temp = None
        
        if temp :
            child = Node(temp, cur_node.g+1, h(temp, goalState))    
            childs.append(child)
            
            
    return childs

def show(board):
        print("-------------")
        for row in board:
            print("| " + " | ".join(row) + " |")
            print("-------------")
        print("* * * * * * * ")
     
def a_star(initState, goalState):
    level= 0 # which gonna be our g(x) function
    start = Node(initState, level, h(initState, goalState))
    tree = [start]
    visited = {start}

    path = []

    while True:
        cur_node = tree[0]
        childs = generate_childs(cur_node, goalState)
            
        
        path.append(cur_node.value)
        
        if(cur_node.value == goalState):
            break
        
        for child in childs:
            if child not in visited:
                tree.append(child)
                visited.add(child)
        
        tree.pop(0)
        
        tree.sort(key = lambda el:el.f)

    return path

       
if __name__=="__main__":
        
    board = [["2","8","3"],
             ["1","6","4"],
             ["7"," ","5"]]
    
    
    goalState = [["1","2","3"],
                ["8"," ","4"],
                ["7","6","5"]]
    
    a_star(board, goalState)

    
    

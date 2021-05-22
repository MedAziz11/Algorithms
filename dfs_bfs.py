import copy


class Node:
    def __init__(self,value, parent=None):
        self.value = value
        self.parent = parent
        
    def __hash__(self):
        return hash(str(self.value))
    
    def __eq__(self, node):
        return node.value == self.value


def empty_pos(board):
    """ get the empty position """
    for i, row in enumerate(board):
        if " "in row:
            return i, row.index(" ")
        

    
def generate_childs(cur_node:Node):
    i, j = empty_pos(cur_node.value)
    moves= [ (i-1, j),(i+1, j), (i, j+1),(i, j-1)] #up, down, right, left
    
    childs = []
    for x, y in moves:
        temp= copy.deepcopy(cur_node.value)
        
        if x in range(3) and y in range(3):
            temp[x][y], temp[i][j] = temp[i][j], temp[x][y]

        else:
            temp = None
        
        if temp :
            child = Node(temp, cur_node)    
            childs.append(child)
            
            
    return childs


def dfs_limited(start, goalState, i, visited=set()):
    visited.add(start)
    
    if start.value == goalState or i ==10 :

        return True
    
    childs = generate_childs(start)
    for child in childs:
        i+=1
        if not(child in visited):
            if dfs_limited(child, goalState, i, visited):
                show(child.value)
                return True
  
    return False


def dfs(start, goalState, i, visited=set()):
    visited.add(start)
    
    if start.value == goalState :

        return True
    
    childs = generate_childs(start)
    for child in childs:
        i+=1
        if not(child in visited):
            if dfs(child, goalState, i, visited):
                show(child.value)
                return True
  
    return False
        


def bfs(board,  goalState):
    start = Node(board)
    
    visited = {start}
    queue = []
    queue.append(start)

    path= [start.value]
    if start.value == goalState: return


    while queue :
        cur_node = queue.pop(0)
        childs = generate_childs(cur_node)
        for child in childs:

            if child not in visited:
                queue.append(child)
                visited.add(child)
                
                path.append(child.value)
                
                show(child.value)
                
                if child.value == goalState:
                    return path
            

                      
def show(board):
    print("-------------")
    for row in board:
        print("| " + " | ".join(row) + " |")
        print("-------------")
    print("* * * * * * * ")
        

        

        
        
if __name__=="__main__":
    board = [["1","2","3"],
             ["8","6"," "],
             ["7","5","4"]]

    
    goalState = [["1","2","3"],
                 ["8"," ","4"],
                 ["7","6","5"]]
    
    
    start = Node(board)
    
    #dfs(start, goalState, 0)
    dfs_limited(start, goalState, 0)
    #bfs(board, goalState)
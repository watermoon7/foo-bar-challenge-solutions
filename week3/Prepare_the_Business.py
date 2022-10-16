from copy import deepcopy
def solution(maze):
    class Node():
        def __init__(self, parent = None, position = None):
            self.parent = parent
            self.position = position
            
            self.g = 0
            self.h = 0
            self.f = 0
            
        def __eq__(self, other):
            return self.position == other.position
    
    def generate_neighbours(maze, node):
        nodes = []
        for move in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            new_pos = [node.position[0] + move[0], node.position[1] + move[1]]
            if new_pos[0] < 0 or new_pos[0] > len(maze[0])-1:
                continue
            elif new_pos[1] < 0 or new_pos[1] > len(maze)-1:
                continue
            elif maze[new_pos[1]][new_pos[0]] == 1:
                continue
            
            new_node = Node(node, new_pos)
            nodes.append(new_node)
        return nodes
        
    def a_star(maze, start, end):
        start_node = Node(None, start)
        end_node = Node(None, end)
        
        open_list = []
        closed_list = []
        
        open_list.append(start_node)
        
        while len(open_list) > 0:
            c_node = open_list[0]
            c_index = 0
            for i, o in enumerate(open_list):
                if o.f < c_node.f and o not in closed_list:
                    c_node = o
                    c_index = i
                    
            open_list.pop(c_index)
            closed_list.append(c_node)
    
            if c_node == end_node:
                path = []
                c = c_node
                while c is not None:
                    path.append(c.position)
                    c = c.parent
                return path
            
            children = []
            for i in generate_neighbours(maze, c_node):
                children.append(i)
            
            
            for child in children:
                for c in closed_list:
                    if child == c:
                        continue
                    
                child.g = c_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h
    
                for o in open_list:
                    if child == o and child.g > o.g:
                        continue
    
                open_list.append(child)
    
    start = [len(maze[0])-1, len(maze)-1]
    end = [0, 0]
    
    totals = []
    maze_copy = deepcopy(maze)
    for e in range(len(maze[0]*len(maze))):
        for i, o in enumerate(maze):
            for j, k in enumerate(o):
                if k == 1:
                    maze_copy[i][j] = 0
                    f = a_star(maze_copy, start, end)
                    totals.append(len(f))
                    maze_copy = deepcopy(maze)
    return min(totals)

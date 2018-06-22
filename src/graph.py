import random

class Edge:
    def __init__(self, destination):
        self.destination = destination

class Vertex:
    def __init__(self, value, **pos):
        self.value =  value
        self.color = 'white'
        self.pos = pos
        self.edges = []

class Graph:
    def __init__(self):
        self.vertexes = []

    def debug_create_test_data(self):
        debug_vertex_1 = Vertex('t1', x=100, y=100)
        debug_vertex_2 = Vertex('t2', x=100, y=300)
        debug_vertex_3 = Vertex('t3', x=200, y=300)
        debug_vertex_4 = Vertex('t4', x=300, y=400)
        debug_vertex_5 = Vertex('t5', x=100, y=400)
        debug_vertex_6 = Vertex('t6', x=200, y=200)

        debug_edge_1 = Edge(debug_vertex_2)
        debug_edge_2 = Edge(debug_vertex_3)
        debug_edge_3 = Edge(debug_vertex_4)
        debug_edge_4 = Edge(debug_vertex_5)
        debug_edge_5 = Edge(debug_vertex_6)
        debug_edge_6 = Edge(debug_vertex_1)
        

        debug_vertex_1.edges.append(debug_edge_1)
        debug_vertex_2.edges.append(debug_edge_2)
        debug_vertex_3.edges.append(debug_edge_3)
        debug_vertex_4.edges.append(debug_edge_4)
        debug_vertex_5.edges.append(debug_edge_5)
        debug_vertex_6.edges.append(debug_edge_6)

        self.vertexes.extend([debug_vertex_1, debug_vertex_2, debug_vertex_3, debug_vertex_4, debug_vertex_5, debug_vertex_6])


    def randomize(self, width, height, pxBox, probability):
        def connectVerts(v0, v1):
            v0.edges.append(Edge(v1))
            v1.edges.append(Edge(v0))

        grid = []
        count = 0

        for y in range(height):
            row = []
            for x in range(width):
                v = Vertex('default', x=300, y=300)
                v.value = f"t{count}"
                count += 1
                row.append(v)
            grid.append(row)
            print(v.value)

        for y in range(height):
            for x in range(width):
                if (y < height - 1):
                    if random.randint(0, 50) < probability:
                        connectVerts(grid[y][x], grid[y+1][x])
                if (x < width - 1):
                    if random.randint(0, 50) < probability:
                        connectVerts(grid[y][x], grid[y][x+1])

        boxBuffer = 0.8
        boxInner = pxBox * boxBuffer
        boxInnerOffset = (pxBox - boxInner) // 2

        for y in range(height):
            for x in range(width):
                grid[y][x].pos['x'] = int((x * pxBox + boxInnerOffset + (random.uniform(0, 50)) * boxInner)) 
                grid[y][x].pos['y'] = int((y * pxBox + boxInnerOffset + (random.uniform(0, 50)) * boxInner))

        for y in range(height):
            for x in range(width):
                self.vertexes.append(grid[y][x])




    def bfs(self, start):
        random_color = "#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        queue = []
        found = []

        queue.append(start)
        found.append(start)

        start.color = random_color

        while len(queue) > 0:
            v = queue[0]
            for edge in v.edges:
                if edge.destination not in found:
                    found.append(edge.destination)
                    queue.append(edge.destination)
                    edge.destination.color = random_color
            
            queue.pop(0)
        return found

    def connected_components(self):
       searched=[]
       for vertex in self.vertexes:
           if vertex not in searched:
               searched.append(self.bfs(vertex))
       return searched



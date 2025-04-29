class Graph():
    def __init__(self, type = "Unordered"):

        self.vertexes = []  #lists all created vertexes
        self.counter = 0    #assigns key numbers to vertexes
        self.type = type    #determines whether edges are added as directed or not
class Graph():
    def __init__(self, _type = "Unordered"):
        self.vertexes = []  #lists all created vertexes
        self.counter = 0    #assigns key numbers to vertexes
        self.types = ("Unordered", "Ordered")
        if _type in self.types:
            self.type = _type    #determines whether edges are added as directed or not
        else:
            raise NameError()
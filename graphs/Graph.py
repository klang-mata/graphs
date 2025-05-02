class Graph():
    #LM: rename `_type`` to `type_`. The ida is not for a variable to be "pythonically private", but to avoid name collision with built-in `type()` function.
    def __init__(self, type_ = "Unordered"):
        self.vertexes = []  #lists all created vertexes
        self.counter = 0    #assigns key numbers to vertexes
        self.types = ("Unordered", "Ordered")
        if type_ in self.types:
            self.type = type_    #determines whether edges are added as directed or not
        else:
            raise NameError()
import json
from pyley.gremlin_query import GremlinQuery


class GraphObject():
    def __init__(self):
        self.__opts = {}

    def V(self):
        return GremlinQuery("g.V()")

    def V(self, *node_ids):
        builder = ""
        l = len(node_ids)
        for index, node_id in enumerate(node_ids):
            if index == l - 1:
                builder += u"'{0:s}'".format(node_id)
            else:
                builder += u"'{0:s}',".format(node_id)

        s__format = u"g.V({0:s})".format(builder)
        return GremlinQuery(s__format)

    def M(self):
        return GremlinQuery("g.Morphism()")

    def Vertex(self):
        return self.V()

    def Vertex(self, *node_ids):
        if len(node_ids) == 0:
            return self.V()

        return self.V(node_ids)

    def Morphism(self):
        return self.M()

    def Emit(self, data):
        return u"g.Emit({0:s})".format(json.dumps(data, default=lambda o: o.__dict__))
import sys

from collections import defaultdict, namedtuple
import re

Edge = namedtuple('Edge', ['weight', 'parent', 'child'])

def create_graph(lines):
    graph = defaultdict(set)
    parents = defaultdict(set)
    orders_to = defaultdict(int)
    orders_from = defaultdict(int)
    for line in lines:
        rs = re.search(r'(Step )(\w)(.)+\s(\w)\s(can)', line)
        node_from = rs.group(2)
        node_to = rs.group(4)

        parents[node_to].add(node_from)

        # this ensures that all the nodes are initialized in the order count
        orders_to[node_from]
        orders_from[node_to]

        weight = ord(node_to) - ord('A')
        orders_to[node_to] += 1
        orders_from[node_from] += 1
        graph[node_from].add(Edge(weight=weight, parent=node_from, child=node_to, traversed=False))

    first = [k for (k,v) in orders_to.iteritems() if v == 0][0]
    last = [k for (k,v) in orders_from.iteritems() if v == 0][0]
    return graph, first, last, parents

class Graph(object):
    def __init__(self):
        self._graph = defaultdict(set)
        self._g_to = defaultdict(set)
        self._g_from = defaultdict(set)
        self._nodes = set()

    def add(self, line):
        rs = re.search(r'(Step )(\w)(.)+\s(\w)\s(can)', line)
        node_from = rs.group(2)
        node_to = rs.group(4)
        self._nodes.add(node_from)
        self._nodes.add(node_to)

        self._g_to[node_to].add(node_from)
        self._g_from[node_from].add(node_to)

        weight = ord(node_to) - ord('A')
        self._graph[node_from].add(Edge(weight=weight, parent=node_from, child=node_to))

    def get_edges(self, node):
        return self._graph[node]

    def get_from(self, node):
        return self._g_from[node]

    def get_to(self, node):
        return self._g_to[node]
    
    def get_num_to(self, node):
        return len(self._g_to[node])

    def get_num_from(self, node):
        return len(self._g_from[node])

    def remove_edge(self, edge):
        self._g_from[edge.parent].remove(edge.child)
        self._g_to[edge.child].remove(edge.parent)
        self._graph[edge.parent].remove(edge)

    def get_first(self):
        for n in self._nodes:
            if len(self._g_to[n]) == 0:
                return n
        else:
            raise ValueError('Could not find first')

    def get_last(self):
        for n in self._nodes:
            if len(self._g_from[n]) == 0:
                return n
        else:
            raise ValueError('Could not find last')

def p1(lines):
    graph = Graph()
    for line in lines:
        graph.add(line)

    currents = set([graph.get_first()])
    path = graph.get_first()
    last = graph.get_last()

    while True:
        edges = set()
        for c in currents:
            edges.update(graph.get_edges(c))

        edges_f = set()
        for e in edges:
            to_nodes = graph.get_to(e.child)
            print 'to: %s %s' % (e.child, to_nodes)
            if (len(to_nodes) < 2 or currents.issuperset(to_nodes)) and e.child not in path:
                edges_f.add(e)

        for e in edges_f:
            print '(%s,%s)' % (e.parent, e.child)

        best_edge = min(edges_f, key=(lambda e: e.weight))
        print '(%s -> %s)' % (best_edge.parent, best_edge.child)

        currents.add(best_edge.child)

        path += best_edge.child

        if best_edge.child == last:
            break

        graph.remove_edge(best_edge)

        # pruning currents
        currents = {c for c in currents if graph.get_num_from(c)}
        print currents

    return path

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        print p1(lines)


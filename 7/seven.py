import sys

from collections import defaultdict, namedtuple
import re
import pdb

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
        self.first = []
        self.last = ''

    def create(self, lines):
        for line in lines:
            rs = re.search(r'(Step )(\w)(.)+\s(\w)\s(can)', line)
            node_from = rs.group(2)
            node_to = rs.group(4)
            self._nodes.add(node_from)
            self._nodes.add(node_to)

            self._g_to[node_to].add(node_from)
            self._g_from[node_from].add(node_to)

            weight = ord(node_to) - ord('A')
            self._graph[node_from].add(Edge(weight=weight, parent=node_from, child=node_to))

        for n in self._nodes: 
            if len(self._g_to[n]) == 0:
                weight = ord(n) - ord('A')
                self._graph['0'].add(Edge(weight=weight, parent='0', child=n))
                self.first.append(n)

        self.last = min(n for n in self._nodes if len(self._g_from[n]) == 0)

    def get_edges(self, node):
        return self._graph[node]

    def get_to(self, node):
        return self._g_to[node]
    
    def get_num_to(self, node):
        return len(self._g_to[node])

    def get_num_from(self, node):
        # ensures the 0 node is never pruned
        if node == '0':
            return 1
        else:
            return len(self._g_from[node])

    def remove_edge(self, edge):
        if not edge.parent == '0':
            self._g_from[edge.parent].remove(edge.child)
            self._g_to[edge.child].remove(edge.parent)

        self._graph[edge.parent].remove(edge)

    def find_candidate_edges(self, currents, path):
        # find all candidate edges
        edges = set()
        for c in currents:
            edges.update(self.get_edges(c))

        finished = {c for c in path}.union(currents)

        edges_f = []
        for e in edges:
            to_nodes = self.get_to(e.child)
            #print 'to: %s %s' % (e.child, to_nodes)
            if (len(to_nodes) < 2 or finished.issuperset(to_nodes)) and e.child not in path:
                edges_f.append(e)

        edges_f.sort(key=lambda e: e.weight, reverse=True)
        return edges_f

def p1(lines):
    graph = Graph()
    graph.create(lines)

    currents = set('0')
    path = ''

    while True:
        edges = set()
        for c in currents:
            edges.update(graph.get_edges(c))

        finished = {c for c in path}.union(currents)
        edges_f = set()
        for e in edges:
            to_nodes = graph.get_to(e.child)
            #print 'to: %s %s' % (e.child, to_nodes)
            if (len(to_nodes) < 2 or finished.issuperset(to_nodes)) and e.child not in path:
                edges_f.add(e)

        for e in edges_f:
            print '(%s,%s)' % (e.parent, e.child)

        best_edge = min(edges_f, key=(lambda e: e.weight))
        print '(%s -> %s)' % (best_edge.parent, best_edge.child)

        currents.add(best_edge.child)
        path += best_edge.child

        if best_edge.child == graph.last:
            break

        graph.remove_edge(best_edge)

        # pruning currents
        currents = {c for c in currents if graph.get_num_from(c)}
        print currents

    return path

class Worker(object):
    def __init__(self):
        self.id = 0
        self.time_left = 0
        self.node = None 

    def __str__(self):
        if self.node:
            return 'id: %d, node: %s, time left: %d' % (self.id, self.node, self.time_left)
        else:
            return 'id: %d, idle' % (self.id)

def p2(lines, num_workers=2, time_per_step=0):
    graph = Graph()
    graph.create(lines)

    currents = set('0')
    path = ''
    time = 0

    workers = [Worker() for w in xrange(num_workers)]
    for w in xrange(num_workers):
        workers[w].id = w

    busy_nodes = set()

    while True:

        ## assign to workers
        for worker in workers:
            # if not busy 
            if not worker.time_left: 

                # if was doing something before, finish up
                if worker.node:
                    currents.add(worker.node)
                    path += worker.node
                    # pruning currents
                    currents = {c for c in currents if graph.get_num_from(c)}

                edges_f = graph.find_candidate_edges(currents, path)
                available_nodes = list(set(e.child for e in edges_f if e.child not in busy_nodes))
                available_nodes.sort(reverse=True)

                # if there is something more to do, assign, if not set to idle
                if available_nodes:
                    n = available_nodes.pop()
                    busy_nodes.add(n)
                    worker.time_left = ord(n) - ord('A') + time_per_step + 1
                    worker.node = n
                    print 'starting %s at %d' % (n, time)
                else:
                    worker.node = None

            #print 'time: %d worker: %s' % (time, worker)

        if graph.last in path:
            break

        # do work
        time += 1

        for worker in workers:
            if worker.node:
                worker.time_left -= 1

    print path
    return time

if __name__ == '__main__':

    with open(sys.argv[1]) as f:
        lines = f.read().splitlines()
        #print p1(lines)
        print p2(lines, num_workers=5, time_per_step=60)
        #print p2(lines, num_workers=5, time_per_step=0)

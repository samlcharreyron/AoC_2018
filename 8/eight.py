import sys
from collections import defaultdict, namedtuple, deque

class Node(object):
    __slots__ = ('d_start', 'm_start', 'num_nodes', 'num_md')
    def __init__(self, num_nodes=-1, num_md=-1, d_start=-1, m_start=-1): 
        self.num_nodes = num_nodes
        self.d_start = d_start
        self.m_start = m_start
        self.num_md = num_md
        
    def __repr__(self):
        return 'Node(num_nodes=%d, num_md=%d, d_start=%d, m_start=%d)' % (self.num_nodes,
                self.num_md, self.d_start, self.m_start)

def dfs(tree, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(tree[vertex] - visited)
    return visited

def p1_old(string):
    ready = {0}
    complete = {0}
    stack = [0]
    tree = defaultdict(set)
    root = Node(num_nodes=string[0], num_md=string[1], 
            d_start=2, m_start=(len(string) - string[1]))
    nodes = defaultdict(Node)
    nodes[0] = root

    it = 0
    while stack:
        vid = stack.pop()
        print('popped %d' % vid)

        if vid in ready:
            vertex = nodes[vid] 

            if vertex.num_nodes == 0:
                # we are at a leaf
                print('%d is a leaf' % vid)
                vertex.m_start = vertex.d_start 
                complete.add(vid)
                if stack:
                    nid = stack[-1]
                    n_vertex = nodes[nid]
                    head = vertex.m_start + vertex.num_md
                    n_vertex.num_nodes = string[head]
                    n_vertex.num_md = string[head+1]
                    n_vertex.d_start = head + 2
                    print('adding %d to ready' % nid)
                    ready.add(nid)

            elif tree[vid]: 
                if tree[vid].issubset(complete): 
                    # get leaf from depth first search
                    path = list(dfs(tree, vid))
                    path.sort()
                    lid = path[-1]
                    leaf = nodes[lid]
                    vertex.m_start = leaf.m_start + leaf.num_md 
                    print('adding %d to complete' % vid)
                    complete.add(vid)
                    if stack:
                        nid = stack[-1]
                        n_vertex = nodes[nid]
                        head = vertex.m_start + vertex.num_md
                        n_vertex.num_nodes = string[head]
                        n_vertex.num_md = string[head+1]
                        n_vertex.d_start = head + 2
                        print('adding %d to ready' % nid)
                        ready.add(nid)
            else:
                if vid not in complete:
                    print('adding %d to stack' % vid)
                    stack.append(vid)

                # populate tree
                for i in range(1, vertex.num_nodes):
                    child = Node()
                    cid = len(nodes.keys())
                    nodes[cid] = child
                    tree[vid].add(cid)
                    stack.append(cid)
                    print('adding %d to stack' % cid)

                child = Node(num_nodes=string[vertex.d_start],
                        num_md=string[vertex.d_start+1], d_start=(vertex.d_start) + 2)
                cid = len(nodes.keys())
                nodes[cid] = child
                tree[vid].add(cid)
                print('adding %d to ready' % cid)
                ready.add(cid)
                print('adding %d to stack' % cid)
                stack.append(cid)

        else:
            print('%d not ready' % vid)
            stack.append(vid)

        it += 1

    for node in nodes.values():
        if node.m_start == -1:
            raise ValueError('invalid tree')

    return sum([sum(string[node.m_start:node.m_start+node.num_md]) for node in nodes.values()])


def process(data):
    children, md = data[:2]
    data = data[2:]
    total = 0

    for c in range(children):
        data, s_md = process(data)
        total += s_md

    total += sum(data[:md])

    if children == 0:
        return (data[md:], total)
    else:
        return (data[md:], total)

if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        string = f.read().strip().split(' ')
        string_i = [int(c) for c in string]
        _, total = process(string_i)
        print(total)

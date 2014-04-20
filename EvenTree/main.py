#!/usr/bin/python3

import sys
import collections

class Node:
    def __init__(self):
        self.children = set()
        self.weight = 1

    def __str__(self):
        return "children: {}, weight: {}".format(self.children, self.weight)

def dfs(node, graph):

    for child in graph[node].children:
        if graph[child].weight==1 and graph[child].children:
            dfs(child, graph)

    graph[node].weight += sum([graph[child].weight for child in graph[node].children])

def solve(node, graph, edges_to_remove):
    for child in graph[node].children:
        if graph[child].weight%2==0:
            edges_to_remove.add((node, child))
        solve(child, graph, edges_to_remove)

if __name__ == "__main__":

    [_, M] = [int(X) for X in sys.stdin.readline().split()]

    graph = collections.defaultdict(Node)

    for edge in range(M):

        [child, parent] = [int(X) for X in sys.stdin.readline().split()]

        graph[parent].children.add(child)

    dfs(1, graph)

    edges_to_remove = set()
    solve(1, graph, edges_to_remove)

    print(len(edges_to_remove))


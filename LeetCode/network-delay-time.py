# https://leetcode.com/problems/network-delay-time/description/

import math  # We'll need it for the inf constant
from collections import defaultdict


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Process input (see example below)
        edges = defaultdict(list)  # A dict with no KeyError exceptions
        for edge in times:
            edges[edge[0]].append(edge[1:])
        # For example:
        # times = [
        #    ...
        #    [2, 1, 1]
        #    ...
        #    [2, 3, 1]
        #    ...
        #]
        # edges[2] == [
        #    [1, 1],
        #    [3, 1]
        # ]

        # Run Dijkstra
        next_nodes = {k: 0}  # Nodes that we have seen, but not yet processed
                             # This is not a `defaultdict` because we would need
                             # to default-initialize its items with `inf`,
                             # which we have not learnt to do yet
        max_time = 0  # The answer to the problem
        processed = set()  # Nodes that we have seen AND processed
        node_id = k  # ID of the node that we're processing on this iteration

        # While there's still something that we have seen,
        # but not processed yet
        while next_nodes:
            node_time = next_nodes.pop(node_id)  # 'Weight' of the current node
            processed.add(node_id)  # So that we don't process this node again
            max_time = max(max_time, node_time)  # Update the answer

            # Now let's see this node's neighbours
            for edge in edges[node_id]:
                v = edge[0]  # Node that can be reached from the current node
                weight = edge[1]  # Weight of the edge towards it
                
                # Unfortunately, setting up a sorted structure is tricky,
                # so `next_nodes` is just a dictionary; it is not sorted,
                # and later we will have to iterate through it (O(n) ops)
                # to find where to go next. Hence we update `next_nodes`
                # values just as we always do for a `dict`. 
                if v not in processed:  # Neighbour is either a new or a not processed yet node
                    if v not in next_nodes: # Neighbour is a brand new node
                        next_nodes[v] = node_time + weight
                    else:  # We have seen this neighbour, but maybe it can be reached faster
                        next_nodes[v] = min(next_nodes[v], node_time + weight)
            
            # The O(n) search of the next node to go
            min_time = math.inf
            for node, time in next_nodes.items():
                if min_time > time:
                    min_time = time
                    node_id = node
        if len(processed) != n:  # If we haven't visited all of the nodes
            return -1
        else:
            return max_time

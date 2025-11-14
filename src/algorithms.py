import heapq

class SPFA_Algorithms:
    @staticmethod
    def dijkstras(n, edges, src, dst):
        adj = {i: [] for i in range(n)}

        # edges: (u,v,w)
        for u, v, w in edges:
            adj[u].append((v, w))

        dist = {i: float("inf") for i in range(n)}
        parent = {i: None for i in range(n)}

        dist[src] = 0
        pq = [(0, src)]

        while pq:
            cur_dist, node = heapq.heappop(pq)

            if node == dst:
                break  # we found the shortest path to the goal

            if cur_dist > dist[node]:
                continue

            for neigh, w in adj[node]:
                new_dist = cur_dist + w
                if new_dist < dist[neigh]:
                    dist[neigh] = new_dist
                    parent[neigh] = node
                    heapq.heappush(pq, (new_dist, neigh))

        # reconstruct path
        path = []
        cur = dst
        while cur is not None:
            path.append(cur)
            cur = parent[cur]

        path.reverse()
        return path     # list of node indices

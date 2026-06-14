class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        all_nodes = {}
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
            all_nodes[u] = False
            all_nodes[v] = False
        
        start_node = next(iter(adj_list))
        visited = {start_node}
        q = deque()
        parts = 0
        originalN = n
        while all_nodes:
            nt = next(iter(all_nodes))
            q.append(nt)
            while q:
                node = q.popleft()

                all_nodes.pop(node, 'not found')
                originalN -= 1
                for neighbor in adj_list[node]:
                    if neighbor not in visited:

                        visited.add(neighbor)
                        q.append(neighbor)
            parts += 1
        return parts + (n - len(visited))
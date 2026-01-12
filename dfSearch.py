def DFS(graph,node,visited=None):
    if visited is None:
        visited=set()
    if node not in visited:
        print(f"Visited:{node}")
        visited.add(node)
        for neighbour in graph[node]:
            DFS(graph,neighbour,visited)

graph={"A":["B","C"],"B":["A","D","E"],"C":["A","F"],"D":["B"],"E":["B","F"],"F":["C","E"]}
DFS(graph,"A",visited=None)
from collections import deque
def BFS(graph,start_node):
    queue=deque([start_node])
    visited=set()
    while queue:
        node=queue.popleft()
        if(node not in visited):
            print(f"Visited:{node}")
            visited.add(node)
        queue.extend(neighbours for neighbours in graph[node] if neighbours not in visited)
graph={"A":["B","C"],"B":["A","D","E"],"C":["A","F"],"D":["B"],"E":["B","F"],"F":["C","E"]}
BFS(graph,"A")
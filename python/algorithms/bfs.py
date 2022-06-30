from collections import deque 

graph = {
  'A': set('B'),
  'B': set('C'),
  'D': set(['G', 'C']),
  'G': set('A'),
  'C': set('C')
}



def getNeighbors(graph, nodeId: str):
  return list(graph.get(nodeId))


def bfs(graph, source: str, target: str):

  visited = set()
  visited.add(source)
  queue = deque([source])

  while len(queue) > 0:
    visiting = queue.popleft() #dfs is the same with pop instead of popleft
    for neighbor in getNeighbors(graph, visiting):
      if neighbor == target: return True
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
  return False

def dfs(graph, source: str, target: str):

  visited = set()
  visited.add(source)
  queue = deque([source])

  while len(queue) > 0:
    visiting = queue.pop() #bfs is the same with popleft instead of pop
    for neighbor in getNeighbors(graph, visiting):
      if neighbor == target: return True
      if neighbor not in visited:
        visited.add(neighbor)
        queue.append(neighbor)
  return False
      
print(bfs(graph, 'B', 'C'))
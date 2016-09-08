graph = {
	1:[2,3,4],
	2:[5,6],
	3:[10],
	4:[7,8],
	5:[9,10],
	7:[11,12],
	11:[13],
}

def bfs(graph,start,end):
    visited,queue = set(),[[start]]
    while queue:
	path = queue.pop(0)
	vertex = path[-1]
	print queue 
	if vertex == end:
	   return path
	elif vertex not in visited:
 	   for neighbor in graph.get(vertex,[]):
		new_path = list(path)
		new_path.append(neighbor)
		queue.append(new_path)
	   visited.add(vertex)


 	
print ("BFS looks like following")	
'bfs(graph,1,13)'
dfs(graph,1)
'''
print ("DFS looks like following")	
dfs(graph,'A')
'''

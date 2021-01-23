from collections import defaultdict,deque
import heapq
with open('dijkstraData.txt','r') as f:
    data=f.readlines()

graph=defaultdict(list)

node_size=0
for row in data:
    parsed=row.split('\t')[:-1]
    print(parsed)
    node_size+=1
    for edge in parsed[1:]:
        node,val=edge.split(',')
        graph[int(parsed[0])].append((int(node),int(val)))


src=1
min_heap=[(0,src)]
distance=[1000000 if i!=int(src) else 0 for i in range(node_size+1)]
visited=set()


while min_heap:
    u=heapq.heappop(min_heap)
    visited.add(u[1])
    print(u)
    for v in graph[u[1]]:
        d_val=(v[1]+distance[u[1]])
        if v not in visited and d_val<distance[v[0]]:
            distance[v[0]]=d_val
            heapq.heappush(min_heap,(distance[v[0]],v[0]))

','.join([str(distance[i]) for i in [7,37,59,82,99,115,133,165,188,197]])
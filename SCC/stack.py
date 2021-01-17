import sys,resource 

sys.setrecursionlimit(2**20)
hardlimit=resource.getrlimit(resource.RLIMIT_STACK)[1]
resource.setrlimit(resource.RLIMIT_STACK,(hardlimit,hardlimit))

class SCC:
    def __init__(self):
        from collections import defaultdict
        graph="""1 4\n2 8\n3 6\n4 7\n5 2\n6 9\n7 1\n8 5\n8 6\n9 7\n9 3"""
        # graph="""1 2\n2 6\n2 3\n2 4\n3 1\n3 4\n4 5\n5 4\n6 5\n6 7\n7 6\n7 8\n8 5\n8 7"""
        # graph="""1 2\n2 3\n3 1\n3 4\n5 4\n6 4\n8 6\n6 7\n7 8\n4 3\n4 6"""
        # graph="""1 2\n2 3\n2 4\n2 5\n3 6\n4 5\n4 7\n5 2\n5 6\n5 7\n6 3\n6 8\n7 8\n7 10\n8 7\n9 7\n10 9\n10 11\n11 12\n12 10"""
        # self.g=defaultdict(list)
        # self.r_g=defaultdict(list)
        # node_num=set()

        # for i in graph.split('\n'):
        #     tmp=i.split(' ')
        #     source=tmp[0]
        #     target=tmp[1]
        #     self.g[int(source)].append(int(target))
        #     self.r_g[int(target)].append(int(source))
        #     node_num.add(source)
        #     node_num.add(target)
        # node_num=len(node_num)+1

        with open('graph.txt','r') as f:
            graph=f.readlines() 

        self.g=defaultdict(list)
        self.r_g=defaultdict(list)
        node_num=set()
        for i in graph:
            tmp=i.split(' ')
            source=tmp[0]
            target=tmp[1]
            self.g[int(source)].append(int(target))
            self.r_g[int(target)].append(int(source))
            node_num.add(source)
            node_num.add(target)
        node_num=len(node_num)+1

        print('parsing over...')
        self.t=0
        self.s=None
        self.visited=[False]*node_num
        self.leader=[-1]*node_num
        self.finish_time=[0]*node_num
        for node in range(node_num-1,0,-1):
            if not self.visited[node]:
                self.s=node
                self.dfs1(node)

        self.visited2=[False]*node_num
        self.g_second_pass=defaultdict(list)
        for source in range(node_num-1,0,-1):
            for target in self.g[source]:
                self.g_second_pass[self.finish_time[source]].append(self.finish_time[target])

        self.res=[]
        for node in range(node_num-1,0,-1):
            if not self.visited2[node]:
                self.res.append(self.dfs2(node))

    def dfs1(self, node):
        stack=[(node, 0)]
        while stack:
            tup = stack.pop()
            curr = tup[0]
            end = True
            for i in range(tup[1], len(self.r_g[curr])):
                if (not self.visited[self.r_g[curr][i]]) and (self.r_g[curr][i] != curr):
                    end = False
                    stack.append((curr, i+1))
                    stack.append((self.r_g[curr][i], 0))
                    break
            if end or len(self.r_g[curr]) == tup[1]:
                self.t+=1
                self.finish_time[curr]=self.t
            self.visited[curr]=True
            self.leader[curr]=node
    
    def dfs2(self,node):
        agg=0
        if not self.visited2[node]:
            self.visited2[node]=True
            for dfs_node in self.g_second_pass[node]:
                if not self.visited2[dfs_node]:
                    agg+=self.dfs2(dfs_node)
            return 1+agg
        return 0

if __name__=='__main__':
    s=SCC()
    s.res.sort()
    print(s.res[-10:])


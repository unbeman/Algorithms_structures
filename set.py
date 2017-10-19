class Set:
    def __init__(self, n):
        self.__parent = [0 for i in range(n+1)]
        self.__rank = [0 for i in range(n+1)]

    def MakeSet(self ,i):
        self.__parent[i] = i
        self.__rank[i] = 0

    def Find(self, i):
        if i != self.__parent[i]:
            self.__parent[i] = self.Find(self.__parent[i])
        return self.__parent[i]

    def Union(self, i, j):
        i_id = self.Find(i)
        j_id = self.Find(j)
        if i_id == j_id:
            return i_id, i_id, j_id
        if self.__rank[i_id] > self.__rank[j_id]:
            self.__parent[j_id] = i_id
            return i_id, i_id, j_id
        else:
            self.__parent[i_id] = j_id
            if self.__rank[i_id] == self.__rank[j_id]:
                self.__rank[j_id] += 1
            return j_id, i_id, j_id #временно!
        

n, m = map(int, input().split(' '))
t = list(map(int, input().split(' ')))
tables_size = [max(t)]
tables_size.extend(t)
path = []
s = Set(n)
for i in range(1,n + 1):
    s.MakeSet(i)

for i in range(m):
    dst, src = map(int, input().split(' '))
    root, i_id, j_id = s.Union(dst, src)
    if i_id != j_id:
        tables_size[root] = tables_size[i_id] + tables_size[j_id]
    tables_size[0] = tables_size[root] if tables_size[root] > tables_size[0] else tables_size[0]
    print(tables_size[0])

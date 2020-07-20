class Solution(object):
    def findRedundantConnection1(self, edges):
        parent = [0] * len(edges)

        def find(x):
            print(parent)
            if parent[x] == 0:
                return x
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            return True

        for x, y in edges:
            if not union(x - 1, y - 1):
                return [x, y]

        raise ValueError("Illegal input.")

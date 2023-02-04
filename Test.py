import collections

dq = collections.deque()
def find(a, b, vis=None):
	if
	if a == b:
		return l1[b[0]][b[1]]
	if vis is None:
		vis = [[True, True, True], [True, True, True], [True, True, True]]
	vis[a[0]][a[1]] = False
	
l = [[1, 1, 1, 1, 1],
     [1, 0, 1, 0, 1],
     [1, 0, 1, 0, 1],
     [1, 0, 0, 0, 1],
     [1, 1, 1, 1, 1]]

l1 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

print(find([1, 1], [1, 3]))

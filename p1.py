# def aStarAlgo(start_node, stop_node):
#     open_set = set(start_node)
#     print('open_set', open_set)
#     closed_set = set()
#     print('set', set)
#     g = {}
#     parents = {}
#     print('parents', parents)
#
#     g[start_node] = 0
#
#     parents[start_node] = start_node
#     print('Start_node', start_node)
#
#     while len(open_set) > 0:
#         print('open_set1', open_set)
#         n = None
#         print('n', n)
#
#         for v in open_set:
#             if n == None or g[v] + heuristic(v) < g[n] + heuristic(n):
#
#                 print('g[v]', g[v])
#                 print('heuristic(v)', heuristic(v))
#
#                 n = v
#                 print('v', v)
#
#         if n == stop_node or Graph_nodes[n] == None:
#             print('n1', n)
#             pass
#         else:
#             for (m, weight) in get_neighbors(n):
#                 print('m', m)
#                 print('weight', weight)
#                 print('get_neighbors(n)', get_neighbors(n))
#
#
#
#                 if m not in open_set and m not in closed_set:
#                     print('open_set', open_set)
#                     print('closed_set', closed_set)
#                     open_set.add(m)
#                     parents[m] = n
#                     print('n1', n)
#                     g[m] = g[n] + weight
#                     print('g[m]', g[m])
#                     print('g[n]', g[n])
#                     print('weight', weight)
#
#
#                 else:
#                     if g[m] > g[n] + weight:
#                         print('g1[m]', g[m])
#
#                         g[m] = g[n] + weight
#
#                         parents[m] = n
#                         print('n2', n)
#
#                         if m in closed_set:
#                             print('m', m)
#                             closed_set.remove(m)
#                             open_set.add(m)
#                             print('open_set.add(m)', open_set.add(m))
#         if n == None:
#             print('Path does not exist!')
#             return None
#
#         if n == stop_node:
#             print('n3', n)
#             path = []
#             print('path', path)
#             while parents[n] != n:
#                 print('n4', n)
#                 path.append(n)
#                 n = parents[n]
#                 print('n5', n)
#                 print('parents[n]', parents[n])
#             path.append(start_node)
#             path.reverse()
#             print('path.reverse()', path.reverse())
#             print('Path found: {}'.format(path))
#             return path
#
#         open_set.remove(n)
#         closed_set.add(n)
#         print(' closed_set.add(n)', closed_set.add(n))
#     print('Path does not exist!')
#     return None
#
#
#
# def get_neighbors(v):
#     if v in Graph_nodes:
#         print('v1', v)
#         return Graph_nodes[v]
#         print(Graph_nodes[v])
#     else:
#         return None
# def heuristic(n):
#     H_dist = {
#         'S': 7,
#         'A': 6,
#         'B': 2,
#         'C': 1,
#         'D': 0,
#     }
#     return H_dist[n]
#     print('H_dist[n]', H_dist[n])
# Graph_nodes = {
#     'S': [('A', 1), ('B', 4)],
#     'A': [('B', 2), ('D', 12)],
#     'B': [('C', 2)],
#     'C': [('D', 3)],
# }
# aStarAlgo('S', 'D')
#
#
print('back')

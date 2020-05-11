# question related to coloring a map with only 4 colors.
# look up numberphile video for more background
# requirement that there is always solution AND that
# only 3 paths can exist between gardens allow for no graph traversal

def flower_paths(N, paths):

    paths_list = []
    for i in range(N):
        paths_list.append([])

    for pair in paths:

        paths_list[pair[0] - 1].append(pair[1])
        paths_list[pair[1] - 1].append(pair[0])

    print(paths_list)
    flowers_planted = [0] * N
    for i in range(len(paths_list)):
        current_garden_neighbors = paths_list[i]
        print(i + 1, "neightbors",current_garden_neighbors)
        allowed_flowers = [1,2,3,4]
        num_removed = 0
        for p in current_garden_neighbors:
            if flowers_planted[p - 1] != 0 and flowers_planted[p - 1] in allowed_flowers:
                allowed_flowers.remove(flowers_planted[p - 1])

        flowers_planted[i] = allowed_flowers[0]

    print(flowers_planted)

N = 3
paths = [[1,2],[2,3],[3,1]]
flower_paths(N,paths)

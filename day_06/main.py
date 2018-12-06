from collections import defaultdict

data = [i.strip() for i in open('input').readlines()]
coords = [tuple(map(int, line.split(", "))) for line in data]
max_x = max([x for (x, _) in coords])
max_y = max([y for (y, _) in coords])

def manhattan_dist(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)

if __name__ == "__main__":
    coords_dict = {id_coord: pos for id_coord, pos in enumerate(coords, start=1)}
    regions = defaultdict(int)
    ids_infinite = set()

    for i in range(max_x + 1):
        for j in range(max_y + 1):
            min_dists = sorted([(manhattan_dist(x, i, y, j), id_coord) for id_coord, (x, y) in coords_dict.items()])
            # if closest distances are equal, ignore
            if min_dists[0][0] != min_dists[1][0]:
                id_coord = min_dists[0][1]
                regions[id_coord] += 1

                if i == 0 or i == max_x or j == 0 or j == max_y:
                    ids_infinite.add(id_coord)
    
    largest = max(size for id_coord, size in regions.items() if id_coord not in ids_infinite)
    print("Largest finite area: {:d}".format(largest))
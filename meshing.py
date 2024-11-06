import numpy as np
import pandas as pd
import matplotlib; matplotlib.rcParams["savefig.directory"] = "."
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 18})

bench_height = 1
bench_width = 1
#bench_angle = np.degrees()
n_cuts = 5
buffer_depth = (bench_height * n_cuts)*0.2
cuts = []
points = []

def add(new_point):
    assert type(new_point) is tuple
    if new_point in points:
        return points.index(new_point)
    points.append(new_point)
    return len(points)-1


for i in range(n_cuts): # each cut
    polygons = []
    n = i+1 # number of benches in this cut

    for j in range(n): # each bench
        x0 = 0-bench_width*(i-j)
        y0 = 0-bench_height*j
        # top left
        x1 = x0-bench_width
        y1 = y0
        # bottom left
        x2 = x1
        y2 = y0-bench_height
        # bottom right
        x3 = x0
        y3 = y2

        i0 = add((x0, y0))
        i1 = add((x1, y1))
        i2 = add((x2, y2))
        i3 = add((x3, y3))
        polygons.append((i0,i1,i2,i3))

    cuts.append(polygons)

print("model new")
print("sketch set create 'jason'")

for p in points:
    print(f"sketch point create {p}")

for i, cut in enumerate(cuts):
    for poly in cut:
        print(f"sketch edge create by-points {poly[1-1]+1} {poly[2-1]+1}")
        print(f"sketch edge create by-points {poly[2-1]+1} {poly[3-1]+1}")
        print(f"sketch edge create by-points {poly[3-1]+1} {poly[4-1]+1}")
        print(f"sketch edge create by-points {poly[4-1]+1} {poly[1-1]+1}")
        print(f"sketch block create by-points {poly[1-1]+1} {poly[2-1]+1} {poly[3-1]+1} {poly[4-1]+1} group 'cut{i}'")
print("sketch block create automatic")
print("zone generate from-sketch")

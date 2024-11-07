
import numpy as np
import pandas as pd
import matplotlib; matplotlib.rcParams["savefig.directory"] = "."
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 18})

bench_height = 10
dx = 2.5  # target zone size
bench_width = 15
#bench_angle = np.degrees()
n_cuts = 5
buffer_depth = (bench_height * n_cuts)*0.4
buffer_back = (bench_width * n_cuts)*0.75
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
    final_points = dict()
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
        final_points[i1] = None
        final_points[i2] = None
        final_points[i3] = None
        polygons.append((i0,i1,i2,i3))

    cuts.append(polygons)

print("model new")
print("sketch set create 'jason'")
print(f"sketch edge zone-length-default {dx}")
f0 = add((-75, -22)) # fault
f1 = add((-24, -48))

# outer box
box = (add((-(n_cuts*bench_width+buffer_back), 0)),
       add((-(n_cuts*bench_width+buffer_back), -(n_cuts*bench_height+buffer_depth))),
       add((0, -(n_cuts*bench_height+buffer_depth))))

for p in points:
    print(f"sketch point create {p}")

for i, cut in enumerate(cuts):
    for poly in cut:
        print(f"sketch edge create by-points {poly[1-1]+1} {poly[2-1]+1}")
        print(f"sketch edge create by-points {poly[2-1]+1} {poly[3-1]+1} group 'cut{i}'")
        print(f"sketch edge create by-points {poly[3-1]+1} {poly[4-1]+1} group 'cut{i}'")
        print(f"sketch edge create by-points {poly[4-1]+1} {poly[1-1]+1}")
        print(f"sketch block create by-points {poly[1-1]+1} {poly[2-1]+1} {poly[3-1]+1} {poly[4-1]+1} group 'cut{i}'")


print(f"sketch edge create by-points {f0+1} {f1+1}")
print(f"sketch edge create by-points {tuple(final_points.keys())[0]+1} {box[0]+1}")
print(f"sketch edge create by-points {box[0]+1} {box[1]+1}")
print(f"sketch edge create by-points {box[1]+1} {box[2]+1}")
print(f"sketch edge create by-points {box[2]+1} {tuple(final_points.keys())[-1]+1}")
intact = list(final_points.keys())+list(box)
print(f"sketch block create by-points {tuple(map(lambda _:_+1, intact))}")
print(f"sketch mesh target-size {dx}")
print("zone generate from-sketch")

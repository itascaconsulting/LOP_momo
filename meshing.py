import numpy as np
import pandas as pd
import matplotlib; matplotlib.rcParams["savefig.directory"] = "."
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 18})

bench_height = 15
bench_width = 20
#bench_angle = np.degrees()
n_cuts = 5
buffer_depth = (bench_height * n_cuts)*0.2
cuts = []
points = []
for i in range(n_cuts): # each cut
    polygons = []

    for j in range(i+1): # each bench
        # top right
        x0 = -j*bench_width
        y0 = -i*bench_height

        # top left
        x1 = -(j+1)*bench_width
        y1 = -i*bench_height
        # bottom left
        x2 = -(j+1)*bench_width
        y2 = -(i+1)*bench_height
        # bottom right
        x3 = -j*bench_width
        y3 = -(i+1)*bench_height

        points.append((x0, y0))
        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x3, y3))
        polygons.append(tuple(range(len(points)-4,len(points))))
    cuts.append(polygons)

# sketch point create {t_0}
# sketch point create {t_1}
# sketch point create {t_2}
# sketch point create {t_3}
# sketch edge create by-points 1 2 size {int(round(d/H*mesh_size)+2*mesh_size)}
# sketch edge create by-points 2 3 size {mesh_size}
# sketch edge create by-points 3 4 size {2*mesh_size}
# sketch edge create by-points 4 1 size {int(round(hyp/H*mesh_size))}
# sketch mesh type unstructured
# sketch block create automatic
# zone generate from-sketch
for p in points:
    print(f"sketch point create {p}")

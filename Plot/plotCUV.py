import matplotlib.pyplot as plt
import matplotlib.animation as amp
import numpy as np
from timeit import default_timer as timer
import cartopy.crs as ccrs

def image(np_array, lat, lon) :
    n = int(max(lat))
    s = int(min(lat))
    e = int(max(lon))
    w = int(min(lon))

    lon = np.linspace(w, e, (e-w)*2+1)
    lat = np.linspace(s, n, (n-s)*2+1)

    X, Y = np.meshgrid(lon, lat)
    C = np_array[0]
    U = np_array[1]
    V = np_array[2]

    fig = plt.figure(figsize=(35, 25))
    box = [100, 135, 25, 50]
    scale = '50m'
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent(box, crs=ccrs.PlateCarree())
    ax.coastlines(scale)
    ax.set_xticks(np.arange(box[0], box[1], 0.5), crs=ccrs.PlateCarree())
    ax.set_yticks(np.arange(box[2], box[3], 0.5), crs=ccrs.PlateCarree())
    ax.grid(b=True)

    c = ax.pcolormesh(X, Y, C)
    Q = ax.quiver(X, Y, U, V, scale=30, scale_units='inches')

    plt.show()
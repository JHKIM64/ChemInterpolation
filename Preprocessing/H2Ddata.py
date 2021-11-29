import xarray as xr
import datetime as dt
import numpy as np
hourly_data = xr.open_dataset('/home/intern01/jhk/Observation/EA_AQ_1920_05x05.nc')

hours = hourly_data.time.values

tick = hours[0]
for hour in hours :
    if tick != hour :
        print('miss')
        tick = hour
    else :
        print(hour)
    tick += np.timedelta64(1,'h')

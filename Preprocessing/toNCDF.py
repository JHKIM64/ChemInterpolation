import pandas as pd
from Preprocessing.AirKorea import getKRAQ
from Preprocessing.AirChina import getCHAQ
#'20210101', '20210430', 39, 34, 124, 133
def run(begin, end, top, bottom, left, right) :
    krdf = getKRAQ.EA_AQdata(begin, end, top, bottom, left, right)
    chdf = getCHAQ.EA_AQdata(begin, end, top, bottom, left, right)
    print(krdf.time)
    print(chdf.time)
    df = pd.concat([krdf,chdf]).sort_index()
    df.reset_index(inplace=True)
    df["datetime"] = pd.to_datetime(df["datetime"],format="%Y-%m-%d %H:%M:%S")
    df = df.rename(columns={"datetime":"time","Lat":"latitude","Lon":"longitude"})
    df = df.set_index(['time', 'latitude', 'longitude'])

    aqxarray = df.to_xarray()
    print(aqxarray)
    aqxarray.to_netcdf("/home/intern01/jhk/Observation/EA_AQ_1920_05x05.nc")

run('20190101', '20201231', 50, 25, 100, 135)
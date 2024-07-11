import xarray as xr
from webdav4.client import Client
from webdav4.fsspec import WebdavFileSystem
import os

# Add your token/macaroon to the environmental variables, or paste it in manually:
c = Client(
    base_url="https://webdav.grid.surfsara.nl",
    headers={"Authorization": f"bearer {os.environ["DCACHE_MACAROON"]}"}
)

fs = WebdavFileSystem(
    "https:/webdav.grid.surfsara.nl/",
    client=c,
)

path_to_zarr = "zarr/.fr-GAjwU6/zarrdata-main/air_temperature.zarr"
fsmap = fs.get_mapper(path_to_zarr)
ds = xr.open_zarr(fsmap, consolidated=True)

print(ds)
print(ds["air"].isel(time=0).to_numpy())

# How to access dcache/webdav zarr data in xarray

Python requirements are in the `requirements.txt` file.

Add your macaroon to your environmental variables, and modify the `path_to_zarr`
variable in `webdav_zarr_access.py` to point to your zarr store.

Run the python file, and you should see the contents of your zarr store.

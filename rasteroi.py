import numpy
import rasterio
import subprocess

with rasterio.drivers(CPL_DEBUG=True):
# https://gis.stackexchange.com/questions/138914/calculating-ndvi-with-rasterio
    # Read raster bands directly to Numpy arrays.
    #
    dsRed = rasterio.open('downloads/LC81970212013122LGN01/LC81970212013122LGN01_B3.TIF')
    bandRed = dsRed.read_band(1)

    dsNir = rasterio.open('downloads/LC81970212013122LGN01/LC81970212013122LGN01_B5.TIF')
    bandNir = dsNir.read_band(1)

    ndvi = numpy.zeros(dsRed.shape, dtype=rasterio.uint16)

    ndvi_upper = bandNir + bandRed
    ndvi_lower = bandNir - bandRed

    ndvi = ndvi_lower / ndvi_upper

    kwargs = dsRed.meta
    kwargs.update(
        dtype=rasterio.uint16,
        count=1,
        compress='lzw')

    with rasterio.open('example-total.tif', 'w', **kwargs) as dst:
        dst.write_band(1, ndvi.astype(rasterio.uint16))


# Dump out gdalinfo's report card and open the image.
info = subprocess.check_output(['gdalinfo', '-stats', 'example-total.tif'])
print(info)

subprocess.call(['open', 'example-total.tif'])
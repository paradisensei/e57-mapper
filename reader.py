import numpy as np
import pye57  # using this library - https://github.com/davidcaron/pye57
# if pip install pye57 fails on mac os / linux, just install xerces-c lib (f.e. - brew install xerces-c)

# read 3D scan of the site
e57 = pye57.E57("data/CustomerCenter1 1.e57")

# print out some file header info
# the ScanHeader object wraps most of the scan information:
print('----------------------------------------------')
header = e57.get_header(0)
print(header.point_count)
print(header.rotation_matrix)
print(header.translation)
# all the header information can be printed using:
for line in header.pretty_print():
    print(line)
print('----------------------------------------------')

#
# neither of these 2 read scans below work :( at index 0
#
# read scan at index 0
# data = e57.read_scan(0)
# read scan at index 0 with colors and intensity information
# data = e57.read_scan(0, intensity=True, colors=True)

# turned out that there are 2 rows to scan in data
print(e57.scan_count)

# the 'read_scan' method filters points using the 'cartesianInvalidState' field
# if you want to get everything as raw, untransformed data, use:
data = e57.read_scan_raw(0)  # reads 1st row

# print out available data arrays
print(data.keys())

# read all available points data to corresponding arrays
cartesianX = data["cartesianX"]
cartesianY = data["cartesianY"]
cartesianZ = data["cartesianZ"]
intensity = data["intensity"]
colorRed = data["colorRed"]
colorGreen = data["colorGreen"]
colorBlue = data["colorBlue"]

print("number of points = %n".format(len(cartesianX)))

data1 = e57.read_scan_raw(1)  # reads 1st row
print(data1.keys())  # with the same data arrays as the data from 1st row

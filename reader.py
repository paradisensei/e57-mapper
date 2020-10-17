import numpy as np
import pye57  # using this library - https://github.com/davidcaron/pye57
# if pip install pye57 fails on mac os / linux, just install xerces-c lib (f.e. - brew install xerces-c)

# read 3D scan of the site
e57 = pye57.E57("data/CustomerCenter1 1.e57")

# read scan at index 0
data = e57.read_scan(0, ignore_missing_fields=True)

# 'data' is a dictionary with the point types as keys
data = e57.read_scan(0, intensity=True, colors=True, row_column=True)

# the 'read_scan' method filters points using the 'cartesianInvalidState' field
# if you want to get everything as raw, untransformed data, use:
data_raw = e57.read_scan_raw(0)

# the ScanHeader object wraps most of the scan information:
header = e57.get_header(0)
print(header.point_count)
print(header.rotation_matrix)
print(header.translation)

# all the header information can be printed using:
for line in header.pretty_print():
    print(line)

# the scan position can be accessed with:
position_scan_0 = e57.scan_position(0)
import numpy as np
import pye57
import pickle

e57 = pye57.E57("e57_file.e57")

data_raw_0 = e57.read_scan_raw(0)

x_tr = np.array([ data_raw_0["cartesianX"], data_raw_0["cartesianY"], data_raw_0["cartesianZ"] ])
x = x_tr.transpose()

with open("points_raw_0.pkl", "wb") as f:
  pickle.dump(x,f)
  
with open('points_raw_0.pkl','rb') as f:
  x_load = pickle.load(f)
  print(x_load.shape)
  
  

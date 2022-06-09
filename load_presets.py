import numpy as np

with open("presets.npy", 'rb') as f:
    integer_presets = np.load(f, allow_pickle=True)[()]




print(integer_presets[0]["melody"])

print(len(integer_presets[0]["melody"]))
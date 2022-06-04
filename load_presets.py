import numpy as np

with open("presets.npy", 'rb') as f:
    integer_presets = np.load(f, allow_pickle=True)[()]


for key, value in integer_presets.items():
    print(len(value["melody"]))

print(integer_presets[1]["melody"])

print(len(integer_presets[0]["melody"]))
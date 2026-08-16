import numpy as np

sensor1 = np.array([10, 20, 30])
sensor2 = np.array([40, 50, 60])

# Concatenate arrays
combined = np.concatenate((sensor1, sensor2))

print("Combined Sensor Readings:", combined)
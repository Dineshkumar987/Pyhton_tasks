import numpy as np

temperatures = np.array([28, 31, 35, 27, 40, 22])

high_temperature = temperatures[temperatures > 30]

print(high_temperature)
import numpy as np

seed = 23_10_26
rng = np.random.default_rng(seed)

result = rng.permutation(np.arange(1, 12))
print(result)

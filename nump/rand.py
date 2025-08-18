import numpy as np

# seed = same copy of previous run
rng = np.random.default_rng(seed=1)
print(rng.integers(1,7, size=(3,2)))


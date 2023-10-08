import numpy as np
from numpy.random import MT19937
from numpy.random import RandomState, SeedSequence

rs = RandomState(MT19937(SeedSequence(123456789)))

def simulate_ride_distances():
    ride_dists = np.concatenate(
        (
            10 * np.random.random(size=370),
            30 * np.random.random(size=10),     # Long Distances
            10 * np.random.random(size=10),     # Same Distance
            10 * np.random.random(size=10),     # Same Distance
        )
    )

    return ride_dists

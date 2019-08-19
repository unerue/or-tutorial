import numpy as np
from sklearn.metrics.pairwise import euclidean_distances


class GenerateCities:
    """Generate Cities
    
    Generating coordinates and distance matrix randomly.
    
    Parameters
    ----------
    x : x coordinate of a city
    y : y coordinate of a city
    num_cities: number of cities
    random_state : seed
    
    Returns
    -------
    coords : city coordinates 
    matrix : distance numpy matrix
    """
    def __init__(self, x, y, num_cities, random_state=None):
        self.x = x
        self.y = y
        self.num_cities = num_cities
        self.random_state = random_state

    def generate(self):
        np.random.seed(self.random_state)
        x = np.random.randint(self.x, size=self.num_cities)
        y = np.random.randint(self.y, size=self.num_cities)
        coords = np.column_stack((x, y))
              
        return coords, np.int32(euclidean_distances(coords))
import numpy as npimport numpy.random as nprimport unittestfrom gmap_retrieval.street_view import *class TestStreetView(unittest.TestCase):    @classmethod    def setUpClass(cls):        # procedures before tests are started. This code block is executed only once        pass    @classmethod    def tearDownClass(cls):        # procedures after tests are finished. This code block is executed only once        pass        def test_get_lat_lon(self):        def calc_distance(loc1, loc2):            """Calculate distance between two locations."""            lat1, lon1 = float(loc1.split(',')[0]), float(loc1.split(',')[1])            lat2, lon2 = float(loc2.split(',')[0]), float(loc2.split(',')[1])                        R = 6371            phi1 = lat1 * np.pi / 180            phi2 = lat2 * np.pi / 180            delta_phi = (lat2 - lat1) * np.pi / 180            delta_lambda = (lon2 - lon1) * np.pi / 180                        a = (np.sin(delta_phi / 2) ** 2                 + np.cos(phi1) * np.cos(phi2)                 * np.sin(delta_lambda / 2) ** 2)                        c = 2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a))                        d = R * c                        return d                n_locs = 10                lats = npr.uniform(-180, 180, n_locs)        lons = npr.uniform(-180, 180, n_locs)        locs = [str(lats[i]) + "," + str(lons[i]) for i in range(n_locs)]        directions = npr.uniform(0, 2 * np.pi, n_locs)        distances = npr.uniform(0, 40075 / 2, n_locs)                for i in range(n_locs):            new_loc = get_lat_lon(locs[i], distances[i], directions[i])            self.Equal(distances[i], calc_distance(locs[i], new_loc))
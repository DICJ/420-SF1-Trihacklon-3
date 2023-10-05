import unittest
from CalculatriceMatrices import CalculatriceMatrices as calculatrice 

class TransfoMatriceTest(unittest.TestCase):
    carre = [
        [20, 30, 40, 50],
        [21, 22, 23, 24],
        [31, 32, 33, 34],
        [41, 42, 43, 44]
    ]
    
    large = [ 
        [20, 30, 40, 50, 99, -60],
        [21, 22, 23, 24, 800, 1],
        [31, 32, 33, 34, 80, -255]
    ]

    haute = [
        [20, 30],
        [21, 22],
        [31, 32],
        [41, 42],
        [800, 9],
        [90, 89],
        [71, -6]
    ]

    petit_carre = [
        [20, 30],
        [21, 22]
    ]

    mini_carre = [ [ 20 ] ]

    gros_carre = [ 
        [ 20,  30,  40,  50,  500, -50],
        [ 21,  22,  23,  24,  240, -24],
        [ 31,  32,  33,  34,  340, -34],
        [ 41,  42,  43,  44,  440, -44],
        [-31, -32, -33, -35, -340,  35],
        [-41, -42, -43, -45, -440,  45]
    ]

    def test_rotation_90_horaire(self):
        self.assertListEqual([ 
                [41, 31, 21, 20],
                [42, 32, 22, 30],
                [43, 33, 23, 40],
                [44, 34, 24, 50]
            ],
            calculatrice.rotation_90_horaire(self.carre))
    
    def test_rotation_90_Horaire_gros(self):
        self.assertListEqual([
                [-41,  -31,  41,  31,  21, 20],
                [-42,  -32,  42,  32,  22, 30],
                [-43,  -33,  43,  33,  23, 40],
                [-45,  -35,  44,  34,  24, 50],
                [-440, -340, 440, 340, 240,  500],
                [45, 35, -44, -34, -24,  -50]
            ],
            calculatrice.rotation_90_horaire(self.gros_carre))
    
    def test_rotation_90_horaire_petit(self):
        self.assertListEqual([[21, 20], [22, 30]],
            calculatrice.rotation_90_horaire(self.petit_carre))
        self.assertListEqual([[20]],
            calculatrice.rotation_90_horaire(self.mini_carre))
    
    def test_rotation_180(self):
        self.assertListEqual([
                [44, 43, 42, 41],
                [34, 33, 32, 31],
                [24, 23, 22, 21],
                [50, 40, 30, 20]
            ],
            calculatrice.rotation_180(self.carre))
        
    def test_rotation_180_gros(self):
        self.assertListEqual([  
                [45,  -440,  -45,  -43,  -42, -41],
                [35,  -340,  -35,  -33,  -32, -31],
                [-44,  440,  44,  43,  42, 41],
                [-34,  340,  34,  33,  32, 31],
                [-24, 240, 24, 23, 22,  21],
                [-50, 500, 50, 40, 30,  20]
            ],
            calculatrice.rotation_180(self.gros_carre))
    
    def test_rotation_180_petit(self):
        self.assertListEqual([
                [22, 21],
                [30, 20]
            ],
        calculatrice.rotation_180(self.petit_carre))
        self.assertListEqual([[20]],
            calculatrice.rotation_180(self.mini_carre))
       
    def test_rotation_90_antihoraire(self):
        self.assertListEqual([
                [50, 24, 34, 44],
                [40, 23, 33, 43],
                [30, 22, 32, 42],
                [20, 21, 31, 41]
            ],
            calculatrice.rotation_90_antihoraire(self.carre))
    
    def test_rotation_90_antihoraire_gros(self):
        self.assertListEqual([
                [-50,  -24,  -34, -44,  35,  45],
                [500,  240,  340, 440,-340,-440],
                [ 50,   24,   34,  44, -35, -45],
                [ 40,   23,   33,  43, -33, -43],
                [ 30,   22,   32,  42, -32, -42],
                [ 20,   21,   31,  41, -31, -41]
            ],
            calculatrice.rotation_90_antihoraire(self.gros_carre))
    
    def test_rotation_90_antihoraire_petit(self):
        self.assertListEqual([
                [30, 22],
                [20, 21]
            ],
            calculatrice.rotation_90_antihoraire(self.petit_carre))
        self.assertListEqual([[20]],
            calculatrice.rotation_90_antihoraire(self.mini_carre))
    
    
    def test_transpose_carree(self):
        self.assertListEqual([
                [20, 21, 31, 41],
                [30, 22, 32, 42],
                [40, 23, 33, 43],
                [50, 24, 34, 44]
            ],
            calculatrice.transpose(self.carre))
    
    def test_transpose_carree_gros(self):
        self.assertListEqual([
                [20,  21,  31,  41,  -31, -41],
                [30,  22,  32,  42,  -32, -42],
                [40,  23,  33,  43,  -33, -43],
                [50,  24,  34,  44,  -35, -45],
                [500, 240, 340, 440, -340,  -440],
                [-50, -24, -34, -44, 35,  45]
            ],
            calculatrice.transpose(self.gros_carre))


    def test_transpose_carree_petit(self):
        self.assertListEqual([
                [20, 21],
                [30, 22]
            ],
            calculatrice.transpose(self.petit_carre))
        self.assertListEqual([[20]],
            calculatrice.transpose(self.mini_carre))
    
    def test_transpose_rect(self):
        self.assertListEqual([
                [20, 21, 31 ],
                [30, 22, 32 ],
                [40, 23, 33 ],
                [50, 24, 34 ],
                [99, 800, 80],
                [-60, 1, -255]
            ],
            calculatrice.transpose(self.large))
        self.assertListEqual([
                 [20, 21, 31, 41, 800, 90, 71],
                 [30, 22, 32, 42, 9, 89, -6]
            ],
            calculatrice.transpose(self.haute))
    
    def test_est_symetrique(self):
        self.assertFalse(calculatrice.est_symetrique(self.haute))
        self.assertFalse(calculatrice.est_symetrique(self.large))
        self.assertFalse(calculatrice.est_symetrique(self.petit_carre))
        self.assertFalse(calculatrice.est_symetrique(self.carre))
        self.assertFalse(calculatrice.est_symetrique(self.gros_carre))

        self.assertTrue(calculatrice.est_symetrique(self.mini_carre))

    def test_est_symetrique_encore(self):
        self.assertTrue(calculatrice.est_symetrique([
            [20, 21, 31, 41],
            [21, 22, 23, 24],
            [31, 23, 33, 34],
            [41, 24, 34, 44]
        ]))
        self.assertFalse(calculatrice.est_symetrique([
            [20, 21, 31, 41],
            [21, 22, 22, 24],
            [31, 23, 33, 34],
            [41, 24, 34, 44]
        ]))
        self.assertTrue(calculatrice.est_symetrique([
            [1, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 3, 0],
            [0, 0, 0, 4]
        ]))
    
    def test_est_diagonale(self):
        self.assertFalse(calculatrice.est_diagonale(self.haute))
        self.assertFalse(calculatrice.est_diagonale(self.large))
        self.assertFalse(calculatrice.est_diagonale(self.petit_carre))
        self.assertFalse(calculatrice.est_diagonale(self.carre))
        self.assertFalse(calculatrice.est_diagonale(self.gros_carre))

        self.assertTrue(calculatrice.est_diagonale(self.mini_carre))

    
    def test_est_diagonale_encore(self):
        self.assertTrue(calculatrice.est_diagonale([
            [20, 0, 0, 0],
            [0, 22, 0, 0],
            [0, 0, 33, 0],
            [0, 0, 0, 44]
        ]))
        self.assertFalse(calculatrice.est_diagonale([
            [20, 0, 0, 0],
            [0, 22, 22, 0],
            [0, 23, 0, 0],
            [0, 0, 0, 44]
        ]))
        self.assertTrue(calculatrice.est_diagonale([
            [1, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 3, 0],
            [0, 0, 0, 4]
        ]))
        self.assertTrue(calculatrice.est_diagonale([
            [1, 0, 0, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 4]
        ]))
        self.assertFalse(calculatrice.est_diagonale([
            [1, 0, 0, 0],
            [0, 2, 2, 0],
            [0, 2, 3, 0],
            [0, 0, 0, 4]
        ]))
    
    def test_matrices_egales(self):
        self.assertTrue(calculatrice.matrices_egales(self.carre, self.carre))
        self.assertFalse(calculatrice.matrices_egales(self.gros_carre, self.carre))
        self.assertFalse(calculatrice.matrices_egales(self.carre, self.gros_carre))
    
    def test_matricesEgalesCarre(self):
        self.assertTrue(calculatrice.matrices_egales([
                [20, 30, 40, 50],
                [21, 22, 23, 24],
                [31, 32, 33, 34],
                [41, 42, 43, 44]
            ],
            self.carre))
        self.assertFalse(calculatrice.matrices_egales([
                [20, 30, 40, 50],
                [21, 22, 23, 24],
                [31, 32, 33, 34],
                [41, 42, 43, 43]
            ], 
            self.carre))
    
    def test_matrices_egales_rect(self):
        self.assertTrue(calculatrice.matrices_egales([
                [20, 30, 40, 50, 99, -60],
                [21, 22, 23, 24, 800, 1 ],
                [31, 32, 33, 34, 80, -255]
            ], 
            self.large))
        self.assertFalse(calculatrice.matrices_egales([
                [20, 30, 40, 50, 99, -60],
                [21, 22, 23, 24, 800, 1 ],
                [31, 32, 33, 34, 80, -0 ]
            ], 
            self.large))
    
import unittest
from CalculatriceMatrices import CalculatriceMatrices as calculatrice 

class CoordMatriceTest(unittest.TestCase):
    def test_est_carree(self):
        self.assertTrue(calculatrice.est_carree(30 * [30 * [0]]))
        self.assertTrue(calculatrice.est_carree([[0]]))
        self.assertFalse(calculatrice.est_carree(30 * [15 * [0]]))
        self.assertFalse(calculatrice.est_carree(15 * [30 * [0]]))
    
    def test_est_rangee_valide(self):
        self.assertTrue(calculatrice.est_rangee_valide(30 * [30 * [0]], 5))
        self.assertTrue(calculatrice.est_rangee_valide(30 * [15 * [0]], 5))
        self.assertTrue(calculatrice.est_rangee_valide(30 * [3 * [0]], 29))
        self.assertTrue(calculatrice.est_rangee_valide(10 * [10 * [0]], 0))
        self.assertFalse(calculatrice.est_rangee_valide(10 * [30 * [0]], 10))
        self.assertFalse(calculatrice.est_rangee_valide(4 * [30 * [0]], 9))
        self.assertFalse(calculatrice.est_rangee_valide(30 * [30 * [0]], -1))
    
    def test_est_colonne_valide(self):
        self.assertTrue(calculatrice.est_colonne_valide(30 * [30 * [0]], 5))
        self.assertTrue(calculatrice.est_colonne_valide(30 * [15 * [0]], 5))
        self.assertTrue(calculatrice.est_colonne_valide(30 * [3 * [0]], 2))
        self.assertTrue(calculatrice.est_colonne_valide(10 * [10 * [0]], 0))
        self.assertFalse(calculatrice.est_colonne_valide(30 * [3 * [0]], 3))
        self.assertFalse(calculatrice.est_colonne_valide(40 * [30 * [0]], 35))
        self.assertFalse(calculatrice.est_colonne_valide(30 * [30 * [0]], -1))
    
    def test_estDedansTest(self):
        self.assertTrue(calculatrice.est_dedans(30 * [30 * [0]], 5, 5))
        self.assertTrue(calculatrice.est_dedans(30 * [15 * [0]], 21, 12))
        self.assertTrue(calculatrice.est_dedans(30 * [3 * [0]], 29, 2))
        self.assertTrue(calculatrice.est_dedans(10 * [10 * [0]], 0, 0))
        self.assertFalse(calculatrice.est_dedans(30 * [10 * [0]], 30, 1))
        self.assertFalse(calculatrice.est_dedans(30 * [3 * [0]], 1, 4))
        self.assertFalse(calculatrice.est_dedans(40 * [30 * [0]], 35, 35))
        self.assertFalse(calculatrice.est_dedans(40 * [30 * [0]], 40, 15))
        self.assertFalse(calculatrice.est_dedans(3 * [3 * [0]], -1, 2))
        self.assertFalse(calculatrice.est_dedans(3 * [3 * [0]], 1, -1))
        self.assertFalse(calculatrice.est_dedans(3 * [3 * [0]], -1, -1))
    
    def test_nbCellulesTest(self):
        self.assertEqual(30 * 30, calculatrice.nb_cellules(30 * [30 * [0]]))
        self.assertEqual(30 * 15, calculatrice.nb_cellules(30 * [15 * [0]]))
        self.assertEqual(30 * 3, calculatrice.nb_cellules(30 * [3 * [0]]))
        self.assertEqual(10 * 10, calculatrice.nb_cellules(10 * [10 * [0]]))
    
    def test_densiteTest(self):
        self.assertEqual(0, calculatrice.densite(30 * [30 * [0]]))
        self.assertEqual(1, calculatrice.densite([
            [20, 30, 40, 50],
            [21, 22, 23, 24],
            [31, 32, 33, 34],
            [41, 42, 43, 44]
        ]))
        self.assertEqual(12.0 / 16.0, calculatrice.densite([        
            [0, 30, 40, 0],
            [21, 22, 23, 24],
            [0, 32, 0, 34],
            [41, 42, 43, 44]
        ]))
    
    def test_densiteEncore(self):
        self.assertEqual(0, calculatrice.densite(10 * [3 * [0]]))
        self.assertEqual(1, calculatrice.densite([
            [20, 30, 40, 50, 99, -60],
            [21, 22, 23, 24, 800, 1],
            [31, 32, 33, 34, 80, -255]
        ]))
        self.assertEqual(15.0 / 18.0, calculatrice.densite([
            [20, 0, 40, 50, 99, -60],
            [21, 22, 0, 24, 800, 1],
            [31, 32, 33, 0, 80, -255]
        ]))
    
    def test_copierMatricesTest(self):
        carre = [
            [20, 30, 40, 50],
            [21, 22, 23, 24],
            [31, 32, 33, 34],
            [41, 42, 43, 44]
        ]
        
        copie = calculatrice.copier(carre)
        self.assertListEqual(carre, copie)
        self.assertIsNot(copie, carre)
    
    def test_copierMatricesRectTest(self):
        haute = [
            [20, 30],
            [21, 22],
            [31, 32],
            [41, 42],
            [800, 9],
            [90, 89],
            [71, -6]
        ]
        copie = calculatrice.copier(haute)
        self.assertListEqual(haute, copie)
        self.assertIsNot(copie, haute)

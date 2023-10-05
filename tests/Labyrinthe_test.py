import unittest
from CalculatriceMatrices import CalculatriceMatrices as calculatrice 

class LabyrintheTest(unittest.TestCase):
    def test_est_labyrinthe(self):
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0, -2,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        self.assertTrue(calculatrice.labyrinthe(carre, 0, 0))
        self.assertTrue(calculatrice.labyrinthe(carre, 3, 1))
        self.assertFalse(calculatrice.labyrinthe(carre, 1, 3))
    
    def test_est_labyrinthe_encore(self):
        carre = [
            [  0,  0, -2, -2 ],
            [ -2,  0, -2,  0 ],
            [  0, -2, -2, -2 ],
            [ -2,  0,  0, -1 ]
        ]
        self.assertTrue(calculatrice.labyrinthe(carre, 3, 1))
        self.assertFalse(calculatrice.labyrinthe(carre, 0, 0))
    
    def test_est_labyrinthe_peu_murs(self):
        carre = [
            [  0,  0,  0, -1 ],
            [  0,  0,  0,  0 ],
            [ -2, -2,  0,  0 ],
            [  0, -2,  0,  0 ]
        ]
        self.assertTrue(calculatrice.labyrinthe(carre, 0, 0))
        self.assertTrue(calculatrice.labyrinthe(carre, 3, 3))
        self.assertFalse(calculatrice.labyrinthe(carre, 3, 0))
    
    def test_est_labyrinthe_large(self):
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2,  0 ],
            [ -2, -2, -2, -2, -2,  0 ],
        ]
        self.assertTrue(calculatrice.labyrinthe(large, 0, 0))
        self.assertTrue(calculatrice.labyrinthe(large, 2, 0))
        self.assertFalse(calculatrice.labyrinthe(large, 2, 5))
    
    def test_labyrinthe_petit(self):
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0,  0,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        self.assertTrue(calculatrice.labyrinthe(carre, 0, 0))
        self.assertFalse (calculatrice.labyrinthe(carre, 0, 3))
    
    def test_labyrinthe_large(self):
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2, -2 ],
            [ -2, -2, -2, -2, -2, -2 ],
        ]
        self.assertTrue(calculatrice.labyrinthe(large, 0, 0))
        self.assertFalse(calculatrice.labyrinthe(large, 3, 5))
    
    def test_labyrinthe_large_chemin(self):
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2, -2 ],
            [ -2, -2, -2, -2, -2, -2 ],
        ]
        calculatrice.labyrinthe(large, 0, 0, 1)
        self.assertListEqual( [
                [  1,  2, -2, -2,  9, -1 ],
                [ -2,  3, -2,  7,  8, -2 ],
                [  0,  4,  5,  6, -2, -2 ],
                [ -2, -2, -2, -2, -2, -2 ],
            ],
            large)
    
    def test_labyrinthe_petit_chemin(self):    
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0,  0,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        calculatrice.labyrinthe(carre, 0, 0, 1)
        self.assertListEqual([
                [  1, 2, -2, -2 ],
                [ -2, 3,  0,  0 ],
                [  0, 4, -2, -2 ],
                [ -2, 5,  6, -1 ]
            ],
            carre)

    def test_est_labyrinthe_chemin(self):
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0, -2,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        solution = [
            [  1, 2, -2, -2 ],
            [ -2, 3, -2,  0 ],
            [  0, 4, -2, -2 ],
            [ -2, 5,  6, -1 ]
        ]
        calculatrice.labyrinthe(carre, 0, 0, 1)
        self.assertListEqual(solution, carre)
    
    def test_est_labyrinthe_encore_chemin(self):
        carre = [
            [  0,  0, -2, -2 ],
            [ -2,  0, -2,  0 ],
            [  0, -2, -2, -2 ],
            [ -2,  0,  0, -1 ]
        ]
        solution = [
            [  0,  0, -2, -2 ],
            [ -2,  0, -2,  0 ],
            [  0, -2, -2, -2 ],
            [ -2,  1,  2, -1 ]
        ]
        calculatrice.labyrinthe(carre, 3, 1, 1)
        self.assertListEqual(solution, carre)
    
    def test_est_labyrinthe_large_chemin(self):
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2,  0 ],
            [ -2, -2, -2, -2, -2,  0 ],
        ]
        solution = [
            [  1,  2, -2, -2,  9, -1 ],
            [ -2,  3, -2,  7,  8, -2 ],
            [  0,  4,  5,  6, -2,  0 ],
            [ -2, -2, -2, -2, -2,  0 ],
        ]

        calculatrice.labyrinthe(large, 0, 0, 1)
        self.assertListEqual(solution, large)
    

    # POUR DONNER PLUS D'ÉTOILES
    def test_est_labyrinthe(self):
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0, -2,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        self.assertTrue(calculatrice.labyrinthe(carre, 0, 0))
        self.assertTrue(calculatrice.labyrinthe(carre, 3, 1))
        self.assertFalse(calculatrice.labyrinthe(carre, 1, 3))
    
    def test_est_labyrinthe_encore(self):
        carre = [
            [  0,  0, -2, -2 ],
            [ -2,  0, -2,  0 ],
            [  0, -2, -2, -2 ],
            [ -2,  0,  0, -1 ]
        ]
        self.assertTrue(calculatrice.labyrinthe(carre, 3, 1))
        self.assertFalse(calculatrice.labyrinthe(carre, 0, 0))
    

    def test_est_labyrinthe_peu_murs(self):    
        carre = [
            [  0,  0,  0, -1 ],
            [  0,  0,  0,  0 ],
            [ -2, -2,  0,  0 ],
            [  0, -2,  0,  0 ]
        ]
        self.assertTrue(calculatrice.labyrinthe(carre, 0, 0))
        self.assertTrue(calculatrice.labyrinthe(carre, 3, 3))
        self.assertFalse(calculatrice.labyrinthe(carre, 3, 0))
    
    def test_est_labyrinthe_large(self):
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2,  0 ],
            [ -2, -2, -2, -2, -2,  0 ],
        ]
        self.assertTrue(calculatrice.labyrinthe(large, 0, 0))
        self.assertTrue(calculatrice.labyrinthe(large, 2, 0))
        self.assertFalse(calculatrice.labyrinthe(large, 2, 5))
    

    def test_labyrinthe_petit(self):
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0,  0,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        self.assertTrue(calculatrice.labyrinthe(carre, 0, 0))
        self.assertFalse(calculatrice.labyrinthe(carre, 0, 3))
    
    def test_labyrinthe_large(self):
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2, -2 ],
            [ -2, -2, -2, -2, -2, -2 ],
        ]
        self.assertTrue(calculatrice.labyrinthe(large, 0, 0))
        self.assertFalse(calculatrice.labyrinthe(large, 3, 5))
    
    def test_labyrinthe_large_chemin(self):
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2, -2 ],
            [ -2, -2, -2, -2, -2, -2 ],
        ]
        calculatrice.labyrinthe(large, 0, 0, 1)
        self.assertListEqual([
                [  1,  2, -2, -2,  9, -1 ],
                [ -2,  3, -2,  7,  8, -2 ],
                [  0,  4,  5,  6, -2, -2 ],
                [ -2, -2, -2, -2, -2, -2 ],
            ],
            large)
    
    def test_labyrinthe_petit_chemin(self):
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0,  0,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        calculatrice.labyrinthe(carre, 0, 0, 1)
        self.assertListEqual([
                [  1, 2, -2, -2 ],
                [ -2, 3,  0,  0 ],
                [  0, 4, -2, -2 ],
                [ -2, 5,  6, -1 ]
            ],
            carre)

    def test_est_labyrinthe_chemin(self):
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0, -2,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        solution = [
            [  1, 2, -2, -2 ],
            [ -2, 3, -2,  0 ],
            [  0, 4, -2, -2 ],
            [ -2, 5,  6, -1 ]
        ]
        calculatrice.labyrinthe(carre, 0, 0, 1)
        self.assertListEqual(solution, carre)
    
    def test_est_labyrinthe_encore_chemin(self):
        carre = [
            [  0,  0, -2, -2 ],
            [ -2,  0, -2,  0 ],
            [  0, -2, -2, -2 ],
            [ -2,  0,  0, -1 ]
        ]

        solution = [
            [  0,  0, -2, -2 ],
            [ -2,  0, -2,  0 ],
            [  0, -2, -2, -2 ],
            [ -2,  1,  2, -1 ]
        ]
        calculatrice.labyrinthe(carre, 3, 1, 1)
        self.assertListEqual(solution, carre)
    
    def test_est_labyrinthe_large_chemin(self):
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2,  0 ],
            [ -2, -2, -2, -2, -2,  0 ],
        ]
        solution = [
            [  1,  2, -2, -2,  9, -1 ],
            [ -2,  3, -2,  7,  8, -2 ],
            [  0,  4,  5,  6, -2,  0 ],
            [ -2, -2, -2, -2, -2,  0 ],
        ]
        calculatrice.labyrinthe(large, 0, 0, 1)
        self.assertListEqual(solution, large)
    
    def test_est_labyrinthe(self):    
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0, -2,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        self.assertTrue(calculatrice.labyrinthe(carre, 0, 0))
        self.assertTrue(calculatrice.labyrinthe(carre, 3, 1))
        self.assertFalse(calculatrice.labyrinthe(carre, 1, 3))
    
    def test_est_labyrinthe_encore(self):
        carre =  [
            [  0,  0, -2, -2 ],
            [ -2,  0, -2,  0 ],
            [  0, -2, -2, -2 ],
            [ -2,  0,  0, -1 ]
            ]
        self.assertTrue(calculatrice.labyrinthe(carre, 3, 1))
        self.assertFalse(calculatrice.labyrinthe(carre, 0, 0))
    
    def test_est_labyrinthe_peu_murs(self):    
        carre = [
            [  0,  0,  0, -1 ],
            [  0,  0,  0,  0 ],
            [ -2, -2,  0,  0 ],
            [  0, -2,  0,  0 ]
            ]
        self.assertTrue(calculatrice.labyrinthe(carre, 0, 0))
        self.assertTrue(calculatrice.labyrinthe(carre, 3, 3))
        self.assertFalse(calculatrice.labyrinthe(carre, 3, 0))
    
    def test_est_labyrinthe_large(self):    
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2,  0 ],
            [ -2, -2, -2, -2, -2,  0 ],
        ]
        self.assertTrue(calculatrice.labyrinthe(large, 0, 0))
        self.assertTrue(calculatrice.labyrinthe(large, 2, 0))
        self.assertFalse(calculatrice.labyrinthe(large, 2, 5))
    

    def test_labyrinthe_petit(self):    
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0,  0,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        self.assertTrue(calculatrice.labyrinthe(carre, 0, 0))
        self.assertFalse(calculatrice.labyrinthe(carre, 0, 3))
    

    def test_labyrinthe_large(self):
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2, -2 ],
            [ -2, -2, -2, -2, -2, -2 ],
        ]
        self.assertTrue(calculatrice.labyrinthe(large, 0, 0))
        self.assertFalse(calculatrice.labyrinthe(large, 3, 5))

    def test_labyrinthe_large_chemin(self):
        large = [
            [  0,  0, -2, -2,  0, -1 ],
            [ -2,  0, -2,  0,  0, -2 ],
            [  0,  0,  0,  0, -2, -2 ],
            [ -2, -2, -2, -2, -2, -2 ],
        ]
        calculatrice.chemin_labyrinthe(large, 0, 0, 1)
        self.assertListEqual([
                [  1,  2, -2, -2,  9, -1 ],
                [ -2,  3, -2,  7,  8, -2 ],
                [  0,  4,  5,  6, -2, -2 ],
                [ -2, -2, -2, -2, -2, -2 ],
            ],
            large)
    
    def test_labyrinthe_petit_chemin(self):    
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0,  0,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        calculatrice.chemin_labyrinthe(carre, 0, 0, 1)
        self.assertListEqual( [
                [  1, 2, -2, -2 ],
                [ -2, 3,  0,  0 ],
                [  0, 4, -2, -2 ],
                [ -2, 5,  6, -1 ]
            ],
            carre)
    
    def test_est_labyrinthe_chemin(self):
        carre = [
            [  0, 0, -2, -2 ],
            [ -2, 0, -2,  0 ],
            [  0, 0, -2, -2 ],
            [ -2, 0,  0, -1 ]
        ]
        solution = [
            [  1, 2, -2, -2 ],
            [ -2, 3, -2,  0 ],
            [  0, 4, -2, -2 ],
            [ -2, 5,  6, -1 ]
        ]
        calculatrice.chemin_labyrinthe(carre, 0, 0, 1)
        self.assertListEqual(solution, carre)
    
    def test_est_labyrinthe_encore_chemin(self):
    
        carre = [
            [  0,  0, -2, -2 ],
            [ -2,  0, -2,  0 ],
            [  0, -2, -2, -2 ],
            [ -2,  0,  0, -1 ]
        ]
        solution = [
            [  0,  0, -2, -2 ],
            [ -2,  0, -2,  0 ],
            [  0, -2, -2, -2 ],
            [ -2,  1,  2, -1 ]
        ]
        calculatrice.chemin_labyrinthe(carre, 3, 1, 1)
        self.assertListEqual(solution, carre)

    def test_est_labyrinthe_large_chemin(self):
        large = [
                [  0,  0, -2, -2,  0, -1 ],
                [ -2,  0, -2,  0,  0, -2 ],
                [  0,  0,  0,  0, -2,  0 ],
                [ -2, -2, -2, -2, -2,  0 ],
        ]
        solution = [
                [  1,  2, -2, -2,  9, -1 ],
                [ -2,  3, -2,  7,  8, -2 ],
                [  0,  4,  5,  6, -2,  0 ],
                [ -2, -2, -2, -2, -2,  0 ],
        ]
        calculatrice.chemin_labyrinthe(large, 0, 0, 1)
        self.assertListEqual(solution, large)

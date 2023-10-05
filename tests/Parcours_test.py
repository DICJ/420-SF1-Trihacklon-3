import unittest
from CalculatriceMatrices import CalculatriceMatrices as calculatrice 

class ParcoursMatriceTest(unittest.TestCase):
    carre = [
        [20, 30, 40, 50],
        [21, 22, 23, 24],
        [31, 32, 33, 34],
        [41, 42, 43, 44]
    ]

    large =  [
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

    petitCarre = [
        [20, 30],
        [21, 22]
    ]

    miniCarre = [ 
        [ 20 ] 
    ]

    grosCarre = [
        [ 20,  30,  40,  50,  500, -50],
        [ 21,  22,  23,  24,  240, -24],
        [ 31,  32,  33,  34,  340, -34],
        [ 41,  42,  43,  44,  440, -44],
        [-31, -32, -33, -35, -340,  35],
        [-41, -42, -43, -45, -440,  45],
    ]
    
    def test_zigzag_carre_moyen(self):
        self.assertListEqual(
                [ 20, 30, 40, 50, 24, 23, 22, 21, 31, 32, 33, 34, 44, 43, 42, 41 ],
            calculatrice.zigzag_horizontal(self.carre))

    def test_zigzag_carre_gros(self):
        self.assertListEqual(
            [ 20,  30,  40,  50,  500, -50,
                -24, 240, 24, 23, 22, 21,
                31,  32,  33,  34,  340, -34,
                -44, 440, 44, 43, 42, 41,
                -31, -32, -33, -35, -340,  35,
                45, -440, -45, -43, -42, -41 ],
            calculatrice.zigzag_horizontal(self.grosCarre))

    def test_zigzag_rect_haut(self):
        self.assertListEqual(
            [ 20, 30, 22, 21, 31, 32, 42, 41, 800, 9, 89, 90, 71, -6 ],
            calculatrice.zigzag_horizontal(self.haute))

    def test_zigzag_rect_large(self):
        self.assertListEqual(
            [ 20, 30, 40, 50, 99, -60, 1, 800, 24, 23, 22, 21, 31, 32, 33, 34, 80, -255 ],
            calculatrice.zigzag_horizontal(self.large))
        
    def test_spirale_carre_moyen(self):
        self.assertListEqual(
            [ 20, 30, 40, 50, 24, 34, 44, 43, 42, 41, 31, 21, 22, 23, 33, 32 ],
            calculatrice.spirale(self.carre))
    
    def test_spirale_carre_petit(self):
        self.assertListEqual(
            [ 20, 30, 22, 21 ],
            calculatrice.spirale(self.petitCarre))
        
    def test_spirale_carre_mini(self):
        self.assertListEqual(
            [ 20 ],
            calculatrice.spirale(self.miniCarre))

    def test_spirale_carre_vide(self):
        self.assertListEqual(
            [ 1, 2, 3 ],
            calculatrice.spirale([ [ 1, 2, 3 ] ]))

    def test_spirale_carre_gros(self):
        self.assertListEqual(
            [
                20, 30, 40, 50, 500, -50,
                -24, -34, -44, 35, 45,
                -440, -45, -43, -42, -41,
                -31, 41, 31, 21,
                22, 23, 24, 240, 340, 440, -340, -35, -33, -32, 42, 32,
                33, 34, 44, 43
            ],
            calculatrice.spirale(self.grosCarre))
        
    def test_spirale_rect_large(self):
        self.assertListEqual(
            [ 20, 30, 40, 50, 99, -60, 1, -255, 80, 34, 33, 32, 31, 21, 22, 23, 24, 800 ],
            calculatrice.spirale(self.large))

    def test_spirale_rect_haut(self):
        self.assertListEqual(
            [ 20, 30, 22, 32, 42, 9, 89, -6, 71, 90, 800, 41, 31, 21 ],
            calculatrice.spirale(self.haute))

    def test_diagonales_descendantes_carre_moyen(self):
        self.assertListEqual(
            [ 20, 30, 21, 40, 22, 31, 50, 23, 32, 41, 24, 33, 42, 34, 43, 44 ],
            calculatrice.diagonales_descendantes(self.carre))
    
    def test_diagonales_descendantes_carre_petit(self):
        self.assertListEqual(
            [ 20, 30, 21, 22 ],
            calculatrice.diagonales_descendantes(self.petitCarre))
    
    def test_diagonales_descendantes_carre_gros(self):
        self.assertListEqual(
            [
                20,
                30, 21,
                40, 22, 31,
                50, 23, 32, 41,
                500, 24, 33, 42, -31,
                -50, 240, 34, 43, -32, -41,
                -24, 340, 44, -33, -42,
                -34, 440, -35, -43,
                -44, -340, -45,
                35, -440,
                45],
        calculatrice.diagonales_descendantes(self.grosCarre))

    def test_diagonales_descendantes_rect_large(self):
        self.assertListEqual(
            [ 20, 30, 21, 40, 22, 31, 50, 23, 32, 99, 24, 33, -60, 800, 34, 1, 80, -255 ],
            calculatrice.diagonales_descendantes(self.large))
        self.assertListEqual(
            [ 20, 30, 21, 22, 31, 32, 41, 42, 800, 9, 90, 89, 71, -6 ],
            calculatrice.diagonales_descendantes(self.haute))
    
    def test_diagonales_montantes_carre(self):
        self.assertListEqual(
            [ 20, 21, 30, 31, 22, 40, 41, 32, 23, 50, 42, 33, 24, 43, 34, 44 ],
            calculatrice.diagonales_montantes(self.carre))
    
    def test_diagonales_montantes_carre_petit(self):
        self.assertListEqual(
            [ 20, 21, 30, 22 ],
            calculatrice.diagonales_montantes(self.petitCarre))
    
    def test_diagonales_montantes_carre_gros(self):
        self.assertListEqual(
            [
                20,
                21, 30,
                31, 22, 40,
                41, 32, 23, 50,
                -31, 42, 33, 24, 500,
                -41, -32, 43, 34, 240, -50,
                -42, -33, 44, 340, -24,
                -43, -35, 440, -34,
                -45, -340, -44,
                -440, 35,
                45],
            calculatrice.diagonales_montantes(self.grosCarre))
    
    def test_diagonales_montantes_rect_large(self):
        self.assertListEqual(
            [ 20, 21, 30, 31, 22, 40, 32, 23, 50, 33, 24, 99, 34, 800, -60, 80, 1, -255 ],
            calculatrice.diagonales_montantes(self.large))
        self.assertListEqual(
            [ 20, 21, 30, 31, 22, 41, 32, 800, 42, 90, 9, 71, 89, -6 ],
            calculatrice.diagonales_montantes(self.haute))
    
    def test_colombe_carre(self):
        self.assertListEqual(
            [ 20, 30, 21, 31, 22, 40, 50, 23, 32, 41, 42, 33, 24, 34, 43, 44 ],
            calculatrice.queue_de_colombe(self.carre))
    
    def test_colombe_carre_petit(self):
        self.assertListEqual(
            [ 20, 30, 21, 22 ],
            calculatrice.queue_de_colombe(self.petitCarre))
    
    def test_colombe_carre_mini(self):
        self.assertListEqual(
            [ 20 ],
            calculatrice.queue_de_colombe(self.miniCarre))

    def test_colombe_carre_vide(self):
        self.assertListEqual(
            [ 1, 2, 3 ],
            calculatrice.queue_de_colombe([[ 1, 2, 3 ]]))
    
    def test_colombe_carre_gros(self):
        self.assertListEqual(
            [
                20,
                30, 21,
                31, 22, 40,
                50, 23, 32, 41,
                -31, 42, 33, 24, 500,
                -50, 240, 34, 43,  -32, -41,
                -42, -33, 44, 340, -24,
                -34, 440, -35, -43,
                -45, -340, -44,
                35,-440,
                45],
            calculatrice.queue_de_colombe(self.grosCarre))
    
    def test_colombe_rect_large(self):
        self.assertListEqual(
            [ 20, 30, 21, 31, 22, 40, 50, 23, 32, 33, 24, 99, -60, 800, 34, 80, 1, -255 ],
            calculatrice.queue_de_colombe(self.large))
    
    def test_colombe_rect_haut(self):
        self.assertListEqual(
            [ 20, 30, 21, 31, 22, 32, 41, 800, 42, 9, 90, 71, 89, -6 ],
            calculatrice.queue_de_colombe(self.haute))
    
from CalculatriceMatrices import CalculatriceMatrices
import re

class Program :
    QUIT = 'Q'

    def mot_important(s:str):
        """
        Imprime une chaîne à la console en Cyan, puis rétablit à couleur initiale
            
            Parameters:
                s(str): La chaîne à imprimer en couleur
        """ 
        print('\033[36m' + s + '\033[0m', end = '')    

    def imprimer_matrice(m: list[list[int]]):
        """
        Imprime une matrice à la console avec une jolie bordure
        
            Parameters:
                m(list[list[int]]): La matrice à imprimer
        """ 
        cellule_plus_large = 0
        for l in m:
            for c in l:
                if len(str(c)) > cellule_plus_large:
                    cellule_plus_large = len(str(c))
        
        cellule_plus_large += 1
        largeur = cellule_plus_large * len(m[0]) + 1
        Program.mot_important('╔')
        for i in range(largeur):
             Program.mot_important('═')
        Program.mot_important('╗')
        print()
        for i in range(len(m)):        
            Program.mot_important('║')
            for j in range(len(m[0])):
                print(' ' * (cellule_plus_large - len(str(m[i][j]))) + str(m[i][j]), end = '')
            Program.mot_important(' ║')
            print()
        
        Program.mot_important('╚')
        for i in range(largeur):
            Program.mot_important('═')
        Program.mot_important('╝')
        print()
    

    def Imprimer_labyrhinthe(m: list[list[int]]):
        """
        Imprime un labyrinthe à la console avec une jolie bordure.
            
            Parameters:
                m(list[list[int]]): Le labyrinthe à imprimer
        """ 
        largeur = 3 * len(m[0])
        Program.mot_important('╔')
        for i in range(largeur) :
            Program.mot_important('═')
        Program.mot_important('╗')
        print()
        for i in range(len(m)) :   
            Program.mot_important('║')
            for j in range(len(m[0])):
                if (m[i][j] <= -2):
                    print('███', end = '')
                elif (m[i][j] == -1):
                    print(' $ ', end = '')
                elif (m[i][j] == 0):
                    print('   ', end = '')
                else:
                    print(' · ', end = '')
            Program.mot_important('║')
            print()
        
        Program.mot_important('╚')
        for i in range(largeur):
            Program.mot_important('═')
        Program.mot_important('╝')
        print()
    
    def imprimerTableau(t: list[int]):
        """
        Imprime un tableau à la console, avec jolie bordure
        
            Parameters:
                t(list[int]): Le tableau à imprimer
        """ 
        largeur = 0
        for c in t:
            largeur += len(str(c)) + 1
        Program.mot_important('╔')
        for _ in range(largeur): 
            Program.mot_important('═')
        Program.mot_important('╗')
        print()

        Program.mot_important('║')
        for c in t:
            print(str(c) + ' ', end = '')
        Program.mot_important('║')
        print()

        Program.mot_important('╚')
        for i in range(largeur): 
            Program.mot_important('═')
        Program.mot_important('╝')
        print()

    def decortiquer(entree: str) -> list[list[int]]:
        """
        Bâtit ne matrice d'entier à partir d'une string dans laquelle les lignes sont séparées par des  
        
            Parameters:
                entree(str): Une chaîne de caractères
            
            Returns:
                La matrice décrite par la chaîne. Nul si la chaîne ne représente pas une matrice d'entiers
        """ 
        if not re.match(r'^(-?\d|\s|X)+$', entree):
            return None
        lignes = list(filter(None, entree.split('X')))#, StringSplitOptions.RemoveEmptyEntries)

        colonnes = list(filter(None, lignes[0].split(' '))) if 'X' in entree else [lignes]
        nb_colonnes = len(colonnes)
        nb_lignes = len(lignes)
        m = [[0 for _ in range(nb_colonnes)] for _ in range(nb_lignes)]
        for i in range(nb_lignes):
            colonnes = lignes[i].split(' ')
            if (len(colonnes) != nb_colonnes):
                return None
            for j in range(nb_colonnes):
                m[i][j] = int(colonnes[j])
        return m
    

    def lireMatrice() -> list[list[int]]:
        """
        Lit une entrée multiligne de l'usager puis bâtit une matrice d'entiers avec.
        Si l'entrée ne représente pas une matrice, la matrice retournée est nulle.
        
            Returns:
                Une matrice contenant l'entrée de l'usager. Nul si l'entrée ne représente pas une matrice.
        """ 
        entree = ''
        next_line = input().strip()
        while next_line != '':
            entree += next_line + 'X'
            next_line = input().strip()
        return Program.decortiquer(entree)
    
    
    def imprimerCaracteristiquesMatrices(m: list[list[int]]):
        """
        Affiche des caractéristiques d'une matrice
        """ 
        Program.imprimer_matrice(m)
        print()

        print('\nDiagonale descendante')
        Program.imprimerTableau(CalculatriceMatrices.diagonales_descendantes(m))
        print('\nDiagonale montante')
        Program.imprimerTableau(CalculatriceMatrices.diagonales_montantes(m))
        print('\nQueue de colombe')
        Program.imprimerTableau(CalculatriceMatrices.queue_de_colombe(m))
        print('\nZigzag horizontal')
        Program.imprimerTableau(CalculatriceMatrices.zigzag_horizontal(m))
        print('\nSpirale')
        Program.imprimerTableau(CalculatriceMatrices.spirale(m))

        if CalculatriceMatrices.est_carree(m):    
            print('\nElle est carrée')
            print('Sa rotation de 90 degrés dans le sens des aiguilles d\'une montre')
            Program.imprimer_matrice(CalculatriceMatrices.rotation_90_horaire(m))
            print('\nSa rotation de 180 degrés')
            Program.imprimer_matrice(CalculatriceMatrices.rotation_180(m))
            print('\nSa rotation de 90 degrés dans le sens contraire des aiguilles d\'une montre')
            Program.imprimer_matrice(CalculatriceMatrices.rotation_90_antihoraire(m))
        
        if CalculatriceMatrices.est_symetrique(m):
            print('\nElle est symétrique')

        print(f'\nSa densité est de {round(CalculatriceMatrices.densite(m) * 100)}%.')
        print('\nSa transpose')
        Program.imprimer_matrice(CalculatriceMatrices.transpose(m))


    def main():
        """
        Affiche des caractéristiques de matrices entrées par l'utilisateur
        """ 
        while True:
            print('Entrez une matrice ligne par ligne')
            print('Séparez les cases par des espaces. Pour terminer, entrez une ligne vide.')
            matrice =  Program.lireMatrice()
            if matrice is not None:
                 Program.imprimerCaracteristiquesMatrices(matrice)
            else:
                print('Ceci n\'est pas une matrice d\'entier valide.')

if __name__ == '__main__':
    Program.main()
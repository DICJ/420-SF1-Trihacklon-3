class CalculatriceMatrices:
    """
    Classe contenant diverses fonctions utiles sur les matrices, représentées par des listes de listes.
    """
        
    def zigzag_horizontal(m: list[list[int]]) -> list[int]:
        """
            4★ Parcourt la matrice de gauche à droite, puis de droite à gauche (en zig zag descendant)
                1 2 3
                6 5 4
                7 8 9
            
                Parameters:
                    m(list[list[int]]): Une matrice d'entiers quelconque
                
                Returns:
                    Un tableau contenant les cases de la matrices, en zig zag descendant, à partir du coin supérieur gauche
        """
        return []
            
    def spirale(m: list[list[int]]) -> list[int]:
        """
        7★ Parcourt la matrice en spirale
            1 2 3
            8 9 4
            7 6 5
        
            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque
            
            Returns:
                Un tableau contenant les cases de la matrices en spirale
        """
        return []
    
    def diagonales_descendantes(m: list[list[int]]) -> list[int]:
        """
        4★ Parcourt la matrice dans l'ordre des diagonales descendantes
            1 2 4
            3 5 7
            6 8 9
            
            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque
            
            Returns:
                Un tableau contenant les cases de la matrices, dans l'ordre des diagonales descendantes
        """
        return []
    
    def diagonales_montantes(m: list[list[int]]) -> list[int]:
        """
        4★ Parcourt la matrice dans l'ordre des diagonales montantes
            1 3 6
            2 5 8
            4 7 9
        
            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque
            
            Returns:
                Un tableau contenant les cases de la matrices, dans l'ordre des diagonales montantes
        """
        return []
        
    def queue_de_colombe(m: list[list[int]]) -> list[int]:
        """
        7★ Parcourt la matrice dans l'ordre de la queue de colombe (diagonale descendantes et montante en alternance)
            1 2 6
            3 5 7
            4 8 9
        
            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque
            
            Returns:
                Un tableau contenant les cases de la matrices, dans l'ordre de la queue de colombe
        """
        return []

    def est_rangee_valide(m: list[list[int]], rangee:int) -> bool:
        """
        ★ Détermine si la rangée se situe dans la matrice
        
            Examples:
                La rangée 1 existe dans une matrice ayant 2 rangées
                La rangée 36 n'existe pas dans une matrice ayant 20 rangées
                La rangée 10 n'existe pas dans une matrice ayant 10 rangées
                
            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque
                rangee(int): L'indice d'une rangée
                
            Returns:
                Vrai si la rangée est dans la matrice, faux sinon
        """
        return False
    

    def est_colonne_valide(m: list[list[int]], colonne:int) -> bool:
        """
        ★ Détermine si la colonne se situe dans la matrice
        
            Examples: 
                La colonne 1 existe dans une matrice ayant 2 colonnes
                La colonne 36 n'existe pas dans une matrice ayant 20 colonnes
                La colonne 10 n'existe pas dans une matrice ayant 10 colonnes

            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque
                colonne(int): L'indice d'une colonne

            Returns:
                Vrai si la colonne est dans la matrice, faux sinon
        """
        return False
    
    def est_carree(m: list[list[int]]) -> bool:
        """
        ★ Vérifie si la matrice donnée est carrée.

            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque

            Returns:
                bool: Vrai si la matrice est carrée, faux sinon.
        """
        return False
    

    def est_dedans(m: list[list[int]], rangee:int, colonne:int) -> bool:
        """
        ★ Détermine si la rangée et la colonne se situent dans la matrice
        
            Examples:
                La cellule (1,1) existe dans une matrice 2 par 2
                La cellule (0,36) n'existe pas dans une matrice 100 par 10
                La cellule (10,10) n'existe pas dans une matrice 10 par 10

            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque
                rangee(int): L'indice d'une rangee
                colonne(int): L'indice d'une colonne

            Returns:
                Vrai si la coordonnée est dans la matrice, faux sinon
        """
        return False
    

    def nb_cellules(m: list[list[int]]) -> int:
        """
        ★ Trouve le nombre de cellules dans un matrice 

            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque

            Returns:
                Le nombre de cases dans la matrice
        """
        return -1

    def densite(m: list[list[int]]) -> float:    
        """
        ★★ Calcule la densité d'une matrice. La densité d'une matrice est sa proportion d'éléments non-nuls.
        Pour la calculer : Nb de cases non nulles / Nb de cases totales.
        Une matrice vide a une densité de 0.
        
            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque

            Returns:
                La densité
        """
        return 0
    


    def matrices_egales(m: list[list[int]], n:list[list[int]]) -> bool:
        """
        ★★★ Déterminent si deux matrices sont égales. Deux matrices sont égales si elles
        ont les mêmes dimensions et que chaque cellule est pareille.
        
            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque
                n(list[list[int]]): Une deuxième matrice quelconque

            Returns:
                Vrai si m est égale à n, faux sino
        """
        return False

    def est_symetrique(m: list[list[int]]) -> bool :
        """
        ★★ Détermine si une matrice est symétrique. Une matrice est symétrique si elle est carrée et
        que chaque cellule est identique à son opposé par rapport à la diagonale principales.
        Une matrice est symétrique si elle est égale à sa transposée.
        
            Example:
                1 4 3 2
                4 5 8 7
                3 8 7 9
                2 7 9 1 est symétrique
                
            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque

            Returns:
                Vrai si m est symétrique, faux sinon
        """
        return False

    def transpose(m: list[list[int]]) -> list[list[int]]:
        """
        4★ Bâtit la transposée d'une matrice. La transposée d'une matrice est une matrice dans laquelle les 
        rangées de la première deviennent les colonnes de la deuxième. Fonctionne autant sur des1 2 3 matrices
        carrées que rectangulaires

            Examples: 
                1 2 3       1 4 7 
                4 5 6  -->  2 5 8
                7 8 9       3 6 9

            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque

            Returns:
                Sa transposée
        """
        return [[]]
    

    def rotation_90_horaire(m: list[list[int]]) -> list[list[int]]:
        """
        ★★★ Bâtit une matrice identique à la première, mais sur laquelle on a appliqué une rotation de 90 degrés
        dans le sens des aiguilles d'une montre. Ne fonctionne que sur des matrices carrées.
        
            Example:
                1 2 3       7 4 1
                4 5 6  -->  8 5 2
                7 8 9       9 6 3
            
            Parameters:
                m(list[list[int]]): Une matrice carrée

            Returns:
                Sa rotation de 90 degrés dans le sens horaire
        """
        return [[]]

    def rotation_90_antihoraire(m: list[list[int]]) -> list[list[int]]:
        """
        ★★★ Bâtit une matrice identique à la première, mais sur laquelle on a appliqué une rotation de 90 degrés
        dans le sens contraire des aiguilles d'une montre. Ne fonctionne que sur des matrices carrées.
        
            Examples:
                1 2 3       3 6 9
                4 5 6  -->  2 5 8
                7 8 9       1 4 7

            Parameters:
                m(list[list[int]]): Une matrice carrée

            Returns:
            Sa rotation de 90 degrés dans le sens anti-horaire
        """
        return [[]]
    
    def rotation_180(m: list[list[int]]) -> list[list[int]]:
        """
        ★★★ Bâtit une matrice identique à la première, mais sur laquelle on a appliqué une rotation de 180 degrés
        Ne fonctionne que sur des matrices carrées.
        
            Examples:
            1 2 3       9 8 7
            4 5 6  -->  6 5 4
            7 8 9       3 2 1
            
            Parameters:
                m(list[list[int]]): Une matrice carrée

            Returns:
                Sa rotation de 90 degrés dans le sens horaire
        """
        return [[]]

    def est_diagonale(m: list[list[int]]) -> bool :
        """
        ★★ Détermine si une matrice est diagonale. Une matrice diagonale est une matrice carrée avec
        des zéros partout, sauf peut-être sur la diagonale principale.
        
            Example:
                1 0 0 
                0 9 0  Est diagonale
                0 0 7 

            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque

            Returns:
                Vrai si la matrice est diagonale, faux sinon
        """
        return False
    
    def copier(m: list[list[int]]) -> list[list[int]]:
        """
        ★★ Copie une matrice d'entier

            Parameters:
                m(list[list[int]]): Une matrice d'entiers quelconque

            Returns:
                Une copie de cette matrice
        """
        return []

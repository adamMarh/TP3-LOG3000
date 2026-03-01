"""operators.py: Fonctions arithmétiques de base pour la calculatrice.

Ce module regroupe les opérations élémentaires utilisées par
l'application (addition, soustraction, multiplication, division).
Chaque fonction prend deux nombres en entrée et retourne un résultat numérique.
"""


def add(a, b):
    """Additionne deux nombres.

    Args:
        a (float | int) : Premier opérande.
        b (float | int) : Deuxième opérande.

    Returns:
        float | int : Résultat de l'addition a + b.
    """
    return a + b


def subtract(a, b):
    """Soustrait le second nombre du premier.

    Args:
        a (float | int) : Premier opérande.
        b (float | int) : Deuxième opérande.

    Returns:
        float | int : Résultat de la soustraction a - b.
    """
    return a - b


def multiply(a, b):
    """Multiplie deux nombres.

    Args:
        a (float | int) : Premier opérande.
        b (float | int) : Deuxième opérande.

    Returns:
        float | int : Résultat de la multiplication a * b.
    """
    return a * b


def divide(a, b):
    """Divise le premier nombre par le second.

    Args:
        a (float | int) : Numérateur.
        b (float | int) : Dénominateur (ne doit pas être nul).

    Returns:
        float : Résultat de la division a / b.

    Raises:
        ZeroDivisionError : Si b est égal à 0.
    """
    return a / b  # La gestion de la division par zéro est déléguée à Python
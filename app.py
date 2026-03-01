"""app.py: Application principale Flask pour la calculatrice web.

Ce module définit :
- le serveur web Flask,
- la logique de parsing et d’évaluation des expressions,
- la route unique qui affiche l’interface et traite les soumissions du formulaire.
"""

from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

# Création de l’instance principale de l’application Flask.
# Cette instance sera utilisée pour enregistrer les routes et démarrer le serveur.
app = Flask(__name__)

# Dictionnaire associant chaque symbole d’opérateur
# à la fonction correspondante.
# Permet d’éviter une succession de if/elif et rend le code plus extensible.
OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(expr: str):
    """Analyse et évalue une expression arithmétique simple.

    L'expression doit contenir exactement deux opérandes numériques
    séparés par un seul opérateur parmi (+, -, *, /).
    Les espaces sont supprimés avant l’analyse.

    Args:
        expr (str) : Chaîne représentant une expression,
                     par exemple "3+5" ou "12 / 4".

    Returns:
        float : Résultat numérique de l’opération.

    Raises:
        ValueError : Si l’expression est vide, contient plusieurs opérateurs,
                     si l’opérateur est mal positionné ou si les opérandes
                     ne sont pas numériques.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("expression vide")

    # Suppression des espaces pour simplifier l’analyse
    # (évite de gérer les cas "3 + 5" séparément).
    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    # Parcours caractère par caractère pour détecter l’unique opérateur.
    # On impose un seul opérateur pour garder une logique simple.
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("un seul opérateur est autorisé")
            op_pos = i
            op_char = ch

    # L’opérateur ne peut pas être au début ni à la fin
    # sinon il manquerait un opérande.
    if op_pos <= 0 or op_pos >= len(s) - 1:
        raise ValueError("format d'expression invalide")

    # Découpage de la chaîne en deux parties : gauche et droite
    left = s[:op_pos]
    right = s[op_pos + 1:]

    # Conversion en float pour autoriser les nombres décimaux.
    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("les opérandes doivent être numériques")

    # Appel dynamique de la fonction correspondant à l’opérateur.
    # Ce mécanisme rend l’ajout d’un nouvel opérateur très simple.
    return OPS[op_char](a, b)


@app.route('/', methods=['GET', 'POST'])
def index():
    """Affiche la page de la calculatrice et traite les soumissions.

    - En GET : affiche la calculatrice avec un affichage vide.
    - En POST : récupère l’expression envoyée par le formulaire,
      l’évalue et affiche le résultat ou un message d’erreur.

    Returns:
        str : Code HTML généré pour la page.
    """
    result = ""

    # On distingue GET et POST pour séparer affichage initial
    # et traitement des données envoyées par l’utilisateur.
    if request.method == 'POST':
        expression = request.form.get('display', '')

        try:
            result = calculate(expression)
        except Exception as e:
            # Capture générique pour éviter que l’application
            # ne plante et afficher un message clair à l’utilisateur.
            result = f"Erreur : {e}"

    return render_template('index.html', result=result)


if __name__ == '__main__':
    # Mode debug activé pour faciliter le développement
    # (rechargement automatique et affichage détaillé des erreurs).
    app.run(debug=True)
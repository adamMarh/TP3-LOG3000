# templates/

## Objectif
Ce répertoire contient les templates **HTML Jinja2** rendus par le backend Flask.

## Fichier
| Fichier | Description |
|---------|-------------|
| `index.html` | Page principale (et unique) de la calculatrice. Contient le champ d’affichage, les boutons numériques (0–9), les boutons opérateurs (+, −, ×, ÷), un bouton de réinitialisation (C) et un bouton de validation (=). Un script JavaScript dans une balise <script> gère l’ajout des caractères dans l’affichage ainsi que sa réinitialisation. |

## Dépendances
- La fonction `render_template` de Flask (appelée depuis `app.py`).
- Le fichier CSS situé dans `static/style.css` (lié via `url_for`).

## Remarques
- Le formulaire utilise `method="POST"` : lorsque l’on appuie sur =, la valeur affichée est envoyée au serveur, qui évalue l’expression et renvoie le résultat.

- Le champ `display` est défini comme `readonly` ; l’interaction utilisateur est gérée via des gestionnaires `onclick` sur les boutons.

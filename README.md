# Calculatrice Flask

## Nom du projet
**Calculatrice Flask** – Une calculatrice arithmétique simple basée sur le web.

## Équipe
Équipe 19 – LOG3000

## Objectif
Fournir une calculatrice minimale basée sur le navigateur qui prend en charge les quatre opérations arithmétiques de base (addition, soustraction, multiplication, division) en utilisant un backend Python/Flask et un frontend HTML/CSS/JS vanille.

---

## Prérequis
| Outil | Version minimale |
|-------|------------------|
| Python | 3.9+ |
| pip | 21+ |
| Git | 2.30+ |
| Un navigateur web moderne | — |

## Installation

```bash
# 1. Cloner le dépôt
git clone <REPO_URL>
cd TP3---LOG3000

# 2. (Optionnel) Créer un environnement virtuel
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

# 3. Installer les dépendances
pip install flask

# 4. Lancer l'application
python app.py
```

Le serveur démarre à **http://127.0.0.1:5000**.

## Utilisation
1. Ouvrez votre navigateur et allez à `http://127.0.0.1:5000`.
2. Cliquez sur les boutons des chiffres et des opérateurs pour construire une expression (par exemple, `12+8`).
3. Appuyez sur `=` pour soumettre l'expression. Le résultat (ou un message d'erreur) s'affiche à l'écran.
4. Appuyez sur `C` pour effacer l'affichage.

## Ex.cution des tests

```bash
# Depuis la racine du projet
python -m pytest tests/ -v
```

Tous les tests sont situés dans le répertoire `tests/`. Consultez `tests/README.md` pour plus de détails sur ce qui est couvert.

## Flux de contribution
1. Créez une nouvelle branche à partir de `main` pour chaque problème ou fonctionnalité :
   ```bash
   git checkout -b fix/issue-<number>
   ```
2. Effectuez vos modifications et commitez avec un message clair expliquant quoi a été changé et pourquoi.
3. Poussez la branche et ouvrez une Pull Request (PR) sur GitHub.
4. Au moins un membre de l'équipe doit examiner la PR avant la fusion.
5. Après approbation, fusionnez la PR dans `main` et supprimez la branche de fonctionnalité.

## Structure du projet
```
TP3---LOG3000/
├── app.py            # Serveur Flask & analyseur d'expressions
├── operators.py      # Fonctions des opérateurs arithmétiques
├── static/
│   └── style.css     # Style de la calculatrice
├── templates/
│   └── index.html    # Page HTML de la calculatrice
├── tests/
│   ├── test_operators.py   # Tests unitaires pour les opérateurs
│   ├── test_app.py         # Tests d'intégration pour l'application
│   └── README.md           # Documentation des tests
└── README.md         # Ce fichier
```

## License
Ce dépôt fait partie d'un devoir universitaire (LOG3000) et n'est pas licencié pour une utilisation externe.

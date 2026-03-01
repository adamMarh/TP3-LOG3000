# tests/

## Objectif
Ce répertoire contient la suite de **tests automatisés** du projet Flask Calculator.
Les tests sont écrits avec le framework intégré `unittest` de Python et peuvent également être exécutés avec `pytest`.

## Fichiers
| Fichier | Description |
|------|-------------|
| `test_operators.py` | Tests unitaires pour chaque fonction de `operators.py` (add, subtract, multiply, divide). Ces tests mettent en évidence les trois bugs connus. |
| `test_app.py` | Tests d’intégration pour l’application Flask : vérifie la fonction `calculate()` ainsi que la route HTTP. |

## Comment exécuter les tests

```bash
# Depuis le répertoire racine du projet
python -m pytest tests/ -v
```

Ou avec unittest unittest:
```bash
python -m unittest discover -s tests -v
```

## Ce que couvrent les tests
- **Addition**: vérifie que `add(a, b)` retourne la somme correcte.
- **Soustraction**: vérifie que `subtract(a, b)` retourne `a - b` (échoue actuellement à cause d’un bug d’inversion des opérandes).
- **Multiplication**: vérifie que `multiply(a, b)` retourne `a * b` (échoue actuellement car `**` est utilisé à la place de `*`).
- **Division**: vérifie que `divide(a, b)` retourne true division `a / b` (échoue actuellement car l’opérateur `//` de division entière est utilisé).
- **Analyse d'expressions**: vérifie que `calculate()` analyse et évalue correctement des expressions simples.
- **Cas limites** : entrée vide, opérateurs invalides, division par zéro, opérandes non numériques.

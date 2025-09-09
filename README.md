name: Antivirus File Scanner
description: >
  Petit script Python qui scanne les fichiers d’un répertoire et vérifie leur signature binaire
  pour détecter des fichiers corrompus ou suspects.
  Le script compare la signature attendue avec celle présente dans chaque fichier.
usage: |
  python antivirus.py
  # Par défaut, scanne le répertoire courant (.)
  # Modifie `directory` et `expected_signature` dans le code si nécessaire.

requirements:
  - Python 3.7+
  - Aucun package externe requis (uniquement la librairie standard)

features:
  - Vérifie si un fichier correspond à une signature binaire attendue
  - Parcourt récursivement les sous-dossiers
  - Affiche un rapport simple dans la console
  - Gère les erreurs (fichier introuvable, autres exceptions)

limitations:
  - La "signature" attendue doit être définie manuellement dans le code
  - Ne remplace pas un antivirus complet (pas de base de données de malwares)

example:
  expected_signature: "EXPECTED_SIGNATURE"
  directory: "."
  command: "python antivirus.py"


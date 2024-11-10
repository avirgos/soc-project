# README - Script d'Extraction de Règles Splunk

## Description
Ce script Python est conçu pour extraire les règles enregistrées de Splunk via l'API REST et les sauvegarder dans des fichiers YAML individuels. Chaque fichier YAML contient des informations importantes sur la règle Splunk, telles que le nom, l'événement d'alerte, la requête de recherche, la description et le type d'alerte.

## Prérequis
- Python doit être installé sur votre système.

  ```bash
  pip install requests
  ```
  ```bash
  pip install pyyaml
  ```

## Utilisation
1. **Configuration**
   - Mettez à jour les valeurs de `username` et `password` avec vos identifiants Splunk.
   - Mettez à jour `splunk_url` avec l'URL de votre instance Splunk.

2. **Exécution**
     ```bash
     python script_name.py
     ```
   - Le script se connecte à l'API REST de Splunk pour récupérer les règles enregistrées et les sauvegarde en tant que fichiers YAML

3. **Structure du Fichier YAML**
   - Chaque fichier YAML généré contient les informations suivantes :
     - `name`: Le nom de la règle.
     - `alert_event`: L'événement d'alerte, ou "Unnamed_Event" s'il n'est pas défini.
     - `search`: La requête de recherche Splunk associée à la règle.
     - `description`: Une description de la règle.
     - `alert_type`: Le type d'alerte défini pour la règle.

## Avertissements
- **Connexion non sécurisée** : Il est conseillé d'activer la vérification SSL si le script est exécuté en production, dans un environnement sensible :)
- **Nom des fichiers** : Les caractères spéciaux dans les noms de fichiers sont remplacés par des caractères valides pour éviter des erreurs lors de la création des fichiers.

## Dépendances
- `requests`: Pour effectuer des requêtes HTTP vers l'API REST de Splunk.
- `pyyaml`: Pour générer des fichiers YAML à partir des données de la règle.

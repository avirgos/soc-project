# documentation


# Matrice de Communication - Projet Splunk

## Groupe 6 INSA CVL STI5A-APP

| **Membre**           | **Rôle/Responsabilité (BUILD)**                 | **Rôle/Responsabilité (RUN)**                   | **Point de communication**                | **Remarques**                      |
|----------------------|-------------------------------------------------|-------------------------------------------------|-------------------------------------------|------------------------------------|
| Rayane BENDAHMANE    | Splunk & Règles Sigma - Domain Controller, Server | Surveillance des performances, gestion des alertes critiques | Rapports sur les incidents, scénarios de détection | Partage les rapports d’analyse     |
| Shérif MAKALOU       | Splunk & Règles Sigma - Server, Domain Controller | Analyse en temps réel des logs, gestion des notifications d'alerte | Rapports sur les incidents, scénarios de détection | Partage les rapports d’analyse     |
| Ayet MERZOUQI        | Splunk & Règles Sysmon, Server, Suricata, Domain Controller       | Surveillance des logs Sysmon, analyse des flux réseau Suricata | Rapports sur les incidents, scénarios de détection | Partage les rapports d’analyse     |
| Philémon ST-JEAN     | Splunk & Règles Sigma - Domain Controller, Server | Audit de la sécurité, maintenance des règles et optimisation | Rapports sur les incidents, scénarios de détection | Partage les rapports d’analyse     |
| Antoine VIRGOS       | Automatisation, Sysmon, Suricata, Server               | Maintenance des scripts d'automatisation, veille des indicateurs de menace | Automatisation des procédures, scripts Python | Partage les rapports d’analyse     |


---

## Matrice d'Escalade

| **Type d'incident**         | **Niveau 1**                | **Niveau 2**                 | **Niveau 3**               | **Canal de communication**             |
|-----------------------------|-----------------------------|-----------------------------|---------------------------|---------------------------------------|
| Incident mineur            | Rayane BENDAHMANE           | Shérif MAKALOU              | Antoine VIRGOS            | E-mail, Teams                         |
| Incident modéré            | Shérif MAKALOU              | Philémon ST-JEAN               | Ayet MERZOUQI          | Teams, Slack                          |
| Incident critique          | Philémon ST-JEAN           | Rayane BENDAHMANE            | Antoine VIRGOS            | Téléphone, E-mail (urgent)            |
| Panne système (service Splunk) | Shérif MAKALOU              | Ayet MERZOUQI           | Antoine VIRGOS            | Téléphone, E-mail                     |
| Intrusion détectée         | Philémon ST-JEAN            | Antoine VIRGOS               | Ayet MERZOUQI         | Teams, Téléphone (urgence maximale)   |

---

### Guide d'Escalade
1. **Incident mineur** : Problèmes qui n'affectent pas les services critiques. Gestion en interne avec une réponse sous 24 heures.
2. **Incident modéré** : Impact modéré sur le service, nécessite une résolution rapide dans les 4 à 8 heures.
3. **Incident critique** : Affecte les systèmes critiques, nécessitant une réponse immédiate avec notification en temps réel.
4. **Panne système** : Actions rapides pour rétablir le service avec communication continue.
5. **Intrusion détectée** : Toute tentative de sécurité doit être signalée immédiatement et les équipes doivent être mobilisées.

## Infrastructure

| Adresse IP | Hostname    |
|---------------|---------------|
| 192.168.10.10 | SRV-PRD-DC    |
| 192.168.10.21 | SRV-PRD-WEB   |
| 192.168.10.22 | SRV-PRD-DB    |
| 192.168.10.23 | SRV-PRD-SHARE |
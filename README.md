# WebGoat_Projet8100

## Pipeline CI/CD

Le pipeline CI/CD consiste en 4 workflows, assurant le déploiement sécurisé de l'application. Ces workflows sont :

1.  **Analyse de sécurité CodeQL**
2.  **Scan de sécurité pour image docker**
3.  **Déploiement de l'image sur DockerHub**
4.  **Déploiement de l'application**

---

## Détails des Workflows

### 1. Analyse de sécurité CodeQL

Ce workflow effectue une analyse de sécurité du code source.

**Étapes :**

*   Récupération du code source : Extraction de la dernière version du code du dépôt.
*   Initialisation de CodeQL : Configuration et installation des éléments nécessaires pour l'analyse CodeQL.
*   Analyse CodeQL : Analyse du code pour la détection de vulnérabilités.

---

### 2. Scan de sécurité pour image docker

Ce workflow analyse l'image Docker pour détecter d'éventuelles vulnérabilités.

**Étapes :**

*   Récupération du code source : Extraction de la dernière version du code du dépôt.
*   Configuration de Trivy : Mise en place de l'outil Trivy.
*   Récupération de l'image Docker : Téléchargement de l'image docker `enriquitotupapi/webgoat:main` depuis Docker Hub.
*   Analyse avec Trivy : Exécution de l'analyse de l'image avec Trivy.
*   Publication du rapport Trivy : Mise à disposition des résultats de l'analyse dans la section "actions" de GitHub.

---

### 3. Déploiement de l'image sur DockerHub

Ce workflow construit et publie l'image Docker sur DockerHub.

**Étapes :**

*   Récupération du code source : Extraction de la dernière version du code du dépôt.
*   Configuration de JDK 21 : Configuration de l'environnement JAVA.
*   Exécution du build Maven : Lancement du processus de build Maven.
*   Connexion à Docker Hub : Établissement de la connexion à DockerHub via les identifiants.
*   Extraction des métadonnées : Extraction des métadonnées (tags, labels) pour Docker.
*   Construction et publication de l'image Docker : Construction et publication de l'image sur DockerHub.

---

### 4. Déploiement de l'application

Ce workflow déploie l'application dans l'environnement cible.

**Étapes :**

*   Récupération du code source : Extraction de la dernière version du code du dépôt.
*   Connexion à Azure : Établissement de la connexion à Azure via les identifiants.
*   Configuration de Terraform : Mise en place de la configuration pour Terraform.
*   Initialisation de Terraform : Exécution de la commande `terraform init`.
*   Planification de Terraform : Exécution de la commande `terraform plan`.
*   Récupération de kubeconfig : Récupération du fichier kubeconfig en utilisant Azure CLI.
*   Exécution du playbook Ansible : Lancement de l'exécution du playbook Ansible.

---


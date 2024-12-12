
# WebGoat_Projet8100

## CI/CD
Le pipeline CI/CD consiste en 4 workflows assurant que l'application est déployé de manière sécuritaire.

    1. Analyse de sécurité CodeQL
    2. Scan de sécurité pour image docker 
    3. Déploiement de l'image sur DockerHub
    4. Déploiement de l'application

## Analyse de sécurité CodeQL
    Étapes :
        1- Checkout repository: Pull la dernière version de code du repo
        2- Initialize CodeQL: Configure et installe les éléments nécessaires à la réalisation d'une analyse avec CodeQL
        3- Perform CodeQL Analysis: Analyse le code et détecte les vulnérabilités

## Scan de sécurité pour image docker
    Étapes :    
        1- Checkout repository: Pull la dernière version de code du repo
        2- Set up Trivy: Configure et mets en place l'outils Trivy
        3- Pull Docker Image from Docker Hub: Pull l'image docker enriquitotupapi/webgoat:main provenant de Docker Hub
        4- Run Trivy Scan: Analyse de l'image
        5- Upload Trivy Report: Mise à disposition des résultats de l'analyse dans la section action de github

## Déploiement de l'image sur DockerHub
    Étapes :    
        1- Check out the repo: Pull la dernière version de code du repo
        2- Set up JDK 21: Configuration environnement JAVA
        3- Run Maven clean install: Execute le build "Maven"
        4- Log in to Docker Hub: Connection à DockerHub via les crédentiels
        5- Extract metadata (tags, labels) for Docker: Extraction des données
        6- Build and push Docker image: Construction et publication de l'image
## Déploiement de l'application
    Étapes : 
        1- Checkout code: Pull la dernière version de code du repo
        2- Azure Login: Connection à Azure via les credentiels
        3- Setup Terraform: Configuration de Terraform
        4- Terraform Init: Execution la commande Terraform init
        5- Terraform Plan: Execution la commande Terraform apply
        6- Fetch kubeconfig using Azure CLI: Récupérer du fichier kubeconfig en utilisant Azure CLI.
        7- Ansible Playbook: Execution du playbook Ansible
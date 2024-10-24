pipeline {
    agent any
    stages {
        stage('Clonage du dépôt GitHub') {
            steps {
                // Cloner le dépôt GitHub
                git branch: 'main', url: 'https://github.com/bxancho/Pipeline_Test.git'
            }
        }
        
        stage('Installation de Python 3.11 et pip') {
            steps {
                // Installer Python 3.11 et pip
                sh '''
                sudo apt update
                sudo apt install -y python3.11 python3.11-venv python3.11-dev
                sudo apt install -y python3-pip
                '''
            }
        }

        stage('Exécution du script Python') {
            steps {
                // Exécuter le script Python
                sh '''
                python3.11 os_detector.py
                '''
            }
        }
    }
}

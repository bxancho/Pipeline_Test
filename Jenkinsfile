pipeline {
    agent any
    stages {
        stage('Clonage du dépôt GitHub') {
            steps {
                // Cloner le dépôt GitHub
                git branch: 'main', url: 'https://github.com/bxancho/Pipeline_Test.git'
            }
        }
        
        stage('Installation de Python 3 et pip') {
            steps {
                // Installer Python 3 et pip
                sh '''
                sudo apt update
                sudo apt install  -y python3
                sudo apt install -y python3-pip
                '''
            }
        }

        stage('Exécution du script Python') {
            steps {
                // Exécuter le script Python
                sh '''
                python3 os_detector.py
                '''
            }
        }
    }
}

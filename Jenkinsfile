pipeline {
    agent any
    
    stages {
        stage('Clonage du dépôt GitHub') {
            steps {
                // Cloner le dépôt GitHub
                git branch: 'main', url: 'https://github.com/bxancho/Pipeline_Test.git'
            }
        }
        stage('Build') {
            steps {
                script {
                    // Détecter le système d'exploitation et exécuter la commande `make` en conséquence
                    if (isUnix()) {
                        sh 'make'
                    } else {
                        bat 'make'
                    }
                }
            }
        }

        stage('Permissions') {
            when {
                expression { isUnix() } // Cette étape ne s'exécute que si le système est de type Unix
            }
            steps {
                script {
                    // Donner les droits d'exécution au binaire si nous sommes sous Unix
                    sh 'chmod +x StringInverser'
                }
            }
        }

        stage('Nettoyage') {
            steps {
                script {
                    // Exécuter `make clean` pour nettoyer les fichiers temporaires
                    if (isUnix()) {
                        sh 'make clean'
                    } else {
                        bat 'make clean'
                    }
                }
            }
        }
    }
}

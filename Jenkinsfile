pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh 'bash jenkins/build.sh'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh 'pwd'
                sh 'bash jenkins/setup.sh'
                sh 'bash jenkins/test.sh http://localhost:5000'
            }
        }
        stage('Deploy Dev') {
            steps {
                echo 'Deploying....'
                sh 'bash jenkins/deploy.sh dev'
            }
        }
        stage('Test Dev') {
            steps {
                echo 'Testing.. Dev'
                sh 'bash jenkins/test.sh dev'
                sh 'exit $(cat /tmp/EXIT)'
            }
        }
        stage('Deploy stge') {
            steps {
                echo 'Deploying....'
                sh 'bash jenkins/deploy.sh stge'
            }
        }
        stage('Test Stage') {
            steps {
                echo 'Testing.. stge'
                sh 'bash jenkins/test.sh stge'
                sh 'exit $(cat /tmp/EXIT)'
            }
        }
        stage('Deploy prod') {
            steps {
                echo 'Deploying....'
                sh 'bash jenkins/deploy.sh prod'
            }
        }
        stage('Test Prod') {
            steps {
                echo 'Testing.. stge'
                sh 'bash jenkins/test.sh prod'
                sh 'exit $(cat /tmp/EXIT)'
            }
        }
    }
}

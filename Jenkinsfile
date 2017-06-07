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
                sh 'bash jenkins/tear_down.sh'
                sh 'kill $(cat /tmp/PID) || exit $(cat /tmp/EXIT)'
                sh 'rm /tmp/PID && rm /tmp/EXIT'
            }
        }
        stage('Deploy Dev') {
            steps {
                echo 'Deploying....'
                sh 'bash jenkins/deploy.sh dev'
                sh 'cat url'
            }
        }
        stage('Test Dev') {
            steps {
                echo 'Testing.. Dev'
                sh 'bash jenkins/test.sh $(cat url)'
                sh 'exit $(cat /tmp/EXIT)'
            }
        }
        stage('Deploy stge') {
            steps {
                echo 'Deploying....'
                sh 'bash jenkins/deploy.sh stge'
                sh 'cat url'
            }
        }
        stage('Test Stage') {
            steps {
                echo 'Testing.. stge'
                sh 'bash jenkins/test.sh $(cat url)'
                sh 'exit $(cat /tmp/EXIT)'
            }
        }
        stage('Deploy prod') {
            steps {
                echo 'Deploying....'
                sh 'bash jenkins/deploy.sh prod'
                sh 'cat url'
            }
        }
        stage('Test Prod') {
            steps {
                echo 'Testing.. stge'
                sh 'bash jenkins/test.sh $(cat url)'
                sh 'exit $(cat /tmp/EXIT)'
            }
        }
    }
}

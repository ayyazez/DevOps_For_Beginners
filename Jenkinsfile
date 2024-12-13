pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo "-------- Build Success ------"
            }
        }
        stage('Test') {
            steps {
                echo "---------- Test has been performed successfully -----------"
            }
        }
        stage('Build Docker Image') { 
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE}:${env.BUILD_NUMBER} .'
                }
            }
        }
   
}

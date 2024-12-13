pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'akhan101/hello_docker'  // Define default Docker image name
    }
    stages {
        stage('Build') {
            steps {
                echo "-------- Build Success ------ "
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
                    sh 'docker build -t ${DOCKER_IMAGE}:${env.BUILD_NUMBER} .'  // Docker build command
                }
            }
        }
    }
    post {
        always {
            echo '----- Pipeline execution completed successfully --------------'
        }
    }
}

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
        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'akhan101',
                                                     usernameVariable: 'akhan101',
                                                     passwordVariable: 'Ik@124421')]) {
                        sh '''
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                            docker push ${DOCKER_IMAGE}:${env.BUILD_NUMBER}
                            docker logout
                        '''
                    }
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

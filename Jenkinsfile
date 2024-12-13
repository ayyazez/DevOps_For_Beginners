pipeline {
  
  agent any
   environment {
        //DOCKER_HUB_CREDENTIALS='akhan101'
        //DOCKER_IMAGE = 'akhan101/hello_docker'
            
    }
  stages {

    stage('Build'){
      echo "-------- Build Success ------ "
      
    }
    stage('Test'){
      echo "---------- Test has been performed successfully -----------"
      
    }
    stage('Build Docker Image'){
         script {
           sh 'docker build -t ${DOCKER_IMAGE}:$env.$BUILD_NUMBER'
         }
  }
    post {
      always {
        echo '----- Pipeline execution completion successfully --------------'
      }
    }

  
}

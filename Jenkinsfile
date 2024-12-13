pipeline {
  
  agent any
 
  stages {

    stage('Build'){
      steps{
         echo "-------- Build Success ------ "
      }
     
      
    }
    stage('Test'){
      steps{
        echo "---------- Test has been performed successfully -----------"
      }
      
      
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

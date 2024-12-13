node {
	stage('Build') {
		echo "Build"
		echo "PATH - $PATH"
		echo "BUILD_NUMBER - $env.BUILD_NUMBER"
	}
	stage('Test') {
		echo "Test"
	}
	stage('Build Docker Image') {
		//docker build -t akhan101/hello_docker:$env.BUILD_TAG
	}
}

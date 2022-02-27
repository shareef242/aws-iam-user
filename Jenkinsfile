pipeline {
	environment {
		VERSION = "latest"
		PROJECT = "gsws-2.0-dev-revenue-service-api"
		IMAGE = "$PROJECT:$VERSION"
	}
  agent any 
    parameters {
      string (
        name: 'user',
        defaultValue: 'false',
        decription: 'Enter user name')
      string (
        name: 'group_option',
        defaultValue: 'false',
        decription: 'Enter group Number')
    }  
  stages {
	stage('SCM Checkout') {
            steps {
            // Get source code from Gitlab Repository
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], doGenerateSubmoduleConfigurations: false, extensions: [[$class: 'RelativeTargetDirectory', relativeTargetDir: '']], userRemoteConfigs: [[credentialsId: 'github-cred', url: 'https://github.com/shareef242/aws-iam-user.git']]])
            }
		}
		stage('Run Script') {
			steps {
				script {
				    sh 'python iam-user-creation.py $user $group_option '
				}
			}
		}
	}   
}

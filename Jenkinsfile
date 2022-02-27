pipeline {
	environment {
		VERSION = "latest"
		PROJECT = "gsws-2.0-dev-revenue-service-api"
		IMAGE = "$PROJECT:$VERSION"
	}
  agent any 
    parameters {
      string (
        name: 'USER_NAME',
        defaultValue: 'false',
        description: 'Enter user name')
      choice (
        name: 'GROUP_OPTION',
        choices: ['1', '2', '3'],
        description: 'Enter group Number')
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
					user = params.USER_NAME
					group_option = params.GROUP_OPTION
					sh 'python iam-user-creation.py --user ${user} --group ${group_option}'
				}
			}
		}
	}   
}

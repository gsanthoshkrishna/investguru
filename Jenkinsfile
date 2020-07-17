pipeline {
  agent any
  environment{
    tomail = "test"
  }	
  stages {
    stage('test build') {
        steps {
            $tomail = 'updated'
            
        }
	}
  }
  post{
    emailext body: '', subject: 'test', to: '$tomail'
  }
  
 
}

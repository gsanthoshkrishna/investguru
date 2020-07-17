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
 
}
  post{
    emailext{
      subject: "This is test"
      body: "this is test body"
      to: $tomail
      }
  }
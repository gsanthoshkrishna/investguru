pipeline {
  agent any
  environment{
    tomail = "santhosh@test.com"
  }	
  stages {
    stage('test build') {
        steps {
            echo "hi"
            
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
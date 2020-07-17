pipeline {
  agent any
  environment{
    tomail = "santhosh@test.com"
  }	
  stages {
    stage('test build') {
        steps {
            echo "hi"
            env.tomail = "gsanthoshkrishna@gmail.com"
            
        }
	}
  }
 

  post {
    success{
      emailext(
      subject: "This is test",
      body: "this is test body",
      to: env.tomail
      )
    }
    
  }
}
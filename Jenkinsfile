pipeline {
  agent any
  environment{
    tomail = "santhosh@test.com"
  }	
  stages {
    stage('test build') {
        steps {
            echo "hi"
            script {
          withEnv(["tomail=gsanthoshkrishna@gmail.com"]) {
            echo env.tomail // prints: FOO = newbar
          }
        }
            
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
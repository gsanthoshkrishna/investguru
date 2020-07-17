tomail = "test@test.com"
pipeline {
  agent any
  	
  stages {
    stage('test build') {
        steps {
            echo "hi"
            script{
            tomail = "gsanthoshkrishna@gmail.com"
            }
        }
	}
  }
 

  post {
    success{
      emailext(
      subject: "This is test",
      body: "this is test body",
      to: "${tomail}"
      )
    }
    
  }
}
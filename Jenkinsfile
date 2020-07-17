tomail = "test@test.com"
pipeline {
  agent any
  stages {
    stage('test build') {
        steps {
            echo "hi"
            tomail = "gsanthoshkrishna@gmail.com" // prints: FOO = newbar
          
            
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
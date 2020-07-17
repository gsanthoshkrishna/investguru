tomail = "test@test.com"
pipeline {
  agent any
  	
  stages {
    stage('test build') {
        steps {
            echo "hi"
            script{
            tomail = "gsanthoshkrishna@gmail.com"
            test = sh(script: 'git show -s | grep Author: | grep -E -o "\\\\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\\\.[A-Za-z]{2,6}\\\\b"'
            }
            echo "${test}"
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
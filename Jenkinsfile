pipeline {
  agent {
    docker {
      image 'python:3.10-alpine'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh 'echo \'message\''
      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh 'python3 test_hello.py'
          }
        }

        stage('Test-2') {
          steps {
            sh 'python3 test_world.py'
          }
        }

      }
    }

    stage('error') {
      steps {
        sh 'python3 basic_py_file.py'
      }
    }

  }
}
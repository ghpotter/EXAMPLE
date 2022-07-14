pipeline {
  agent {
    docker {
      image 'python:3.10-alpine'
    }

  }
  stages {
    stage('Build') {
      steps {
        echo 'this message'
      }
    }

    stage('Test') {
      parallel {
        stage('Test') {
          steps {
            sh 'python test_hello.py'
          }
        }

        stage('Test-2') {
          steps {
            sh 'python test_world.py'
          }
        }

      }
    }

    stage('error') {
      steps {
        sh 'python basic_py_file.py'
      }
    }

  }
}
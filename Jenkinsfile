pipeline {
  agent { docker { image 'python:3' } }
  stages {
    stage('build') {
      steps {
        sh 'pip install -r requirements.txt'
      }
    }
    stage('test') {
      steps {
        sh 'pytest tests/test.py'
      }
    }
  }
}

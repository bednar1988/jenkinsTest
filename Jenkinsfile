pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
    }

  }
  stages {
    stage('test docker image build') {
      steps {
        sh 'python --version'
      }
    }

  }
}